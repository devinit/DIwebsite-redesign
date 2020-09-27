import { DIChart } from './dicharts';
import { DIChartConfig, DIChartPlotlyOptions } from './utils';
import { DIPlotlyChart } from './plotly';

export const handler = (function () {
  const charts: DIChartConfig[] = [];

  const getElementsByClassName = (className: string) => {
    if (!className) {
      throw new Error('An indentifying class for the element is required');
    }

    return document.querySelectorAll(`.${className}:not(.dicharts-handler--active)`);
  };
  const handlePlotly = (chartNode: HTMLElement, config: DIChartPlotlyOptions) => {
    const manager = new DIPlotlyChart(chartNode, config);
    manager.showLoading();
    manager.setLayout(config.layout).setConfig(config.config);
    if (config.data && config.data.length) {
      manager
        .setData(config.data)
        .updatePlot()
        .then(({ plot }) => {
          console.log(plot); // TODO: add event property to call when new plot is created
        });
    } else if (config.csv) {
      manager.csv(config.csv.url).then((data) => {
        config.csv?.onFetch(data, config, manager);
      });
    }
  };
  const init = (chart: DIChartConfig) => {
    const chartNodes = getElementsByClassName(chart.className);
    Array.prototype.forEach.call(chartNodes, (chartNode: HTMLElement) => {
      chartNode.classList.add('dicharts-handler--active');
      if (chart.plotly) {
        handlePlotly(chartNode, chart.plotly);
      }
    });
  };

  return {
    addChart: (chart: DIChartConfig) => {
      charts.push(chart);
      if (chart.onAdd) {
        chart.onAdd(chart);
      }
      init(chart);
    },
    getCharts: () => charts,
  };
})();

export { DIChart as Chart };
