import { generateObjectDataset, getAggregatedDatasetSource } from '..';
import { DashboardData, DashboardGrid, EventOptions } from '../../../utils/types';
import { addChartReverseListener, grid, hideNarrative, showNarrative } from '../chart';

const colours = ['#07482e', '#005b3e', '#1e8259', '#5ab88a', '#c5e1cb'];
const dashboardMetrics = [
  'Ranking on IATI dashboard (suggest move from top 10% to top 5%)',
  ['# active projects DIPR', '# active projects DII'],
  [
    'Number of projects with On track status',
    'Number of projects with Warning status',
    'Number of projects with High risk status',
  ],
  ['% projects overspending', '% projects underspending', '% projects on track'],
];
const getEventHandlers = (metrics: string | string[]) => {
  return {
    onClick: ({ data, chart, params }: EventOptions): void => {
      if (!params.data) return;
      const { year: y } = params.data;
      const source = generateObjectDataset(
        (data as DashboardData[]).filter(({ metric, year }) => metrics.includes(metric) && y === year),
      );
      addChartReverseListener(chart);

      chart.setOption({ dataset: { source, dimensions: ['quarter'].concat(metrics) } });
    },
    onHover: ({ chart, params }: EventOptions): void => {
      if (!params.data) return;
      const metric = params.seriesName;
      const narrative = params.data[`${metric} - narrative`];

      if (narrative) {
        showNarrative(chart.getDom() as HTMLDivElement, narrative);
      }
    },
    onBlur: ({ chart }: EventOptions): void => hideNarrative(chart.getDom() as HTMLDivElement),
  };
};

export const projectManagement: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'iati-ranking',
        meta: dashboardMetrics[0] as string,
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, [dashboardMetrics[0] as string]),
          options: {
            color: colours,
            tooltip: { show: false, trigger: 'axis' },
            legend: { show: false },
            dataset: { dimensions: ['year', dashboardMetrics[0] as string] },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3 },
            series: [
              {
                type: 'bar',
                label: {
                  show: true,
                  position: 'top',
                  /* eslint-disable-next-line @typescript-eslint/no-explicit-any */
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                },
              },
            ],
          },
          ...getEventHandlers(dashboardMetrics[0]),
        },
      },
      {
        id: 'active-projects',
        meta: 'Active Projects DIPR vs DII',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, dashboardMetrics[1] as string[]),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'axis' },
            legend: { show: true },
            dataset: { dimensions: ['year', ...(dashboardMetrics[1] as string[])] },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3 },
            series: [{ type: 'bar' }, { type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[1]),
        },
      },
      {
        id: 'project-status',
        meta: 'Project Status',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, dashboardMetrics[2] as string[]),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'axis' },
            legend: { show: true },
            dataset: { dimensions: ['year', ...(dashboardMetrics[2] as string[])] },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3 },
            series: [{ type: 'bar' }, { type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[2]),
        },
      },
      {
        id: 'project-spending',
        meta: 'Project Spending',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, dashboardMetrics[3] as string[]),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'axis' },
            legend: { show: true },
            dataset: { dimensions: ['year', ...(dashboardMetrics[3] as string[])] },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar' }, { type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[3]),
        },
      },
    ],
  },
];
