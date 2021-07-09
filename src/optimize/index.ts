const toggleFeature = (classNames: string, show = true) => {
  const elements = document.querySelectorAll<HTMLElement>(classNames);
  Array.prototype.forEach.call(elements, (element: HTMLElement) => {
    if (show) {
      element.classList.remove('display-none');
    } else {
      element.classList.add('display-none');
    }
  })
}

const setupOptimize = () => {
  const variant = window.google_optimize.get('_aj7TeknQICK1m3pwQRBKw');
  console.log(variant);

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
