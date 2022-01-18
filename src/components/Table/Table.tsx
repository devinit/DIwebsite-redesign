import React, { FC } from 'react';
import styled from 'styled-components';

interface TableProps {
  columns: string[];
  rows: string[][];
  rowHeader?: boolean;
  minimumValue?: string;
}

interface StyledTableDataProps {
  cell: string;
  minimumValue: string;
}

const TableData = styled.td<StyledTableDataProps>`
  background: ${(p) => (p.minimumValue ? (+p.cell <= +p.minimumValue ? '#ffb3b3' : 'none') : 'none')};
`;
const TableHeader = styled.th`
  font-weight: bold;
`;
const ColumnTotalHeader = styled.th`
  font-weight: bold;
  white-space: nowrap;
`;
const Table: FC<TableProps> = (props) => {
  return (
    <div className="table-styled">
      <table>
        <thead>
          <tr>
            {props.columns.map((column) =>
              column !== 'Grand Total' ? (
                <TableHeader key={column} scope="col">
                  {column}
                </TableHeader>
              ) : (
                <ColumnTotalHeader key={column} scope="col">
                  {column}
                </ColumnTotalHeader>
              ),
            )}
          </tr>
        </thead>
        <tbody>
          {props.rows.map((row, index) => {
            return (
              <tr key={`${index}`}>
                {row.map((cell, key) =>
                  key === 0 && props.rowHeader ? (
                    <TableHeader key={key} scope="col">
                      {cell}
                    </TableHeader>
                  ) : (
                    <TableData key={key} cell={cell} minimumValue={props.minimumValue as string}>
                      {cell ? cell.replace(/\B(?=(\d{3})+(?!\d))/g, ',') : cell}
                    </TableData>
                  ),
                )}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};

export { Table };
