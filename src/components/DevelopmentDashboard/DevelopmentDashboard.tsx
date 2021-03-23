import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section/Section';

type DevelopmentDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const DevelopmentDashboard: FunctionComponent<DevelopmentDashboardProps> = () => {
  return (
    <Section title="Development & Fundraising">
      <div>Content Goes Here</div>
    </Section>
  );
};

export { DevelopmentDashboard };
