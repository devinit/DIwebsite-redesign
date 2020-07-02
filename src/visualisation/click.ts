
// trigger a double click on an element
const dblclick = (node: HTMLElement, descendentSelector: string, index: int) => {
  var item = node.querySelectorAll(descendentSelector)[index];
  item.dispatchEvent(new MouseEvent('mousedown'));
  item.dispatchEvent(new MouseEvent('mouseup'));
  item.dispatchEvent(new MouseEvent('mousedown'));
  item.dispatchEvent(new MouseEvent('mouseup'));
};

// trigger a double click on a legend element
export const dblclickLegendItem = (legend: SVGElement, index: int) => {
  dblclick(legend, 'rect.legendtoggle', index);
};

