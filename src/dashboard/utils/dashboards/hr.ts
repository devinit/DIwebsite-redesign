import { fullMonths, generateObjectDataset, getAggregatedDatasetSource } from '../';
import { DashboardContent, DashboardData, DashboardGrid, EventOptions } from '../../../utils/types';
import { addChartReverseListener, getBarLabelConfig, getEventHandlers, grid } from '../chart';

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
          data: (data: DashboardData[]): Record<string, React.ReactText>[] => {
            const metrics = ['Total Staff', 'Total leavers in the period'];
            const metricData = data.filter(({ metric }) => metrics.includes(metric));

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
            dataset: { dimensions: ['year', 'Total Staff', 'Total leavers in the period'] },
            grid,
            toolbox: { show: true, feature: { saveAsImage: { show: true } } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', splitNumber: 3 },
            series: [
              { type: 'bar', stack: 'hr' },
              { type: 'bar', stack: 'hr' },
            ],
          },
          onClick: ({ data, chart, params }: EventOptions): void => {
            if (!params.data) return;
            const { year: y } = params.data;
            const source = generateObjectDataset(
              (data as DashboardData[]).filter(
                ({ metric, year }) => ['Total Staff', 'Total leavers in the period'].includes(metric) && y === year,
              ),
            );
            addChartReverseListener(chart);

            chart.setOption({
              dataset: {
                source,
                dimensions: ['quarter', 'Total Staff', 'Total leavers in the period'],
              },
            });
          },
        },
      },
      {
        id: 'stability',
        meta: 'Stability Index',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, ['Stability Index']),
          options: {
            color: colours,
            tooltip: { show: false, trigger: 'axis' },
            legend: { show: false },
            dataset: { dimensions: ['year', 'Stability Index'] },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
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
          onClick: ({ data, chart, params }: EventOptions): void => {
            if (!params.data) return;
            const { year: y } = params.data;
            const source = generateObjectDataset(
              (data as DashboardData[]).filter(
                ({ metric, year }) => ['Stability Index'].includes(metric) && y === year,
              ),
            );
            addChartReverseListener(chart);

            chart.setOption({ dataset: { source, dimensions: ['quarter', 'Stability Index'] } });
          },
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
              series: [
                {
                  type: 'bar',
                  label: {
                    show: true,
                    position: 'bottom',
                    formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                  },
                },
              ],
            },
            onClick: ({ data, chart, params }: EventOptions): void => {
              if (!params.data) return;
              const { year: y } = params.data;
              const source = generateObjectDataset(
                (data as DashboardData[]).filter(({ metric, year }) => [meta].includes(metric) && y === year),
              );
              addChartReverseListener(chart);

              chart.setOption({ dataset: { source, dimensions: ['quarter', meta] } });
            },
          },
        };
      }),
      /* eslint-enable @typescript-eslint/no-explicit-any */
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
