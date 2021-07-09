declare const google_optimize: { get: (id: string) => string };

window.addEventListener('load', () => {
  const setupOptimize = () => {
    if (google_optimize) {
      const variant = google_optimize.get('_aj7TeknQICK1m3pwQRBKw');
      const params = new URLSearchParams(window.location.search);
      const { origin, pathname } = window.location;
      if (variant && variant === '1' && variant !== params.get('variant')) {
        window.location.href = `${origin}${pathname}?variant=1`;
      }
      if (variant && variant === '0' && params.get('variant') === '1') {
        window.location.href = `${origin}${pathname}`;
      }
    }
  };

  setupOptimize();
});
