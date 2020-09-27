import { Config, Data, Layout } from 'plotly.js';
import { DIChart } from './dicharts';
import { DIChartPlotlyConfig } from './utils';
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
  private config: DIChartPlotlyConfig;
  private plot?: PlotlyEnhancedHTMLElement;

  constructor(chartNode: HTMLElement, config: DIChartPlotlyConfig) {
    super(chartNode);

    this.config = config;
  }

  newPlot = (
    chartNode: HTMLElement,
    data: Data[],
    layout: Partial<Layout> = {},
    config: Partial<Config> = {},
  ): Promise<{ plot: PlotlyEnhancedHTMLElement; config: DIChartPlotlyConfig }> => {
    return window.Plotly.newPlot(chartNode, data, layout, this.getConfig(config)).then(
      (plot: PlotlyEnhancedHTMLElement) => {
        this.addPlot(plot);

        return { plot, config: this.config };
      },
    );
  };

  getPlot = (): PlotlyEnhancedHTMLElement | undefined => {
    return this.plot;
  };

  getConfig = (config: Partial<Config> = {}): Config => {
    return deepmerge(defaultConfig, config);
  };

  private addPlot(plot: PlotlyEnhancedHTMLElement): DIPlotlyChart {
    this.plot = plot;

    return this;
  }
}
