import 'core-js/stable';
import debounce from 'debounce';
import 'isomorphic-fetch';
import { PlotlyHTMLElement } from 'plotly.js';
import 'regenerator-runtime/runtime';
import { dblclickLegendItem } from './click';
import { config } from './config';
import { getTreemapData } from './data';
import { addLoading, removeLoading } from './loading';
import { loadPlotlyCode } from './modules';
import { assignOptions, getOptions } from './options';
import { removeTitle, setDefaultColorway, updateDataHoverTemplate, updateLayoutColorway } from './styles';
import { PlotlyConfig } from './types';

type Aggregated = 'True' | 'False' | undefined;

const initChart = (wrapper: HTMLElement) => {
  const chartNode = wrapper.getElementsByClassName('js-plotly-chart')[0] as HTMLDivElement | undefined;
  const selectNode = wrapper.getElementsByClassName('js-plotly-chart-data-selector')[0] as
    | HTMLSelectElement
    | undefined;
  const scriptNode = wrapper.getElementsByClassName('js-plotly-chart-raw-data')[0] as HTMLScriptElement | undefined;

  if (chartNode) {
    const data = scriptNode ? JSON.parse(scriptNode.innerHTML) : null; // TODO: surround in try/catch
    const url = chartNode.dataset.url;
    const aggregated = chartNode.dataset.aggregated as Aggregated;
    const minWidth = chartNode.dataset.minWidth ? parseInt(chartNode.dataset.minWidth) : 400; // TODO: use a constant

    const init = async () => {
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
};

// Find and initiliase all charts
const initPlotlyCharts = () => {
  const wrappers = document.getElementsByClassName('js-plotly-chart-wrapper');

  if (wrappers.length) {
    for (let index = 0; index < wrappers.length; index++) {
      const wrapper = wrappers.item(index) as HTMLElement;

      if (wrapper && wrapper.classList.contains('js-lazy-loading')) {
        const bounds = wrapper.getBoundingClientRect();
        if (bounds.top + bounds.height > 0 && bounds.top - window.innerHeight <= 50) {
          wrapper.classList.remove('js-lazy-loading');
          initChart(wrapper);
        } else {
          const chartNode = wrapper.getElementsByClassName('js-plotly-chart')[0] as HTMLDivElement | undefined;
          if (chartNode) {
            addLoading(chartNode); // TODO: show placeholder image instead
          }
        }
      }
    }
  }
};

// Initiliase a static chart
const initStaticChart = async (element: HTMLElement, chartConfig: PlotlyConfig) => {
  try {
    const { data, layout } = chartConfig;

    const { newPlot, relayout } = await loadPlotlyCode(data);
    // const config = { responsive: true };
    removeLoading(element);
    removeTitle(layout);
    updateDataHoverTemplate(data);
    setDefaultColorway(layout);
    newPlot(element, data, layout, config).then(() => updateLayoutColorway(element, relayout));
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
    const { newPlot, react, relayout } = await loadPlotlyCode(_data);
    const all = 'All data';
    let data = _data.slice();
    const traces = Array.from(data);
    const isTreemap = data[0].type === 'treemap';
    let lastSelected = -1;
    let legend: HTMLElement | undefined = undefined;

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

    // set the default layout colorway
    setDefaultColorway(layout);

    // set the data to the first item if treemap
    if (isTreemap) {
      data = [traces[0]];
    }

    const updatePlot = (event: Event, plot: PlotlyHTMLElement & { data: Plotly.Data[] }) => {
      if (event.target) {
        const value = (event.target as HTMLSelectElement).value;
        if (isTreemap) {
          data = getTreemapData(traces, selectNode.value);
          react(chartNode, data, layout);

          return;
        }

        if (plot.data.find((trace) => trace.transforms)) {
          const updatedData = plot.data
            .map((trace) => {
              trace.transforms?.forEach((transform) => {
                if (transform.type === 'groupby') {
                  transform.styles?.forEach((style) => {
                    style.value.visible = style.target === value || value === all;
                  });
                }
              });

              return trace;
            })
            .slice();
          react(chartNode, updatedData, layout, config);
        } else {
          const updatedData = plot.data
            .map((trace) => {
              trace.visible = value === all || trace.name === value;

              return trace;
            })
            .slice();

          react(chartNode, updatedData, layout, config);
        }
      }
    };

    // initialise the chart and selector
    newPlot(chartNode, data, layout, config)
      .then((myPlot) => {
        updateLayoutColorway(chartNode, relayout);

        return myPlot;
      })
      .then((myPlot: PlotlyHTMLElement & { data: Plotly.Data[] }) => {
        // TODO: clean up this function
        // store a reference to the legend and hide it
        legend = chartNode.querySelectorAll('.legend')[0] as HTMLElement | undefined;
        if (!legend) return; // TODO: handle this scenario better ... error log?
        legend.style.cssText = 'display: none;';

        // create options list from legend (or data if treemap)
        const options = getOptions(legend, traces);

        // add an extra all data option at the top if aggregated
        if (!isTreemap && aggregated) {
          options.unshift(all);
        } else {
          // otherwise select the first legend item
          try {
            lastSelected = 0;
            dblclickLegendItem(legend, lastSelected);
          } catch (e) {}
        }

        // get the select and assign options
        assignOptions(selectNode, options as string[]);

        // assign change event listener
        selectNode.addEventListener('change', (event: Event) => updatePlot(event, myPlot), false);
      });
  } catch (error) {
    // if there's a problem then try a static chart
    initStaticChart(chartNode, chartConfig);
  }
};

initPlotlyCharts();
window.addEventListener('scroll', debounce(initPlotlyCharts, 200));
