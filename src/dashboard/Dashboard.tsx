import React, { FunctionComponent, useState } from 'react';
import { Card, CardMetaLarge, CardTitleLarge } from '../components/Card';
import { DashboardSection } from '../components/DashboardSection';
import { DataSystemsDashboard } from '../components/DataSystemsDashboard';
import { Filter, Option } from '../components/Filter';
import { Grid } from '../components/Grid';
import { Section } from '../components/Section';
import { useDashboardData } from './hooks/data';
import {
  comms,
  financeDashboard,
  fundraising,
  hr as humanResourcesDashboard,
  projectManagement,
} from './utils/dashboards';

const years: Option[] = [
  { value: 2020, caption: '2020' },
  { value: 2021, caption: '2021' },
];

const quarters: Option[] = [
  { value: '1', caption: 'Q1' },
  { value: '2', caption: 'Q2' },
  { value: '3', caption: 'Q3' },
  { value: '4', caption: 'Q4' },
];

const Dashboard: FunctionComponent = () => {
  const data = useDashboardData();
  const [year, setYear] = useState<number>(2020);
  const [quarter, setQuarter] = useState<string>();

  const onSelectYear = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setYear(parseInt(event.currentTarget.value));
  };

  const onSelectQuarter = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setQuarter(event.currentTarget.value);
  };
  console.log(quarter);

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
      <Section id="summary">
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
      </Section>
      <DashboardSection
        id="finance"
        title="Finance"
        department="Finance"
        data={data}
        grids={financeDashboard}
        year={year}
      />
      <DashboardSection
        id="hr"
        title="Human Resources"
        department="HR"
        data={data}
        grids={humanResourcesDashboard}
        year={year}
      />
      <DashboardSection
        id="project-management"
        title="Project Management"
        department="Project management"
        data={data}
        grids={projectManagement}
        year={year}
        quarter={4}
      />
      <DashboardSection
        id="communications"
        title="Communications"
        department="Comms and engagement"
        data={data}
        grids={comms}
        year={year}
        quarter={4}
      />
      <DashboardSection
        id="development"
        title="Development & Fundraising"
        department="Development and fundraising"
        data={data}
        grids={fundraising}
        year={year}
      />
      <DataSystemsDashboard data={data} />
    </>
  );
};

export { Dashboard };
