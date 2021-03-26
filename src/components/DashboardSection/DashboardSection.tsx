import deepmerge from 'deepmerge';
import React, { FunctionComponent } from 'react';
import { DashboardChart, DashboardData, DashboardGrid } from '../../utils/types';
import { ApacheChart } from '../ApacheChart';
import { Card } from '../Card';
import { Grid } from '../Grid';
import { Section } from '../Section';

type DashboardSectionProps = {
  id: string;
  title?: string;
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
  grids: DashboardGrid[];
};

const DashboardSection: FunctionComponent<DashboardSectionProps> = ({ data, ...props }) => {
  const renderChart = (chart: DashboardChart) => {
    if (chart.data && chart.options) {
      const dataset = chart.data(data);
      const options = deepmerge(chart.options, { dataset: { source: dataset } });

      return <ApacheChart options={options} height="250px" />;
    }

    return <ApacheChart demo options={{ title: { text: 'THIS IS A DEMO CHART' } }} height="250px" />;
  };

  return (
    <Section title={props.title} id={props.id}>
      {!data.length ? (
        <div>Loading...</div>
      ) : (
        props.grids.map(({ id, columns, content }) => (
          <Grid key={id} columns={columns || 1}>
            {content.map(({ meta, title, chart, ...item }) => (
              <Card key={item.id} meta={meta} title={title && typeof title === 'function' ? title() : title}>
                {chart ? renderChart(chart) : null}
              </Card>
            ))}
          </Grid>
        ))
      )}
    </Section>
  );
};

export { DashboardSection };
