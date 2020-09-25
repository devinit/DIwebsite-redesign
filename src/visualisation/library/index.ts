import { addLoading, removeLoading } from '../loading';

class DICharts {
  private chartElement: HTMLElement;

  constructor(chartNode: string | HTMLElement) {
    this.chartElement = this.setChartElement(chartNode);
  }

  showLoading = (): void => {
    const chartWrapper = this.getParentElement();
    if (chartWrapper) {
      addLoading(chartWrapper);
    }
  };
  hideLoading = (): void => {
    const chartWrapper = this.getParentElement();
    if (chartWrapper) {
      removeLoading(chartWrapper);
    }
  };

  private setChartElement(chartNode: string | HTMLElement) {
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
  }

  private getParentElement() {
    return this.chartElement.parentElement;
  }
}

export { DICharts as Chart };
