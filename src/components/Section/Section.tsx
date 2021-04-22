import classNames from 'classnames';
import React, { FunctionComponent, ReactText } from 'react';

type SectionProps = {
  title?: ReactText;
  id?: string;
  className?: string;
};

const Section: FunctionComponent<SectionProps> = (props) => {
  return (
    <section className={classNames('section', props.className)} id={props.id}>
      <div className="row row--narrow">
        {props.title ? <h2 className="section__heading">{props.title}</h2> : null}

        {props.children}
      </div>
    </section>
  );
};

export { Section };
