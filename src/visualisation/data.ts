import { ChartOptions } from './types';

export const getTreemapDataByLabel = (traces: Plotly.Data[], label: string): Partial<Plotly.PlotData>[] => {
  const newDataIndex = traces.findIndex((trace) => trace.name === label);

  return [traces[newDataIndex]];
};

export const showTraceByAggregationOption = (name: string, options: ChartOptions): boolean | null => {
  if (options.aggregationExcludes && options.aggregationExcludes.includes(name)) {
    return false;
  }
  if (options.aggregationIncludes) {
    return options.aggregationIncludes.includes(name);
  }

  return null; // return null if no aggregation options are configured
};

export const showTraceByChartOptions = (name: string, options: ChartOptions, defaultValue = false): boolean => {
  if (options.aggregated) {
    const showByAggregation = showTraceByAggregationOption(name, options);

    return showByAggregation !== null ? showByAggregation : options.aggregated;
  }

  return defaultValue;
};

export const setDefaultTraceVisibility = (data: Plotly.Data[], options: ChartOptions): void =>
  data.forEach((trace, traceIndex) => {
    if (trace.transforms) {
      trace.transforms.forEach((transform) => {
        if (transform.type === 'groupby' && Array.isArray(transform.groups)) {
          transform.styles = [];
          (transform.groups as string[]).forEach((group, groupIndex) => {
            const groupStyle = transform.styles?.find((style) => style.target === group);
            if (!groupStyle) {
              transform.styles?.push({
                target: group,
                value: { visible: showTraceByChartOptions(group, options, groupIndex === 0) },
              });
            } else {
              groupStyle.value.visible = showTraceByChartOptions(group, options, groupIndex === 0);
            }
          });
        }
      });
    } else {
      trace.visible = !!trace.name && showTraceByChartOptions(trace.name, options, traceIndex === 0);
    }
  });

export const showTraceByCondition = (
  data: Plotly.Data[],
  condition: (name: string, index: number) => boolean,
): Plotly.Data[] => {
  if (data.find((trace) => trace.transforms)) {
    return data
      .map((trace) => {
        trace.transforms?.forEach((transform) => {
          if (transform.type === 'groupby') {
            transform.styles?.forEach((style, index) => {
              style.value.visible = condition(style.target as string, index);
            });
          }
        });

        return trace;
      })
      .slice();
  }

  return data
    .map((trace, index) => {
      trace.visible = condition(trace.name as string, index);

      return trace;
    })
    .slice();
};

export const showTraceByIndex = (data: Plotly.Data[], index = 0): Plotly.Data[] => {
  const condition = (_name: string, idx: number) => idx === index;

  return showTraceByCondition(data, condition);
};
