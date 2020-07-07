// trigger a double click on an element
const dblclick = (node: Element, descendentSelector: string, index: number): void => {
  const item = node.querySelectorAll(descendentSelector)[index];
  item.dispatchEvent(new MouseEvent('mousedown'));
  item.dispatchEvent(new MouseEvent('mouseup'));
  item.dispatchEvent(new MouseEvent('mousedown'));
  item.dispatchEvent(new MouseEvent('mouseup'));
};

// trigger a double click on a legend element
export const dblclickLegendItem = (legend: HTMLElement, index: number): void => {
  dblclick(legend, 'rect.legendtoggle', index);
};
