import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Card } from '../Card';
import { Grid } from '../Grid';
import { Section } from '../Section';

type FinanceDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const FinanceDashboard: FunctionComponent<FinanceDashboardProps> = () => {
  return (
    <Section title="Finance" id="finance">
      <Grid columns={2}>
        <Card meta="Proportion of staff time spent on projects">Content Goes Here</Card>
        <Card meta="Proportion of value of staff time spent on direct & indirect overheads">Content Goes Here</Card>
        <Card meta="Personnel costs as a proportion of income (% of target)">Chart Goes Here</Card>
        <Card meta="Consultant costs %, YTD (excluding GNR)">Chart Goes Here</Card>
      </Grid>
    </Section>
  );
};

export { FinanceDashboard };
