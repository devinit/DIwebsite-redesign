import { colours, generateArrayDataset, generateObjectDataset } from '../';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const projectManagement: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'staff',
        meta: 'Project Status',
        chart: {
          data: (data: DashboardData[]): React.ReactText[][] => {
            const test = generateArrayDataset(
              data.filter(({ metric }) =>
                [
                  'Number of projects with Amber status',
                  'Number of projects with Green status',
                  'Number of projects with Red status',
                ].includes(metric),
              ),
            );
            console.log(test);

            return test;
          },
          options: {
            color: colours,
            tooltip: {
              trigger: 'item',
            },
            legend: { show: false },
            dataset: {},
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
            xAxis: { show: false, type: 'category' },
            yAxis: { show: false },
            series: [
              {
                type: 'pie',
                id: 'pie',
                radius: '65%',
                center: ['50%', '50%'],
                encode: {
                  itemName: 'metric',
                  value: '2020 Q4',
                  tooltip: '2020 Q4',
                },
              },
            ],
          },
        },
      },
    ],
  },
];
