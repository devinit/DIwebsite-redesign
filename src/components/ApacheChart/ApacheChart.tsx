import React, { FunctionComponent, useEffect, useRef } from 'react';
import { makeBasicLineChart, renderBasicColumnChart, renderBasicPieChart, renderChart } from './utils';

type ApacheChartProps = {
  demo?: boolean;
  width?: string;
  height?: string;
  options: echarts.EChartOption;
  type?: 'bar' | 'line' | 'pie';
};

const ApacheChart: FunctionComponent<ApacheChartProps> = (props) => {
  const element = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (element.current) {
      if (props.demo) {
        switch (props.type) {
          case 'line':
            makeBasicLineChart(element.current);
            break;
          case 'bar':
            renderBasicColumnChart(element.current);
            break;
          case 'pie':
            renderBasicPieChart(element.current);
            break;
          default:
            break;
        }
      } else {
        renderChart(element.current, props.options);
      }
    }
  }, []);

  return <div ref={element} style={{ height: props.height }}></div>;
};

ApacheChart.defaultProps = {
  height: '300px',
  type: 'line',
};

export { ApacheChart };
