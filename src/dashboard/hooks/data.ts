import { useEffect, useState } from 'react';
import { DashboardData } from '../../utils/types';

export const useDashboardData = (): DashboardData[] => {
  const [data, setData] = useState<DashboardData[]>([]);
  useEffect(() => {
    const dataURL = `${window.location.origin}/api/dashboard/data/`;
    window
      .fetch(dataURL)
      .then((response) => response.json())
      .then(({ data, error }) => {
        if (error) {
          console.log('Failed to fetch data:', error);

          return;
        }
        if (data) {
          setData(data);
        }
      });
  }, []);

  return data;
};
