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

export const getColumns = (data: Record<string, unknown>[], propertyName: string) => {
  return data
    .reduce<string[]>((columns, current) => {
      if (!columns.includes(current[propertyName] as string)) {
        return columns.concat(current[propertyName] as string);
      }

      return columns;
    }, [])
    .sort();
};
