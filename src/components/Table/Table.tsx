import classNames from 'classnames';
import React, { FC } from 'react';

interface TableProps {
  className?: string;
}

const Table: FC<TableProps> = (props) => {
  return (
    <div className={classNames('table-styled', props.className)}>
      <table>{props.children}</table>
    </div>
  );
};

export { Table };
