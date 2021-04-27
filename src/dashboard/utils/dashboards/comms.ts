import { getAggregatedDatasetSource } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';
import { getBarLabelConfig, getEventHandlers, grid, tootipFormatter } from '../chart';

const colours = ['#65093d', '#7e1850', '#9f1459', '#d12568', '#f3a5b6'];
const dashboardMetrics = [
  'Bounce rate on the website (%)',
  'Dwell time on the website (minutes)',
  'Overall site SEO score',
  'Twitter engagement rate',
  'Linkedin engagement rate',
  'Proportion of new linkedin followers from target stakeholder groups',
];

export const comms: DashboardGrid[] = [
  {
    id: '1',
    columns: 3,
    content: [
      {
        id: 'bounce-rate',
        meta: dashboardMetrics[0],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[0])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ suffix: '%' }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[0]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar', label: getBarLabelConfig({ suffix: '%' }) }],
          },
          ...getEventHandlers(dashboardMetrics[0]),
        },
      },
      {
        id: 'dwell-time',
        meta: dashboardMetrics[1],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[1])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({}) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[1]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}' } },
            series: [{ type: 'bar', label: getBarLabelConfig({}) }],
          },
          ...getEventHandlers(dashboardMetrics[1]),
        },
      },
      {
        id: 'seo-score',
        meta: dashboardMetrics[2],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[2])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({}) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[2]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}' } },
            series: [{ type: 'bar', label: getBarLabelConfig({}) }],
          },
          ...getEventHandlers(dashboardMetrics[2]),
        },
      },
      {
        id: 'twitter-engagement',
        meta: dashboardMetrics[3],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[3])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ suffix: '%' }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[3]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar', label: getBarLabelConfig({ suffix: '%' }) }],
          },
          ...getEventHandlers(dashboardMetrics[3]),
        },
      },
      {
        id: 'linkedin-engagement',
        meta: dashboardMetrics[4],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[4])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ suffix: '%' }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[4]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar', label: getBarLabelConfig({ suffix: '%' }) }],
          },
          ...getEventHandlers(dashboardMetrics[4]),
        },
      },
    ],
  },
  {
    id: '2',
    columns: 1,
    className: 'm-pills',
    content: [
      {
        id: 'linkedin-followers',
        meta: dashboardMetrics[5],
        styled: true,
        chart: {
          data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
            getAggregatedDatasetSource(data, Array<string>().concat(dashboardMetrics[5])),
          options: {
            color: colours,
            tooltip: { show: true, trigger: 'item', formatter: tootipFormatter({ suffix: '%' }) },
            legend: { show: false },
            dataset: { dimensions: ['year'].concat(dashboardMetrics[5]) },
            grid,
            toolbox: { feature: { saveAsImage: {} } },
            xAxis: { type: 'category' },
            yAxis: { type: 'value', show: false, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
            series: [{ type: 'bar', label: getBarLabelConfig({ suffix: '%' }) }],
          },
          ...getEventHandlers(dashboardMetrics[5]),
        },
      },
    ],
  },
];
