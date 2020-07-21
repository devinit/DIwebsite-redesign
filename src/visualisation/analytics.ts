const pushEvent: (options: Record<string, unknown>) => void = (window as any).dataLayer.push; // eslint-disable-line @typescript-eslint/no-explicit-any

export const onOptionSelected = (selectedChartOption: string, chartTitle: string, chartLink = ''): void => {
  pushEvent({ event: 'chartSelectorChanged', selectedChartOption, chartTitle, chartLink });
};

export const onChartDownload = (chartTitle: string, chartLink = ''): void => {
  pushEvent({ event: 'chartDownloaded', chartTitle, chartLink });
};
