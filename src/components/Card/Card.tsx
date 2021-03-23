import React, { FunctionComponent, ReactText } from 'react';

type CardProps = {
  meta?: ReactText;
  title?: ReactText;
};

const Card: FunctionComponent<CardProps> = (props) => {
  return (
    <div className="card card--offset">
      <div className="card__body">
        {props.meta ? <span className="card__meta">{props.meta}</span> : null}
        {props.title ? <h3 className="card__title">{props.title}</h3> : null}
        {props.children}
      </div>
    </div>
  );
};

export { Card };
