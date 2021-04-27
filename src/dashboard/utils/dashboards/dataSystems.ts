import { getAggregatedDatasetSource } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';
import { getEventHandlers, grid, tootipFormatter } from '../chart';

const colours = ['#302b2e', '#555053', '#736e73', '#a9a6aa', '#d9d4da'];
const dashboardMetrics = [
  'Roadmap in place for global Infrastructure with capacity for growth',
  'Fully hosted systems with reduced internal reliance',
  'Standardised global support',
];

export const dataSystems: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'global-infrastructure',
        meta: `${dashboardMetrics[0]} (Progress indicator %)`,
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
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[0]),
        },
      },
      {
        id: 'hosted-systems',
        meta: `${dashboardMetrics[1]} (Progress Indicator %)`,
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[1])),
          options: {
            color: colours,
            tooltip: {
              show: true,
              trigger: 'item',
              formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                const { value, seriesName } = params;

                if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                  return `${(value as any)[seriesName]}%`; // eslint-disable-line
                }

                return 'No Data';
              },
            },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[1]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[1]),
        },
      },
      {
        id: 'global-support',
        meta: `${dashboardMetrics[2]} (Progress Indicator %)`,
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[2])),
          options: {
            color: colours,
            tooltip: {
              show: true,
              trigger: 'item',
              formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                const { value, seriesName } = params;

                if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                  return `${(value as any)[seriesName]}%`; // eslint-disable-line
                }

                return 'No Data';
              },
            },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[2]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[2]),
        },
      },
    ],
  },
];
