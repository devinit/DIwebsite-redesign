import { getQuarterYear } from '../../../dashboard/utils';
import { DashboardData, DashboardGrid } from '../../../utils/types';

export const grids: DashboardGrid[] = [
  {
    id: '1',
    columns: 2,
    content: [
      {
        id: 'project-time',
        meta: 'Proportion of staff time spent on projects',
        chart: {
          data: (data: DashboardData[]): Record<string, unknown>[] => {
            const financeData = data.filter(
              ({ department, metric }) =>
                department === 'Finance' && (metric === 'Non-Overhead Staff' || metric === 'All Staff'),
            );
            // extract unique metrics & dates
            const metrics = [...new Set(financeData.map(({ metric }) => metric))];
            const dates = [...new Set(financeData.map(({ date }) => date))];

            return dates.map((date) => {
              const [quarter, year] = getQuarterYear(date);
              const dataset: Record<string, string | number> = { quarter: `${year} Q${quarter}`, year };
              metrics.forEach((metric) => {
                const matchingData = financeData.find((item) => item.date === date && metric === item.metric);
                if (matchingData) {
                  dataset[metric] = matchingData.value;
                  if (matchingData.target) {
                    dataset['target'] = matchingData.target;
                  }
                }
              });

              return dataset;
            });
          },
          options: {
            tooltip: {
              trigger: 'axis',
            },
            legend: {},
            dataset: {
              dimensions: ['quarter', 'Non-Overhead Staff', 'All Staff'],
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
            yAxis: { type: 'value' },
            series: [{ type: 'bar' }, { type: 'bar' }],
          },
        },
      },
    ],
  },
];
