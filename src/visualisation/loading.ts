
// add loading on chart init
export const addLoading = (el: HTMLElement) => {
  const loading = document.createElement('div');
  loading.innerHTML = '<div class="chart-loading__block">' + '<div></div><div></div><div></div><div></div></div>';
  loading.classList.add('chart-loading');
  el.classList.add('chart-container--loading');
  el.prepend(loading);
};

// remove loading from inited chart
export const removeLoading = (element: HTMLElement) => {
  element.classList.remove('chart-container--loading');
  const loadingIndicator = element.querySelector('.chart-loading');
  if (loadingIndicator) {
    loadingIndicator.remove();
  }
};
