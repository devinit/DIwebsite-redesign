export type DashboardData = {
  metric: string;
  date: string;
  value: number;
  department: string;
  narrative?: string;
  target?: number;
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
  data: (data: DashboardData[]) => Record<string, unknown>[];
  options: echarts.EChartOption;
};
