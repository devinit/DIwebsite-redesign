import React, { FC, useEffect, useState } from 'react';
import { Filter as SelectFilter } from '../Filter';
import { Table } from '../Table';
import { PivotTableProps, Filter, applyFilters, getFilterValues } from './utils';

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
    return filters.map((filter, index) => {
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

  console.log(data);

  return (
    <div>
      <div className="filter--wrapper highlight">
        <form className="form resources-filters">{renderFilters()}</form>

        <Table />
      </div>
    </div>
  );
};

export { PivotTable };
