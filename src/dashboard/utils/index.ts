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

export const colours = ['#6c120a', '#a21e25', '#cd2b2a', '#dc372d', '#ec6250', '#f6b0a0', '#fbd7cb', '#fce3dc'];

export const generateDataset = (data: DashboardData[]): Record<string, React.ReactText>[] => {
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
      }
    });

    return dataset;
  });
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
