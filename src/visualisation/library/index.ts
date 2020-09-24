import { DIChartsInstance } from './utils';
import { addLoading, removeLoading } from '../loading';

const getChartElement = (chartNode: string | HTMLElement): HTMLElement => {
  if (!chartNode) {
    throw new Error('An id to the chart element or an actual element is required');
  }
  if (typeof chartNode === 'string') {
    const chartElement = document.getElementById(chartNode as string);

    if (!chartElement) {
      throw new Error(`No element with id ${chartNode}`);
    }

    return chartElement;
  }

  return chartNode;
};

export const init = (chartNode: string | HTMLElement): DIChartsInstance => {
  const chartElement: HTMLElement = getChartElement(chartNode);

  const showLoading = (): void => {
    const chartWrapper = chartElement.parentElement;
    if (chartWrapper) {
      addLoading(chartWrapper);
    }
  };
  const hideLoading = (): void => {
    const chartWrapper = chartElement.parentElement;
    if (chartWrapper) {
      removeLoading(chartWrapper);
    }
  };

  return {
    loading: {
      show: showLoading,
      hide: hideLoading,
    },
    chartElement,
    parentElement: chartElement.parentElement,
  };
};
