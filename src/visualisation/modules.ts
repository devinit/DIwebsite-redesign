import Plotly from 'plotly.js';
import { PlotlyCustom } from './plotly.custom';

// Get and return the correct plotly module based on chart type
export const loadPlotlyCode = async (data: Plotly.Data[]): Promise<PlotlyCustom> => {
  const chartTypes: Plotly.PlotType[] = data
    .map((trace) => trace.type)
    .reduce<Plotly.PlotType[]>(
      (prev, curr: Plotly.PlotType) => (prev.indexOf(curr) === -1 ? prev.concat([curr]) : prev),
      [],
    );

  const { newPlot, purge, register, react } = await import('./plotly.custom');

  register(await Promise.all(chartTypes.map(async (type) => await import(`plotly.js/lib/${type}`))));
  register([
    require('plotly.js/lib/aggregate'),
    require('plotly.js/lib/filter'),
    require('plotly.js/lib/groupby'),
    require('plotly.js/lib/sort'),
  ]);

  return { newPlot, purge, react };
};
