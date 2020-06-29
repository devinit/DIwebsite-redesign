
// Get and return the correct plotly module based on chart type
const loadPlotlyCode = async (data: Plotly.Data[]): Promise<typeof Plotly> => {
  const chartTypes = {
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

  const isChartType = chartTypes => {
    return chartTypes.filter((chart) => data.find((_data) => _data.type === chart)).length;
  }

  for (const el of Object.values(chartTypes)) {
    if (isChartType(el.types)) {
      return await el.dist();
    }
  }

  return await import('plotly.js');
};

// Find and initiliase all charts
const initPlotlyCharts = () => {
  const wrappers = document.getElementsByClassName('js-plotly-chart-wrapper');

  if (wrappers.length) {

    for (let index = 0; index < wrappers.length; index++) {
      const element = wrappers.item(index) as HTMLElement;

      if (element) {
        const chartNode = element.getElementsByClassName('js-plotly-chart')[0] as HTMLDivElement | undefined;
        const selectNode = element.getElementsByClassName('js-plotly-chart-data-selector')[0] as HTMLSelectElement | undefined;
        const scriptNode = element.getElementsByClassName('js-plotly-chart-raw-data')[0] as HTMLScriptElement | undefined;

        if (chartNode) {
          const data = scriptNode ? JSON.parse(scriptNode.innerHTML) : null;
          const url = chartNode.dataset.url;
          const aggregated = chartNode.dataset.aggregated;

          // async data is used for live/page embedded chart requests
          if (url) {
            fetch(url).then(response => {
              response.json().then(d => {
                if (selectNode) {
                  initSelectableChart(chartNode, d, selectNode, aggregated);
                }
                else {
                  initStaticChart(chartNode, d);
                }
              });
            });
          }

          // raw data in the page is used for previewing and drafts
          else {
            if (selectNode) {
              initSelectableChart(chartNode, data, selectNode, aggregated);
            }
            else {
              initStaticChart(chartNode, data);
            }
          }

        }
      }
    }
  }
};

// Initiliase a static chart
const initStaticChart = async (el, d) => {
  try {
    const { data, layout } = d;
    const { newPlot } = await loadPlotlyCode(data);
    const config = { responsive: true };
    updateDataHoverTemplate(data);
    updateLayoutColorway(layout);
    newPlot(el, data, layout, config);
  } catch (error) {
    console.log(error);
  }
}

// Initiliase an selectable chart
const initSelectableChart = async (el, d, selectNode, aggregated = false) => {
  try {
    let { data, layout } = d;
    const { newPlot, react } = await loadPlotlyCode(data);
    const config = { responsive: true };
    const all = 'All data';
    const traces = data.slice();
    const options = [];
    const isTreemap = data[0].type == 'treemap';

    // update the hover template
    updateDataHoverTemplate(data);

    // update the layout colorway
    updateLayoutColorway(layout);

    // add an extra all data option at the top if aggregated
    if (aggregated) {
        options.push(all);
    }

    // add the actual data options
    traces.forEach(el => {
        !isTreemap ? options.push(el.meta.columnNames.y) : options.push(el.name);
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
        if (selectNode.value == all) {
            data = traces;
        }

        // otherwise find matching index and set data to the selected one
        else {
            const newDataIndex = traces.findIndex(el => !isTreemap ? el.meta.columnNames.y == selectNode.value : el.name == selectNode.value);
            data = [traces[newDataIndex]];
        }

        // update the chart
        react(el, data, layout);
    }

    // assign change event listener
    selectNode.addEventListener('change', updateData, false);

    // initialise the chart
    newPlot(el, data, layout, config);

  } catch (error) {
    console.log(error);
  }
}

// Begin initialisation
initPlotlyCharts();

// Default hover template
const hovertemplate = '<b>%{fullData.meta.columnNames.y}</b><br>' +
                       '%{xaxis.title.text}: <b>%{x}</b><br>' +
                       '%{yaxis.title.text}: <b>%{y}</b><extra></extra>';

// Assign an option to a select node
const assignOption = (selectNode, value) => {
    const currentOption = document.createElement('option');
    currentOption.text = value;
    selectNode.appendChild(currentOption);
};

// Take an array of strings and assign as options to a select node
const assignOptions = (selectNode, options) => {
  options.forEach(el => {
      assignOption(selectNode, el);
  });
  selectNode.classList.add('data-selector--active');
};

// Assign the default hover template to each data node if there isn't one defined
const updateDataHoverTemplate = data => {
  data.forEach(el => {
      if (!el.hovertemplate) {
          el.hovertemplate = hovertemplate;
      }
  });
};

// Assign a new colorway to the layout
const updateLayoutColorway = layout => {
  layout.colorway = ["#c2135b", "#e84439", "#eb642b", "#f49b21", "#109e68", "#0089cc", "#893f90"];
};
