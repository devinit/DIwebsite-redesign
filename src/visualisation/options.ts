import { CalcData } from './types';

// Assign an option to a select node
export const assignOption = (selectNode: HTMLSelectElement, value: string): void => {
  const currentOption = document.createElement('option');
  currentOption.text = value;
  selectNode.appendChild(currentOption);
};

// Take an array of strings and assign as options to a select node
export const assignOptions = (selectNode: HTMLSelectElement, options: string[]): void => {
  if (!options.length) {
    return;
  }
  options.forEach((option) => {
    if (!option) {
      return;
    }
    assignOption(selectNode, option);
  });
  selectNode.classList.add('data-selector--active');
};

// get the options from the legend items
export const getOptions = (legend: HTMLElement, traces: Plotly.Data[]): (string | undefined)[] => {
  if (legend) {
    const options: string[] = [];
    legend.querySelectorAll('.legendtext').forEach((el) => options.push((el as any).dataset.unformatted)); // eslint-disable-line @typescript-eslint/no-explicit-any

    return options;
  }

  return traces.map((el) => el.name);
};

export const createOptionsFromLegendData = (calcData: CalcData[][]): string[] => {
  return calcData.map((item) => item[0].trace.name as string);
};
