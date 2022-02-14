import { createElement } from 'react';
import { render } from 'react-dom';
import { DynamicTable } from '../components/DynamicTable';

export const initDynamicTables = function (): void {
  const dynamicTables = document.querySelectorAll('.js-dynamic-table');
  Array.prototype.forEach.call(dynamicTables, (tableWrapper: HTMLDivElement) => {
    const { url: dataURL } = tableWrapper.dataset;
    if (dataURL) {
      window.d3.csv(dataURL, (data) => {
        render(
          createElement(DynamicTable, {
            data,
          }),
          tableWrapper,
        );
      });
    }
  });
};
