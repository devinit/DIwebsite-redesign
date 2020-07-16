import { Config } from 'plotly.js';

// min width at which interactive chart should be displayed at
export const minWidth = 700;

// config object for new plots
export const config: Partial<Config> = {
  displayModeBar: true,
  responsive: true,
  showLink: true,
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
