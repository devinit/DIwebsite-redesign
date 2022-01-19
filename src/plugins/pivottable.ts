import { createElement } from 'react';
import { render } from 'react-dom';
import { Filter, PivotTable } from '../components/PivotTable';

const parseFiltersFromString = (filters: string[], filterDefaults: string[]): Filter[] =>
  filters.map((filter, index) => ({
    name: filter,
    value: index < filterDefaults.length ? filterDefaults[index] : undefined,
  }));

export const initPivotTables = function (): void {
  const pivotTables = document.querySelectorAll('.js-pivot-table');
  Array.prototype.forEach.call(pivotTables, (tableWrapper: HTMLDivElement) => {
    const {
      url: dataURL,
      filters,
      row,
      column,
      cell,
      rowTotal,
      columnTotal,
      filterDefaults,
      minimumValue,
    } = tableWrapper.dataset;
    if (dataURL) {
      window.d3.csv(dataURL, (data) => {
        render(
          createElement(PivotTable, {
            data,
            filters: parseFiltersFromString(filters?.split(',') || [], filterDefaults?.split(',') || []),
            rowLabel: row || '',
            columnLabel: column || '',
            showRowTotal: rowTotal === 'True',
            showColumnTotal: columnTotal === 'True',
            cellValue: cell || '',
            minimumValue: minimumValue || '',
          }),
          tableWrapper,
        );
      });
    }
  });
};
