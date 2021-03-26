import { colours, generateObjectDataset } from '../';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const hr: DashboardGrid[] = [
  {
    id: '1',
    columns: 1,
    content: [
      {
        id: 'staff',
        meta: 'Ratio of Staff and Leavers',
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
    ],
  },
];
