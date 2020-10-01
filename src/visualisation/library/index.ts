import { DIChart } from './dicharts';
import { DIChartConfig, DIChartPlotlyOptions, DIChartEChartOptions } from './utils';
import { DIPlotlyChart } from './plotly';
import { DIEChart } from './echarts';

export const handler = (function () {
  const charts: DIChartConfig[] = [];

  const getElementsByClassName = (className: string) => {
    if (!className) {
      throw new Error('An indentifying class for the element is required');
    }

    return document.querySelectorAll(`.${className}:not(.dicharts-handler--active)`);
  };
  const onAdd = (chart: DIChartConfig, nodes: NodeListOf<Element>) => {
    if (chart.plotly && chart.plotly.onAdd) {
      chart.plotly.onAdd(nodes);
    }
    if (chart.d3 && chart.d3.onAdd) {
      chart.d3.onAdd(nodes);
    }
    if (chart.echarts && chart.echarts.onAdd) {
      chart.echarts.onAdd(nodes);
    }
  };
  const handlePlotly = (chartNode: HTMLElement, config: DIChartPlotlyOptions) => {
    const manager = new DIPlotlyChart(chartNode, config);
    manager.showLoading();
    manager.setLayout(config.layout).setConfig(config.config);
    if (config.data && config.data.length) {
      manager.setData(config.data).updatePlot();
    } else if (config.csv) {
      manager.csv(config.csv.url).then((data) => {
        manager.setSourceData(data);
        config.csv?.onFetch(data, config, manager);
      });
    }
  };
  const handleEChart = (chartNode: HTMLElement, config: DIChartEChartOptions) => {
    const manager = new DIEChart(chartNode, config);
    manager.showLoading();
    if (config.csv) {
      manager.csv(config.csv.url).then((data) => {
        manager.setSourceData(data);
        config.csv?.onFetch(data, manager);
      });
    }
    if (config.onInit) {
      config.onInit(manager);
    }
  };
  const init = (chart: DIChartConfig) => {
    const chartNodes = getElementsByClassName(chart.className);
    onAdd(chart, chartNodes);
    Array.prototype.forEach.call(chartNodes, (chartNode: HTMLElement) => {
      chartNode.classList.add('dicharts-handler--active');
      if (chart.plotly) {
        handlePlotly(chartNode, chart.plotly);
      } else if (chart.echarts) {
        handleEChart(chartNode, chart.echarts);
      }
    });
  };

  return {
    addChart: (chart: DIChartConfig) => {
      charts.push(chart);
      init(chart);
    },
    getCharts: () => charts,
  };
})();

export { DIChart as Chart };
