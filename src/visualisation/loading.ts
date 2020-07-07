// add loading on chart init
export const addLoading = (element: HTMLElement): void => {
  const loading = document.createElement('div');
  loading.innerHTML = '<div class="chart-loading__block">' + '<div></div><div></div><div></div><div></div></div>';
  loading.classList.add('chart-loading');
  element.classList.add('chart-container--loading');
  element.prepend(loading);
};

// remove loading from inited chart
export const removeLoading = (element: HTMLElement): void => {
  element.classList.remove('chart-container--loading');
  const loadingIndicator = element.querySelector('.chart-loading');
  if (loadingIndicator) {
    loadingIndicator.remove();
  }
};
