import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { ApacheChart } from '../ApacheChart';
import { Card } from '../Card';
import { Grid } from '../Grid';
import { Section } from '../Section';

type DevelopmentDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const DevelopmentDashboard: FunctionComponent<DevelopmentDashboardProps> = () => {
  return (
    <Section title="Development & Fundraising" id="development">
      <Grid columns={2}>
        <Card meta="Proportion of staff time spent on projects">
          <ApacheChart demo options={{}} height="250px" />
        </Card>
        <Card meta="Proportion of value of staff time spent on direct & indirect overheads">
          <ApacheChart demo options={{}} height="250px" />
        </Card>
        <Card meta="Personnel costs as a proportion of income (% of target)">
          <ApacheChart demo options={{}} height="250px" />
        </Card>
        <Card meta="Consultant costs %, YTD (excluding GNR)">
          <ApacheChart demo options={{}} height="250px" type="pie" />
        </Card>
      </Grid>
      <Grid columns={1}>
        <Card meta="Testing Bar Chart">
          <ApacheChart demo options={{}} height="250px" type="bar" />
        </Card>
      </Grid>
      <Grid columns={3}>
        <Card meta="Testing Pie Charts">
          <ApacheChart demo options={{}} height="250px" type="pie" />
        </Card>
        <Card meta="Testing Pie Charts">
          <ApacheChart demo options={{}} height="250px" type="pie" />
        </Card>
        <Card meta="Testing Pie Charts">
          <ApacheChart demo options={{}} height="250px" type="pie" />
        </Card>
      </Grid>
    </Section>
  );
};

export { DevelopmentDashboard };
