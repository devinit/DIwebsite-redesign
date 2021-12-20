import { createElement } from 'react';
import { render } from 'react-dom';
import { PivotTable } from '../components/PivotTable';

export const initPivotTables = function (): void {
  const pivotTables = document.querySelectorAll('.js-pivot-table');
  Array.prototype.forEach.call(pivotTables, (tableWrapper: HTMLDivElement) => {
    const dataURL = tableWrapper.dataset.url;
    if (dataURL) {
      window.d3.csv(dataURL, (data) => {
        render(createElement(PivotTable, { data }), tableWrapper);
      });
    }
  });
};
