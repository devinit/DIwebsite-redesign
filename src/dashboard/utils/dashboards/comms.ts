import { getAggregatedDatasetSource } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';
import { getEventHandlers, grid } from '../chart';

const colours = ['#7d4712', '#a85d00', '#df8000', '#f9b865', '#feedd4'];
const dashboardMetrics = ['Bounce rate on the website (%)'];

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

                return `${(value as any)[seriesName!]}%`; // eslint-disable-line
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
    ],
  },
  {
    id: '2',
    columns: 3,
    content: [
      {
        id: 'bounce-rate',
        meta: 'Bounce rate on the website (%)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Bounce rate on the website (%)';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric.trim() === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}%` : 'None';
        },
      },
      {
        id: 'dwell-time',
        meta: 'Dwell time on the website (minutes)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Dwell time on the website (minutes)';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric.trim() === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}` : 'None';
        },
      },
      {
        id: 'seo',
        meta: 'Overall on-page SEO score',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Overall on-page SEO score';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric.trim() === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}` : 'None';
        },
      },
      {
        id: 'twitter',
        meta: 'Twitter engagement rate',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Twitter engagement rate';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric.trim() === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}%` : 'None';
        },
      },
      {
        id: 'linkedin',
        meta: 'Linkedin engagement rate',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Linkedin engagement rate';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric.trim() === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}%` : 'None';
        },
      },
    ],
  },
];
