import { Layout, Data, Config, LegendClickEvent, PlotMouseEvent } from 'plotly.js';
import { DIPlotlyChart } from '../plotly';

export interface DIChartConfig {
  className: string;
  plotly?: DIChartPlotlyOptions;
  onAdd?: (config: DIChartConfig) => void;
  elements?: HTMLElement[];
}

interface ChartWidgets {
  filters?: ChartFilter[];
  legend?: ChartLegend;
}

export interface ChartFilter {
  className: string;
  options?: string[];
  multi?: boolean; // multi-select
  getOptions?: (manager: DIPlotlyChart) => string[];
  onChange: (event: MouseEvent, manager: DIPlotlyChart) => void;
}

export interface ChartLegend {
  onClick?: (data: LegendClickEvent, manager: DIPlotlyChart) => void;
}

export interface FilterData {
  name: string;
  value: string[];
}

interface PlotlyCSV {
  url: string;
  onFetch: (data: Array<{ [key: string]: any }>, config: DIChartPlotlyOptions, manager: DIPlotlyChart) => void; // eslint-disable-line @typescript-eslint/no-explicit-any
}

export interface SeriesGroup {
  name: string;
}

export type ChartTheme = 'default' | 'sunflower' | 'marigold' | 'rose' | 'lavendar' | 'bluebell' | 'leaf' | 'rainbow';

export interface DIChartPlotlyOptions {
  data?: Data[]; // if provided, use as the single source of chart data. Takes precendece over csv property
  layout: Partial<Layout>;
  config: Partial<Config>;
  csv?: PlotlyCSV; // only used if data property is not provided - URL of the CSV data source
  widgets: Partial<ChartWidgets>;
  onClick?: (data: PlotMouseEvent, manager: DIPlotlyChart) => void;
  seriesGroups?: SeriesGroup[];
  theme?: ChartTheme;
  utils: { [key: string]: any }; // eslint-disable-line @typescript-eslint/no-explicit-any
}

export interface FilterOptions {
  labelPrefix?: string;
  labelSuffix?: string;
}
