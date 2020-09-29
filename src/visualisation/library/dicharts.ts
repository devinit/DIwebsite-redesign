import { addLoading, removeLoading } from '../loading';
import { FilterOptions, ChartTheme } from './utils';

export class DIChart {
  chartElement: HTMLElement;
  theme: ChartTheme = 'default';

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
    selectElement.classList.add('data-selector--active');

    return selectElement;
  };

  getParentElement(): HTMLElement | null {
    return this.chartElement.parentElement;
  }

  getFilterText(option: string, { labelPrefix, labelSuffix }: FilterOptions = {}): string {
    return `${labelPrefix || ''}${option}${labelSuffix || ''}`;
  }

  getThemes = (): { [key in ChartTheme]: string[] } => {
    return {
      rainbow: [
        '#e84439',
        '#eb642b',
        '#f49b21',
        '#109e68',
        '#0089cc',
        '#893f90',
        '#c2135b',
        '#f8c1b2',
        '#f6bb9d',
        '#fccc8e',
        '#92cba9',
        '#88bae5',
        '#c189bb',
        '#e4819b',
      ],
      default: ['#6c120a', '#a21e25', '#cd2b2a', '#dc372d', '#ec6250', '#f6b0a0', '#fbd7cb', '#fce3dc'],
      sunflower: ['#7d4712', '#ba6b15', '#df8000', '#f7a838', '#fac47e', '#fedcab', '#fee7c1', '#feedd4'],
      marigold: ['#7a2e05', '#ac4622', '#cb5730', '#ee7644', '#f4a57c', '#facbad', '#fcdbbf', '#fde5d4'],
      rose: ['#65093d', '#8d0e56', '#9f1459', '#d12568', '#e05c86', '#f3a5b6', '#f6b8c1', '#f9cdd0'],
      lavendar: ['#42184c', '#632572', '#732c85', '#994d98', '#af73ae', '#cb98c4', '#deb5d6', '#ebcfe5'],
      bluebell: ['#0a3a64', '#00538e', '#1060a3', '#4397d3', '#77adde', '#a3c7eb', '#bcd4f0', '#d3e0f4'],
      leaf: ['#08492f', '#005b3e', '#00694a', '#3b8c62', '#74bf93', '#a2d1b0', '#b1d8bb', '#c5e1cb'],
    };
  };

  getTheme = (theme: ChartTheme = 'default'): [ChartTheme, string[]] => {
    return theme ? [theme, this.getThemes()[theme]] : [this.theme, this.getThemes()[this.theme]];
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
}
