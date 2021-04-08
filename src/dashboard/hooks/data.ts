import * as localforage from 'localforage';
import { useEffect, useState } from 'react';
import { DashboardData } from '../../utils/types';

export const useDashboardData = (): DashboardData[] => {
  const [data, setData] = useState<DashboardData[]>([]);
  useEffect(() => {
    localforage.getItem('dashboard.updatedAt').then((value: string | null) => {
      const updatedAt = value && new Date(value);
      if (updatedAt) {
        updatedAt.setHours(updatedAt.getHours() + 1);
      }
      if ((updatedAt && Date.now() - updatedAt.getTime() > 60 * 60) || !updatedAt) {
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
              localforage.setItem('dashboard.data', data);
              localforage.setItem('dashboard.updatedAt', new Date());
            }
          });
      } else {
        localforage.getItem('dashboard.data').then((data: DashboardData[]) => {
          setData(data);
        });
      }
    });
  }, []);

  return data;
};
