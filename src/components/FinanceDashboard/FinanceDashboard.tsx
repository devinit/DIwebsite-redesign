import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section/Section';

type FinanceDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const FinanceDashboard: FunctionComponent<FinanceDashboardProps> = () => {
  return <Section title="Finance Dashboard">Content Goes Here</Section>;
};

export { FinanceDashboard };
