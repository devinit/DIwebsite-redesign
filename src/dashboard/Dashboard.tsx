import * as echarts from 'echarts';
import React, { FunctionComponent, useEffect, useRef } from 'react';
import { Card } from '../components/Card';
import { Grid } from '../components/Grid';

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
  chart.setOption(option);
};

const Dashboard: FunctionComponent = () => {
  const element = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (element.current) {
      makeBasicChart(element.current);
    }
  }, []);

  return (
    <>
      <Grid>
        <Card meta="Salary" title="$75,0000"></Card>
        <Card></Card>
        <Card></Card>
      </Grid>
      <Grid columns={1}>
        <Card>
          <div ref={element} style={{ height: '300px' }}></div>
        </Card>
      </Grid>
    </>
  );
};

export { Dashboard };
