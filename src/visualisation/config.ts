import { Config } from 'plotly.js';
import { PlotlyEnhancedHTMLElement } from './types';
const modebarButtons = require('plotly.js/src/components/modebar/buttons'); // eslint-disable-line

const onImageClick = modebarButtons.toImage.click;
modebarButtons.toImage.click = (chartNode: PlotlyEnhancedHTMLElement) => {
  // customise layout before downloading image
  chartNode.layout.title = { text: window.location.href };
  onImageClick(chartNode);
  chartNode.layout.title = { text: '' };
};

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
