import { Layout } from 'plotly.js';

export interface DIChartConfig {
  className: string;
  plotly?: DIChartPlotlyConfig;
  onAdd?: (config: DIChartConfig) => void;
}

export interface DIChartPlotlyConfig {
  layout: Layout;
  utils: { [key: string]: any }; // eslint-disable-line @typescript-eslint/no-explicit-any
}

export interface FilterOptions {
  labelPrefix?: string;
  labelSuffix?: string;
}
