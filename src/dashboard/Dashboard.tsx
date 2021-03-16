import * as Plottable from 'plottable';
import 'plottable/plottable.css';
import React, { FunctionComponent, useEffect, useRef } from 'react';
import { Card } from './components/Card';
import { Grid } from './components/Grid';

const makeBasicChart = (node: HTMLDivElement) => {
  // const Plottable = await import('plottable');
  const xScale = new Plottable.Scales.Linear();
  const yScale = new Plottable.Scales.Linear();

  const xAxis = new Plottable.Axes.Numeric(xScale, 'bottom');
  const yAxis = new Plottable.Axes.Numeric(yScale, 'left');

  const plot = new Plottable.Plots.Line();
  plot.x((d: { x: number; y: number }) => d.x, xScale);
  plot.y((d) => d.y, yScale);
  const data = [
    { x: 0, y: 1 },
    { x: 1, y: 2 },
    { x: 2, y: 4 },
    { x: 3, y: 8 },
  ];

  const dataset = new Plottable.Dataset(data);
  plot.addDataset(dataset);

  const chart = new Plottable.Components.Table([
    [yAxis, plot],
    [null, xAxis],
  ]);

  chart.renderTo(node);
};

const Dashboard: FunctionComponent = () => {
  const element = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (element.current) {
      makeBasicChart(element.current);
    }
  }, []);

  return (
    <Grid>
      <Card></Card>
      <Card></Card>
      <Card></Card>
      <div ref={element} style={{ height: '300px' }}></div>
    </Grid>
  );
};

export { Dashboard };
