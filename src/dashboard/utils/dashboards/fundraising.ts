import { toPounds } from '../';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const fundraising: DashboardGrid[] = [
  {
    id: '1',
    columns: 1,
    content: [
      {
        id: 'contracts',
        meta: 'Contracts - Q1 2021',
      },
    ],
  },
  {
    id: '2',
    columns: 2,
    content: [
      {
        id: 'contract-income',
        meta: 'Income Secured - Q1 2021',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Income secured this quarter';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Contracts' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
      {
        id: 'contract-weighted',
        meta: 'Weighted value 50/80% probable pipeline at end of quarter',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Weighted value 50/80% probable pipeline at end of quarter';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Contracts' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
  {
    id: '3',
    columns: 1,
    content: [
      {
        id: 'grants',
        meta: 'Grants - Q1 2021',
      },
    ],
  },
  {
    id: '4',
    columns: 4,
    content: [
      {
        id: 'grant-income-secured',
        meta: 'Income Secured',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Income secured this quarter';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
  {
    id: '5',
    columns: 1,
    className: 'm-pills',
    content: [
      {
        id: 'grant-income',
        meta: 'Income at 90% at end of quarter (waiting for agreement to be signed for 2021-2023)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Income at 90% at end of quarter (waiting for agreement to be signed for 2021-2023)';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
  {
    id: '6',
    columns: 1,
    className: 'm-pills',
    content: [
      {
        id: 'grant-weighted',
        meta: 'Weighted value of 50% & 80% probable pipeline at end of quarter (income 2021-2023)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Weighted value of 50% & 80% probable pipeline at end of quarter (income 2021-2023)';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
  {
    id: '7',
    columns: 2,
    content: [
      {
        id: 'grant-speculative',
        meta: 'Speculative pipeline value, not weighted (>50% probable)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Speculative pipeline value, not weighted (>50% probable)';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
];
