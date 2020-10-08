import { addLoading, removeLoading } from '../loading';
import { ChartFilter, ChartTheme, ChartWidgets, FilterData, FilterOption, FilterOptions } from './utils';

export class DIChart {
  chartElement: HTMLElement;
  theme: ChartTheme = 'default';
  filters: FilterData[] = [];

  constructor(chartNode: string | HTMLElement) {
    this.chartElement = this.getElement(chartNode);
  }

  setFilters = (filters: FilterData[]): void => {
    this.filters = filters;
  };

  getFilters = (): FilterData[] => {
    return this.filters;
  };

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

  addFilter = (
    selectNode: string | HTMLSelectElement,
    options: (string | FilterOption)[],
    extra?: FilterOptions,
  ): HTMLSelectElement => {
    const selectElement = this.getElement(selectNode) as HTMLSelectElement;
    options.forEach((option) => {
      const optionElement = document.createElement('option');
      optionElement.value = typeof option === 'string' ? option : option.value;
      optionElement.text = this.getFilterText(typeof option === 'string' ? option : option.label, extra);
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

  getPageTheme = (): [ChartTheme, string[]] | undefined => {
    const bodyClass = document.body.classList;
    const colorways = this.getThemes();
    let theme: [ChartTheme, string[]] | undefined;
    Object.keys(colorways).forEach((colour: ChartTheme) => {
      if (bodyClass.contains(`body--${colour}`)) {
        theme = this.getTheme(colour);
      }
    });

    return theme;
  };

  handleFilter(filter: ChartFilter): void {
    const parent = this.getParentElement();
    if (parent) {
      const selectElement = parent.querySelector(`.${filter.className}`) as HTMLSelectElement | null;
      if (selectElement) {
        let { options } = filter;
        if (!options && filter.getOptions) {
          options = filter.getOptions(this);
        }
        if (options && options.length) {
          this.addFilter(selectElement, options || []);
          this.addFilterEvents(selectElement, filter);
          this.setFilters(this.filters.concat({ name: filter.className, value: [options[0]] }));
        }
      } else {
        throw new Error(`No element with class ${filter.className}`);
      }
    }
  }

  addFilterEvents(element: HTMLSelectElement, filter: ChartFilter): void {
    if (filter.onChange) {
      element.addEventListener('change', (event: MouseEvent) => {
        const { value } = <HTMLSelectElement>event.target;
        this.setFilters(
          this.filters.map((item) => {
            if (item.name === filter.className && item.value.indexOf(value) === -1) {
              item.value = filter.multi ? item.value.concat(value) : [value];
            }

            return item;
          }),
        );
        filter.onChange(event, this);
      });
    }
  }

  initCustomWidgets(widgets: ChartWidgets): void {
    if (widgets.filters) {
      widgets.filters.forEach((filter) => this.handleFilter(filter));
    }
  }

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
