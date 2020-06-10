import $ from 'jquery';

export default function entry() {
    initChart('#iha-donors-public-area');
    initChart('#iha-donors-public-bar');
}

const initChart = (selector) => {
    const el = $(selector);
    Plotly.d3.json(el.first().data('url'), d => {

        const data = d;
        const traces = data.data.slice();
        data.data = data.data.slice(0, 1);

        const options = [];

        for (var i = 0; i < traces.length; i++ ) {
            options.push(traces[i].meta.columnNames.y);
        }

        function assignOptions(textArray, selector) {
            for (var i = 0; i < textArray.length;  i++) {
                var currentOption = document.createElement('option');
                currentOption.text = textArray[i];
                selector.appendChild(currentOption);
            }
        }

        Plotly.newPlot(el[0], data);

        const dataSelector = el.closest('.chart-container').find('.data-selector')[0];
        assignOptions(options, dataSelector);

        function updateData() {
            const newDataIndex = traces.findIndex(element => element.meta.columnNames.y == dataSelector.value);
            data.data = [traces[newDataIndex]];
            Plotly.react(el[0], data);
        }

        dataSelector.addEventListener('change', updateData, false);

    });
}
