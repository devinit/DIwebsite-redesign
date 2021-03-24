import deepmerge from 'deepmerge';
import * as echarts from 'echarts';
import React, { FunctionComponent, useEffect, useRef } from 'react';
import { defaultOptions } from '../../utils/echarts';

type ApacheChartProps = {
  width?: string;
  height?: string;
  options: echarts.EChartOption;
};

const makeBasicChart = (node: HTMLDivElement) => {
  const chart = echarts.init(node);
  const option: echarts.EChartOption = {
    xAxis: {
      type: 'category',
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        data: [150, 230, 224, 218, 135, 147, 260],
        type: 'line',
      },
    ],
  };
  chart.setOption(deepmerge(defaultOptions, option));
};

const ApacheChart: FunctionComponent<ApacheChartProps> = (props) => {
  const element = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (element.current) {
      makeBasicChart(element.current);
    }
  }, []);

  return <div ref={element} style={{ height: props.height }}></div>;
};

ApacheChart.defaultProps = {
  height: '300px',
};

export { ApacheChart };
