import React, { FC } from 'react';
import styled from 'styled-components';

interface TableHeadProps {
  column: string;
}

const TableHeader = styled.th`
  font-weight: bold;
`;
const ColumnTotalHeader = styled.th`
  font-weight: bold;
  white-space: nowrap;
`;

const TableHead: FC<TableHeadProps> = (props) => {
  if (props.column !== 'Grand Total') {
    if (props.column === 'Row Labels') {
      return (
        <TableHeader key={props.column} scope="col">
          {props.column}
        </TableHeader>
      );
    }

    return (
      <th key={props.column} scope="col">
        {props.column}
      </th>
    );
  }

  return (
    <ColumnTotalHeader key={props.column} scope="col">
      {props.column}
    </ColumnTotalHeader>
  );
};
export { TableHead };
