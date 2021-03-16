import React, { FunctionComponent } from 'react';

const Card: FunctionComponent = () => {
  return (
    <div className="card card--offset">
      <div className="card__body">
        <span className="card__meta">Salary 2020</span>
        <h3 className="card__title">$75,000</h3>
      </div>
    </div>
  );
};

export { Card };
