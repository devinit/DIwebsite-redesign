import React, { FunctionComponent, useEffect, useRef } from 'react';
import { makeBasicLineChart, renderBasicColumnChart, renderBasicPieChart, renderChart } from './utils';

type ApacheChartProps = {
  demo?: boolean;
  width?: string;
  height?: string;
  options: echarts.EChartOption;
  type?: 'bar' | 'line' | 'pie';
  data: unknown;
  onClick?: (data: unknown, chartNode: HTMLDivElement, params: unknown) => void; // eslint-disable-line @typescript-eslint/no-explicit-any
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
        renderChart(element.current, props.options).then((chart) => {
          if (props.onClick) {
            chart.on('click', (params: unknown) => {
              props.onClick!(props.data, element.current!, params); // eslint-disable-line @typescript-eslint/no-non-null-assertion
            });
          }
        });
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
