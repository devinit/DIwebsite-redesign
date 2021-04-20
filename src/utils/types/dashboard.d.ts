export type DashboardData = {
  metric: string;
  date: string;
  value: number;
  department: string;
  narrative?: string;
  target?: number;
  year: number;
  quarter: string;
  category: string;
};

export type DashboardGrid = {
  id: string;
  columns?: number;
  content: DashboardContent[];
  className?: string;
};

export type DashboardContent = {
  id: string;
  meta: string;
  title?: string | ((data: DashboardData[]) => React.ReactText);
  styled?: boolean; // refers to styled meta & title - usually used for stat cards
  chart?: DashboardChart;
  info?: string | ((data: DashboardData[]) => string);
};

export interface DashboardChart extends DashboardChartEvents {
  height?: string;
  data: (data: DashboardData[]) => Record<string, React.ReactText>[] | React.ReactText[][];
  options: echarts.EChartOption;
}

export type DashboardChartEvents = {
  /* eslint-disable @typescript-eslint/no-explicit-any */
  onClick?: (options: EventOptions) => void;
  onHover?: (options: EventOptions) => void;
  onBlur?: (options: EventOptions) => void;
  /* eslint-enable @typescript-eslint/no-explicit-any */
};

export type DashboardFilters = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  department?: string;
};

export type Quarter = 1 | 2 | 3 | 4;

export type EventOptions = {
  data: unknown[];
  chart: echarts.ECharts;
  params: any; // eslint-disable-line @typescript-eslint/no-explicit-any
};
