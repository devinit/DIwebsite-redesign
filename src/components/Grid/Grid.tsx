import classNames from 'classnames';
import React, { FunctionComponent } from 'react';

type GridProps = {
  columns?: number;
  className?: string;
};

const Grid: FunctionComponent<GridProps> = ({ columns, children, className }) => {
  return <div className={classNames(`l-${columns}up`, className)}>{children}</div>;
};

Grid.defaultProps = {
  columns: 3,
};

export { Grid };
