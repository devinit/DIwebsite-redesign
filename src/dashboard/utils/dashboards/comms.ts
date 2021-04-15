import { DashboardData, DashboardGrid } from '../../../utils/types';

// const colours = ['#7d4712', '#a85d00', '#df8000', '#f9b865', '#feedd4'];
export const comms: DashboardGrid[] = [
  {
    id: '1',
    columns: 1,
    content: [
      {
        id: 'comms-title',
        meta: 'Q1 2021',
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
