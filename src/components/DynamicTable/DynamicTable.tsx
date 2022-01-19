import React, { FC } from 'react';
import { Table } from '../Table';

interface DynamicTableProps {
  columns: string[];
  rows: string[][];
}
const DynamicTable: FC<DynamicTableProps> = (props) => {
  return (
    <div>
      <Table>
        <tr>
          {props.columns.map((column, index) => (
            <th key={index}>{column}</th>
          ))}
        </tr>
        <tbody>
          {props.rows.map((row, key) => (
            <tr key={key}>
              {row.map((cell, id) => (
                <td key={id}>{cell}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export { DynamicTable };
