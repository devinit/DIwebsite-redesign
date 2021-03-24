import React, { FunctionComponent, useEffect, useRef } from 'react';
import { makeBasicLineChart } from './utils';

type ApacheChartProps = {
  width?: string;
  height?: string;
  options: echarts.EChartOption;
  type?: 'bar' | 'line' | 'pie';
};

const ApacheChart: FunctionComponent<ApacheChartProps> = (props) => {
  const element = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (element.current) {
      if (props.type === 'line') {
        makeBasicLineChart(element.current);
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
