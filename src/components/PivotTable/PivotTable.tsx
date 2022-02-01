import React, { FC, useEffect, useState } from 'react';
import styled from 'styled-components';
import { Filter as SelectFilter } from '../Filter';
import { Table } from '../Table';
import {
  PivotTableProps,
  Filter,
  applyFilters,
  getFilterValues,
  getColumnValues,
  getRows,
  getColumnTotals,
  getRowsWithTotals,
  addCommas,
  highlightCell,
  RowHighlight,
  rowHighlightChecker,
} from './utils';

const HighlightedTableCell = styled.td<{ cell: string; highlight: boolean }>`
  background: ${(p) => (p.highlight ? '#ffb3b3' : 'none')};
`;
const BoldTableHeader = styled.th`
  font-weight: bold;
`;
export const StyledPivotTableHeader = styled.th<{ column: string }>`
  font-weight: ${(p) => (p.column === 'Grand Total' || 'Row Labels' ? 'bold' : 'normal')};
  white-space: ${(p) => (p.column === 'Grand Total' ? 'nowrap' : 'none')};
`;
export const FilterWrapper = styled.div`
  padding: 1rem 2rem 2rem 2rem;
`;
export const TableRow = styled.tr<{ highlightColor: string }>`
  background: ${(p) => (p.highlightColor ? p.highlightColor : 'none')};
`;

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

  const columns = props.showRowTotal
    ? [props.rowLabelHeading].concat(getColumnValues(data, props.columnLabel)).concat('Grand Total')
    : [props.rowLabelHeading].concat(getColumnValues(data, props.columnLabel));
  const [dataRows, highlightedRows] = getRows(
    data,
    { row: props.rowLabel, column: props.columnLabel, cell: props.cellValue },
    columns,
    props.showRowTotal as boolean,
    props.showColumnTotal as boolean,
    props.rowHighlights as RowHighlight[],
  );
  const columnValueTotals = getColumnTotals(columns, dataRows);
  const rows = props.showColumnTotal ? getRowsWithTotals(dataRows, columnValueTotals) : dataRows;

  return (
    <div>
      {props.filters.length ? (
        <FilterWrapper className="filter--wrapper">
          <form className="form resources-filters">{renderFilters()}</form>
        </FilterWrapper>
      ) : null}
      <Table>
        <thead>
          <tr>
            {columns.map((column, key) => (
              <StyledPivotTableHeader key={key} column={column}>
                {column}
              </StyledPivotTableHeader>
            ))}
          </tr>
        </thead>
        <tbody>
          {addCommas(rows).map((row, index) => (
            <TableRow key={`${index}`} highlightColor={rowHighlightChecker(highlightedRows, row[0])}>
              {row.map((cell, key) =>
                key === 0 ? (
                  cell === 'Grand Total' ? (
                    <BoldTableHeader key={key} scope="col">
                      {cell}
                    </BoldTableHeader>
                  ) : (
                    <th key={key} scope="col">
                      {cell}
                    </th>
                  )
                ) : (
                  <HighlightedTableCell
                    key={key}
                    cell={cell}
                    highlight={highlightCell(cell, props.cellHighlightCondition, Number(props.cellHighlightValue))}
                  >
                    {cell}
                  </HighlightedTableCell>
                ),
              )}
            </TableRow>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export { PivotTable };
