import React, { FC, useEffect, useState } from 'react';
import { Filter as SelectFilter } from '../Filter';
import { Table } from '../Table';
import { PivotTableProps, Filter, applyFilters, getFilterValues, getColumnValues, getRows } from './utils';

const PivotTable: FC<PivotTableProps> = (props) => {
  const [data, setData] = useState(props.data);
  const [filters, setFilters] = useState(props.filters);

  useEffect(() => {
    setData(applyFilters(props.data, filters));
  }, [props.data.length, filters]);

  const onChange = (event: React.ChangeEvent<HTMLSelectElement>, filter: Filter) => {
    setFilters(
      filters.map((_filter) => {
        if (_filter.name === filter.name) {
          filter.value = event.currentTarget.value;
        }

        return _filter;
      }),
    );
  };

  const renderFilters = () => {
    return filters.map((filter) => {
      return (
        <SelectFilter
          key={filter.name}
          id={filter.name}
          label={filter.name}
          options={getFilterValues(props.data, filter).map((value) => ({ value: value, caption: value }))}
          value={filter.value || ''}
          onChange={(event) => onChange(event, filter)}
        />
      );
    });
  };

  const columns = ['Row Labels'].concat(getColumnValues(data, props.columnLabel));
  const rows = getRows(data, { row: props.rowLabel, column: props.columnLabel, cell: props.cellValue }, columns);

  return (
    <div>
      <div className="filter--wrapper" style={{ padding: '3rem 0' }}>
        <form className="form resources-filters">{renderFilters()}</form>
      </div>

      <Table columns={columns} rows={rows} rowHeader />
    </div>
  );
};

export { PivotTable };
