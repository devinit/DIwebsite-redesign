import React, { FunctionComponent, useState } from 'react';
import styled from 'styled-components';
import { MediaCaption } from '../MediaCaption';

type ComponentProps = {
  buttonCaption: string;
};
const StyledButton = styled.button`
  padding: 0.8rem;
`;

const HiddenMediaCaption: FunctionComponent<ComponentProps> = (props) => {
  const [show, setShow] = useState(false);

  const onHover = () => setShow(true);
  const onBlur = () => setShow(false);

  return (
    <div className="media-caption__hidden">
      <StyledButton className="button" onMouseEnter={onHover} onMouseLeave={onBlur}>
        {props.buttonCaption}
      </StyledButton>
      {show ? <MediaCaption>{props.children}</MediaCaption> : null}
    </div>
  );
};

export { HiddenMediaCaption };
