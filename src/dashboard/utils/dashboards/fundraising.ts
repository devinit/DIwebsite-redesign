import { generateObjectDataset, getAggregatedDatasetSource, toPounds } from '../';
import { DashboardData, DashboardGrid, EventOptions } from '../../../utils/types';
import { addChartReverseListener, getEventHandlers, grid, tootipFormatter } from '../chart';

const colours = ['#42184c', '#632572', '#994d98', '#cb98c4', '#ebcfe5'];
const dashboardMetrics = ['Income secured this quarter', 'Weighted value 50/80% probable pipeline at end of quarter'];

export const fundraising: DashboardGrid[] = [
  {
    id: '1',
    columns: 1,
    className: 'm-pills',
    content: [
      {
        id: 'contract-income',
        meta: 'Total Income Secured (Contracts + Grants)',
        styled: true,
        chart: {
          height: '300px',
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            const metricData = data.filter(({ metric }) => dashboardMetrics[0].includes(metric));

            const dataAggregateForMetricYear = metricData.reduce<DashboardData[]>((prev, curr) => {
              const categoryMetric = `${dashboardMetrics[0]} - ${curr.category.trim()}`;
              if (!prev.find((item) => item.metric === categoryMetric && item.year === curr.year)) {
                const metricDataForYear = metricData.filter(
                  ({ metric, year, category }) =>
                    metric === curr.metric && year === curr.year && category === curr.category,
                );
                const sum = metricDataForYear.reduce((currentSum, curr) => currentSum + curr.value, 0);
                prev.push({ ...curr, metric: categoryMetric, value: sum });
              }

              return prev;
            }, []);

            return generateObjectDataset(dataAggregateForMetricYear);
          },

          options: {
            color: colours,
            tooltip: { show: true, trigger: 'axis' },
            legend: { show: false },
            dataset: {
              dimensions: [
                'year',
                `${dashboardMetrics[0] as string} - Contracts`,
                `${dashboardMetrics[0] as string} - Grants`,
              ],
            },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: {
              type: 'value',
              show: true,
              axisLine: { show: true },
              axisTick: { show: true },
              axisLabel: { formatter: '£{value}' },
            },
            series: [
              { type: 'bar', barWidth: '30%', stack: 'fundraising' },
              { type: 'bar', barWidth: '30%', stack: 'fundraising' },
            ],
          },
          ...getEventHandlers(dashboardMetrics[0]),
          onClick: ({ data, chart, params }: EventOptions): void => {
            if (!params.data) return;
            const { year: y } = params.data;
            const metricData = (data as DashboardData[]).filter(
              ({ metric, year }) => dashboardMetrics[0].includes(metric) && y === year,
            );
            const dataAggregateForMetricYear = metricData.reduce<DashboardData[]>((prev, curr) => {
              const categoryMetric = `${dashboardMetrics[0]} - ${curr.category.trim()}`;
              if (!prev.find((item) => item.metric === categoryMetric)) {
                const metricDataForYear = metricData.filter(
                  ({ metric, quarter, category }) =>
                    metric === curr.metric && quarter === curr.quarter && category === curr.category,
                );
                const sum = metricDataForYear.reduce((currentSum, curr) => currentSum + curr.value, 0);
                prev.push({ ...curr, metric: categoryMetric, value: sum });
              } else {
                prev.push({ ...curr, metric: categoryMetric });
              }

              return prev;
            }, []);
            const source = generateObjectDataset(dataAggregateForMetricYear);
            addChartReverseListener(chart);

            chart.setOption({
              dataset: {
                source,
                dimensions: [
                  'quarter',
                  `${dashboardMetrics[0] as string} - Contracts`,
                  `${dashboardMetrics[0] as string} - Grants`,
                ],
              },
            });
          },
        },
      },
    ],
  },
  {
    id: '0',
    columns: 1,
    className: 'pt-20',
    content: [
      {
        id: 'contracts',
        meta: 'Contracts',
      },
    ],
  },
  {
    id: '2',
    columns: 2,
    content: [
      {
        id: 'contract-weighted',
        meta: dashboardMetrics[1],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[1])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ currency: true }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[1]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '£{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[1]),
        },
      },
    ],
  },
  {
    id: '3',
    columns: 1,
    content: [
      {
        id: 'grants',
        meta: 'Grants - Q1 2021',
      },
    ],
  },
  {
    id: '4',
    columns: 4,
    content: [
      {
        id: 'grant-income-secured',
        meta: 'Income Secured',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Income secured this quarter';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
  {
    id: '5',
    columns: 1,
    className: 'm-pills',
    content: [
      {
        id: 'grant-income',
        meta: 'Income at 90% at end of quarter (waiting for agreement to be signed for 2021-2023)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Income at 90% at end of quarter (waiting for agreement to be signed for 2021-2023)';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
  {
    id: '6',
    columns: 1,
    className: 'm-pills',
    content: [
      {
        id: 'grant-weighted',
        meta: 'Weighted value of 50% & 80% probable pipeline at end of quarter (income 2021-2023)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Weighted value of 50% & 80% probable pipeline at end of quarter (income 2021-2023)';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
  {
    id: '7',
    columns: 2,
    content: [
      {
        id: 'grant-speculative',
        meta: 'Speculative pipeline value, not weighted (>50% probable)',
        styled: true,
        title: (data: DashboardData[]): React.ReactText => {
          const currentMetric = 'Speculative pipeline value, not weighted (>50% probable)';
          const metricData = data.filter(
            ({ metric, year, quarter, category }) =>
              metric.trim() === currentMetric && category.trim() === 'Grants' && year === 2021 && quarter === 'Q1',
          );

          return metricData && metricData.length && metricData[0].value ? toPounds(metricData[0].value) : 'None';
        },
      },
    ],
  },
];
