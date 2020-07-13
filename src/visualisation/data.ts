export const getTreemapDataByLabel = (traces: Plotly.Data[], label: string): Partial<Plotly.PlotData>[] => {
  const newDataIndex = traces.findIndex((trace) => trace.name === label);

  return [traces[newDataIndex]];
};

export const setDefaultTraceVisibility = (data: Plotly.Data[], aggregated = false): void =>
  data.forEach((trace, traceIndex) => {
    if (trace.transforms) {
      trace.transforms.forEach((transform) => {
        if (transform.type === 'groupby' && Array.isArray(transform.groups)) {
          transform.styles = [];
          transform.groups.forEach((group, groupIndex) => {
            const groupStyle = transform.styles.find((style) => style.target === group);
            if (!groupStyle) {
              transform.styles.push({ target: group, value: { visible: aggregated || groupIndex === 0 } });
            } else {
              groupStyle.value.visible = aggregated || groupIndex === 0;
            }
          });
        }
      });
    } else {
      trace.visible = aggregated || traceIndex === 0;
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
