import React, { FC } from 'react';
import styled from 'styled-components'

interface TableProps {
  columns: string[];
  rows: string[][];
  rowHeader?: boolean;
}

interface StyledTableDataProps {
  cell: string;
}

const Table: FC<TableProps> = (props) => {
  const TableData = styled.td<StyledTableDataProps>`
    background: ${p => (+p.cell <= 1) ? '#ffb3b3': 'none' }
  `
  return (
    <div className="table-styled">
      <table>
        <thead>
          <tr>
            {props.columns.map((column) => (
              <th key={column} scope="col">
                {column}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {props.rows.map((row, index) => {
            return (
              <tr key={`${index}`}>
                {row.map((cell, key) =>
                  key === 0 && props.rowHeader ? (
                    <th key={key} scope="col">
                      {cell}
                    </th>
                  ) : (
                    <TableData key={key} cell={cell}>
                      {cell}
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
