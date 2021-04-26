import React, { FunctionComponent } from 'react';
import { dataSystems } from '../../dashboard/utils/dashboards/dataSystems';
import { DashboardData } from '../../utils/types';
import { DashboardSection } from '../DashboardSection';

type DataSystemsDashboardProps = {
  year?: number;
  quarter?: 1 | 2 | 3 | 4;
  data: DashboardData[];
};

const DataSystemsDashboard: FunctionComponent<DataSystemsDashboardProps> = ({ data }) => {
  return (
    <DashboardSection
      id="data-systems"
      title="IT"
      department="IT systems and data systems"
      data={data}
      grids={dataSystems}
    />
  );
};

export { DataSystemsDashboard };
