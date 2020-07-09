export const getTreemapDataByLabel = (traces: Plotly.Data[], label: string): Partial<Plotly.PlotData>[] => {
  const newDataIndex = traces.findIndex((trace) => trace.name === label);

  return [traces[newDataIndex]];
};
