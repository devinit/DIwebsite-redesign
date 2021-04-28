import { DashboardData, DashboardFilters } from '../../utils/types';

export type DateDivision = 'month' | 'quarter'; // determines whether to split x-axis dates by month or quarter
export const fullMonths = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December',
];
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'];

export const getQuarterYear = (dateString: string): [number, number] => {
  try {
    const date = new Date(dateString);
    const quarter = Math.floor((date.getMonth() + 3) / 3);

    return [quarter, date.getFullYear()];
  } catch (error) {
    return [0, 0];
  }
};

export const getMonthYear = (dateString: string): [string, number] => {
  try {
    const date = new Date(dateString);

    return [months[date.getMonth()], date.getFullYear()];
  } catch (error) {
    return ['', 0];
  }
};

const getAnnualTargetFromData = (data: DashboardData[], metric: string, date: string): number | null => {
  const year = new Date(date).getFullYear();
  const annualData = data.find((item) => metric === item.metric && item.year === year && item.quarter === 'Annual');

  return (annualData && annualData.target) || null;
};

export const generateObjectDataset = (
  data: DashboardData[],
  division: DateDivision = 'quarter', // determines whether to split x-axis dates by month or quarter
): Record<string, React.ReactText>[] => {
  // extract unique metrics & dates
  const metrics = [...new Set(data.map(({ metric }) => metric))];
  const dates = [...new Set(data.map(({ date }) => date))].sort();

  return dates.reduce<Record<string, string | number>[]>((prev, date) => {
    const [quarterMonth, year] = division === 'quarter' ? getQuarterYear(date) : getMonthYear(date);
    const quarter = division === 'quarter' ? `${year} Q${quarterMonth}` : quarterMonth;
    const matchingDataset = prev.find((_dataset) => _dataset.quarter === quarter);
    const dataset: Record<string, string | number> = matchingDataset || { quarter: quarter, year };

    metrics.forEach((metric) => {
      const matchingData = data.find((item) => item.date === date && metric === item.metric);
      if (matchingData) {
        if (matchingDataset) {
          (dataset[metric] as number) += matchingData.value;
        } else {
          dataset[metric] = matchingData.value;
        }
        if (matchingData.target) {
          dataset['Target'] = matchingData.target;
        } else {
          const target = getAnnualTargetFromData(data, metric, date);
          if (target) {
            dataset['Target'] = target;
          }
        }
        if (matchingData.narrative) {
          dataset[`${metric} - narrative`] = matchingData.narrative;
        }
      }
    });
    if (!matchingDataset) prev.push(dataset);

    return prev;
  }, []);
};

export const generateArrayDataset = (data: DashboardData[]): React.ReactText[][] => {
  // extract unique metrics & dates
  const metrics = [...new Set(data.map(({ metric }) => metric))];
  const dates = [...new Set(data.map(({ date }) => date))];

  const dataset: React.ReactText[][] = metrics.map((metric) =>
    new Array<React.ReactText>(metric).concat(
      dates.map((date) => {
        const matchingData = data.find((item) => item.date === date && metric === item.metric);

        return matchingData ? matchingData.value : 0;
      }),
    ),
  );

  return [
    new Array<React.ReactText>('metric').concat(
      dates.map((date) => {
        const [quarter, year] = getQuarterYear(date);

        return `${year} Q${quarter}`;
      }),
    ),
  ].concat(dataset);
};

export const filterDashboardData = (
  data: DashboardData[],
  { year, quarter, department }: DashboardFilters,
): DashboardData[] => {
  return data
    .filter((row) => (department ? row.department === department : true))
    .filter((row) => {
      if (year && !quarter) {
        return row.year === year;
      }
      if (quarter && !year) {
        return row.quarter === `Q${quarter}`;
      }
      if (year && quarter) {
        return row.year === year && row.quarter === `Q${quarter}`;
      }

      return true;
    });
};

export const toPounds = (value: number): string => {
  const formatter = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'GBP' });

  return formatter.format(value);
};

export const getAggregatedDatasetSource = (
  data: DashboardData[],
  metrics: string[],
  aggregation: 'sum' | 'average' = 'average',
  division: DateDivision = 'quarter', // determines whether to split x-axis dates by month or quarter
): Record<string, React.ReactText>[] => {
  const metricData = data.filter(({ metric }) => metrics.includes(metric));

  const dataAggregateForMetricYear = metricData.reduce<DashboardData[]>((prev, curr) => {
    if (!prev.find((item) => item.metric === curr.metric && item.year === curr.year)) {
      const metricDataForYear = metricData.filter(
        ({ metric, year, value }) => metric === curr.metric && year === curr.year && typeof value === 'number',
      );
      const sum = metricDataForYear.reduce((currentSum, curr) => currentSum + curr.value, 0);
      if (aggregation === 'average') {
        const average = sum / metricDataForYear.length;
        prev.push({ ...curr, value: average, quarter: '', narrative: '' }); // TODO: add actual narratives for year
      } else {
        prev.push({ ...curr, value: sum, quarter: '', narrative: '' }); // TODO: add actual narratives for year
      }
    }

    return prev;
  }, []);

  return generateObjectDataset(dataAggregateForMetricYear, division);
};
