import React, { FC } from 'react';
import styled from 'styled-components';

interface TableBodyProps {
  row: string[];
  rowHeader?: boolean;
  minimumValue?: string;
  index: number;
}
interface StyledTableDataProps {
  cell: string;
  minimumValue: string;
}

const TableData = styled.td<StyledTableDataProps>`
  background: ${(p) => (p.minimumValue ? (+p.cell <= +p.minimumValue ? '#ffb3b3' : 'none') : 'none')};
`;
const TableHeader = styled.th`
  font-weight: bold;
`;

const TableBody: FC<TableBodyProps> = (props) => {
  return (
    <tr key={`${props.index}`}>
      {props.row.map((cell, key) =>
        key === 0 && props.rowHeader ? (
          cell === 'Grand Total' ? (
            <TableHeader key={key} scope="col">
              {cell}
            </TableHeader>
          ) : (
            <th key={key} scope="col">
              {cell}
            </th>
          )
        ) : (
          <TableData key={key} cell={cell} minimumValue={props.minimumValue as string}>
            {cell ? cell.replace(/\B(?=(\d{3})+(?!\d))/g, ',') : cell}
          </TableData>
        ),
      )}
    </tr>
  );
};
export { TableBody };
