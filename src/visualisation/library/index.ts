import { DICharts } from './dicharts';
import { DIChartConfig } from './utils';

export const handler = (() => {
  const charts: DIChartConfig[] = [];

  const getElementsByClassName = (className: string) => {
    if (!className) {
      throw new Error('An indentifying class for the element is required');
    }

    return document.querySelectorAll(`.${className}:not(.dicharts-handler--active)`);
  };
  const init = (chart: DIChartConfig) => {
    const chartNodes = getElementsByClassName(chart.className);
    Array.prototype.forEach.call(chartNodes, (chartNode: HTMLElement) => {
      chartNode.classList.add('dicharts-handler--active');
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

export { DICharts as Chart };
