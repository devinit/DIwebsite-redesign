export const initFilters = function (): void {
  const filters = document.querySelectorAll('.js-filter');

  Array.prototype.forEach.call(filters, (filter: HTMLDivElement) => {
    const selector = filter.querySelector('.js-filter--selector');
    const items = filter.querySelectorAll('.js-filter--item');
    if (selector) {
      selector.addEventListener('change', (event: Event) => {
        const value = (event.target as HTMLSelectElement).value;
        let visibleCount = 0;
        Array.prototype.forEach.call(items, (item: HTMLDivElement) => {
          if (visibleCount < 9 && (!value || item.classList.contains(value))) {
            item.classList.remove('hidden');
            visibleCount = visibleCount + 1;
          } else {
            item.classList.add('hidden');
          }
        });
      });
    }
  });
};
