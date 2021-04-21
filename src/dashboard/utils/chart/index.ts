export * from './events';

export const colours = ['#6c120a', '#a21e25', '#cd2b2a', '#dc372d', '#ec6250', '#f6b0a0', '#fbd7cb', '#fce3dc'];
export const grid: echarts.EChartOption.Grid = {
  left: '3%',
  right: '4%',
  bottom: '3%',
  containLabel: true,
};

/**
 * Use when updating a chart's options
 * Captures the current options & adds an event listener that will revert to the old options when the canvas is clicked
 * @param chart echarts.ECharts
 */
export const addChartReverseListener = (chart: echarts.ECharts, merge = false): void => {
  const currentOptions = chart.getOption();
  const chartNode = chart.getDom();
  const canvas = chartNode.getElementsByTagName('canvas')[0];
  if (canvas) {
    const onClick = () => {
      chart.setOption(currentOptions, !merge);
      canvas.removeEventListener('click', onClick);
    };
    canvas.addEventListener('click', onClick);
  }
};

export const tootipFormatter = ({ prefix = '', suffix = '' }: { prefix?: string; suffix?: string }) => (
  params: echarts.EChartOption.Tooltip.Format,
): string => {
  const { value, seriesName } = params;

  /* eslint-disable @typescript-eslint/no-explicit-any */
  return value && seriesName && (value as any)[seriesName]
    ? `${prefix}${(value as any)[seriesName]}${suffix}`
    : 'No Data';
  /* eslint-enable @typescript-eslint/no-explicit-any */
};
