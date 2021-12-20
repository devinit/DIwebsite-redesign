export const initPivotTables = function (): void {
  // TODO: add code here
  const pivotTables = document.querySelectorAll('.js-pivot-table');
  Array.prototype.forEach.call(pivotTables, (table: HTMLDivElement) => {
    const dataURL = table.dataset.url;
    if (dataURL) {
      window.d3.csv(dataURL, (data) => {
        console.log(data);
      });
    }
  });
};
