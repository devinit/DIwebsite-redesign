import { getAggregatedDatasetSource } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';
import { getEventHandlers, grid } from '../chart';

const colours = ['#7d4712', '#a85d00', '#df8000', '#f9b865', '#feedd4'];
const dashboardMetrics = [
  'Bounce rate on the website (%)',
  'Dwell time on the website (minutes)',
  'Overall on-page SEO score',
  'Twitter engagement rate',
  'Linkedin engagement rate',
];

export const comms: DashboardGrid[] = [
  {
    id: '1',
    columns: 3,
    content: [
      {
        id: 'bounce-rate',
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
              formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                const { value, seriesName } = params;

                if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                  return `${(value as any)[seriesName]}%`; // eslint-disable-line
                }

                return 'No Data';
              },
            },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[0]) },
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
        id: 'dwell-time',
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
              formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                const { value, seriesName } = params;

                if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                  return `${(value as any)[seriesName]}`; // eslint-disable-line
                }

                return 'No Data';
              },
            },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[1]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[1]),
        },
      },
      {
        id: 'seo-score',
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
              formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                const { value, seriesName } = params;

                if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                  return `${(value as any)[seriesName]}`; // eslint-disable-line
                }

                return 'No Data';
              },
            },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[2]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[2]),
        },
      },
      {
        id: 'twitter-engagement',
        meta: dashboardMetrics[3],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[3])),
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
            dataset: { dimensions: ['year'].concat(dashboardMetrics[3]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[3]),
        },
      },
      {
        id: 'linkedin-engagement',
        meta: dashboardMetrics[4],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[4])),
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
            dataset: { dimensions: ['year'].concat(dashboardMetrics[4]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[4]),
        },
      },
    ],
  },
];
