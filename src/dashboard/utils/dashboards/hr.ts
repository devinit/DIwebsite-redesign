import { generateObjectDataset } from '../';
import { DashboardData, DashboardGrid } from '../../../utils/types';

const colours = ['#0c457b', '#0071b1', '#4397d3', '#00538e', '#88bae5', '#0089cc']; // shades of blue
export const hr: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'staff',
        meta: 'Ratio of Staff to Leavers',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(
              data.filter(({ metric }) => metric === 'Total Staff' || metric === 'Total leavers in the period'),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: {},
            dataset: {
              dimensions: ['quarter', 'Total Staff', 'Total leavers in the period'],
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
            series: [
              { type: 'bar', stack: 'hr' },
              { type: 'bar', stack: 'hr' },
            ],
          },
        },
      },
      {
        id: 'stability',
        meta: 'Stability Index',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(data.filter(({ metric }) => metric === 'Stability Index')),
          options: {
            color: colours,
            tooltip: {
              show: false,
              trigger: 'axis',
            },
            legend: { show: false },
            dataset: {
              dimensions: ['quarter', 'Stability Index'],
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
            yAxis: { type: 'value', show: false, splitNumber: 3 },
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
