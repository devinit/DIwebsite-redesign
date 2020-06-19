const loadPlotlyCode = async (data: Plotly.Data[]): Promise<typeof Plotly> => {
  const basicCharts = ['bar', 'scatter', 'pie'];
  const cartesianCharts = [
    'box',
    'heatmap',
    'histogram',
    'histogram2d',
    'histogram2dcontour',
    'image',
    'contour',
    'scatterternary',
    'violin',
  ];
  const geoCharts = ['scattergeo', 'choropleth'];
  const geo3dCharts = ['scatter3d', 'surface', 'mesh3d', 'isosurface', 'volume', 'cone', 'streamtube'];
  const geo2dCharts = ['scattergl', 'splom', 'pointcloud', 'heatmapgl', 'contourgl', 'parcoords'];
  const mapboxCharts = ['scattermapbox', 'choroplethmapbox', 'densitymapbox'];
  const financeCharts = ['histogram', 'funnelarea', 'ohlc', 'candlestick', 'funnel', 'waterfall', 'indicator'];
  if (financeCharts.filter((chart) => data.find((_data) => _data.type === chart))) {
    return await import('plotly.js-finance-dist');
  }
  if (mapboxCharts.filter((chart) => data.find((_data) => _data.type === chart))) {
    return await import('plotly.js-mapbox-dist');
  }
  if (geo2dCharts.filter((chart) => data.find((_data) => _data.type === chart))) {
    return await import('plotly.js-gl2d-dist');
  }
  if (geo3dCharts.filter((chart) => data.find((_data) => _data.type === chart))) {
    return await import('plotly.js-gl3d-dist');
  }
  if (geoCharts.filter((chart) => data.find((_data) => _data.type === chart))) {
    return await import('plotly.js-geo-dist');
  }
  if (cartesianCharts.filter((chart) => data.find((_data) => _data.type === chart))) {
    return await import('plotly.js-cartesian-dist');
  }
  if (basicCharts.filter((chart) => data.find((_data) => _data.type === chart))) {
    return await import('plotly.js-basic-dist');
  }

  return await import('plotly.js');
};

const initPlotlyChart = async () => {
  const wrappers = document.getElementsByClassName('plotly-chart-wrapper');
  if (wrappers.length) {
    for (let index = 0; index < wrappers.length; index++) {
      const element = wrappers.item(index) as HTMLElement;
      if (element) {
        const chartNode = element.getElementsByClassName('plotly-chart')[0] as HTMLDivElement | undefined;
        const inputNode = element.getElementsByClassName('plotly-chart-input')[0] as HTMLInputElement | undefined;
        if (chartNode && inputNode) {
          const options = inputNode.value;
          try {
            const { data, layout } = JSON.parse(options);
            const { newPlot } = await loadPlotlyCode(data);
            newPlot(element, data, layout);
          } catch (error) {
            console.log(error);
          }
        }
      }
    }
  }
};

initPlotlyChart();
