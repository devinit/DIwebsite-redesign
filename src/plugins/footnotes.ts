const toggleFootnoteVisibility = (show: boolean): void => {
  const footnotes = document.querySelectorAll('.footnotes .footnotes__list.extra');

  Array.prototype.forEach.call(footnotes, (footnote: HTMLUListElement) => {
    if (show) {
      footnote.classList.remove('hidden');
    } else {
      footnote.classList.add('hidden');
    }
  });
};

export const handleFootnotes = function (): void {
  const button = document.querySelector('.footnotes button');
  if (button) {
    button.addEventListener('click', (event: Event) => {
      event.preventDefault();
      const showMore = button.innerHTML.toLowerCase() === 'show more';
      toggleFootnoteVisibility(showMore);
      button.innerHTML = showMore ? 'show less' : 'show more';
    });
  }
};
