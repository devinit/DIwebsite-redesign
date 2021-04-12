import deepmerge from 'deepmerge';
import React, { FunctionComponent, useEffect, useState } from 'react';
import { filterDashboardData } from '../../dashboard/utils';
import { DashboardChart, DashboardContent, DashboardData, DashboardGrid } from '../../utils/types';
import { ApacheChart } from '../ApacheChart';
import { Card, CardMetaLarge, CardTitleLarge } from '../Card';
import { Grid } from '../Grid';
import { Section } from '../Section';

type DashboardSectionProps = {
  id: string;
  title?: string;
  department?: string;
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
  grids: DashboardGrid[];
};

const DashboardSection: FunctionComponent<DashboardSectionProps> = ({ year, quarter, department, ...props }) => {
  const [data, setData] = useState(props.data);
  useEffect(() => {
    setData(filterDashboardData(props.data, { year, quarter, department }));
  }, [props.data.length]);

  const renderChart = (chart: DashboardChart) => {
    if (chart.data && chart.options) {
      const dataset = chart.data(data);
      const options = deepmerge(chart.options, { dataset: { source: dataset } });

      return <ApacheChart options={options} height={chart.height || '250px'} />;
    }

    return <ApacheChart demo options={{ title: { text: 'THIS IS A DEMO CHART' } }} height="250px" />;
  };

  const renderCard = ({ meta, chart, ...content }: DashboardContent) => {
    const title = content.title && typeof content.title === 'function' ? content.title(data) : content.title;
    if (meta && !title && !chart) {
      return (
        <div key={content.id} className="m-stat__title">
          {meta}
        </div>
      );
    }

    if (content.styled) {
      return (
        <Card key={content.id}>
          {meta ? <CardMetaLarge>{meta}</CardMetaLarge> : null}
          {title ? <CardTitleLarge>{title}</CardTitleLarge> : null}
          {chart ? renderChart(chart) : null}
        </Card>
      );
    }

    return (
      <Card key={content.id} meta={meta} title={title}>
        {chart ? renderChart(chart) : null}
      </Card>
    );
  };

  return (
    <Section title={props.title} id={props.id}>
      {!data.length ? (
        <div>Loading...</div>
      ) : (
        props.grids.map(({ id, columns, content }) => (
          <Grid key={id} columns={columns || 1}>
            {content.map(renderCard)}
          </Grid>
        ))
      )}
    </Section>
  );
};

export { DashboardSection };
