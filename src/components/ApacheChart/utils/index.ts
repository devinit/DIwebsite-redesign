import deepmerge from 'deepmerge';
import { colours } from '../../../dashboard/utils';
import { defaultOptions } from '../../../utils/echarts';

export const renderChart = async (node: HTMLDivElement, option: echarts.EChartOption): Promise<void> => {
  const { init } = await import('echarts');
  const chart = init(node);
  chart.setOption(deepmerge(defaultOptions, option));
};

export const makeBasicLineChart = async (node: HTMLDivElement): Promise<void> => {
  const { init } = await import('echarts');
  const chart = init(node);
  const option: echarts.EChartOption = {
    color: colours,
    tooltip: {
      trigger: 'axis',
    },
    legend: {
      data: ['Step Start', 'Step Middle', 'Step End'],
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true,
    },
    toolbox: {
      feature: {
        saveAsImage: {},
      },
    },
    xAxis: {
      type: 'category',
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        name: 'Step Start',
        type: 'line',
        step: 'start',
        data: [120, 132, 101, 134, 90, 230, 210],
      },
      {
        name: 'Step Middle',
        type: 'line',
        step: 'middle',
        data: [220, 282, 201, 234, 290, 430, 410],
      },
      {
        name: 'Step End',
        type: 'line',
        step: 'end',
        data: [450, 432, 401, 454, 590, 530, 510],
      },
    ],
  };
  chart.setOption(deepmerge(defaultOptions, option));
};

export const renderBasicColumnChart = async (node: HTMLDivElement): Promise<void> => {
  const { init } = await import('echarts');
  const chart = init(node);
  const option: echarts.EChartOption = {
    color: colours,
    legend: {},
    tooltip: {},
    dataset: {
      dimensions: ['product', '2015', '2016', '2017'],
      source: [
        { product: 'Matcha Latte', '2015': 43.3, '2016': 85.8, '2017': 93.7 },
        { product: 'Milk Tea', '2015': 83.1, '2016': 73.4, '2017': 55.1 },
        { product: 'Cheese Cocoa', '2015': 86.4, '2016': 65.2, '2017': 82.5 },
        { product: 'Walnut Brownie', '2015': 72.4, '2016': 53.9, '2017': 39.1 },
      ],
    },
    xAxis: { type: 'category' },
    yAxis: {},
    // Declare several bar series, each will be mapped
    // to a column of dataset.source by default.
    series: [{ type: 'bar' }, { type: 'bar' }, { type: 'bar' }],
  };
  chart.setOption(deepmerge(defaultOptions, option));
};

export const renderBasicPieChart = async (node: HTMLDivElement): Promise<void> => {
  const { init } = await import('echarts');
  const chart = init(node);
  const option: echarts.EChartOption = {
    color: colours,
    legend: {
      top: 'bottom',
    },
    toolbox: {
      show: true,
      feature: {
        mark: { show: true },
        dataView: { show: true, readOnly: false },
        restore: { show: true },
        saveAsImage: { show: true },
      },
    },
    xAxis: { show: false },
    yAxis: { show: false },
    series: [
      {
        name: 'Rose',
        type: 'pie',
        radius: '65%',
        center: ['50%', '50%'],
        label: {
          show: true,
        },
        data: [
          { value: 40, name: 'rose 1' },
          { value: 38, name: 'rose 2' },
          { value: 32, name: 'rose 3' },
          { value: 30, name: 'rose 4' },
        ],
      },
    ],
  };
  chart.setOption(deepmerge(defaultOptions, option));
};
