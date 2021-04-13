import { colours, toPounds } from '../';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const fundraising: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'contract-income',
        meta: 'Income Secured From Contracts (Q1 2021)',
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
        id: 'grant-income',
        meta: 'Income Secured From Grants (Q1 2021)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          console.log(data);

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
    id: '2',
    columns: 2,
    content: [
      {
        id: 'ops-dropped',
        meta: 'Total number of ops dropped due to capacity constraints',
        styled: true,
        chart: {
          data: (): Record<string, React.ReactText>[] => {
            // generateObjectDataset(data.filter(({ metric }) => metric === 'Income secured this quarter')),
            return ['2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4'].map((quarter) => ({
              quarter,
              contracts: 6,
              grants: 9,
            }));
          },
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {
              formatter: (name): string => (name === 'contracts' ? 'Contracts' : 'Grants'),
            },
            dataset: {
              dimensions: ['quarter', 'contracts', 'grants'],
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
            xAxis: { type: 'category' },
            yAxis: { type: 'value', splitNumber: 3 },
            series: [{ type: 'line' }, { type: 'line' }],
          },
        },
      },
      {
        id: 'proposals',
        meta: 'Total value of proposals submitted in quarter',
        styled: true,
        chart: {
          data: (): Record<string, React.ReactText>[] => {
            // generateObjectDataset(data.filter(({ metric }) => metric === 'Income secured this quarter')),
            return ['2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4'].map((quarter) => ({
              quarter,
              contracts: 12000,
              grants: 34567,
            }));
          },
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {
              formatter: (name): string => (name === 'contracts' ? 'Contracts' : 'Grants'),
            },
            dataset: {
              dimensions: ['quarter', 'contracts', 'grants'],
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
            xAxis: { type: 'category' },
            yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '£{value}' } },
            series: [{ type: 'bar' }, { type: 'bar' }],
          },
        },
      },
    ],
  },
];
