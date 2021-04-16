import { colours, generateObjectDataset, getAggregatedDatasetSource } from '../';
import { DashboardData, DashboardGrid, EventOptions } from '../../../utils/types';

const grid: echarts.EChartOption.Grid = {
  left: '3%',
  right: '4%',
  bottom: '3%',
  containLabel: true,
};

export const financeDashboard: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'project-time',
        meta: 'Proportion of staff time spent on projects',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, ['Non-Overhead staff', 'All staff']),
          options: {
            color: colours,
            tooltip: { show: false },
            legend: { data: ['Non-Overhead staff', 'All staff'] },
            dataset: {
              dimensions: ['year', 'Non-Overhead staff', 'All staff'],
            },
            grid,
            xAxis: { type: 'category', boundaryGap: true, axisTick: { alignWithLabel: true } },
            yAxis: { type: 'value', scale: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: Array.from(
              { length: 2 },
              (): echarts.EChartOption.Series => ({
                type: 'bar',
                label: {
                  show: true,
                  /* eslint-disable-next-line @typescript-eslint/no-explicit-any */
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                },
              }),
            ),
          },
          onClick: ({ data, chart, params }: EventOptions): void => {
            if (!params.data) return;
            const { year: y } = params.data;
            const source = generateObjectDataset(
              (data as DashboardData[]).filter(
                ({ metric, year }) => (metric === 'Non-Overhead staff' || metric === 'All staff') && y === year,
              ),
            );
            const options: echarts.EChartOption = {
              legend: { data: ['Non-Overhead staff', 'All staff', 'Target'] },
              dataset: {
                source,
                dimensions: ['quarter', 'Non-Overhead staff', 'All staff', 'Target'],
              },
              grid,
              xAxis: { type: 'category', boundaryGap: true, axisTick: { alignWithLabel: true } },
              yAxis: { type: 'value', scale: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
              series: [
                { type: 'line' },
                { type: 'line' },
                {
                  type: 'line',
                  symbol: 'none',
                  lineStyle: { type: 'dashed', color: '#333' },
                  itemStyle: { color: '#333' },
                },
              ],
            };
            const previousOptions = chart.getOption();
            const chartNode = chart.getDom();
            const canvas = chartNode.getElementsByTagName('canvas')[0];
            if (canvas) {
              const onClick = () => {
                chart.setOption(previousOptions);
                canvas.removeEventListener('click', onClick);
              };
              canvas.addEventListener('click', onClick);
            }

            chart.setOption(options);
          },
        },
      },
      {
        id: 'overhead-time',
        meta: 'Proportion of time spent on direct and indirect overheads',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, ['Direct overheads', 'Indirect overheads']),
          options: {
            color: colours,
            tooltip: { show: false },
            legend: { data: ['Direct overheads', 'Indirect overheads'] },
            dataset: {
              dimensions: ['year', 'Direct overheads', 'Indirect overheads'],
            },
            grid,
            xAxis: { type: 'category' },
            yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: Array.from(
              { length: 2 },
              (): echarts.EChartOption.Series => ({
                type: 'bar',
                label: {
                  show: true,
                  /* eslint-disable-next-line @typescript-eslint/no-explicit-any */
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                },
              }),
            ),
          },
          onClick: ({ data, chart, params }: EventOptions): void => {
            if (!params.data) return;
            const { year: y } = params.data;
            const source = generateObjectDataset(
              (data as DashboardData[]).filter(
                ({ metric, year }) => (metric === 'Direct overheads' || metric === 'Indirect overheads') && y === year,
              ),
            );
            const options: echarts.EChartOption = {
              tooltip: { show: true, trigger: 'axis' },
              legend: { data: ['Direct overheads', 'Indirect overheads', 'Target'] },
              dataset: {
                source,
                dimensions: ['quarter', 'Direct overheads', 'Indirect overheads', 'Target'],
              },
              grid,
              xAxis: { type: 'category' },
              yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '{value}%' } },
              series: [
                { type: 'bar', label: { show: false, formatter: () => '' } },
                { type: 'bar', label: { show: false, formatter: () => '' } },
                {
                  type: 'line',
                  symbol: 'none',
                  lineStyle: { type: 'dashed', color: '#333' },
                  itemStyle: { color: '#333' },
                },
              ],
            };
            const previousOptions = chart.getOption();
            const chartNode = chart.getDom();
            const canvas = chartNode.getElementsByTagName('canvas')[0];
            if (canvas) {
              const onClick = () => {
                chart.setOption(previousOptions);
                canvas.removeEventListener('click', onClick);
              };
              canvas.addEventListener('click', onClick);
            }

            chart.setOption(options);
          },
        },
      },
      {
        id: 'personnel-costs',
        meta: 'Personnel costs as a proporation of income (% of target)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, ['Consultants as proportion of income', 'Salary as proportion of income']),
          options: {
            color: colours,
            tooltip: { show: false },
            legend: { top: '10%' },
            dataset: {
              dimensions: ['year', 'Consultants as proportion of income', 'Salary as proportion of income'],
            },
            grid,
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            /* eslint-disable @typescript-eslint/no-explicit-any */
            series: Array.from(
              { length: 2 },
              (): echarts.EChartOption.Series => ({
                type: 'bar',
                label: {
                  show: true,
                  position: 'top',
                  formatter: (params: any): string => `${params.value[params.dimensionNames[params.encode.y[0]]]}%`,
                },
              }),
            ),
            /* eslint-enable @typescript-eslint/no-explicit-any */
          },
          onClick: ({ data, chart, params }: EventOptions): void => {
            if (!params.data) return;
            const { year: y } = params.data;
            const source = generateObjectDataset(
              (data as DashboardData[]).filter(
                ({ metric, year }) =>
                  ['Consultants as proportion of income', 'Salary as proportion of income'].includes(metric) &&
                  y === year,
              ),
            );
            const options: echarts.EChartOption = {
              tooltip: { show: false },
              dataset: {
                source,
                dimensions: ['quarter', 'Consultants as proportion of income', 'Salary as proportion of income'],
              },
              grid,
              xAxis: { type: 'category' },
              yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '{value}%' } },
              series: [{ type: 'bar' }, { type: 'bar' }],
            };
            const previousOptions = chart.getOption();
            const chartNode = chart.getDom();
            const canvas = chartNode.getElementsByTagName('canvas')[0];
            if (canvas) {
              const onClick = () => {
                chart.setOption(previousOptions);
                canvas.removeEventListener('click', onClick);
              };
              canvas.addEventListener('click', onClick);
            }

            chart.setOption(options);
          },
        },
      },
      {
        id: 'consultant-costs',
        meta: 'Average consultant % for year to date (excl GNR)',
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, ['Average consultant % for year to date (excl GNR)']),
          options: {
            color: colours,
            tooltip: { show: false },
            legend: { show: false },
            dataset: {
              dimensions: ['year', 'Average consultant % for year to date (excl GNR)'],
            },
            grid,
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
            ],
            /* eslint-enable @typescript-eslint/no-explicit-any */
          },
          onClick: ({ data, chart, params }: EventOptions): void => {
            if (!params.data) return;
            const { year: y } = params.data;
            const source = generateObjectDataset(
              (data as DashboardData[]).filter(
                ({ metric, year }) =>
                  ['Average consultant % for year to date (excl GNR)'].includes(metric) && y === year,
              ),
            );
            const options: echarts.EChartOption = {
              tooltip: { show: false },
              dataset: {
                source,
                dimensions: ['quarter', 'Average consultant % for year to date (excl GNR)'],
              },
              grid,
              xAxis: { type: 'category' },
              yAxis: { type: 'value', splitNumber: 3, axisLabel: { formatter: '{value}%' } },
              series: [{ type: 'bar' }],
            };
            const previousOptions = chart.getOption();
            const chartNode = chart.getDom();
            const canvas = chartNode.getElementsByTagName('canvas')[0];
            if (canvas) {
              const onClick = () => {
                chart.setOption(previousOptions);
                canvas.removeEventListener('click', onClick);
              };
              canvas.addEventListener('click', onClick);
            }

            chart.setOption(options);
          },
        },
      },
    ],
  },
];
