import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section';

type DataSystemsDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const DataSystemsDashboard: FunctionComponent<DataSystemsDashboardProps> = () => {
  return (
    <Section title="IT & Data Systems">
      <div>Content Goes Here</div>
    </Section>
  );
};

export { DataSystemsDashboard };
