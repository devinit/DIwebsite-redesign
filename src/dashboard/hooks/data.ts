import { useEffect, useState } from 'react';
import { DashboardData } from '../../utils/types';
import * as Papa from 'papaparse';

export const useDashboardData = (): DashboardData[] => {
  const [data, setData] = useState<DashboardData[]>([]);
  useEffect(() => {
    const dataURL =
      'https://raw.githubusercontent.com/devinit/DIwebsite-redesign/patch/advanced-chart-resources/data/organisation_dashboard.csv';
    Papa.parse(dataURL, {
      download: true,
      complete: ({ data }) => {
        const dashboardData = [...data];
        if (dashboardData && dashboardData.length) {
          const titleRow = dashboardData.splice(0, 1)[0] as string[];

          setData(
            dashboardData.map<DashboardData>((row: string[]) => {
              return {
                metric: row[titleRow.indexOf('Indicator')],
                date: row[titleRow.indexOf('Date')],
                value: parseFloat(row[titleRow.indexOf('Value')]),
                department: row[titleRow.indexOf('Department')],
                narrative: row[titleRow.indexOf('Narrative')],
              };
            }),
          );
        }
      },
    });
  }, []);

  return data;
};
