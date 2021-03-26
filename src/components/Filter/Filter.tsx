import React, { FunctionComponent } from 'react';

export type Option = {
  value: string | number;
  caption: string;
};

type FilterProps = {
  id: string;
  label?: string;
  options: Option[];
  onChange?: (event: React.ChangeEvent<HTMLSelectElement>) => void;
};

const Filter: FunctionComponent<FilterProps> = (props) => {
  return (
    <div className="form-field form-field--inline-three">
      <label htmlFor={props.id} className="form-label form-label--hidden">
        {props.label}
      </label>
      <div className="form-field__select-dropdown">
        <select name="team-filter" id={props.id} onChange={props.onChange} defaultValue="">
          <option value="" disabled>
            {props.label}
          </option>
          {props.options.map((option, index) => (
            <option key={`${index}`} value={option.value}>
              {option.caption}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
};

export { Filter };
