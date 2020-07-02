
// get data for treemap based on selected label
export const getTreemapData = (traces: Array, label: string) => {
  const newDataIndex = traces.findIndex(el => el.name == label);
  return [traces[newDataIndex]];
};
