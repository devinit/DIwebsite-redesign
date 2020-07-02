
// Assign an option to a select node
export const assignOption = (selectNode: HTMLSelectElement, value: string) => {
  const currentOption = document.createElement('option');
  currentOption.text = value;
  selectNode.appendChild(currentOption);
};

// Take an array of strings and assign as options to a select node
export const assignOptions = (selectNode: HTMLSelectElement, options: string[]) => {
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
export const getOptions = (legend: SVGElement, traces: Array) => {
  if (legend) {
    const options = [];
    legend.querySelectorAll('.legendtext').forEach(el => options.push(el.dataset.unformatted));
    return options;
  }
  return traces.map(el => el.name);
};

