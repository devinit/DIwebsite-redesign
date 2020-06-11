import $ from 'jquery';

export default function entry() {
    $('.charts__chart').each((i, el) => {
        initChart($(el));
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
}

const initChart = (el) => {
    Plotly.d3.json(el.first().data('url'), d => {
        const data = d;
        const interactive = el.data('interactive');
        const combined = el.data('combined');

        if (!interactive) {
            initStaticChart(el[0], data);
        }
        else {
            initInteractiveChart(el[0], data, combined);
        }
    });
}

const initStaticChart = (el, data) => {
    Plotly.newPlot(el, data);
}

const initInteractiveChart = (el, data, combined = false) => {
    const all = 'All data';
    const traces = data.data.slice();
    const options = [];

    // add an extra all data option at the top if combined
    if (combined) {
        options.push(all);
    }

    // add the actual data options
    for (var i = 0; i < traces.length; i++ ) {
        options.push(traces[i].meta.columnNames.y);
    }

    // if not combined, select the first data set only
    if (!combined) {
        data.data = [traces[0]];
    }

    // get the select and assign options
    const dataSelector = el.closest('.chart-container').find('.data-selector')[0];
    assignOptions(dataSelector, options);

    // assign change event listener
    dataSelector.addEventListener('change', updateData, false);

    function updateData() {

        // if all data selected, set data to whole set
        if (dataSelector.value == all) {
            data.data = traces;
        }

        // otherwise find matching index and set data to the selected one
        else {
            const newDataIndex = traces.findIndex(element => element.meta.columnNames.y == dataSelector.value);
            data.data = [traces[newDataIndex]];
        }

        // update the chart
        Plotly.react(el[0], data);
    }

    // initialise the chart
    Plotly.newPlot(el[0], data);

}
