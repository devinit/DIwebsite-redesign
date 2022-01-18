import React, { FC } from 'react';
import styled from 'styled-components';

interface TableHeadProps {
  columns: string[];
}
interface StyledHeaderProps {
  column?: string;
}

const TableHeader = styled.th<StyledHeaderProps>`
  font-weight: ${(p) => (p.column === 'Grand Total' || 'Row Labels' ? 'bold' : 'normal')};
  white-space: ${(p) => (p.column === 'Grand Total' ? 'nowrap' : 'none')};
`;

const TableHead: FC<TableHeadProps> = (props) => {
  return (
    <thead>
      <tr>
        {props.columns.map((column, key) => (
          <th scope="col" key={key}>
            {column}
          </th>
        ))}
      </tr>
    </thead>
    // <TableHeader key={props.column} column={props.column} scope="col">
    //   {props.column}
    // </TableHeader>
  );
};
export { TableHead };
