import { CalcData } from './types';

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

export const createOptionsFromLegendData = (calcData: CalcData[][]): string[] =>
  calcData.map((item) => item[0].trace.name as string);
