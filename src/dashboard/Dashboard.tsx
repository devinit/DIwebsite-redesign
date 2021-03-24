import * as echarts from 'echarts';
import React, { FunctionComponent, useEffect, useRef, useState } from 'react';
import { Card, CardMetaLarge, CardTitleLarge } from '../components/Card';
import { CommsEngagementDashboard } from '../components/CommsEngagementDashboard';
import { DataSystemsDashboard } from '../components/DataSystemsDashboard';
import { DevelopmentDashboard } from '../components/DevelopmentDashboard';
import { Filter, Option } from '../components/Filter';
import { FinanceDashboard } from '../components/FinanceDashboard';
import { Grid } from '../components/Grid';
import { HumanResourcesDashboard } from '../components/HumanResourcesDashboard';
import { ProjectManagementDashboard } from '../components/ProjectManagementDashboard';
import { Section } from '../components/Section';
import { useDashboardData } from './hooks/data';

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

const years: Option[] = [
  { value: '2020', caption: '2020' },
  { value: '2021', caption: '2021' },
];

const quarters: Option[] = [
  { value: '1', caption: 'Q1' },
  { value: '2', caption: 'Q2' },
  { value: '3', caption: 'Q3' },
  { value: '4', caption: 'Q4' },
];

const Dashboard: FunctionComponent = () => {
  const element = useRef<HTMLDivElement>(null);
  const data = useDashboardData();
  const [year, setYear] = useState<string>();
  const [quarter, setQuarter] = useState<string>();

  useEffect(() => {
    if (element.current) {
      makeBasicChart(element.current);
    }
  }, []);

  const onSelectYear = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setYear(event.currentTarget.value);
  };

  const onSelectQuarter = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setQuarter(event.currentTarget.value);
  };
  console.log(year, quarter);

  return (
    <>
      <Section>
        <div className="highlight">
          <form className="form">
            <Filter id="year" label="Year" options={years} onChange={onSelectYear} />
            <Filter id="quarter" label="Quarter" options={quarters} onChange={onSelectQuarter} />
          </form>
        </div>
      </Section>
      <Section id="general">
        <Grid>
          <Card>
            <CardMetaLarge>Income Secured</CardMetaLarge>
            <CardTitleLarge>$75,000</CardTitleLarge>
          </Card>
          <Card></Card>
          <Card></Card>
        </Grid>
        <Grid columns={1}>
          <Card>
            <div ref={element} style={{ height: '300px' }}></div>
          </Card>
        </Grid>
      </Section>
      <FinanceDashboard data={data} />
      <DevelopmentDashboard data={data} />
      <DataSystemsDashboard data={data} />
      <HumanResourcesDashboard data={data} />
      <ProjectManagementDashboard data={data} />
      <CommsEngagementDashboard data={data} />
    </>
  );
};

export { Dashboard };
