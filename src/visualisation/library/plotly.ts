import deepmerge from 'deepmerge';
import { Config, Data, Layout, LegendClickEvent } from 'plotly.js';
import { PlotlyEnhancedHTMLElement } from '../types';
import { DIChart } from './dicharts';
import { ChartTheme, DIChartPlotlyOptions, PlotlyChartLegend } from './utils';

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

export class DIPlotlyChart extends DIChart {
  private options: DIChartPlotlyOptions;
  private data: Data[] = [];
  private layout: Partial<Layout> = {};
  private config: Partial<Config> = {};
  private plot?: PlotlyEnhancedHTMLElement;
  private sourceData?: { [key: string]: string }[];

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
      colorway: this.getThemes()[theme],
    };
    this.theme = theme;

    return this;
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

    const colorways = this.getThemes();
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
        if (!this.plot && this.options.widgets) {
          this.initCustomWidgets(this.options.widgets);
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

  private initPlotlyWidgets() {
    const { widgets = {} } = this.options;
    if (widgets.legend) {
      this.handleLegend(widgets.legend);
    }
  }

  private handleLegend(legend: PlotlyChartLegend) {
    if (this.plot && legend.onClick) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      this.plot.on(<any>'plotly_legendclick', (data: LegendClickEvent) => {
        if (legend.onClick) {
          return legend.onClick(data, this);
        }

        return true;
      });
    }
  }
}
