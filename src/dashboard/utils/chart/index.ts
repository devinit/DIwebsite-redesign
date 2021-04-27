import { toPounds } from '..';

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

type FormatterOptions = { prefix?: string; suffix?: string; currency?: boolean };

export const tootipFormatter = ({ prefix = '', suffix = '', currency }: FormatterOptions) => (
  params: echarts.EChartOption.Tooltip.Format,
): string => {
  const { value, seriesName } = params;

  /* eslint-disable @typescript-eslint/no-explicit-any */
  if (value && seriesName && (value as any)[seriesName]) {
    let rawValue = (value as any)[seriesName];
    if (typeof rawValue === 'number') {
      rawValue = Math.round(rawValue * 100) / 100;
    }
    const parsedValue = currency ? toPounds(rawValue) : rawValue;

    return `${prefix}${parsedValue}${suffix}`;
  }

  return 'No Data';
  /* eslint-enable @typescript-eslint/no-explicit-any */
};

export const getBarLabelConfig = (options: FormatterOptions & { position?: string }) => ({
  show: true,
  position: options.position || 'top',
  /* eslint-disable-next-line @typescript-eslint/no-explicit-any */
  formatter: (params: any): string => {
    const value = params.value[params.dimensionNames[params.encode.y[0]]];
    if (typeof value === 'number') {
      const roundedValue = Math.round(value * 100) / 100;

      return `${options.prefix || ''}${roundedValue}${options.suffix || ''}`;
    }

    return `${options.prefix || ''}${value}${options.suffix || ''}`;
  },
});
