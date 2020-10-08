import { EChartOption } from 'echarts';
import { Layout, Data, Config, LegendClickEvent, PlotMouseEvent } from 'plotly.js';
import { DIPlotlyChart } from '../plotly';
import { DIChart } from '../dicharts';
import { DIEChart } from '../echarts';

export interface DIChartConfig {
  className: string;
  plotly?: DIChartPlotlyOptions;
  d3?: DIChartD3Options;
  echarts?: DIChartEChartOptions;
  elements?: HTMLElement[];
}

export interface ChartWidgets {
  filters?: ChartFilter[];
}

interface PlotlyChartWidgets extends ChartWidgets {
  legend?: PlotlyChartLegend;
}

export interface ChartFilter {
  className: string;
  options?: string[];
  multi?: boolean; // multi-select
  getOptions?: (manager: DIChart) => string[];
  onChange: (event: MouseEvent, manager: DIChart) => void;
}

export interface PlotlyChartLegend {
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
  widgets: Partial<PlotlyChartWidgets>;
  onClick?: (data: PlotMouseEvent, manager: DIPlotlyChart) => void;
  seriesGroups?: SeriesGroup[];
  theme?: ChartTheme;
  onAdd?: (elements: NodeListOf<Element>) => void;
  utils: { [key: string]: any }; // eslint-disable-line @typescript-eslint/no-explicit-any
}

export interface FilterOptions {
  labelPrefix?: string;
  labelSuffix?: string;
}

export interface FilterOption {
  label: string;
  value: string;
}

export interface DIChartD3Options {
  onAdd?: (elements: NodeListOf<Element>) => void;
  widgets?: Partial<ChartWidgets>;
}

export interface DIChartEChartOptions {
  options?: EChartOption;
  csv?: {
    url: string;
    onFetch: (data: Array<{ [key: string]: any }>, manager: DIEChart) => void; // eslint-disable-line @typescript-eslint/no-explicit-any
  };
  onInit?: (manager: DIEChart) => void;
  onAdd?: (elements: NodeListOf<Element>) => void;
  widgets?: Partial<ChartWidgets>;
}
