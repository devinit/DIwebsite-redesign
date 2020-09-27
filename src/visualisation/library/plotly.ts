import { Config, Data, Layout } from 'plotly.js';
import { DIChart } from './dicharts';
import { DIChartPlotlyOptions } from './utils';
import { PlotlyEnhancedHTMLElement } from '../types';
import deepmerge from 'deepmerge';

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

export class DIPlotlyChart extends DIChart {
  private options: DIChartPlotlyOptions;
  private data: Data[] = [];
  private layout: Partial<Layout> = {};
  private config: Partial<Config> = {};
  private plot?: PlotlyEnhancedHTMLElement;

  constructor(chartNode: HTMLElement, config: DIChartPlotlyOptions) {
    super(chartNode);

    this.options = config;
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

    return this;
  };

  setConfig = (config: Partial<Config> = {}): DIPlotlyChart => {
    this.config = deepmerge(this.config, config);

    return this;
  };

  getConfig = (config: Partial<Config> = {}): Config => {
    return deepmerge(defaultConfig, config);
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
      return this.newPlot(this.chartElement, this.data, this.layout, this.getConfig(this.config));
    }

    return window.Plotly.react(this.chartElement, this.data, this.layout, this.getConfig(this.config)).then(
      (plot: PlotlyEnhancedHTMLElement) => {
        this.addPlot(plot);

        return { plot, config: this.options };
      },
    );
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
        this.addPlot(plot);

        return { plot, config: this.options };
      },
    );
  }
}
