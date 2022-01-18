import React, { FC } from 'react';
import styled from 'styled-components';

interface TableHeadProps {
  columns: string[];
  as?: 'pivotTableHeader' | 'tableHeader';
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
        {props.columns.map((column, key) =>
          props.as === 'tableHeader' ? (
            <th scope="col" key={key}>
              {column}
            </th>
          ) : (
            <TableHeader key={key} column={column}>
              {column}
            </TableHeader>
          ),
        )}
      </tr>
    </thead>
  );
};
TableHead.defaultProps = { as: 'tableHeader' };
export { TableHead };
