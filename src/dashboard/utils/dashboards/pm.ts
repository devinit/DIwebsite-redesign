import { colours, generateArrayDataset } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';
import { hideNarrative, showNarrative } from '../chart';

export const projectManagement: DashboardGrid[] = [
  {
    id: '1',
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
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Ranking on IATI dashboard (suggest move from top 10% to top 5%)';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric === currentMetric && year === 2020 && quarter === 'Q4',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}%` : 'None';
        },
      },
      {
        id: 'iati-q2',
        meta: 'Q1 2021',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          console.log(data);

          const currentMetric = 'Ranking on IATI dashboard (suggest move from top 10% to top 5%)';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}%` : 'None';
        },
      },
    ],
  },
  {
    id: '3',
    columns: 1,
    content: [
      {
        id: 'projects-title',
        meta: 'Active Projects',
      },
    ],
  },
  {
    id: '4',
    columns: 4,
    content: [
      {
        id: 'active-projects-dipr',
        meta: 'DIPR (Q1 2021)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = '# active projects DIPR';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}` : 'None';
        },
      },
      {
        id: 'active-projects-dii',
        meta: 'DII (Q1 2021)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = '# active projects DII';
          const metricData = data.filter(
            ({ metric, year, quarter }) => metric === currentMetric && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? `${metricData[0].value}` : 'None';
        },
      },
    ],
  },
  {
    id: '5',
    columns: 2,
    content: [
      {
        id: 'project-status',
        meta: 'Project Status (Q4 2020)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): React.ReactText[][] =>
            generateArrayDataset(
              data.filter(
                ({ metric, year, quarter }) =>
                  [
                    'Number of projects with On track status',
                    'Number of projects with Warning status',
                    'Number of projects with High risk status',
                  ].includes(metric) &&
                  year === 2020 &&
                  quarter === 'Q4',
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
                      case 'Number of projects with On track status':
                        return `On Track: ${value}`;
                      case 'Number of projects with Warning status':
                        return `Warning: ${value}`;
                      case 'Number of projects with High risk status':
                        return `High Risk: ${value}`;

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
        id: 'project-status-2021',
        meta: 'Project Status (Q1 2021)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): React.ReactText[][] =>
            generateArrayDataset(
              data.filter(
                ({ metric, year, quarter }) =>
                  [
                    'Number of projects with On track status',
                    'Number of projects with Warning status',
                    'Number of projects with High risk status',
                  ].includes(metric) &&
                  year === 2021 &&
                  quarter === 'Q1',
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
                  value: '2021 Q1',
                  tooltip: '2021 Q1',
                },
                label: {
                  show: true,
                  formatter: (params: any): string => {
                    const value = params.value[params.encode.value[0]];
                    switch (params.name) {
                      case 'Number of projects with On track status':
                        return `On Track: ${value}`;
                      case 'Number of projects with Warning status':
                        return `Warning: ${value}`;
                      case 'Number of projects with High risk status':
                        return `High Risk: ${value}`;

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
        info: (data: DashboardData[]): string => {
          const metricData = data.filter(
            ({ metric, year, quarter }) =>
              metric === 'Number of projects with Warning status' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].narrative ? `${metricData[0].narrative}` : '';
        },
      },
      {
        id: 'project-spending-2020',
        meta: 'Project Spending (Q4 2020)',
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
      {
        id: 'project-spending-2021',
        meta: 'Project Spending (Q1 2021)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): React.ReactText[][] =>
            generateArrayDataset(
              data.filter(({ metric }) =>
                ['% projects overspending', '% projects underspending', '% projects on track'].includes(metric),
              ),
            ),
          // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types,@typescript-eslint/no-explicit-any
          onHover: (data: DashboardData[], chartNode: HTMLDivElement, params: any): void => {
            const metricData = data.filter(({ metric }) =>
              ['% projects overspending', '% projects underspending', '% projects on track'].includes(metric),
            );
            const index = params.encode.value[0];
            const dimension = params.dimensionNames[index];
            const [year, quarter] = dimension.split(' ');
            const metric = params.data[0];

            const dataPoint = metricData.find(
              (item) => item.metric === metric && `${item.year}` === year && item.quarter === quarter,
            );
            if (dataPoint && dataPoint.narrative) {
              showNarrative(chartNode, dataPoint.narrative);
            }
          },
          onBlur: (_data: DashboardData[], chartNode: HTMLDivElement): void => {
            hideNarrative(chartNode);
          },
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
                  value: '2021 Q1',
                  tooltip: '2021 Q1',
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
