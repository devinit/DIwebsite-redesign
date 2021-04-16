export * from './events';

/**
 * Use when updating a chart's options
 * Captures the current options & adds an event listener that will revert to the old options when the canvas is clicked
 * @param chart echarts.ECharts
 */
export const addChartReverseListener = (chart: echarts.ECharts): void => {
  const currentOptions = chart.getOption();
  const chartNode = chart.getDom();
  const canvas = chartNode.getElementsByTagName('canvas')[0];
  if (canvas) {
    const onClick = () => {
      chart.setOption(currentOptions);
      canvas.removeEventListener('click', onClick);
    };
    canvas.addEventListener('click', onClick);
  }
};
