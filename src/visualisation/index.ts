import 'core-js/stable';
import debounce from 'debounce';
import 'isomorphic-fetch';
import { PlotlyHTMLElement } from 'plotly.js';
import 'regenerator-runtime/runtime';
import { config } from './config';
import { getTreemapDataByLabel } from './data';
import { addLoading, removeLoading } from './loading';
import { loadPlotlyCode } from './modules';
import { addOptionsToSelectNode, createOptionsFromLegendData as createOptionsFromCalcData } from './options';
import { addHoverTemplateToTraces, removeTitle, setDefaultColorway, updateLayoutColorway } from './styles';
import { PlotlyConfig, PlotlyEnhancedHTMLElement } from './types';

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
        addLoading(chartNode);

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
        } else {
          // raw data in the page is used for previewing and drafts
          if (selectNode) {
            initSelectableChart(chartNode, data, selectNode, aggregated === 'True');
          } else {
            initStaticChart(chartNode, data);
          }
        }

        removelistener();
      }
    };
    window.addEventListener('resize', init);
    const removelistener = () => {
      window.removeEventListener('resize', init);
    };

    init();
  }
};

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

const initStaticChart = async (element: HTMLElement, chartConfig: PlotlyConfig) => {
  try {
    const { data, layout } = chartConfig;

    const { react, relayout } = await loadPlotlyCode(data);
    removeLoading(element);
    removeTitle(layout);
    addHoverTemplateToTraces(data);
    setDefaultColorway(layout);
    react(element, data, layout, config).then(() => updateLayoutColorway(element, relayout));
  } catch (error) {
    console.log(error);
  }
};

const showTraceByIndex = (data: Plotly.Data[], index = 0): Plotly.Data[] => {
  if (data.find((trace) => trace.transforms)) {
    return data
      .map((trace) => {
        trace.transforms?.forEach((transform) => {
          if (transform.type === 'groupby') {
            transform.styles?.forEach((style, _index) => {
              style.value.visible = index === _index;
            });
          }
        });

        return trace;
      })
      .slice();
  }

  return data
    .map((trace, _index) => {
      trace.visible = index === _index;

      return trace;
    })
    .slice();
};

const initSelectableChart = async (
  chartNode: HTMLElement,
  chartConfig: PlotlyConfig,
  selectNode: HTMLSelectElement,
  aggregated = false,
) => {
  try {
    const { data: _data, layout } = chartConfig;
    const { react, relayout } = await loadPlotlyCode(_data);
    const VIEW_ALL = 'All data';
    let data = _data.slice();
    const traces = Array.from(data);
    const isTreemap = data[0].type === 'treemap';

    if (!isTreemap) {
      layout.showlegend = false;
    }
    if (!aggregated) {
      data = showTraceByIndex(_data);
    }

    removeLoading(chartNode);
    removeTitle(layout);
    addHoverTemplateToTraces(data);
    setDefaultColorway(layout);

    if (isTreemap) {
      data = [traces[0]];
    }

    const updatePlot = (event: Event, plot: PlotlyHTMLElement & { data: Plotly.Data[] }) => {
      if (event.target) {
        const value = (event.target as HTMLSelectElement).value;
        if (isTreemap) {
          data = getTreemapDataByLabel(traces, selectNode.value);
          react(chartNode, data, layout);

          return;
        }

        if (plot.data.find((trace) => trace.transforms)) {
          const updatedData = plot.data
            .map((trace) => {
              trace.transforms?.forEach((transform) => {
                if (transform.type === 'groupby') {
                  transform.styles?.forEach((style) => {
                    style.value.visible = style.target === value || value === VIEW_ALL;
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
              trace.visible = value === VIEW_ALL || trace.name === value;

              return trace;
            })
            .slice();

          react(chartNode, updatedData, layout, config);
        }
      }
    };

    react(chartNode, data, layout, config)
      .then((myPlot) => {
        updateLayoutColorway(chartNode, relayout);

        return myPlot;
      })
      .then((myPlot: PlotlyEnhancedHTMLElement) => {
        const options = createOptionsFromCalcData(myPlot.calcdata);
        if (aggregated) {
          options.unshift(VIEW_ALL);
        }
        addOptionsToSelectNode(selectNode, options);
        selectNode.addEventListener('change', (event: Event) => updatePlot(event, myPlot), false);
      });
  } catch (error) {
    initStaticChart(chartNode, chartConfig);
  }
};

initPlotlyCharts();
window.addEventListener('scroll', debounce(initPlotlyCharts, 200));
