import { createElement } from 'react';
import { render } from 'react-dom';
import { Filter, HighlightCondition, PivotTable } from '../components/PivotTable';
import { addLoading, removeLoading } from '../visualisation/loading';

const parseFiltersFromString = (filters: string[], filterDefaults: string[]): Filter[] =>
  filters.map((filter, index) => ({
    name: filter,
    value: index < filterDefaults.length ? filterDefaults[index] : undefined,
  }));

export const initPivotTables = function (): void {
  const pivotTables = document.querySelectorAll('.js-pivot-table');
  Array.prototype.forEach.call(pivotTables, (tableWrapper: HTMLDivElement) => {
    const tableParent = tableWrapper.parentElement?.parentElement;
    if (tableParent) {
      addLoading(tableParent);
    }
    const {
      url: dataURL,
      filters,
      row,
      column,
      cell,
      rowLabelHeading,
      rowTotal,
      columnTotal,
      filterDefaults,
      cellHighlightCondition,
      cellHighlightValue,
      rowHighlights,
    } = tableWrapper.dataset;
    if (dataURL) {
      window.d3.csv(dataURL, (data) => {
        if (tableParent) {
          removeLoading(tableParent);
        }
        render(
          createElement(PivotTable, {
            data,
            filters: filters ? parseFiltersFromString(filters?.split(',') || [], filterDefaults?.split(',') || []) : [],
            rowLabel: row || '',
            rowLabelHeading: rowLabelHeading || '',
            columnLabel: column || '',
            showRowTotal: rowTotal === 'True',
            showColumnTotal: columnTotal === 'True',
            cellValue: cell || '',
            cellHighlightCondition: cellHighlightCondition as HighlightCondition,
            cellHighlightValue,
            rowHighlights: JSON.parse(rowHighlights as string),
          }),
          tableWrapper,
        );
      });
    }
  });
};
