import React, { FunctionComponent, useState } from 'react';
import { ApacheChart } from '../components/ApacheChart';
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
  const data = useDashboardData();
  const [year, setYear] = useState<string>();
  const [quarter, setQuarter] = useState<string>();

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
        <Grid columns={4}>
          <Card>
            <CardMetaLarge>Contract Income Secured</CardMetaLarge>
            <CardTitleLarge>£75,000</CardTitleLarge>
          </Card>
          <Card>
            <CardMetaLarge>Grant Income Secured</CardMetaLarge>
            <CardTitleLarge>£185,000</CardTitleLarge>
          </Card>
          <Card>
            <CardMetaLarge>Salary Vs Income</CardMetaLarge>
            <CardTitleLarge>85%</CardTitleLarge>
          </Card>
          <Card>
            <CardMetaLarge>Staff Vs Leavers</CardMetaLarge>
            <CardTitleLarge>84/3</CardTitleLarge>
          </Card>
        </Grid>
        <Grid columns={1}>
          <Card>
            <ApacheChart options={{}} />
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
