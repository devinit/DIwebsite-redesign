const initPlotlyChart = async () => {
    const wrappers = document.getElementsByClassName('plotly-chart-wrapper');
    if (wrappers.length) {
        const { newPlot, register } = await import('plotly.js/lib/core');
        register([ await import('plotly.js/lib/bar' as any), await import('plotly.js/lib/scatter' as any) ]);

        for (let index = 0; index < wrappers.length; index++) {
            const element = wrappers.item(index) as HTMLElement;
            if (element) {
                const chartNode = element.getElementsByClassName('plotly-chart')[0] as HTMLDivElement || undefined;
                const inputNode = element.getElementsByClassName('plotly-chart-input')[0] as HTMLInputElement || undefined;
                if (chartNode && inputNode) {
                    const options = inputNode.value;
                    try {
                        const { data, layout } = JSON.parse(options);
                        newPlot(element, data, layout);
                    }
                    catch (error) {
                        console.log(error);
                    }
                }
            }
        }
    }
};

initPlotlyChart();
