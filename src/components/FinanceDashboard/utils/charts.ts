import { colours, generateDataset } from '../../../dashboard/utils';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const grids: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'project-time',
        meta: 'Proportion of staff time spent on projects',
        chart: {
          data: (data: DashboardData[]): Record<string, unknown>[] =>
            generateDataset(
              data.filter(
                ({ department, metric }) =>
                  department === 'Finance' && (metric === 'Non-Overhead Staff' || metric === 'All Staff'),
              ),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {},
            dataset: {
              dimensions: ['quarter', 'Non-Overhead Staff', 'All Staff', 'Target'],
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
            yAxis: { type: 'value', scale: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [
              { type: 'line' },
              { type: 'line' },
              {
                type: 'line',
                symbol: 'none',
                lineStyle: { type: 'dashed', color: '#333' },
                itemStyle: { color: '#333' },
              },
            ],
          },
        },
      },
      {
        id: 'overhead-time',
        meta: 'Proportion of time spent on direct and indirect overheads',
        chart: {
          data: (data: DashboardData[]): Record<string, unknown>[] =>
            generateDataset(
              data.filter(
                ({ department, metric }) =>
                  department === 'Finance' && (metric === 'Direct Overheads' || metric === 'Indirect Overheads'),
              ),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {},
            dataset: {
              dimensions: ['quarter', 'Direct Overheads', 'Indirect Overheads', 'Target'],
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
            yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [
              { type: 'bar' },
              { type: 'bar' },
              {
                type: 'line',
                symbol: 'none',
                lineStyle: { type: 'dashed', color: '#333' },
                itemStyle: { color: '#333' },
              },
            ],
          },
        },
      },
      {
        id: 'personnel-costs',
        meta: 'Personnel costs as a proporation of income (% of target)',
        chart: {
          data: (data: DashboardData[]): Record<string, unknown>[] =>
            generateDataset(
              data.filter(
                ({ department, metric }) =>
                  department === 'Finance' &&
                  (metric === 'Consultants as proportion of income' || metric === 'Salary as a proportion of income'),
              ),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {
              top: '10%',
            },
            dataset: {
              dimensions: ['quarter', 'Consultants as proportion of income', 'Salary as a proportion of income'],
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
            yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }, { type: 'bar' }],
          },
        },
      },
      {
        id: 'consultant-costs',
        meta: 'Consultant costs %, YTD (excluding GNR)',
        chart: {
          data: (data: DashboardData[]): Record<string, unknown>[] =>
            generateDataset(
              data.filter(
                ({ department, metric }) =>
                  department === 'Finance' && metric === 'Average consultant % for year to date (excl GNR)',
              ),
            ),
          options: {
            color: colours,
            tooltip: { trigger: 'axis' },
            legend: { show: false },
            dataset: {
              dimensions: ['quarter', 'Average consultant % for year to date (excl GNR)'],
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
            yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }],
          },
        },
      },
    ],
  },
];
