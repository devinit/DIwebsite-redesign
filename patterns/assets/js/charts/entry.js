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

const getSplitDataOptions = (data, isTreemap) => {
    const options = [];
    for (var i = 0; i < data.length; i++ ) {
        !isTreemap ? options.push(data[i].meta.columnNames.y) : options.push(data[i].name)
    }
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

const initStaticChart = (el, data) => {
    const traces = data.data.slice();

    $.each(traces, (i, el) => {
        if (!el.hovertemplate) {
            el.hovertemplate = hovertemplate;
        }
    });

    data.data = traces;

    Plotly.newPlot(el[0], data.data, data.layout, config);
}

const initInteractiveChart = (el, data, combined = false, split_data_on) => {
    const all = 'All data';
    const traces = Array.from(data.data);
    const options = [];
    const isTreemap = data.data[0].type == 'treemap';
    const isGroupedTransform = getIsGroupedTransform(traces);

    // hide the legend
    data.layout.showlegend = false;

    $.each(traces, (i, el) => {
        if (!el.hovertemplate) {
            el.hovertemplate = hovertemplate;
        }
    });

    // add an extra all data option at the top if combined
    if (combined) {
        options.push(all);
    }

    // test if data is grouped
    if (isGroupedTransform) {
        // if so get unique options
        Array.prototype.push.apply(options, getGroupedTransformOptions(traces));
    }
    else {
        // otherwise add the individual data options
        Array.prototype.push.apply(options, getSplitDataOptions(traces, isTreemap));
    }

    // if not combined, select the first data set only
    if (!combined) {
        if (isGroupedTransform) {
            data.data = getGroupedTransformData(JSON.parse(JSON.stringify(traces)), options[0]);
        }
        else {
            data.data = [traces[0]];
        }
    }

    // get the select and assign options
    const dataSelector = el.closest('.chart-container').find('.data-selector')[0];
    assignOptions(dataSelector, options);

    // assign change event listener
    dataSelector.addEventListener('change', updateData, false);

    function updateData() {

        // if all data selected, set data to whole set
        if (dataSelector.value == all) {
            data.data = Array.from(traces);
        }

        // otherwise find matching index and set data to the selected one
        else {
            if (isGroupedTransform) {
                data.data = getGroupedTransformData(JSON.parse(JSON.stringify(traces)), dataSelector.value);
            }
            else {
                data.data = getSplitData(traces, dataSelector.value, isTreemap);
            }
        }

        // update the chart
        Plotly.react(el[0], data);
    }

    // initialise the chart
    Plotly.newPlot(el[0], data.data, data.layout, config);

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
