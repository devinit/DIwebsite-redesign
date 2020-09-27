import { Layout, Data, Config } from 'plotly.js';
import { DIPlotlyChart } from '../plotly';

export interface DIChartConfig {
  className: string;
  plotly?: DIChartPlotlyOptions;
  onAdd?: (config: DIChartConfig) => void;
  elements?: HTMLElement[];
}

interface PlotlyCSV {
  url: string;
  onFetch: (data: Array<{ [key: string]: any }>, config: DIChartPlotlyOptions, manager: DIPlotlyChart) => void; // eslint-disable-line @typescript-eslint/no-explicit-any
}

export interface DIChartPlotlyOptions {
  data?: Data[]; // if provided, use as the single source of chart data. Takes precendece over csv property
  layout: Partial<Layout>;
  config: Partial<Config>;
  csv?: PlotlyCSV; // only used if data property is not provided - URL of the CSV data source
  utils: { [key: string]: any }; // eslint-disable-line @typescript-eslint/no-explicit-any
}

export interface FilterOptions {
  labelPrefix?: string;
  labelSuffix?: string;
}
