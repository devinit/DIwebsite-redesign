import React, { FunctionComponent } from 'react';
import { DashboardSection } from '../components/DashboardSection';
import { useDashboardData } from './hooks/data';
import {
  comms,
  financeDashboard,
  fundraising,
  hr as humanResourcesDashboard,
  projectManagement,
  dataSystems,
} from './utils/dashboards';

const Dashboard: FunctionComponent = () => {
  const data = useDashboardData();

  return (
    <>
      <DashboardSection id="finance" title="Finance" department="Finance" data={data} grids={financeDashboard} />
      <DashboardSection id="hr" title="Human Resources" department="HR" data={data} grids={humanResourcesDashboard} />
      <DashboardSection
        id="project-management"
        title="Project Management"
        department="Project management"
        data={data}
        grids={projectManagement}
      />
      <DashboardSection
        id="communications"
        title="Communications"
        department="Comms and engagement"
        data={data}
        grids={comms}
      />
      <DashboardSection
        id="development"
        title="Development & Fundraising"
        department="Development and fundraising"
        data={data}
        grids={fundraising}
      />
      <DashboardSection
        id="data-systems"
        title="IT"
        department="IT systems and data systems"
        data={data}
        grids={dataSystems}
      />
    </>
  );
};

export default Dashboard;
