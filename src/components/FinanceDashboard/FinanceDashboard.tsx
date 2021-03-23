import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section';

type FinanceDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const FinanceDashboard: FunctionComponent<FinanceDashboardProps> = () => {
  return (
    <Section title="Finance">
      <div>Content Goes Here</div>
    </Section>
  );
};

export { FinanceDashboard };
