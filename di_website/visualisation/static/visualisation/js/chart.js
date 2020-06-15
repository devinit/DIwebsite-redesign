"use strict";
const initPlotlyChart = () => {
    const wrappers = document.getElementsByClassName('plotly-chart-wrapper');
    for (let index = 0; index < wrappers.length; index++) {
        const element = wrappers.item(index);
        if (element) {
            const chartNode = element.getElementsByClassName('plotly-chart')[0] || undefined;
            const inputNode = element.getElementsByClassName('plotly-chart-input')[0] || undefined;
            if (chartNode && inputNode) {
                const options = inputNode.value;
                try {
                    const { data, layout } = JSON.parse(options);
                    Plotly.newPlot(element, data, layout);
                }
                catch (error) {
                    console.log(error);
                }
            }
        }
    }
};
initPlotlyChart();
