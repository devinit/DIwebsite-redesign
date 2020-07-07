// get data for treemap based on selected label
export const getTreemapData = (traces: Plotly.Data[], label: string): Partial<Plotly.PlotData>[] => {
  const newDataIndex = traces.findIndex((trace) => trace.name === label);

  return [traces[newDataIndex]];
};
