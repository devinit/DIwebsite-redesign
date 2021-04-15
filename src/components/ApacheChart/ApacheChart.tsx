import React, { FunctionComponent, useEffect, useRef } from 'react';
import { EventOptions } from '../../utils/types';
import { makeBasicLineChart, renderBasicColumnChart, renderBasicPieChart, renderChart } from './utils';

type ApacheChartProps = {
  demo?: boolean;
  width?: string;
  height?: string;
  options: echarts.EChartOption;
  type?: 'bar' | 'line' | 'pie';
  data: unknown[];
  onClick?: (options: EventOptions) => void;
  onHover?: (options: EventOptions) => void;
  onBlur?: (options: EventOptions) => void;
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
          /* eslint-disable @typescript-eslint/no-non-null-assertion */
          if (props.onClick) {
            chart.on('click', (params: unknown) => {
              props.onClick!({ data: props.data, chartNode: element.current!, chart, params });
            });
          }
          if (props.onHover) {
            chart.on('mouseover', (params: unknown) => {
              props.onHover!({ data: props.data, chartNode: element.current!, chart, params });
            });
          }
          if (props.onBlur) {
            chart.on('mouseout', (params: unknown) => {
              props.onBlur!({ data: props.data, chartNode: element.current!, chart, params });
            });
          }
          /* eslint-enable @typescript-eslint/no-non-null-assertion */
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
