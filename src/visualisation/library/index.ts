import Plotly from 'plotly.js';
import { addLoading, removeLoading } from '../loading';
import { FilterOptions } from './utils';
import { PlotlyManager } from './utils/plotly';

class DICharts {
  private chartElement: HTMLElement;

  constructor(chartNode: string | HTMLElement) {
    this.chartElement = this.getElement(chartNode);
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

  addFilter = (selectNode: string | HTMLSelectElement, options: string[], extra?: FilterOptions): HTMLSelectElement => {
    const selectElement = this.getElement(selectNode) as HTMLSelectElement;
    options.forEach((option) => {
      const optionElement = document.createElement('option');
      optionElement.value = option;
      optionElement.text = this.getFilterText(option, extra);
      selectElement.appendChild(optionElement);
    });

    return selectElement;
  };

  addPlotly = (plotly: typeof Plotly): PlotlyManager => {
    return new PlotlyManager(plotly, this.chartElement);
  };

  private getElement(element: string | HTMLElement) {
    if (!element) {
      throw new Error('An id to the element or an actual element is required');
    }
    if (typeof element === 'string') {
      const matchingElement = document.getElementById(element as string);
      if (!matchingElement) {
        throw new Error(`No element with id ${element}`);
      }

      return matchingElement;
    }

    return element;
  }

  private getParentElement() {
    return this.chartElement.parentElement;
  }

  private getFilterText(option: string, { labelPrefix, labelSuffix }: FilterOptions = {}) {
    return `${labelPrefix || ''}${option}${labelSuffix || ''}`;
  }
}

export { DICharts as Chart };
