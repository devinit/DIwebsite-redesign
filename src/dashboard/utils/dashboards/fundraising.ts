import { generateObjectDataset, getAggregatedDatasetSource } from '../';
import { DashboardData, DashboardGrid, EventOptions } from '../../../utils/types';
import { addChartReverseListener, getEventHandlers, grid, tootipFormatter } from '../chart';

const colours = ['#42184c', '#632572', '#994d98', '#cb98c4', '#ebcfe5'];
const dashboardMetrics = [
  'Income secured this quarter',
  'Weighted value 50/80% probable pipeline at end of quarter',
  'Income at 90% at end of quarter (waiting for agreement to be signed for 2021-2023)',
  'Weighted value of 50% & 80% probable pipeline at end of quarter (income 2021-2023)',
  'Speculative pipeline value, not weighted (>50% probable)',
];

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
            legend: { show: true },
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
      {
        id: 'income-secured',
        meta: 'Income Secured From Contracts (Target £1.2M)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            const categoryMetric = 'Contracts';
            const metricData = data.filter(
              ({ metric, category }) => dashboardMetrics[0].includes(metric) && category === categoryMetric,
            );

            return getAggregatedDatasetSource(metricData, Array<string>().concat(dashboardMetrics[0]));
          },
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ currency: true }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[0]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '£{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[0]),
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
        meta: 'Grants',
      },
    ],
  },
  {
    id: '4',
    columns: 2,
    content: [
      {
        id: 'income-secured',
        meta: 'Income Secured From Grants (Target £2.5m)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            const categoryMetric = 'Grants';
            const metricData = data.filter(
              ({ metric, category }) => dashboardMetrics[0].includes(metric) && category === categoryMetric,
            );

            return getAggregatedDatasetSource(metricData, Array<string>().concat(dashboardMetrics[0]));
          },
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ currency: true }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[0]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '£{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[0]),
        },
      },
      {
        id: 'grant-income',
        meta: 'Income at 90% at end of quarter',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[2])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ currency: true }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[2]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '£{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[2]),
        },
      },
      {
        id: 'weighted-value',
        meta: dashboardMetrics[3],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[3])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ currency: true }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[3]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '£{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[3]),
        },
      },
      {
        id: 'speculative-pileline-value',
        meta: dashboardMetrics[4],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[4])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ currency: true }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[4]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '£{value}' } },
            series: [{ type: 'bar' }],
          },
          ...getEventHandlers(dashboardMetrics[4]),
        },
      },
    ],
  },
];
