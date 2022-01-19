import React, { FC } from 'react';
import { Table } from '../Table';

interface DynamicTableProps {
  data: Record<string, unknown>[];
}
const DynamicTable: FC<DynamicTableProps> = (props) => {
  console.log(props.data[0]);

  return (
    <div>
      {/* <Table>
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
      </Table> */}
    </div>
  );
};

export { DynamicTable };
