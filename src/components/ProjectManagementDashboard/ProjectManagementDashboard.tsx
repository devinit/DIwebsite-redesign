import React, { FunctionComponent } from 'react';
import { DashboardData } from '../../utils/types';
import { Section } from '../Section';

type ProjectManagementDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const ProjectManagementDashboard: FunctionComponent<ProjectManagementDashboardProps> = () => {
  return (
    <Section title="Project Management">
      <div>Content Goes Here</div>
    </Section>
  );
};

export { ProjectManagementDashboard };
