import { Layout, Data, Config } from 'plotly.js';

export interface DIChartConfig {
  className: string;
  plotly?: DIChartPlotlyConfig;
  onAdd?: (config: DIChartConfig) => void;
}

export interface DIChartPlotlyConfig {
  data?: Data[];
  layout: Partial<Layout>;
  config: Partial<Config>;
  utils: { [key: string]: any }; // eslint-disable-line @typescript-eslint/no-explicit-any
}

export interface FilterOptions {
  labelPrefix?: string;
  labelSuffix?: string;
}
