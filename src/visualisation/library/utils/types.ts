interface Loading {
  show: () => void;
  hide: () => void;
}

export interface DIChartsInstance {
  loading: Loading;
  chartElement: HTMLElement;
  parentElement: HTMLElement | null;
}

export interface FilterOptions {
  labelPrefix?: string;
  labelSuffix?: string;
}
