import React, { FunctionComponent } from 'react';

type GridProps = {
  columns?: number;
};

const Grid: FunctionComponent<GridProps> = ({ columns, children }) => {
  return <div className={`l-${columns}up`}>{children}</div>;
};

Grid.defaultProps = {
  columns: 3,
};

export { Grid };
