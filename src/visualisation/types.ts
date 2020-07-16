export interface PlotlyConfig {
  data: Plotly.Data[];
  layout: Plotly.Layout;
}

export type PlotlyEnhancedHTMLElement = Plotly.PlotlyHTMLElement & PlotlyConfig & { calcdata: CalcData[][] };

/**
 * Undocumented but accessible as part of the returned object by the newPlot or react promises
 * Contains a lot more options than are documented here
 */
export interface CalcData {
  trace: Plotly.Data;
}
