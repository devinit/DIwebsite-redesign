import { getAggregatedDatasetSource } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';
import { getBarLabelConfig, getEventHandlers, grid, tootipFormatter } from '../chart';

const colours = ['#302b2e', '#555053', '#736e73', '#a9a6aa', '#d9d4da'];
const dashboardMetrics = [
  'Roadmap in place for global Infrastructure with capacity for growth (Progress Indicator)',
  'Fully hosted systems with reduced internal reliance (Progress Indicator)',
  'Standardised global support (Progress Indicator)',
];

export const dataSystems: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'global-infrastructure',
        meta: dashboardMetrics[0],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[0])),
          options: {
            color: colours,
            tooltip: {
              show: true,
              trigger: 'item',
              formatter: tootipFormatter({ suffix: '%' }),
            },
            legend: { show: false },
            dataset: {
              dimensions: ['year'].concat(dashboardMetrics[0]),
            },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [
              {
                type: 'bar',
                label: getBarLabelConfig({ suffix: '%' }),
              },
            ],
          },
          ...getEventHandlers(dashboardMetrics[0]),
        },
      },
      {
        id: 'hosted-systems',
        meta: dashboardMetrics[1],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[1])),
          options: {
            color: colours,
            tooltip: {
              show: true,
              trigger: 'item',
              formatter: tootipFormatter({ suffix: '%' }),
            },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[1]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar', label: getBarLabelConfig({ suffix: '%' }) }],
          },
          ...getEventHandlers(dashboardMetrics[1]),
        },
      },
      {
        id: 'global-support',
        meta: dashboardMetrics[2],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[2])),
          options: {
            color: colours,
            tooltip: {
              show: true,
              trigger: 'item',
              formatter: tootipFormatter({ suffix: '%' }),
            },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[2]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar', label: getBarLabelConfig({ suffix: '%' }) }],
          },
          ...getEventHandlers(dashboardMetrics[2]),
        },
      },
    ],
  },
];
