import { addChartReverseListener } from '.';
import { generateObjectDataset } from '..';
import { DashboardChartEvents, DashboardData, EventOptions } from '../../../utils/types';

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

/**
 * Common handling of events on bar/line charts - click to drilldown & hover to show tooltips
 * @param metrics - Indicators for a particular chart
 * @returns Object with event handlers - onClick, onHover, onBlur
 */
export const getEventHandlers = (metrics: string | string[]): DashboardChartEvents => {
  return {
    onClick: ({ data, chart, params }: EventOptions): void => {
      if (!params.data) return;
      const { year: y } = params.data;
      const source = generateObjectDataset(
        (data as DashboardData[]).filter(({ metric, year }) => metrics.includes(metric) && y === year),
      );
      addChartReverseListener(chart);

      chart.setOption({ dataset: { source, dimensions: ['quarter'].concat(metrics) } });
    },
    onHover: ({ chart, params }: EventOptions): void => {
      if (!params.data) return;
      const metric = params.seriesName;
      const narrative = params.data[`${metric} - narrative`];

      if (narrative) {
        showNarrative(chart.getDom() as HTMLDivElement, narrative);
      }
    },
    onBlur: ({ chart }: EventOptions): void => hideNarrative(chart.getDom() as HTMLDivElement),
  };
};
