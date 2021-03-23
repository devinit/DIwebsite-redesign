import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section';

type DevelopmentDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const DevelopmentDashboard: FunctionComponent<DevelopmentDashboardProps> = () => {
  return (
    <Section title="Development & Fundraising" id="development">
      <div>Content Goes Here</div>
    </Section>
  );
};

export { DevelopmentDashboard };
