export type DashboardData = {
  metric: string;
  date: string;
  value: number;
  department: string;
  narrative?: string;
  target?: number;
  year: number;
  quarter: string;
};

export type DashboardGrid = {
  id: string;
  columns?: number;
  content: DashboardContent[];
};

export type DashboardContent = {
  id: string;
  meta: string;
  title?: string | (() => string);
  styled?: boolean; // refers to styled meta & title - usually used for stat cards
  chart?: DashboardChart;
};

export type DashboardChart = {
  height?: string;
  data: (data: DashboardData[]) => Record<string, React.ReactText>[] | React.ReactText[][];
  options: echarts.EChartOption;
};

export type DashboardFilters = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  department?: string;
};
