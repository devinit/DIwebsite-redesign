export const hideNarrative = (chartNode: HTMLDivElement): void => {
  const parent = chartNode.parentElement;
  if (parent) {
    const narratives = parent.getElementsByClassName('media-caption chart-event-caption');
    Array.prototype.filter.call(narratives, (narrative: HTMLElement) => narrative.remove());
  }
};

export const showNarrative = (chartNode: HTMLDivElement, content: string): void => {
  const parent = chartNode.parentElement;
  if (parent) {
    hideNarrative(chartNode);
    const caption = document.createElement('figcaption');
    caption.classList.add('media-caption', 'chart-event-caption');
    content.split('\n').forEach((note) => {
      const paragraph = document.createElement('p');
      paragraph.innerHTML = note;
      caption.appendChild(paragraph);
    });
    parent.appendChild(caption);
  }
};
