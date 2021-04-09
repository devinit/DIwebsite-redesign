import React, { ReactElement } from 'react';
import { Section } from '../components/Section';

const Dashboard = React.lazy(() => import('./Dashboard'));
export const AsyncDashboard = (): ReactElement => (
  <React.Suspense fallback={<Section title="Loading" />}>
    <Dashboard />
  </React.Suspense>
);
