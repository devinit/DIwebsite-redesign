import React, { FunctionComponent, ReactText } from 'react';

type SectionProps = {
  title?: ReactText;
  id?: string;
};

const Section: FunctionComponent<SectionProps> = (props) => {
  return (
    <section className="section" id={props.id}>
      <div className="row row--narrow">
        {props.title ? <h2 className="section__heading">{props.title}</h2> : null}

        {props.children}
      </div>
    </section>
  );
};

export { Section };