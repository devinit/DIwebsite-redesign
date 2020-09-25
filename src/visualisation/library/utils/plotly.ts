import deepmerge from 'deepmerge';
import Plotly, { Config } from 'plotly.js';
import { PlotlyEnhancedHTMLElement } from '../../types';

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

export class PlotlyManager {
  private plotly: typeof Plotly;
  private chartElement: PlotlyEnhancedHTMLElement;

  constructor(instance: typeof Plotly, chartElement: HTMLElement) {
    this.plotly = instance;
    this.chartElement = chartElement as PlotlyEnhancedHTMLElement;
  }

  getPlotly = (): typeof Plotly => {
    return this.plotly;
  };

  getChartElement = (): PlotlyEnhancedHTMLElement => {
    return this.chartElement;
  };

  addChartElement = (chartElement: PlotlyEnhancedHTMLElement): PlotlyManager => {
    this.chartElement = chartElement;

    return this;
  };

  getConfig = (config: Partial<Config> = {}): Config => {
    return deepmerge(defaultConfig, config);
  };
}
