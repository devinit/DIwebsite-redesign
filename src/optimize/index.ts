const toggleFeature = (classNames: string, show = true) => {
  const elements = document.querySelectorAll<HTMLElement>(classNames);
  Array.prototype.forEach.call(elements, (element: HTMLElement) => {
    if (show) {
      element.classList.remove('display-none');
    } else {
      element.classList.add('display-none');
    }
  });
};

const setupOptimize = () => {
  const variant = window.google_optimize.get('0n_jQyGsR4-IfwB0dHX3Kw');

  toggleFeature('.optimize-original', variant ? !(`${variant}` === '1') : true);
  toggleFeature('.optimize-variant', !!variant && `${variant}` === '1');
};

const waitForOptimize = () => {
  if (window.google_optimize) {
    setupOptimize();
  } else {
    setTimeout(() => waitForOptimize(), 100);
  }
};

waitForOptimize();
