import { colours, generateObjectDataset } from '../';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const financeDashboard: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'project-time',
        meta: 'Proportion of staff time spent on projects',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(
              data.filter(({ metric }) => metric === 'Non-Overhead staff' || metric === 'All staff'),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {},
            dataset: {
              dimensions: ['quarter', 'Non-Overhead staff', 'All staff', 'Target'],
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
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(
              data.filter(({ metric }) => metric === 'Direct overheads' || metric === 'Indirect overheads'),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {},
            dataset: {
              dimensions: ['quarter', 'Direct overheads', 'Indirect overheads', 'Target'],
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
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(
              data.filter(
                ({ metric }) =>
                  metric === 'Consultants as proportion of income' || metric === 'Salary as proportion of income',
              ),
            ),
          options: {
            color: colours,
            tooltip: {
              show: false,
              trigger: 'axis',
            },
            legend: {
              top: '10%',
            },
            dataset: {
              dimensions: ['quarter', 'Consultants as proportion of income', 'Salary as proportion of income'],
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
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            /* eslint-disable @typescript-eslint/no-explicit-any */
            series: [
              {
                type: 'bar',
                label: {
                  show: true,
                  position: 'top',
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                },
              },
              {
                type: 'bar',
                label: {
                  show: true,
                  position: 'top',
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                },
              },
            ],
            /* eslint-enable @typescript-eslint/no-explicit-any */
          },
        },
      },
      {
        id: 'consultant-costs',
        meta: 'Consultant costs %, YTD (excluding GNR)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(
              data.filter(({ metric }) => metric === 'Average consultant % for year to date (excl GNR)'),
            ),
          options: {
            color: colours,
            tooltip: { show: false, trigger: 'axis' },
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
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            /* eslint-disable @typescript-eslint/no-explicit-any */
            series: [
              {
                type: 'bar',
                label: {
                  show: true,
                  position: 'top',
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                },
              },
            ],
            /* eslint-enable @typescript-eslint/no-explicit-any */
          },
        },
      },
    ],
  },
];
