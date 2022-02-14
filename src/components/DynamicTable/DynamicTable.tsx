import React, { FC, useEffect, useState } from 'react';
import { Table } from '../Table';

interface DynamicTableProps {
  data: Record<string, unknown>[];
}
const DynamicTable: FC<DynamicTableProps> = ({ data }) => {
  const [columns, setColumns] = useState<string[]>([]);
  const [rows, setRows] = useState<string[][]>([]);

  useEffect(() => {
    if (data) {
      setColumns(Object.keys(data[0]));
      setRows(data.map((record) => Object.values(record) as string[]));
    }
  }, [data.length]);

  return (
    <div>
      <Table>
        <thead>
          <tr>
            {columns.map((column, index) => (
              <th key={index}>{column}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rows.map((row, key) => (
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
