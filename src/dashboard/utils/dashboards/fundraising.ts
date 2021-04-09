import { finance, datatype } from 'faker';
import { colours } from '../';
import { DashboardGrid } from '../../../utils/types';

export const fundraising: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'income',
        meta: 'Income Secured',
        styled: true,
        chart: {
          data: (): Record<string, React.ReactText>[] => {
            // generateObjectDataset(data.filter(({ metric }) => metric === 'Income secured this quarter')),
            return ['2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4'].map((quarter) => ({
              quarter,
              contracts: finance.amount(),
              grants: finance.amount(),
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
      {
        id: 'ops-dropped',
        meta: 'Total number of ops dropped due to capacity constraints',
        styled: true,
        chart: {
          data: (): Record<string, React.ReactText>[] => {
            // generateObjectDataset(data.filter(({ metric }) => metric === 'Income secured this quarter')),
            return ['2020 Q1', '2020 Q2', '2020 Q3', '2020 Q4'].map((quarter) => ({
              quarter,
              contracts: datatype.number(10),
              grants: datatype.number(10),
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
              contracts: finance.amount(),
              grants: finance.amount(),
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
