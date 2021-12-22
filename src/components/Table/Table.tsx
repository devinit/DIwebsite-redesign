import React, { FC } from 'react';

interface TableProps {
  columns: string[];
  rows: string[][];
  rowHeader?: boolean;
  columnHeader?: boolean;
}

const Table: FC<TableProps> = (props) => {
  console.log(props);

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
      </table>
    </div>
  );
};

export { Table };
