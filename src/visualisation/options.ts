import { ChartOptions } from './types';

// Assign an option to a select node
export const addOptionToSelectNode = (selectNode: HTMLSelectElement, value: string): void => {
  const currentOption = document.createElement('option');
  currentOption.text = value;
  selectNode.appendChild(currentOption);
};

export const addOptionsToSelectNode = (selectNode: HTMLSelectElement, options: string[]): void => {
  if (!options.length) {
    return;
  }
  options.forEach((option) => {
    if (!option) {
      return;
    }
    addOptionToSelectNode(selectNode, option);
  });
  selectNode.classList.add('data-selector--active');
};

const showTraceInSelector = (name: string, options: ChartOptions): boolean => {
  if (options.selectorExcludes && options.selectorExcludes.includes(name)) {
    return false;
  }
  if (options.selectorIncludes) {
    return options.selectorIncludes.includes(name);
  }

  return true;
};

export const createOptionsFromLegendData = (data: Plotly.Data[], chartOptions: ChartOptions): string[] =>
  data
    .filter((item) => (item.name ? showTraceInSelector(item.name, chartOptions) : false))
    .map((item) => item.name as string);
