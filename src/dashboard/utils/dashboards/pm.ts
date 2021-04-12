import { colours, generateArrayDataset } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const projectManagement: DashboardGrid[] = [
  {
    id: '0',
    columns: 1,
    content: [
      {
        id: 'iati-title',
        meta: 'Ranking on IATI dashboard (suggest move from top 10% to top 5%)',
      },
    ],
  },
  {
    id: '2',
    columns: 4,
    content: [
      {
        id: 'iati-q1',
        meta: 'Q4 2020',
        styled: true,
        title: (): React.ReactText => {
          // TODO: Use actual value here

          return '1%';
        },
      },
      {
        id: 'iati-q2',
        meta: 'Q1 2021',
        styled: true,
        title: (): React.ReactText => {
          // TODO: Use actual value here

          return '1%';
        },
      },
    ],
  },
  {
    id: '2',
    columns: 4,
    content: [
      {
        id: 'active-projects-dipr',
        meta: 'Active Projects DIPR',
        styled: true,
        title: (): React.ReactText => {
          // TODO: Use actual value here

          return 5;
        },
      },
      {
        id: 'active-projects-dii',
        meta: 'Active Projects DII',
        styled: true,
        title: (): React.ReactText => {
          // TODO: Use actual value here

          return 3;
        },
      },
    ],
  },
  {
    id: '3',
    columns: 2,
    content: [
      {
        id: 'project-status',
        meta: 'Project Status',
        styled: true,
        chart: {
          data: (data: DashboardData[]): React.ReactText[][] =>
            generateArrayDataset(
              data.filter(({ metric }) =>
                [
                  'Number of projects with Amber status',
                  'Number of projects with Green status',
                  'Number of projects with Red status',
                ].includes(metric),
              ),
            ),
          options: {
            color: colours,
            tooltip: { trigger: 'item', show: false },
            legend: { show: false, top: 'auto', bottom: 10 },
            dataset: {},
            grid: {
              left: '3%',
              right: '4%',
              top: '3%',
              containLabel: true,
            },
            toolbox: {
              feature: {
                saveAsImage: {},
              },
            },
            xAxis: { show: false, type: 'category' },
            yAxis: { show: false },
            /* eslint-disable @typescript-eslint/no-explicit-any,@typescript-eslint/explicit-module-boundary-types */
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
                label: {
                  show: true,
                  formatter: (params: any): string => {
                    const value = params.value[params.encode.value[0]];
                    switch (params.name) {
                      case 'Number of projects with Amber status':
                        return `Status Amber: ${value}`;
                      case 'Number of projects with Green status':
                        return `Status Green: ${value}`;
                      case 'Number of projects with Red status':
                        return `Status Red: ${value}`;

                      default:
                        return 'Status Unknown';
                    }
                  },
                },
              },
            ],
            /* eslint-enable @typescript-eslint/no-explicit-any,@typescript-eslint/explicit-module-boundary-types */
          },
        },
      },
      {
        id: 'project-spending',
        meta: 'Project Spending',
        styled: true,
        chart: {
          data: (data: DashboardData[]): React.ReactText[][] =>
            generateArrayDataset(
              data.filter(({ metric }) =>
                ['% projects overspending', '% projects underspending', '% projects on track'].includes(metric),
              ),
            ),
          options: {
            color: colours,
            tooltip: { trigger: 'item', show: false },
            legend: { show: false, top: 'auto', bottom: 10 },
            dataset: {},
            grid: {
              left: '3%',
              right: '4%',
              top: '3%',
              containLabel: true,
            },
            toolbox: {
              feature: {
                saveAsImage: {},
              },
            },
            xAxis: { show: false, type: 'category' },
            yAxis: { show: false },
            /* eslint-disable @typescript-eslint/no-explicit-any,@typescript-eslint/explicit-module-boundary-types */
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
                label: {
                  show: true,
                  formatter: (params: any): string => {
                    const value = params.value[params.encode.value[0]];
                    switch (params.name) {
                      case '% projects overspending':
                        return `Overspending: ${value}%`;
                      case '% projects underspending':
                        return `Underspending: ${value}%`;
                      case '% projects on track':
                        return `On Track: ${value}%`;

                      default:
                        return 'Expenditured Unknown';
                    }
                  },
                },
              },
            ],
            /* eslint-enable @typescript-eslint/no-explicit-any,@typescript-eslint/explicit-module-boundary-types */
          },
        },
      },
    ],
  },
];
