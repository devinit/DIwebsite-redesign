import React, { FunctionComponent, useEffect, useState } from 'react';

export type Option = {
  value: string | number;
  caption: string;
};

type FilterProps = {
  id: string;
  label?: string;
  options: Option[];
  onChange?: (event: React.ChangeEvent<HTMLSelectElement>) => void;
  value?: string;
};

const Filter: FunctionComponent<FilterProps> = (props) => {
  const [value, setValue] = useState(props.value || '');

  useEffect(() => {
    setValue(props.value || '');
  }, [props.value]);

  return (
    <div className="form-field form-field--inline-three">
      <label htmlFor={props.id} className="form-label form-label--hidden">
        {props.label}
      </label>
      <div className="form-field__select-dropdown">
        <select name="team-filter" id={props.id} onChange={props.onChange} value={value}>
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
