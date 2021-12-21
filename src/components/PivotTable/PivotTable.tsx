import React, { FC, useEffect, useState } from 'react';
import { Filter } from '../Filter';
import { PivotTableProps, applyFilters, getFilterValues } from './utils';

const PivotTable: FC<PivotTableProps> = (props) => {
  const [data, setData] = useState(props.data);
  const [filters, setFilters] = useState(props.filters);

  useEffect(() => {
    setData(applyFilters(props.data, props.filters));
  }, [props.data.length, filters]);
  console.log(data);
  const renderFilters = () => {
    return props.filters.map((filter, index) => {
      return (
        <Filter
          key={filter.name}
          id={filter.name}
          label={filter.name}
          options={getFilterValues(props.data, filter).map((value) => ({ value: value, caption: value }))}
        />
      );
    });
  };

  return (
    <div>
      <div className="filter--wrapper highlight">
        <form className="form resources-filters">{renderFilters()}</form>
      </div>
    </div>
  );
};

export { PivotTable };
