import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section';

type CommsEngagementDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const CommsEngagementDashboard: FunctionComponent<CommsEngagementDashboardProps> = () => {
  return (
    <Section title="Comms & Engagement">
      <div>Content Goes Here</div>
    </Section>
  );
};

export { CommsEngagementDashboard };
