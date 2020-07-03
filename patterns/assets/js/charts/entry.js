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
    if (!options.length) {
        return;
    }
    for (var i = 0; i < options.length;  i++) {
        if (!options[i]) {
            return;
        }
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

const getOptions = (legend, traces) => {
    if (legend) {
        const options = [];
        legend.querySelectorAll('.legendtext').forEach(el => options.push(el.dataset.unformatted));
        return options;
    }
    return traces.map(el => el.name);
};

const getTreemapData = (traces, label) => {
    const newDataIndex = traces.findIndex(el => el.name == label);
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

const dblclick = (legend, index) => {
    var item = legend.querySelectorAll('rect.legendtoggle')[index];
    item.dispatchEvent(new MouseEvent('mousedown'));
    item.dispatchEvent(new MouseEvent('mouseup'));
    item.dispatchEvent(new MouseEvent('mousedown'));
    item.dispatchEvent(new MouseEvent('mouseup'));
};

const initStaticChart = (el, data) => {
    $.each(data.data, (i, el) => {
        if (!el.hovertemplate) {
            el.hovertemplate = hovertemplate;
        }
    });
    Plotly.newPlot(el[0], data.data, data.layout, config);

};

const initInteractiveChart = (el, data, combined = false) => {
    const all = 'All data';
    const traces = Array.from(data.data);
    const isTreemap = data.data[0].type == 'treemap';
    const dataSelector = el.closest('.chart-container').find('.data-selector')[0];
    let lastSelected = -1;
    let legend = undefined;
    const legendOpts = Object.assign(data.layout.legend || {}, {
        x: 1,
        xanchor: 'right',
        y: 1,
    });

    // enable the legend and add opts
    data.layout.showlegend = true;
    data.layout.legend = legendOpts;

    $.each(traces, (i, el) => {
        if (!el.hovertemplate) {
            el.hovertemplate = hovertemplate;
        }
    });

    if (isTreemap) {
        data.data = [traces[0]];
    }

    function updateData() {

        const index = combined ? dataSelector.selectedIndex - 1 : dataSelector.selectedIndex;

        if (isTreemap) {
            data.data = getTreemapData(traces, dataSelector.value);
            Plotly.react(el[0], data)
        }
        else {

            // if index is less than zero, it's an all data reset so don't click again
            if (index < 0) {
                dblclick(legend, 0);
            }
            else {
                // otherwise reset if necessary and then click the selected index
                if (lastSelected > -1) {
                    dblclick(legend, 0);
                }
                dblclick(legend, index);
            }

            // store the selected index
            lastSelected = index;
        }
    }

    // initialise the chart and selector
    Plotly.newPlot(el[0], data.data, data.layout, config)
        .then(() => {
            // store a reference to the legend and hide it
            try {
                legend = el[0].querySelectorAll('.legend')[0];
                legend.style.cssText = 'display: none;';
            } catch (e) {}

            // create options list from legend (or data if treemap)
            const options = getOptions(legend, traces);

            // add an extra all data option at the top if combined
            if (!isTreemap && combined) {
                options.unshift(all);
            }
            else {
                // otherwise select the first legend item
                try {
                    lastSelected = 0;
                    dblclick(legend, lastSelected);
                } catch (e) {}
            }

            // get the select and assign options
            assignOptions(dataSelector, options);

            // assign change event listener
            dataSelector.addEventListener('change', updateData, false);
        });
};

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

};
