import React, { FC } from 'react';

interface PivotTableProps {
  data: Record<string, unknown>[];
}

const PivotTable: FC<PivotTableProps> = () => {
  return <div>Table Goes Here!</div>;
};

export { PivotTable };
