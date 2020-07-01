import Plotly, { Config } from 'plotly.js';
import { PlotlyConfig } from './types';

// Default hover template
const hovertemplate =
  '<b>%{fullData.meta.columnNames.y}</b><br>' +
  '%{xaxis.title.text}: <b>%{x}</b><br>' +
  '%{yaxis.title.text}: <b>%{y}</b><extra></extra>';

// config object for new plots
const config: Partial<Config> = {
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

// min width at which interactive chart should be displayed at
const minWidth = 700;

// Assign an option to a select node
const assignOption = (selectNode: HTMLSelectElement, value: string) => {
  const currentOption = document.createElement('option');
  currentOption.text = value;
  selectNode.appendChild(currentOption);
};

// Take an array of strings and assign as options to a select node
const assignOptions = (selectNode: HTMLSelectElement, options: string[]) => {
  options.forEach((option) => {
    assignOption(selectNode, option);
  });
  selectNode.classList.add('data-selector--active');
};

// Assign the default hover template to each data node if there isn't one defined
const updateDataHoverTemplate = (data: Plotly.Data[]) => {
  data.forEach((item) => {
    if (!item.hovertemplate) {
      item.hovertemplate = hovertemplate;
    }
  });
};

// Assign a new colorway to the layout
const updateLayoutColorway = (layout: Plotly.Layout) => {
  layout.colorway = ['#c2135b', '#e84439', '#eb642b', '#f49b21', '#109e68', '#0089cc', '#893f90'];
};

// add loading on chart init
const addLoading = (el: HTMLElement) => {
  const loading = document.createElement('div');
  loading.innerHTML = '<div class="chart-loading__block">' + '<div></div><div></div><div></div><div></div></div>';
  loading.classList.add('chart-loading');
  el.classList.add('chart-container--loading');
  el.prepend(loading);
};

// remove loading from inited chart
const removeLoading = (element: HTMLElement) => {
  element.classList.remove('chart-container--loading');
  const loadingIndicator = element.querySelector('.chart-loading');
  if (loadingIndicator) {
    loadingIndicator.remove();
  }
};

// Get and return the correct plotly module based on chart type
const loadPlotlyCode = async (data: Plotly.Data[]): Promise<typeof Plotly> => {
  const chartBundles = {
    basicCharts: {
      types: ['bar', 'scatter', 'pie'],
      dist: () => import('plotly.js-basic-dist'),
    },
    cartesianCharts: {
      types: [
        'box',
        'heatmap',
        'histogram',
        'histogram2d',
        'histogram2dcontour',
        'image',
        'contour',
        'scatterternary',
        'violin',
      ],
      dist: () => import('plotly.js-cartesian-dist'),
    },
    financeCharts: {
      types: ['histogram', 'funnelarea', 'ohlc', 'candlestick', 'funnel', 'waterfall', 'indicator'],
      dist: () => import('plotly.js-finance-dist'),
    },
    geoCharts: {
      types: ['scattergeo', 'choropleth'],
      dist: () => import('plotly.js-geo-dist'),
    },
    geo2dCharts: {
      types: ['scattergl', 'splom', 'pointcloud', 'heatmapgl', 'contourgl', 'parcoords'],
      dist: () => import('plotly.js-gl2d-dist'),
    },
    geo3dCharts: {
      types: ['scatter3d', 'surface', 'mesh3d', 'isosurface', 'volume', 'cone', 'streamtube'],
      dist: () => import('plotly.js-gl3d-dist'),
    },
    mapboxCharts: {
      types: ['scattermapbox', 'choroplethmapbox', 'densitymapbox'],
      dist: () => import('plotly.js-mapbox-dist'),
    },
  };

  const isChartType = (chartTypes: string[]) => {
    return chartTypes.filter((chart) => data.find((_data) => _data.type === chart)).length;
  };

  for (const bundle of Object.values(chartBundles)) {
    if (isChartType(bundle.types)) {
      return await bundle.dist();
    }
  }

  return await import('plotly.js');
};

type Aggregated = 'True' | 'False' | undefined;

// Find and initiliase all charts
const initPlotlyCharts = () => {
  const wrappers = document.getElementsByClassName('js-plotly-chart-wrapper');

  if (wrappers.length) {
    for (let index = 0; index < wrappers.length; index++) {
      const element = wrappers.item(index) as HTMLElement;

      if (element) {
        const chartNode = element.getElementsByClassName('js-plotly-chart')[0] as HTMLDivElement | undefined;
        const selectNode = element.getElementsByClassName('js-plotly-chart-data-selector')[0] as
          | HTMLSelectElement
          | undefined;
        const scriptNode = element.getElementsByClassName('js-plotly-chart-raw-data')[0] as
          | HTMLScriptElement
          | undefined;

        if (chartNode) {
          const data = scriptNode ? JSON.parse(scriptNode.innerHTML) : null; // TODO: surround in try/catch
          const url = chartNode.dataset.url;
          const aggregated = chartNode.dataset.aggregated as Aggregated;

          const init = () => {
            // if window greater than min and chart not inited, init chart and set flag
            if (window.matchMedia(`(min-width: ${minWidth}px)`).matches) {
              // add loading on chart init
              addLoading(chartNode);

              // async data is used for live/page embedded chart requests
              if (url) {
                fetch(url).then((response) => {
                  response.json().then((d) => {
                    if (selectNode) {
                      initSelectableChart(chartNode, d, selectNode, aggregated === 'True');
                    } else {
                      initStaticChart(chartNode, d);
                    }
                  });
                });
              }

              // raw data in the page is used for previewing and drafts
              else {
                if (selectNode) {
                  initSelectableChart(chartNode, data, selectNode, aggregated === 'True');
                } else {
                  initStaticChart(chartNode, data);
                }
              }

              // remove listener if chart inited
              removelistener();
            }
          };

          // add the window resize listener
          window.addEventListener('resize', init);

          // remove the window resize listener
          const removelistener = () => {
            window.removeEventListener('resize', init);
          };

          // call the init function
          init();
        }
      }
    }
  }
};

// Initiliase a static chart
const initStaticChart = async (element: HTMLElement, chartConfig: PlotlyConfig) => {
  try {
    const { data, layout } = chartConfig;
    const { newPlot } = await loadPlotlyCode(data);
    // const config = { responsive: true };
    removeLoading(element);
    updateDataHoverTemplate(data);
    updateLayoutColorway(layout);
    newPlot(element, data, layout, config);
  } catch (error) {
    console.log(error);
  }
};

// Initiliase an selectable chart
const initSelectableChart = async (
  chartNode: HTMLElement,
  chartConfig: PlotlyConfig,
  selectNode: HTMLSelectElement,
  aggregated = false,
) => {
  try {
    const { data: _data, layout } = chartConfig;
    const { newPlot, react } = await loadPlotlyCode(_data);
    const config = { responsive: true };
    const all = 'All data';
    let data = _data.slice();
    const traces = data.slice();
    const options: string[] = [];
    const isTreemap = data[0].type === 'treemap';

    // remove loading from inited chart
    removeLoading(chartNode);

    // update the hover template
    updateDataHoverTemplate(data);

    // update the layout colorway
    updateLayoutColorway(layout);

    // add an extra all data option at the top if aggregated
    if (aggregated) {
      options.push(all);
    }

    // add the actual data options
    traces.forEach((trace) => {
      if (!isTreemap) options.push(trace.meta.columnNames.y);
      else if (trace.name) options.push(trace.name);
    });

    // if not aggregated, select the first data set only
    if (!aggregated) {
      data = [traces[0]];
    }

    // get the select and assign options
    assignOptions(selectNode, options);

    // change event listener
    const updateData = () => {
      // if all data selected, set data to whole set
      if (selectNode.value === all) {
        data = traces;
      }
      // otherwise find matching index and set data to the selected one
      else {
        const newDataIndex = traces.findIndex((trace) =>
          !isTreemap ? trace.meta.columnNames.y === selectNode.value : trace.name === selectNode.value,
        );
        data = [traces[newDataIndex]];
      }

      // update the chart
      react(chartNode, data, layout);
    };

    // assign change event listener
    selectNode.addEventListener('change', updateData, false);

    // initialise the chart
    newPlot(chartNode, data, layout, config);
  } catch (error) {
    console.log(error);
  }
};

// Begin initialisation
initPlotlyCharts();
