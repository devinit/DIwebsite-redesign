import { Config } from 'plotly.js';
import { PlotlyEnhancedHTMLElement } from './types';
const modebarButtons = require('plotly.js/src/components/modebar/buttons'); // eslint-disable-line

const MAX_VERTICAL_LEGEND_ITEMS = 25;
const MAX_NEAT_HORIZONTAL_LEGEND_ITEMS = 30;
const onImageClick = modebarButtons.toImage.click;
modebarButtons.toImage.click = (chartNode: PlotlyEnhancedHTMLElement) => {
  // customise layout before downloading image
  chartNode.layout.title = { text: chartNode.dataset.shareLink };
  const xAxisTitle = chartNode.layout.xaxis.title as Plotly.DataTitle;
  const meta = chartNode.layout.meta;
  chartNode.layout.xaxis.title = {
    text: `${xAxisTitle.text || ''}<br><br>${meta.imageCaption || meta.title}${
      meta.source ? `<br><sub>Source: ${meta.source}</sub>` : ''
    }`,
  };
  chartNode.layout.margin = { b: 120 };
  const showLegend = chartNode.layout.showlegend;
  chartNode.layout.showlegend = true;
  const defaultLegendOptions = chartNode.layout.legend || {};
  const visibleLegendItems = chartNode._fullData.filter((data) => data.visible).length;
  if (visibleLegendItems > MAX_VERTICAL_LEGEND_ITEMS) {
    chartNode.layout.legend = {
      ...defaultLegendOptions,
      orientation: 'h',
      y: visibleLegendItems > MAX_NEAT_HORIZONTAL_LEGEND_ITEMS ? -0.7 : -0.4,
      xanchor: 'center',
      x: 0.5,
      traceorder: 'reversed',
    };
  } else {
    chartNode.layout.legend = { ...defaultLegendOptions, orientation: 'v', y: 1, traceorder: 'reversed' };
  }

  onImageClick(chartNode);
  // reset edited chart configs
  chartNode.layout.title = { text: '' };
  chartNode.layout.xaxis.title = xAxisTitle;
  chartNode.layout.margin = { b: 80 };
  chartNode.layout.legend = defaultLegendOptions;
  chartNode.layout.showlegend = showLegend;
};

// config object for new plots
export const config: Partial<Config> = {
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
