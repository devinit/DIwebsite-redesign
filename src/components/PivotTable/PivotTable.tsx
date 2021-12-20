import React, { FC } from 'react';

interface PivotTableProps {
  data: Record<string, unknown>[];
  filters: string[];
  rowLabel: string;
  columnLabel: string;
  cellValue: string;
  showRowTotal?: boolean;
  showColumnTotal?: boolean;
}

const PivotTable: FC<PivotTableProps> = (props) => {
  console.log(props);

  return <div>Table Goes Here!</div>;
};

export { PivotTable };
