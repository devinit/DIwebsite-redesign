import { colours } from '../';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const comms: DashboardGrid[] = [
  {
    id: '1',
    columns: 3,
    content: [
      {
        id: 'bounce-rate',
        meta: 'Bounce rate on the website (mean)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            // generateObjectDataset(data.filter(({ metric }) => metric === 'Bounce rate on the website (mean)'));

            return [
              {
                quarter: '2020 Q1',
                'Bounce rate on the website (mean)': 12,
              },
              {
                quarter: '2020 Q2',
                'Bounce rate on the website (mean)': 23,
              },
              {
                quarter: '2020 Q3',
                'Bounce rate on the website (mean)': 8,
              },
              {
                quarter: '2020 Q4',
                'Bounce rate on the website (mean)': 10,
              },
            ];
          },
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: { show: false },
            dataset: {
              dimensions: ['quarter', 'Bounce rate on the website (mean)'],
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
            xAxis: { type: 'category', boundaryGap: true, axisTick: { alignWithLabel: true } },
            yAxis: { type: 'value', scale: true, splitNumber: 3 },
            series: [{ type: 'line' }],
          },
        },
      },
      {
        id: 'dwell-time',
        meta: 'Dwell time on the website (mean)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            // generateObjectDataset(data.filter(({ metric }) => metric === 'Dwell time on the website (mean)'));
            return [
              {
                quarter: '2020 Q1',
                'Dwell time on the website (mean)': 12,
              },
              {
                quarter: '2020 Q2',
                'Dwell time on the website (mean)': 23,
              },
              {
                quarter: '2020 Q3',
                'Dwell time on the website (mean)': 21,
              },
              {
                quarter: '2020 Q4',
                'Dwell time on the website (mean)': 29,
              },
            ];
          },
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: { show: false },
            dataset: {
              dimensions: ['quarter', 'Dwell time on the website (mean)'],
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
            xAxis: { type: 'category', boundaryGap: true, axisTick: { alignWithLabel: true } },
            yAxis: { type: 'value', scale: true, splitNumber: 3 },
            series: [{ type: 'line' }],
          },
        },
      },
      {
        id: 'seo',
        meta: 'Average SEO ranking',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            // generateObjectDataset(data.filter(({ metric }) => metric === 'Average SEO ranking'));

            return [
              {
                quarter: '2020 Q1',
                'Average SEO ranking': 80,
              },
              {
                quarter: '2020 Q2',
                'Average SEO ranking': 84,
              },
              {
                quarter: '2020 Q3',
                'Average SEO ranking': 94,
              },
              {
                quarter: '2020 Q4',
                'Average SEO ranking': 90,
              },
            ];
          },
          options: {
            color: colours,
            tooltip: {
              trigger: 'axis',
            },
            legend: { show: false },
            dataset: {
              dimensions: ['quarter', 'Average SEO ranking'],
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
            xAxis: { type: 'category', boundaryGap: true, axisTick: { alignWithLabel: true } },
            yAxis: { type: 'value', scale: true, splitNumber: 3 },
            series: [{ type: 'line' }],
          },
        },
      },
    ],
  },
  {
    id: '2',
    columns: 2,
    content: [
      {
        id: 'engagement-rate',
        meta: 'Social media engagement rate',
        styled: true,
        chart: {
          data: (): Record<string, React.ReactText>[] => {
            return [
              {
                quarter: '2020 Q1',
                'Twitter engagement rate': 80,
                'Linkedin engagement rate': 45,
              },
              {
                quarter: '2020 Q2',
                'Twitter engagement rate': 84,
                'Linkedin engagement rate': 23,
              },
              {
                quarter: '2020 Q3',
                'Twitter engagement rate': 94,
                'Linkedin engagement rate': 60,
              },
              {
                quarter: '2020 Q4',
                'Twitter engagement rate': 90,
                'Linkedin engagement rate': 34,
              },
            ];
          },
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
              dimensions: ['quarter', 'Twitter engagement rate', 'Linkedin engagement rate'],
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
    ],
  },
];
