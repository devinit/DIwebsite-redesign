import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { ApacheChart } from '../ApacheChart';
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
        <Card meta="Proportion of staff time spent on projects">
          <ApacheChart options={{}} height="250px" />
        </Card>
        <Card meta="Proportion of value of staff time spent on direct & indirect overheads">
          <ApacheChart options={{}} height="250px" />
        </Card>
        <Card meta="Personnel costs as a proportion of income (% of target)">
          <ApacheChart options={{}} height="250px" />
        </Card>
        <Card meta="Consultant costs %, YTD (excluding GNR)">
          <ApacheChart options={{}} height="250px" />
        </Card>
      </Grid>
      <Grid columns={1}>
        <Card meta="Testing Bar Chart">
          <ApacheChart options={{}} height="250px" type="bar" />
        </Card>
      </Grid>
    </Section>
  );
};

export { FinanceDashboard };
