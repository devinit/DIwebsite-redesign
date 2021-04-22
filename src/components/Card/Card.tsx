import React, { FunctionComponent, ReactText } from 'react';
import styled from 'styled-components';

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

export const CardMetaLarge = styled.span.attrs(() => ({ className: 'card__meta' }))`
  font-size: 1.3rem;
`;

export const CardTitleLarge = styled.h3.attrs(() => ({ className: 'card__title' }))`
  font-size: 3rem;
  margin-bottom: 0;
`;

export { Card };
