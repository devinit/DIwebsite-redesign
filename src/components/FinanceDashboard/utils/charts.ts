import { colours, generateDataset, getQuarterYear } from '../../../dashboard/utils';
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
    ],
  },
];
