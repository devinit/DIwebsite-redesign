import { Config, Data, Layout, LegendClickEvent } from 'plotly.js';
import { DIChart } from './dicharts';
import { DIChartPlotlyOptions, ChartFilter, FilterData, ChartLegend, ChartTheme } from './utils';
import { PlotlyEnhancedHTMLElement } from '../types';
import deepmerge from 'deepmerge';

export const defaultLayout: Partial<Layout> = {
  hovermode: 'closest',
};

export const defaultConfig: Partial<Config> = {
  displayModeBar: true,
  responsive: true,
  showLink: false,
  plotlyServerURL: 'https://chart-studio.plotly.com',
  toImageButtonOptions: {
    width: 1200,
    height: 657,
  },
  modeBarButtonsToRemove: [
    'pan2d',
    'select2d',
    'lasso2d',
    'hoverClosestCartesian',
    'hoverCompareCartesian',
    'toggleSpikelines',
  ],
};

const MAX_TRACES_FOR_THEME = 8;

const colorways: { [key in ChartTheme]: string[] } = {
  rainbow: [
    '#e84439',
    '#eb642b',
    '#f49b21',
    '#109e68',
    '#0089cc',
    '#893f90',
    '#c2135b',
    '#f8c1b2',
    '#f6bb9d',
    '#fccc8e',
    '#92cba9',
    '#88bae5',
    '#c189bb',
    '#e4819b',
  ],
  default: ['#6c120a', '#a21e25', '#cd2b2a', '#dc372d', '#ec6250', '#f6b0a0', '#fbd7cb', '#fce3dc'],
  sunflower: ['#7d4712', '#ba6b15', '#df8000', '#f7a838', '#fac47e', '#fedcab', '#fee7c1', '#feedd4'],
  marigold: ['#7a2e05', '#ac4622', '#cb5730', '#ee7644', '#f4a57c', '#facbad', '#fcdbbf', '#fde5d4'],
  rose: ['#65093d', '#8d0e56', '#9f1459', '#d12568', '#e05c86', '#f3a5b6', '#f6b8c1', '#f9cdd0'],
  lavendar: ['#42184c', '#632572', '#732c85', '#994d98', '#af73ae', '#cb98c4', '#deb5d6', '#ebcfe5'],
  bluebell: ['#0a3a64', '#00538e', '#1060a3', '#4397d3', '#77adde', '#a3c7eb', '#bcd4f0', '#d3e0f4'],
  leaf: ['#08492f', '#005b3e', '#00694a', '#3b8c62', '#74bf93', '#a2d1b0', '#b1d8bb', '#c5e1cb'],
};

export class DIPlotlyChart extends DIChart {
  private options: DIChartPlotlyOptions;
  private data: Data[] = [];
  private layout: Partial<Layout> = {};
  private config: Partial<Config> = {};
  private plot?: PlotlyEnhancedHTMLElement;
  private sourceData?: { [key: string]: string }[];
  private filters: FilterData[] = [];
  private theme: ChartTheme = 'default';

  constructor(chartNode: HTMLElement, options: DIChartPlotlyOptions) {
    super(chartNode);

    this.options = options;
  }

  getPlot = (): PlotlyEnhancedHTMLElement | undefined => {
    return this.plot;
  };

  setData = (data: Data[] = []): DIPlotlyChart => {
    this.data = data;

    return this;
  };

  setLayout = (layout: Partial<Layout> = {}): DIPlotlyChart => {
    this.layout = deepmerge(this.layout, layout);

    return this.setTheme(this.options.theme);
  };

  getLayout = (layout: Partial<Layout> = {}): Layout => {
    return deepmerge(defaultLayout, layout);
  };

  setTheme = (theme: ChartTheme = 'default'): DIPlotlyChart => {
    this.layout = {
      ...this.layout,
      colorway: colorways[theme],
    };
    this.theme = theme;

    return this;
  };

  getTheme = (theme: ChartTheme = 'default'): [ChartTheme, string[]] => {
    return theme ? [theme, colorways[theme]] : [this.theme, colorways[this.theme]];
  };

  setConfig = (config: Partial<Config> = {}): DIPlotlyChart => {
    this.config = deepmerge(this.config, config);

    return this;
  };

  getConfig = (config: Partial<Config> = {}): Config => {
    return deepmerge(defaultConfig, config);
  };

  getOptions = (): DIChartPlotlyOptions => {
    return this.options;
  };

  setFilters = (filters: FilterData[]): void => {
    this.filters = filters;
  };

  getFilters = (): FilterData[] => {
    return this.filters;
  };

  csv = (url: string): Promise<{ [key: string]: string }[]> => {
    return new Promise((resolve) => {
      window.Plotly.d3.csv(url, (data) => {
        resolve(data);
      });
    });
  };

  updatePlot = (): Promise<{ plot: PlotlyEnhancedHTMLElement; config: DIChartPlotlyOptions }> => {
    if (!this.plot) {
      return this.newPlot(this.chartElement, this.data, this.getLayout(this.layout), this.getConfig(this.config));
    }

    return window.Plotly.react(
      this.chartElement,
      this.data,
      this.getLayout(this.layout),
      this.getConfig(this.config),
    ).then((plot: PlotlyEnhancedHTMLElement) => {
      this.addPlot(plot);
      if (!this.options.theme) {
        this.updateLayoutColorway();
      }
      this.hideLoading();

      return { plot, config: this.options };
    });
  };

  setSourceData(data: { [key: string]: string }[]): DIPlotlyChart {
    this.sourceData = data;

    return this;
  }

  getSourceData(): { [key: string]: string }[] | undefined {
    return this.sourceData;
  }

  private updateLayoutColorway = (): void => {
    if (!this.plot) return;

    const count = this.plot.calcdata.length;
    let colorway = undefined;
    if (count > MAX_TRACES_FOR_THEME) {
      colorway = colorways.rainbow;
    } else {
      const bodyClass = document.body.classList;
      for (const [key, value] of Object.entries(colorways)) {
        if (bodyClass.contains(`body--${key}`) && value.length <= MAX_TRACES_FOR_THEME) {
          colorway = value;
          break;
        }
      }
    }
    if (colorway) {
      window.Plotly.relayout(this.chartElement, { colorway });
    }
  };

  private addPlot(plot: PlotlyEnhancedHTMLElement): DIPlotlyChart {
    this.plot = plot;

    return this;
  }

  private newPlot(
    chartNode: HTMLElement,
    data: Data[],
    layout: Partial<Layout> = {},
    config: Partial<Config> = {},
  ): Promise<{ plot: PlotlyEnhancedHTMLElement; config: DIChartPlotlyOptions }> {
    return window.Plotly.newPlot(chartNode, data, layout, this.getConfig(config)).then(
      (plot: PlotlyEnhancedHTMLElement) => {
        plot.on('plotly_click', (data) => {
          if (this.options.onClick) {
            this.options.onClick(data, this);
          }
        });
        if (!this.plot) {
          this.initCustomWidgets();
        }
        this.addPlot(plot);
        this.initPlotlyWidgets();
        if (!this.options.theme) {
          this.updateLayoutColorway();
        }
        this.hideLoading();

        return { plot, config: this.options };
      },
    );
  }

  private initCustomWidgets() {
    const { widgets = {} } = this.options;
    if (widgets.filters) {
      widgets.filters.forEach((filter) => this.handleFilter(filter));
    }
  }

  private initPlotlyWidgets() {
    const { widgets = {} } = this.options;
    if (widgets.legend) {
      this.handleLegend(widgets.legend);
    }
  }

  private handleFilter(filter: ChartFilter) {
    const parent = this.getParentElement();
    if (parent) {
      const selectElement = parent.querySelector(`.${filter.className}`) as HTMLSelectElement | null;
      if (selectElement) {
        let { options } = filter;
        if (!options && filter.getOptions) {
          options = filter.getOptions(this);
        }
        if (options && options.length) {
          this.addFilter(selectElement, options || []);
          this.addFilterEvents(selectElement, filter);
          this.setFilters(this.filters.concat({ name: filter.className, value: [options[0]] }));
        }
      } else {
        throw new Error(`No element with class ${filter.className}`);
      }
    }
  }

  private addFilterEvents(element: HTMLSelectElement, filter: ChartFilter) {
    if (filter.onChange) {
      element.addEventListener('change', (event: MouseEvent) => {
        const { value } = <HTMLSelectElement>event.target;
        this.setFilters(
          this.filters.map((item) => {
            if (item.name === filter.className && item.value.indexOf(value) === -1) {
              item.value = filter.multi ? item.value.concat(value) : [value];
            }

            return item;
          }),
        );
        filter.onChange(event, this);
      });
    }
  }

  private handleLegend(legend: ChartLegend) {
    if (this.plot && legend.onClick) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      this.plot.on(<any>'plotly_legendclick', (data: LegendClickEvent) => {
        if (legend.onClick) {
          legend.onClick(data, this);
        }
      });
    }
  }
}
