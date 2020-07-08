// add loading on chart init
export const addLoading = (element: HTMLElement): void => {
  element.classList.add('chart-container--loading');
};

// remove loading from initiated chart
export const removeLoading = (element: HTMLElement): void => {
  element.classList.remove('chart-container--loading');
  const loadingIndicator = element.querySelector('.chart-loading');
  if (loadingIndicator) {
    loadingIndicator.remove();
  }
};
