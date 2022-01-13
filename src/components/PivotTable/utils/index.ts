import { Filter } from './types';

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

export const getColumnValues = (data: Record<string, unknown>[], propertyName: string) => {
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

export const getTotals = (items: string[][]) => {
  const totals = items.map((item) => {
    const values = item.slice(1).map((value)=> Number(value));
    return values.reduce((previousValue, currentValue) => previousValue + currentValue)
  })
  return totals
}

export const getColumnTotals = (columns: string[], rows: string[]) => {
  const columnValueList: string[][] = [];
  columns.slice(1).map((_column, index) => {
    const columnValues: string[] = [];
    rows.map((row, id) => {
      if(id !== rows.length - 1){
        columnValues.push(row.slice(1)[index])
      }
    })
    columnValueList.push(columnValues)
  })
  return getTotals(columnValueList);
}

export const getRows = (data: Record<string, unknown>[], fields: DataField, columns: string[]): string[][] => {
  const rowLabels = getColumnValues(data, fields.row).concat('Grand Total');
  const rows = rowLabels.map((label) => {
    const row: string[] = [label].concat(
      columns.slice(1).map((column) => {
        const matchingData = data.find((d) => d[fields.row] === label && d[fields.column] === column);

        if (matchingData) {
          // console.log(matchingData);
          const value = matchingData[fields.cell] as string;
          if (value) {
            return `${parseInt(value).toFixed(1)}`;
          }
        }

        return '';
      }),
    );

    return row;
  });
  const rowValueTotals: Number[] = getTotals(rows);
  return rows.map((row, index) => {
    row[row.length-1] = rowValueTotals[index].toString();
    return row
  })
};
