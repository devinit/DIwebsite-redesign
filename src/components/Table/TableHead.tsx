import React, { FC } from 'react';
import { StyledPivotTableHeader } from '../PivotTable/utils';

interface TableHeadProps {
  columns: string[];
  as?: 'pivotTableHeader' | 'tableHeader';
}

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
            <StyledPivotTableHeader key={key} column={column}>
              {column}
            </StyledPivotTableHeader>
          ),
        )}
      </tr>
    </thead>
  );
};
TableHead.defaultProps = { as: 'tableHeader' };
export { TableHead };
