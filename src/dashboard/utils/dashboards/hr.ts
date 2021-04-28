import { fullMonths, generateObjectDataset, getAggregatedDatasetSource } from '../';
import { DashboardContent, DashboardData, DashboardGrid } from '../../../utils/types';
import { getBarLabelConfig, getEventHandlers, grid } from '../chart';

const colours = ['#0c457b', '#0071b1', '#4397d3', '#00538e', '#88bae5', '#0089cc']; // shades of blue
const dashboardMetrics = [
  ['Total Staff', 'Total leavers in the period (Voluntary)', 'Total leavers in the period (Planned)'],
  'Staffing budget',
  'Staffing budget as a %age of org budget (65% ceiling)',
  'Stability Index',
];

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
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            const metricData = data.filter(({ metric }) => dashboardMetrics[0].includes(metric));

            const dataAggregateForMetricYear = metricData.reduce<DashboardData[]>((prev, curr) => {
              if (!prev.find((item) => item.metric === curr.metric && item.year === curr.year)) {
                const metricDataForYear = metricData.filter(
                  ({ metric, year }) => metric === curr.metric && year === curr.year,
                );
                if (curr.metric === 'Total Staff') {
                  const max = Math.max(...metricDataForYear.map((item) => item.value));
                  prev.push({ ...curr, value: max });
                } else {
                  const sum = metricDataForYear.reduce((currentSum, curr) => currentSum + curr.value, 0);
                  prev.push({ ...curr, value: sum });
                }
              }

              return prev;
            }, []);

            return generateObjectDataset(dataAggregateForMetricYear);
          },
          options: {
            color: colours,
            tooltip: { trigger: 'axis' },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[0]) },
            grid,
            toolbox: { show: true, feature: { saveAsImage: { show: true } } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', splitNumber: 3 },
            series: [
              { type: 'bar', stack: 'hr' },
              { type: 'bar', stack: 'hr' },
              { type: 'bar', stack: 'hr' },
            ],
          },
          ...getEventHandlers(dashboardMetrics[0]),
        },
      },
      {
        id: 'stability',
        meta: 'Stability Index',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, [dashboardMetrics[3] as string]),
          options: {
            color: colours,
            tooltip: { show: false, trigger: 'axis' },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[3]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3 },
            /* eslint-disable @typescript-eslint/no-explicit-any */
            series: [{ type: 'bar', label: getBarLabelConfig({}) }],
          },
          ...getEventHandlers(dashboardMetrics[3]),
        },
      },
      ...[
        { id: 'gender-pay-mean', meta: 'Gender Pay Gap (Mean)' },
        { id: 'gender-pay-median', meta: 'Gender Pay Gap (Median)' },
      ].map<DashboardContent>(({ id, meta }) => {
        return {
          id: id,
          meta: meta,
          styled: true,
          chart: {
            data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
              getAggregatedDatasetSource(data, [meta]),
            options: {
              color: colours,
              tooltip: { trigger: 'item' },
              legend: { show: false },
              dataset: { dimensions: ['year', meta] },
              toolbox: { show: true, feature: { saveAsImage: { show: true } } },
              xAxis: { type: 'category', position: 'top' },
              yAxis: { type: 'value', scale: true, splitNumber: 1 },
              series: [{ type: 'bar', label: getBarLabelConfig({ position: 'bottom' }) }],
            },
            ...getEventHandlers(meta),
          },
        };
      }),
      {
        id: 'staffing-budget',
        meta: 'Staffing budget',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, [dashboardMetrics[1] as string]),
          options: {
            color: colours,
            tooltip: { show: false, trigger: 'axis' },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[1]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3 },
            series: [{ type: 'bar', label: getBarLabelConfig({ currency: true, suffix: 'm' }) }],
          },
          ...getEventHandlers(dashboardMetrics[1]),
        },
      },
      {
        id: 'staffing-budget-vs-org-budget',
        meta: 'Staffing budget as a %age of org budget (65% ceiling)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, [dashboardMetrics[2] as string]),
          options: {
            color: colours,
            tooltip: { show: false, trigger: 'axis' },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[2]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3 },
            series: [{ type: 'bar', label: getBarLabelConfig({ suffix: '%' }) }],
          },
          ...getEventHandlers(dashboardMetrics[2]),
        },
      },
      {
        id: 'sick-days',
        meta: 'Total Sick Days',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            const monthlyData = data.filter(
              ({ metric, quarter }) => metric === 'Total Sick Days' && fullMonths.includes(quarter),
            );

            return getAggregatedDatasetSource(monthlyData, ['Total Sick Days'], 'sum', 'month');
          },
          options: {
            color: colours,
            tooltip: { trigger: 'item' },
            legend: { show: false },
            dataset: { dimensions: ['year', 'Total Sick Days'] },
            grid,
            toolbox: { show: true, feature: { saveAsImage: { show: true } } },
            xAxis: { type: 'category', axisTick: { alignWithLabel: true, interval: 1 } },
            yAxis: { type: 'value', splitNumber: 3 },
            series: [{ type: 'bar', label: getBarLabelConfig({}) }],
          },
          ...getEventHandlers('Total Sick Days', { yAxis: { show: false } }, 'month'),
        },
      },
      {
        id: 'sick-days-staff',
        meta: 'Number of Staff Who logged Sick days per period of sickness',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            const monthlyData = data.filter(
              ({ metric, quarter }) =>
                metric === 'No. Staff Logged Sick days/ periods of sickness' && fullMonths.includes(quarter),
            );

            return getAggregatedDatasetSource(
              monthlyData,
              ['No. Staff Logged Sick days/ periods of sickness'],
              'sum',
              'month',
            );
          },
          options: {
            color: colours,
            tooltip: { trigger: 'item' },
            legend: { show: false },
            dataset: { dimensions: ['year', 'No. Staff Logged Sick days/ periods of sickness'] },
            grid,
            toolbox: { show: true, feature: { saveAsImage: { show: true } } },
            xAxis: { type: 'category', axisTick: { alignWithLabel: true, interval: 1 } },
            yAxis: { type: 'value', splitNumber: 3 },
            series: [{ type: 'bar', label: getBarLabelConfig({}) }],
          },
          ...getEventHandlers('No. Staff Logged Sick days/ periods of sickness', { yAxis: { show: false } }, 'month'),
        },
      },
    ],
  },
];
