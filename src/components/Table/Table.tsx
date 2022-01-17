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
}

const Table: FC<TableProps> = (props) => {
  const TableData = styled.td<StyledTableDataProps>`
    background: ${(p) => (props.minimumValue ? (+p.cell <= +props.minimumValue ? '#ffb3b3' : 'none') : 'none')};
  `;
  const TableHeader = styled.th`
    font-weight: bold;
  `;

  return (
    <div className="table-styled">
      <table>
        <thead>
          <tr>
            {props.columns.map((column) => (
              <TableHeader key={column} scope="col">
                {column}
              </TableHeader>
            ))}
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
