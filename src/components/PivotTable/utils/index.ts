import { Filter, HighlightCondition, HighlightedRow, RowHighlight } from './types';

export * from './types';

export const applyFilters = (data: Record<string, unknown>[], filter: Filter[]): Record<string, unknown>[] =>
  data.filter((record) => filter.filter((f) => (f.value ? record[f.name] === f.value : true)).length === filter.length);

export const getFilterValues = (data: Record<string, unknown>[], filter: Filter): string[] => {
  return data.reduce<string[]>((filterValues, current) => {
    const value = current[filter.name] as string | undefined;
    if (value && !filterValues.includes(value)) {
      return filterValues.concat(value);
    }

    return filterValues;
  }, []);
};

export const getColumnValues = (data: Record<string, unknown>[], propertyName: string): string[] => {
  return data
    .reduce<string[]>((columns, current) => {
      if (!columns.includes(current[propertyName] as string)) {
        return columns.concat(current[propertyName] as string);
      }

      return columns;
    }, [])
    .sort();
};

interface DataField {
  row: string;
  column: string;
  cell: string;
}

export const getTotals = (items: string[][]): number[] => {
  const totals = items.map((item) => {
    const values = item.slice(1).map((value) => Number(value));

    return values.reduce((previousValue, currentValue) => previousValue + currentValue);
  });

  return totals;
};

export const getColumnTotals = (columns: string[], rows: string[][]): number[] => {
  const columnValueList: string[][] = [];
  columns.slice(1).map((_column, index) => {
    const columnValues: string[] = [];
    rows.map((row, id) => {
      if (id !== rows.length - 1) {
        columnValues.push(row.slice(1)[index]);
      }
    });
    columnValueList.push(columnValues);
  });
  const totals = columnValueList.map((values) => {
    return values.map((val) => Number(val)).reduce((previousValue, currentValue) => previousValue + currentValue);
  });

  return totals;
};

export const getRowsWithTotals = (rows: string[][], columnTotals: number[]): string[][] => {
  rows.forEach((row, index) => {
    if (index === rows.length - 1) {
      row.forEach((_item, key) => {
        if (key < row.length - 1) {
          row[key + 1] = columnTotals[key]?.toString();
        }
      });
    }
  });

  return rows;
};

const highlightRow = (data: Record<string, unknown>, highlight: RowHighlight) => {
  if (!highlight.condition || !highlight.field || !highlight.value) return false;

  switch (highlight.condition) {
    case 'lt':
      return (data[highlight.field] as number) < highlight.value;
    case 'gt':
      return (data[highlight.field] as number) > highlight.value;
    case 'lte':
      return (data[highlight.field] as number) <= highlight.value;
    case 'gte':
      return (data[highlight.field] as number) >= highlight.value;
    case 'eq':
      return (data[highlight.field] as number | string) === highlight.value;

    default:
      false;
  }
};

export const getRows = (
  data: Record<string, unknown>[],
  fields: DataField,
  columns: string[],
  showRowTotal: boolean,
  showColumnTotal: boolean,
  highlights: RowHighlight[],
): [string[][], HighlightedRow[]] => {
  const GRAND_TOTAL_LABEL = 'Grand Total';
  const rowLabels = showColumnTotal
    ? getColumnValues(data, fields.row).concat(GRAND_TOTAL_LABEL)
    : getColumnValues(data, fields.row);

  const highlightedRows: HighlightedRow[] = [];
  const rows = rowLabels.map((label) => {
    const row: string[] = [label].concat(
      columns.slice(1).map((column) => {
        const matchingData = data.find((d) => d[fields.row] === label && d[fields.column] === column);

        if (matchingData) {
          // for those that match multiple highlight conditions, only the first will be applied
          highlights.forEach((highlight) => {
            if (!highlightedRows.map((item) => item.label).includes(label) && highlightRow(matchingData, highlight)) {
              highlightedRows.push({ label, color: highlight.color as string });
            }
          });
          const value = matchingData[fields.cell] as string;
          if (value) {
            return `${parseInt(value).toFixed()}`;
          }
        }

        return '';
      }),
    );

    return row;
  });
  if (showRowTotal) {
    const rowValueTotals: number[] = getTotals(rows);

    const rowsWithTotals = rows.map((row, index) => {
      row[row.length - 1] = rowValueTotals[index].toString();

      return row;
    });

    return [rowsWithTotals, highlightedRows];
  } else {
    return [rows, highlightedRows];
  }
};

export const addCommas = (rows: string[][]): string[][] => {
  rows.forEach((row) => {
    row.slice(1).forEach((item, index) => {
      if (item) {
        row[index + 1] = item.replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      }
    });
  });

  return rows;
};

export const highlightCell = (cellValue: string, condition?: HighlightCondition, compareValue?: number): boolean => {
  if (!condition || !compareValue) return false;
  const value = Number(cellValue.replace(',', ''));
  switch (condition) {
    case 'lt':
      return value < compareValue;
    case 'gt':
      return value > compareValue;
    case 'lte':
      return value <= compareValue;
    case 'gte':
      return value >= compareValue;
    case 'eq':
      return value === compareValue;
    default:
      return false;
  }
};

export const rowHighlightChecker = (highlightedRows: HighlightedRow[], value: string): string => {
  const highlightedRow = highlightedRows.find((item) => item.label === value);

  return highlightedRow ? highlightedRow.color : '';
};
