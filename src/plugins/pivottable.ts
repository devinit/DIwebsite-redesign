import { createElement } from 'react';
import { render } from 'react-dom';
import { PivotTable } from '../components/PivotTable';

export const initPivotTables = function (): void {
  const pivotTables = document.querySelectorAll('.js-pivot-table');
  Array.prototype.forEach.call(pivotTables, (tableWrapper: HTMLDivElement) => {
    const { url: dataURL, filters, row, column, cell, rowTotal, columnTotal } = tableWrapper.dataset;
    if (dataURL) {
      window.d3.csv(dataURL, (data) => {
        render(
          createElement(PivotTable, {
            data,
            filters: filters?.split(',') || [],
            rowLabel: row || '',
            columnLabel: column || '',
            showRowTotal: rowTotal === 'True',
            showColumnTotal: columnTotal === 'True',
            cellValue: cell || '',
          }),
          tableWrapper,
        );
      });
    }
  });
};
