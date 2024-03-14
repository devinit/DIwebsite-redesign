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
  const button = document.querySelector('.footnotes button') as HTMLElement;
  const footnotes = document.querySelectorAll('a[id^="note-source"]');
  footnotes.forEach((footnote) => {
    const footnoteChild = footnote.firstChild as HTMLElement;
    footnote.addEventListener('click', function (event) {
      event.preventDefault();
      const footnoteText: RegExpMatchArray = (footnoteChild.innerHTML as string)?.match(/\d+/) as RegExpMatchArray;
      const footnoteNumber = parseInt(footnoteText[0]);
      if (button && footnoteNumber > 5) {
        button.click();
        document.querySelector(footnote.getAttribute('href') as string)?.scrollIntoView();
      } else {
        document.querySelector(footnote.getAttribute('href') as string)?.scrollIntoView();
      }
    });
  });
  if (button) {
    button.addEventListener('click', (event: Event) => {
      event.preventDefault();
      const showMore = button.innerHTML.toLowerCase() === 'show more';
      toggleFootnoteVisibility(showMore);
      button.innerHTML = showMore ? 'show less' : 'show more';
    });
  }
};
