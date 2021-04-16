import { DashboardData, DashboardFilters } from '../../utils/types';

export const getQuarterYear = (dateString: string): [number, number] => {
  try {
    const date = new Date(dateString);
    const quarter = Math.floor((date.getMonth() + 3) / 3);

    return [quarter, date.getFullYear()];
  } catch (error) {
    return [0, 0];
  }
};

export const generateObjectDataset = (data: DashboardData[]): Record<string, React.ReactText>[] => {
  // extract unique metrics & dates
  const metrics = [...new Set(data.map(({ metric }) => metric))];
  const dates = [...new Set(data.map(({ date }) => date))];

  return dates.map((date) => {
    const [quarter, year] = getQuarterYear(date);
    const dataset: Record<string, string | number> = { quarter: `${year} Q${quarter}`, year };
    metrics.forEach((metric) => {
      const matchingData = data.find((item) => item.date === date && metric === item.metric);
      if (matchingData) {
        dataset[metric] = matchingData.value;
        if (matchingData.target) {
          dataset['Target'] = matchingData.target;
        }
        if (matchingData.narrative) {
          dataset['narrative'] = matchingData.narrative;
        }
      }
    });

    return dataset;
  });
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
): Record<string, React.ReactText>[] => {
  const metricData = data.filter(({ metric }) => metrics.includes(metric));

  const dataAggregateForMetricYear = metricData.reduce<DashboardData[]>((prev, curr) => {
    if (!prev.find((item) => item.metric === curr.metric && item.year === curr.year)) {
      const metricDataForYear = metricData.filter(({ metric, year }) => metric === curr.metric && year === curr.year);
      const sum = metricDataForYear.reduce((currentSum, curr) => currentSum + curr.value, 0);
      if (aggregation === 'average') {
        const average = sum / metricDataForYear.length;
        prev.push({ ...curr, value: average });
      } else {
        prev.push({ ...curr, value: sum });
      }
    }

    return prev;
  }, []);

  return generateObjectDataset(dataAggregateForMetricYear);
};
