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

export type DashboardChart = {
  height?: string;
  data: (data: DashboardData[]) => Record<string, React.ReactText>[] | React.ReactText[][];
  options: echarts.EChartOption;
  onClick?: (data: DashboardData[], node: HTMLDivElement, params: any) => void; // eslint-disable-line @typescript-eslint/no-explicit-any
  onHover?: (data: DashboardData[], node: HTMLDivElement, params: any) => void; // eslint-disable-line @typescript-eslint/no-explicit-any
  onBlur?: (data: DashboardData[], node: HTMLDivElement, params: any) => void; // eslint-disable-line @typescript-eslint/no-explicit-any
};

export type DashboardFilters = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  department?: string;
};

export type Quarter = 1 | 2 | 3 | 4;
