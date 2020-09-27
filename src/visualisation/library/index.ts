import { DIChart } from './dicharts';
import { DIChartConfig, DIChartPlotlyConfig } from './utils';
import { DIPlotlyChart } from './plotly';

export const handler = (function () {
  const charts: DIChartConfig[] = [];

  const getElementsByClassName = (className: string) => {
    if (!className) {
      throw new Error('An indentifying class for the element is required');
    }

    return document.querySelectorAll(`.${className}:not(.dicharts-handler--active)`);
  };
  const handlePlotly = (chartNode: HTMLElement, config: DIChartPlotlyConfig) => {
    const manager = new DIPlotlyChart(chartNode, config);
    if (config.data) {
      manager.newPlot(chartNode, config.data, config.layout, config.config).then(({ plot }) => {
        console.log(plot);
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
