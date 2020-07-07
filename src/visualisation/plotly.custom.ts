import { Config, Data, Layout, PlotlyHTMLElement, Root } from 'plotly.js';

export { newPlot, Plots, purge, react, register, relayout } from 'plotly.js/lib/core';

export interface PlotlyCustom {
  newPlot: (root: Root, data: Data[], layout?: Partial<Layout>, config?: Partial<Config>) => Promise<PlotlyHTMLElement>;
  purge: (root: Root) => void;
  relayout?: (root: Root, layout: Partial<Layout>) => Promise<PlotlyHTMLElement>;
  react: (root: Root, data: Data[], layout?: Partial<Layout>, config?: Partial<Config>) => Promise<PlotlyHTMLElement>;
}
