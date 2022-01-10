import React, { FC } from 'react';

interface TableProps {
  columns: string[];
  rows: string[][];
  rowHeader?: boolean;
}

const Table: FC<TableProps> = (props) => {
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
                    <td key={key}>{cell}</td>
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
