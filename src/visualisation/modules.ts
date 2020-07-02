import Plotly from 'plotly.js';

// Get and return the correct plotly module based on chart type
export const loadPlotlyCode = async (data: Plotly.Data[]): Promise<typeof Plotly> => {
  const chartBundles = {
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

  const isChartType = (chartTypes: string[]) => {
    return chartTypes.filter((chart) => data.find((_data) => _data.type === chart)).length;
  };

  for (const bundle of Object.values(chartBundles)) {
    // basic doesn't allow groupby transforms, so test that first
    let hasGroupedByTransform = false;
    try {
      hasGroupedByTransform = data[0].transforms[0].type == 'groupby';
    } catch (e) {}

    // if no groupedby transform present, try to get the module based on matching type
    if (!hasGroupedByTransform) {
      if (isChartType(bundle.types)) {
        return await bundle.dist();
      }
    }
  }

  return await import('plotly.js');
};
