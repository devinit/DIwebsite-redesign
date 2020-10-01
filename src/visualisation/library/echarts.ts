import { EChartOption, ECharts } from 'echarts';
import { DIChart } from './dicharts';
import { DIChartEChartOptions } from './utils';

export class DIEChart extends DIChart {
  private config: DIChartEChartOptions;
  private options: EChartOption = {};
  private sourceData?: { [key: string]: string }[];
  private chart?: ECharts;

  constructor(chartNode: HTMLElement, config: DIChartEChartOptions) {
    super(chartNode);

    this.config = config;
    if (config.options) {
      this.options = config.options;
    }
  }

  getConfig = (): DIChartEChartOptions => {
    return this.config;
  };

  setOptions = (options: EChartOption): DIEChart => {
    this.options = options;

    return this;
  };

  setSourceData(data: { [key: string]: string }[]): DIEChart {
    this.sourceData = data;

    return this;
  }

  getSourceData(): { [key: string]: string }[] | undefined {
    return this.sourceData;
  }

  csv = (url: string): Promise<{ [key: string]: string }[]> => {
    return new Promise((resolve) => {
      window.d3.csv(url, (data) => {
        resolve(data);
      });
    });
  };

  setChart = (chart: ECharts): DIEChart => {
    this.chart = chart;

    return this;
  };

  getChart = (): ECharts => {
    if (!this.chart) {
      this.chart = window.echarts.init(this.chartElement as HTMLDivElement);
    }

    return this.chart;
  };

  updateChart = (): ECharts => {
    if (this.chart) {
      this.chart.setOption(this.options);
    } else {
      this.chart = window.echarts.init(this.chartElement as HTMLDivElement);
      this.chart.setOption(this.options);
      if (this.config.widgets) {
        this.initCustomWidgets(this.config.widgets);
      }
    }
    this.hideLoading();

    return this.chart;
  };
}
