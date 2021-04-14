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
              data.filter(
                ({ metric, year }) =>
                  (metric === 'Total Staff' || metric === 'Total leavers in the period') && year === 2020,
              ),
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
            generateObjectDataset(data.filter(({ metric, year }) => metric === 'Stability Index' && year === 2020)),
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
          },
        },
      },
      {
        id: 'gender-pay-mean',
        meta: 'Gender Pay Gap (Mean)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(
              data.filter(
                ({ metric, quarter, year }) =>
                  metric.trim() === 'Gender Pay Gap (Mean)' &&
                  ((year === 2020 && quarter === 'Q4') || (year === 2021 && quarter === 'Q1')),
              ),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: { show: false },
            dataset: {
              dimensions: ['quarter', 'Gender Pay Gap (Mean)'],
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
            xAxis: { name: 'Gender Pay Gap (Mean)', show: false },
            yAxis: { type: 'category' },
            series: [
              {
                type: 'bar',
                encode: {
                  x: 'Gender Pay Gap (Mean)',
                  y: 'quarter',
                },
                label: {
                  show: true,
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.x[0]]]}%`,
                },
              },
            ],
          },
        },
      },
      {
        id: 'gender-pay-median',
        meta: 'Gender Pay Gap (Median)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            generateObjectDataset(
              data.filter(
                ({ metric, quarter, year }) =>
                  metric.trim() === 'Gender Pay Gap (Median)' &&
                  ((year === 2020 && quarter === 'Q4') || (year === 2021 && quarter === 'Q1')),
              ),
            ),
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: { show: false },
            dataset: {
              dimensions: ['quarter', 'Gender Pay Gap (Median)'],
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
            xAxis: {
              name: 'Gender Pay Gap (Median)',
              show: false,
            },
            yAxis: { type: 'category', show: true, axisTick: { alignWithLabel: true } },
            series: [
              {
                type: 'bar',
                label: {
                  show: true,
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.x[0]]]}%`,
                },
              },
            ],
          },
        },
      },
      /* eslint-enable @typescript-eslint/no-explicit-any */
    ],
  },
];
