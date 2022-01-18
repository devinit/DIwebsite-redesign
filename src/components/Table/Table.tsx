import React, { FC } from 'react';

const Table: FC = (props) => {
  return (
    <div className="table-styled">
      <table>{props.children}</table>
    </div>
  );
};

export { Table };
