import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section';

type HumanResourcesDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const HumanResourcesDashboard: FunctionComponent<HumanResourcesDashboardProps> = () => {
  return (
    <Section title="Human Resources" id="hr">
      <div>Content Goes Here</div>
    </Section>
  );
};

export { HumanResourcesDashboard };
