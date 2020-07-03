import Plotly from 'plotly.js';
import { dblclickLegendItem } from './click';
import { minWidth, config } from './config';
import { getTreemapData } from './data';
import { addLoading, removeLoading } from './loading';
import { assignOption, assignOptions, getOptions } from './options';
import { loadPlotlyCode } from './modules';
import { updateDataHoverTemplate, updateLayoutColorway, removeTitle } from './styles';
import { PlotlyConfig } from './types';

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
    removeTitle(layout);
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
    const all = 'All data';
    let data = _data.slice();
    const traces = Array.from(data);
    const options: string[] = [];
    const isTreemap = data[0].type === 'treemap';
    let lastSelected = -1;
    let legend = undefined;

    // enable the legend and add opts
    if (!isTreemap) {
      const legendOpts = Object.assign(layout.legend || {}, {
        x: 1,
        xanchor: 'right',
        y: 1,
      });
      layout.showlegend = true;
      layout.legend = legendOpts;
    }

    // remove loading from inited chart
    removeLoading(chartNode);

    // remove the title
    removeTitle(layout);

    // update the hover template
    updateDataHoverTemplate(data);

    // update the layout colorway
    updateLayoutColorway(layout);

    // set the data to the first item if treemap
    if (isTreemap) {
      data = [traces[0]];
    }

    // change event listener
    const updateData = () => {

        // get the selected index, which will be one higher than required if aggregated
        const index = aggregated ? selectNode.selectedIndex - 1 : selectNode.selectedIndex;

        // if treemap, set the data to the selected index and redraw
        if (isTreemap) {
            data = getTreemapData(traces, selectNode.value);
            react(chartNode, data, layout);
        }

        // otherwise use the legend to update the chart
        else {

            // if this is the first selection trigger double click
            if (lastSelected == -1) {
              dblclickLegendItem(legend, index);
            }

            // if it's not the first click, then handle resetting the view and selecting the new index
            else {

              // if the data is grouped we need to doubleclick the last element to reset the view
              if (data.length == 1) {
                dblclickLegendItem(legend, lastSelected);

                // if index is less than zero, it's an all data reset so don't click again
                if (index > -1) {
                  dblclickLegendItem(legend, index);
                }
              }
              else {
                // if index is less than zero, just click the last selected again to reset
                if (index < 0) {
                  dblclickLegendItem(legend, lastSelected);
                }
                // otherwise reset and then click the selected index
                else {
                  dblclickLegendItem(legend, lastSelected);
                  dblclickLegendItem(legend, index);
                }
              }
            }

            // store the selected index
            lastSelected = index;
        }
    };

    // initialise the chart and selector
    newPlot(chartNode, data, layout, config)
      .then(() => {
        // store a reference to the legend and hide it
        try {
          legend = chartNode.querySelectorAll('.legend')[0];
          legend.style.cssText = 'display: none;';
        } catch (e) {}

        // create options list from legend (or data if treemap)
        const options = getOptions(legend, traces);

        // add an extra all data option at the top if aggregated
        if (!isTreemap && aggregated) {
          options.unshift(all);
        }
        else {
          // otherwise select the first legend item
          try {
            lastSelected = 0;
            dblclickLegendItem(legend, lastSelected);
          } catch (e) {}
        }

        // get the select and assign options
        assignOptions(selectNode, options);

        // assign change event listener
        selectNode.addEventListener('change', updateData, false);
      });
  }

  catch (error) {
    // if there's a problem then try a static chart
    initStaticChart(chartNode, chartConfig);
  }
};

// Begin initialisation
initPlotlyCharts();
