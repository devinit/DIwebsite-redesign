import React, { FunctionComponent, ReactText } from 'react';

type SectionProps = {
  title?: ReactText;
};

const Section: FunctionComponent<SectionProps> = (props) => {
  return (
    <section className="section">
      <div className="row row--narrow">{props.title ? <h2 className="section__heading">{props.title}</h2> : null}</div>
      {props.children}
    </section>
  );
};

export { Section };
