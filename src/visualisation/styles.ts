import Plotly, { relayout as Relayout } from 'plotly.js';
import { PlotlyEnhancedHTMLElement, ChartOptions } from './types';

const MAX_TRACES_FOR_THEME = 8;
// Default hover template
const hovertemplate = `
    <b style="font-family:Geomanist Bold,sans-serif!important;">%{fullData.name}</b><br>
    %{xaxis.title.text}: <b>%{x}</b><br>
    %{yaxis.title.text}: <b>%{meta.yAxisPrefix}%{y:,.1f}%{meta.yAxisSuffix}</b><extra></extra>`;

// Map of colorways, applied based on number of items in legend and body class if present
const colorways = {
  rainbow: [
    '#e84439',
    '#eb642b',
    '#f49b21',
    '#109e68',
    '#0089cc',
    '#893f90',
    '#c2135b',
    '#f8c1b2',
    '#f6bb9d',
    '#fccc8e',
    '#92cba9',
    '#88bae5',
    '#c189bb',
    '#e4819b',
  ],
  default: ['#6c120a', '#a21e25', '#cd2b2a', '#dc372d', '#ec6250', '#f6b0a0', '#fbd7cb', '#fce3dc'],
  sunflower: ['#7d4712', '#ba6b15', '#df8000', '#f7a838', '#fac47e', '#fedcab', '#fee7c1', '#feedd4'],
  marigold: ['#7a2e05', '#ac4622', '#cb5730', '#ee7644', '#f4a57c', '#facbad', '#fcdbbf', '#fde5d4'],
  rose: ['#65093d', '#8d0e56', '#9f1459', '#d12568', '#e05c86', '#f3a5b6', '#f6b8c1', '#f9cdd0'],
  lavendar: ['#42184c', '#632572', '#732c85', '#994d98', '#af73ae', '#cb98c4', '#deb5d6', '#ebcfe5'],
  bluebell: ['#0a3a64', '#00538e', '#1060a3', '#4397d3', '#77adde', '#a3c7eb', '#bcd4f0', '#d3e0f4'],
  leaf: ['#08492f', '#005b3e', '#00694a', '#3b8c62', '#74bf93', '#a2d1b0', '#b1d8bb', '#c5e1cb'],
};

// Assign the default hover template to each data node if there isn't one defined
export const addHoverTemplateToTraces = (data: Plotly.Data[]): void => {
  data.forEach((item) => {
    if (!item.hovertemplate) {
      item.hovertemplate = hovertemplate;
    }
  });
};

export const setDefaultColorway = (layout: Plotly.Layout): void => {
  layout.colorway = colorways.default;
};

// Update the layout colorway based on legend and body class
export const updateLayoutColorway = (plotlyNode: PlotlyEnhancedHTMLElement, relayout: typeof Relayout): void => {
  try {
    const count = plotlyNode.calcdata.length;
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
      relayout(plotlyNode, { colorway });
    }
  } catch (e) {}
};

export const removeTitle = (layout: Plotly.Layout): void => {
  layout.title = '';
};

export const addLayoutMeta = (layout: Plotly.Layout, options: ChartOptions): void => {
  layout.meta = { title: options.title, imageCaption: options.imageCaption, source: options.source };
};
