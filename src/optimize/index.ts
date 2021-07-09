window.addEventListener('load', () => {
  const setupOptimize = () => {
    if (window.google_optimize) {
      const variant = window.google_optimize.get('_aj7TeknQICK1m3pwQRBKw');
      const params = new URLSearchParams(window.location.search);
      const { origin, pathname } = window.location;
      if (variant && variant === '1' && variant !== params.get('variant')) {
        window.location.href = `${origin}${pathname}?variant=1`;
      }
      if (variant && variant === '0' && params.get('variant') === '1') {
        window.location.href = `${origin}${pathname}`;
      }
      if (!!params.get('variant')) {
        window.location.href = `${origin}${pathname}`;
      }
    } else {
      console.log('Google Optimize may not be active');
    }
  };

  setupOptimize();
});
