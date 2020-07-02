import $ from 'jquery';

const hovertemplate = "<b>%{fullData.meta.columnNames.y}</b><br>%{xaxis.title.text}: <b>%{x}</b><br>%{yaxis.title.text}: <b>%{y}</b><extra></extra>";
const config = {
    displayModeBar: true,
    responsive: true,
    showLink: true,
    plotlyServerURL: "https://chart-studio.plotly.com",
    toImageButtonOptions: {
        width: 1200,
        height: 657,
    },
    modeBarButtonsToRemove: [
        'pan2d',
        'select2d',
        'lasso2d',
        'hoverClosestCartesian',
        'hoverCompareCartesian',
        'toggleSpikelines',
    ],
};
const minWidth = 700;

export default function entry() {
    $('.charts__chart').each((i, el) => {

        const init = () => {
            // if window greater than min and chart not inited, init chart and set flag
            if (window.matchMedia(`(min-width: ${minWidth}px)`).matches) {
                initChart($(el));

                // remove listener if chart inited
                removelistener();
            }
        }

        // add the window resize listener
        window.addEventListener('resize', init);

        // remove the window resize listener
        const removelistener = () => {
            window.removeEventListener('resize', init);
        }

        // call the init function
        init();

    });
}

const assignOption = (select, value) => {
    const currentOption = document.createElement('option');
    currentOption.text = value;
    select.appendChild(currentOption);
};

const assignOptions = (select, options) => {
    for (var i = 0; i < options.length;  i++) {
        assignOption(select, options[i]);
    }
    $(select).addClass('data-selector--active');
};

const addLoading = el => {
    el.addClass('chart-container--loading');
    el.prepend('<div class="chart-loading"><div class="chart-loading__block">' +
               '<div></div><div></div><div></div><div></div></div></div>');
};

const removeLoading = el => {
    el.removeClass('chart-container--loading');
    el.find('.chart-loading').remove();
};

const removeTitle = data => {
    try {
        data.layout.title.text = '';
    } catch (e) {}
};

const getIsGroupedTransform = data => {
    try {
        if (data[0].transforms && data[0].transforms[0].type == 'groupby') {
            return true;
        }
        else {
            return false;
        }
    } catch (e) {
        return false;
    }
};

const getGroupedTransformOptions = data => {
    const { x, y, transforms } = data[0];
    const labels = transforms[0].groups;
    return [...new Set(labels.map(item => item))];
};

const getOptions = (legend, traces, isTreemap) => {
    if (isTreemap) {
        return traces.map(el => el.name);

    }
    const options = [];
    legend.querySelectorAll('traces').forEach(el => options.push(el.dataset.unformatted));
    return options;
};

const getGroupedTransformData = (traces, label) => {
    const data = traces[0];
    const groups = data.transforms[0].groups;
    const x = data.x.filter((el, index) => groups[index] == label);
    const y = data.y.filter((el, index) => groups[index] == label);
    const labels = groups.filter(el => el == label);
    data.x = x;
    data.y = y;
    data.transforms[0].groups = labels;
    return [data];
};

const getSplitData = (traces, label, isTreemap) => {
    const newDataIndex = traces.findIndex(el => !isTreemap ? el.meta.columnNames.y == label : el.name == label);
    return [traces[newDataIndex]];
};

const initChart = (el) => {
    addLoading(el);
    Plotly.d3.json(el.first().data('url'), d => {
        const data = d;
        const interactive = el.data('interactive');
        const split_data_on = el.data('split-data-on');
        const combined = el.data('combined');
        const drilldown = el.data('drilldown');

        data.layout.colorway = ["#c2135b", "#e84439", "#eb642b", "#f49b21", "#109e68", "#0089cc", "#893f90"];
        removeLoading(el);
        removeTitle(data);

        if (drilldown) {
            initDrillDownChart(el, data);
        }
        else if (interactive) {
            initInteractiveChart(el, data, combined, split_data_on);
        }
        else {
            initStaticChart(el, data);
        }
    });
}

function click(index) {
    return function() {
        var item = document.querySelectorAll('rect.legendtoggle')[0];
        item.dispatchEvent(new MouseEvent('mousedown'));
        item.dispatchEvent(new MouseEvent('mouseup'));
    };
}

function _dblclick(index) {
    return function() {
        var item = document.querySelectorAll('rect.legendtoggle')[index];
        return new Promise(function(resolve) {
            item.dispatchEvent(new MouseEvent('mousedown'));
            item.dispatchEvent(new MouseEvent('mouseup'));
            item.dispatchEvent(new MouseEvent('mousedown'));
            item.dispatchEvent(new MouseEvent('mouseup'));
            setTimeout(resolve, 20);
        });
    };
}

function dblclick(legend, index) {
    var item = legend.querySelectorAll('rect.legendtoggle')[index];
    item.dispatchEvent(new MouseEvent('mousedown'));
    item.dispatchEvent(new MouseEvent('mouseup'));
    item.dispatchEvent(new MouseEvent('mousedown'));
    item.dispatchEvent(new MouseEvent('mouseup'));
    console.log(item);
}

function delay(duration) {
    return function(value) {
        return new Promise(function(resolve) {
            setTimeout(function() {
                resolve(value);
            }, duration || 0);
        });
    };
}

const initStaticChart = (el, data) => {
    const traces = data.data.slice();

    $.each(traces, (i, el) => {
        if (!el.hovertemplate) {
            el.hovertemplate = hovertemplate;
        }
    });

    data.data = traces;

    Plotly.newPlot(el[0], data.data, data.layout, config)
        .then(_dblclick(0))

}

const initInteractiveChart = (el, data, combined = false, split_data_on) => {
    const all = 'All data';
    const traces = Array.from(data.data);
    const options = [];
    const isTreemap = data.data[0].type == 'treemap';
    const isGroupedTransform = getIsGroupedTransform(traces);
    const dataSelector = el.closest('.chart-container').find('.data-selector')[0];
    let lastSelected = -1;
    let legend = undefined;

    // hide the legend
    data.layout.showlegend = true;
    data.layout.legend = {
        x: 1,
        xanchor: 'right',
        y: 1
    };

    $.each(traces, (i, el) => {
        if (!el.hovertemplate) {
            el.hovertemplate = hovertemplate;
        }
    });

    // add an extra all data option at the top if combined
    if (combined) {
        options.push(all);
    }

    // // test if data is grouped
    // if (isGroupedTransform) {
    //     // if so get unique options
    //     Array.prototype.push.apply(options, getGroupedTransformOptions(traces));
    // }
    // else {
    //     // otherwise add the individual data options
    //     Array.prototype.push.apply(options, getOptions(traces, isTreemap));
    // }

    // if not combined, select the first data set only
    // if (!combined) {
    //     if (isGroupedTransform) {
    //         data.data = getGroupedTransformData(JSON.parse(JSON.stringify(traces)), options[0]);
    //     }
    //     else {
    //         data.data = [traces[0]];
    //     }
    // }

    function updateData() {

        const index = dataSelector.selectedIndex;

        // if this is the first selection trigger double click
        if (lastSelected == -1) {
            dblclick(legend, index);
        }

        // if it's not the first, then we need to set the data as visible, redraw and then double click
        else {
            data.data.forEach(el => el.visible = true);
            Plotly.react(el[0], data)
                .then(() => dblclick(legend, index));
        }

        // store the selected index
        lastSelected = index;
    }

    // initialise the chart
    Plotly.newPlot(el[0], data.data, data.layout, config)
        .then(() => {
            // store a reference to the legend and hide it
            legend = el[0].querySelectorAll('.legend')[0];
            legend.style.cssText = 'display: none;';

            // get the select and assign options
            assignOptions(dataSelector, Array.prototype.push.apply(options, getOptions(legend, traces, isTreemap)));

            // assign change event listener
            dataSelector.addEventListener('change', updateData, false);
        });

}

const initDrillDownChart = (el, data) => {
    const traces = data.data.slice();
    const chart = el[0];
    let lastClicked = null;

    // select the first data set only
    data.data = [traces[0]];

    $.each(traces, (i, el) => {
        el.hovertemplate = "<b>%{fullData.name}</b><br>%{xaxis.title.text}: %{x}<br>%{yaxis.title.text}: %{value}<extra></extra>";
    });

    function updateData() {

        // if all data selected, set data to whole set
        if (!lastClicked) {
            data.data = [traces[0]];
        }

        // otherwise find matching index and set data to the selected one
        else {
            const newDataIndex = traces.findIndex(element => element.name == lastClicked);
            data.data = [traces[newDataIndex]];
        }

        lastClicked = null;

        // update the chart
        Plotly.react(chart, data);
    }

    // initialise the chart
    Plotly.newPlot(chart, data.data, data.layout, config);

    chart.on('plotly_click', function(data) {
        try {
          lastClicked = data.points[0].fullData.name;
        } catch (error) {
            lastClicked = null;
        }
    });

    chart.on('plotly_doubleclick', function(data) {
        updateData();
    });

}
