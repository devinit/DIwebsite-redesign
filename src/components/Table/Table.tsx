import React, { FC } from 'react';
import { TableBody } from './TableBody';
import { TableHead } from './TableHead';

interface TableProps {
  columns: string[];
  rows: string[][];
  rowHeader?: boolean;
  minimumValue?: string;
}

const Table: FC<TableProps> = (props) => {
  return (
    <div className="table-styled">
      <table>
        <thead>
          <tr>
            {props.columns.map((column, key) => (
              <TableHead key={key} column={column} />
            ))}
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
