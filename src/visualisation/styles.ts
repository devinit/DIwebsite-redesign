import Plotly from 'plotly.js';

// Default hover template
const hovertemplate =
  '<b>%{fullData.meta.columnNames.y}</b><br>' +
  '%{xaxis.title.text}: <b>%{x}</b><br>' +
  '%{yaxis.title.text}: <b>%{y}</b><extra></extra>';

// Assign the default hover template to each data node if there isn't one defined
export const updateDataHoverTemplate = (data: Plotly.Data[]): void => {
  data.forEach((item) => {
    if (!item.hovertemplate) {
      item.hovertemplate = hovertemplate;
    }
  });
};

// Assign a new colorway to the layout
export const updateLayoutColorway = (layout: Plotly.Layout): void => {
  layout.colorway = [
    '#e84439',
    '#eb642b',
    '#f49b21',
    '#109e68',
    '#0089cc',
    '#893f90',
    '#c2135b',
    '#f8c1b2',
    '#fccc8e',
    '#f6bb9d',
    '#92cba9',
    '#88bae5',
    '#c189bb',
    '#e4819b',
  ];
};

// remove the chart title
export const removeTitle = (layout: Plotly.Layout): void => {
  layout.title = '';
};
