import React, { FC } from 'react';
import styled from 'styled-components';
import { TableBody } from './TableBody';

interface TableProps {
  columns: string[];
  rows: string[][];
  rowHeader?: boolean;
  minimumValue?: string;
}

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
                column === 'Row Labels' ? (
                  <TableHeader key={column} scope="col">
                    {column}
                  </TableHeader>
                ) : (
                  <th key={column} scope="col">
                    {column}
                  </th>
                )
              ) : (
                <ColumnTotalHeader key={column} scope="col">
                  {column}
                </ColumnTotalHeader>
              ),
            )}
          </tr>
        </thead>
        <tbody>
          {props.rows.map((row, index) => (
            <TableBody
              key={index}
              row={row}
              index={index}
              rowHeader={props.rowHeader}
              minimumValue={props.minimumValue}
            />
          ))}
        </tbody>
      </table>
    </div>
  );
};

export { Table };
