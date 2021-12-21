import React, { FC } from 'react';
import { Filter } from '../Filter';

interface PivotTableProps {
  data: Record<string, unknown>[];
  filters: Filter[];
  rowLabel: string;
  columnLabel: string;
  cellValue: string;
  showRowTotal?: boolean;
  showColumnTotal?: boolean;
}

export interface Filter {
  name: string;
  value?: string | number;
}

const applyFilters = (data: Record<string, unknown>[], filter: Filter[]) => {
  return data.filter(
    (record) => filter.filter((f) => (f.value ? record[f.name] === f.value : true)).length === filter.length,
  );
};

const PivotTable: FC<PivotTableProps> = (props) => {
  console.log(props);
  const renderFilters = () => {
    const filterData = applyFilters(props.data, props.filters);
    console.log(filterData);
  };

  renderFilters();

  return (
    <div>
      <div className="filter--wrapper highlight">
        <form className="form resources-filters">
          <Filter
            id="pivot-filter"
            label="Options:"
            options={[
              { value: 'testing', caption: 'Testing' },
              { value: 'test', caption: 'Loading' },
            ]}
          />
        </form>
      </div>
    </div>
  );
};

export { PivotTable };
