import deepmerge from 'deepmerge';
import React, { FunctionComponent, useEffect, useState } from 'react';
import { filterDashboardData } from '../../dashboard/utils';
import { DashboardChart, DashboardContent, DashboardData, DashboardGrid, Quarter } from '../../utils/types';
import { ApacheChart } from '../ApacheChart';
import { Card, CardMetaLarge, CardTitleLarge } from '../Card';
import { Grid } from '../Grid';
import { HiddenMediaCaption } from '../HiddenMediaCaption';
import { Section } from '../Section';

type DashboardSectionProps = {
  id: string;
  title?: string;
  department?: string;
  year?: number;
  quarter?: Quarter;
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

      return (
        <ApacheChart
          options={options}
          height={chart.height || '250px'}
          data={data}
          onClick={chart.onClick}
          onHover={chart.onHover}
          onBlur={chart.onBlur}
        />
      );
    }

    return (
      <ApacheChart
        demo
        options={{ title: { text: 'THIS IS A DEMO CHART' } }}
        height="250px"
        data={data}
        onClick={chart.onClick}
        onHover={chart.onHover}
        onBlur={chart.onBlur}
      />
    );
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
    const info = content.info && typeof content.info === 'function' ? content.info(data) : content.info;

    if (content.styled) {
      return (
        <Card key={content.id}>
          {meta ? <CardMetaLarge>{meta}</CardMetaLarge> : null}
          {title ? <CardTitleLarge>{title}</CardTitleLarge> : null}
          {chart ? renderChart(chart) : null}
          {info ? (
            <HiddenMediaCaption buttonCaption="Narrative">
              {info.split('\n').map((i, key) => (
                <p key={`${key}`}>{i}</p>
              ))}
            </HiddenMediaCaption>
          ) : null}
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
        props.grids.map(({ id, columns, content, className }) => (
          <Grid key={id} columns={columns || 1} className={className}>
            {content.map(renderCard)}
          </Grid>
        ))
      )}
    </Section>
  );
};

export { DashboardSection };
