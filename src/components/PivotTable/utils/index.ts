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

export const getRows = (data: Record<string, unknown>[], fields: DataField, columns: string[]): string[][] => {
  const rowLabels = getColumnValues(data, fields.row);

  return rowLabels.map((label) => {
    const row: string[] = [label].concat(
      columns.slice(1).map((column) => {
        const matchingData = data.find((d) => d[fields.row] === label && d[fields.column] === column);

        if (matchingData) {
          console.log(matchingData);

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
};

export const getRowTotals = (rows) => {
  const rowTotals = rows.map((row) => {
    const values = row.slice(1).map((value)=> Number(value));
    return values.reduce((previousValue, currentValue) => previousValue + currentValue)
  })
  return rowTotals
}
