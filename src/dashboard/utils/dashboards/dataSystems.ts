import { getAggregatedDatasetSource } from '..';
import { DashboardData, DashboardGrid } from '../../../utils/types';
import { getEventHandlers, grid } from '../chart';

const colours = ['#FF9A5C', '#FFA770', '#FFB485'];

export const dataSystems: DashboardGrid[] = [
    {
        id: '1',
        columns: 3,
        content: [
            {
                id: 'global-infrastructure',
                meta: 'Roadmap in place for global Infrastructure with capacity for growth (Progress Indicator %)',
                styled: true,
                chart: {
                    data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
                        getAggregatedDatasetSource(data, Array<string>().concat('Roadmap in place for global Infrastructure with capacity for growth')),
                    options: {
                        color: colours,
                        tooltip: {
                            show: true,
                            trigger: 'item',
                            formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                            const { value, seriesName } = params;
            
                            if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                                return `${(value as any)[seriesName]}%`; // eslint-disable-line
                            }
            
                            return 'No Data';
                            },
                        },
                        legend: { show: false },
                        dataset: { dimensions: ['year'].concat('Roadmap in place for global Infrastructure with capacity for growth') },
                        grid,
                        toolbox: { feature: { saveAsImage: {} } },
                        xAxis: { type: 'category' },
                        yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
                        series: [{ type: 'bar' }],
                    },
                    ...getEventHandlers('Roadmap in place for global Infrastructure with capacity for growth'),
                },
            },
            {
                id: 'hosted-systems',
                meta: 'Fully hosted systems with reduced internal reliance (Progress Indicator %)',
                styled: true,
                chart: {
                  data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
                    getAggregatedDatasetSource(data, Array<string>().concat('Fully hosted systems with reduced internal reliance')),
                  options: {
                    color: colours,
                    tooltip: {
                      show: true,
                      trigger: 'item',
                      formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                        const { value, seriesName } = params;
        
                        if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                          return `${(value as any)[seriesName]}`; // eslint-disable-line
                        }
        
                        return 'No Data';
                      },
                    },
                    legend: { show: false },
                    dataset: { dimensions: ['year'].concat('Fully hosted systems with reduced internal reliance') },
                    grid,
                    toolbox: { feature: { saveAsImage: {} } },
                    xAxis: { type: 'category' },
                    yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
                    series: [{ type: 'bar' }],
                  },
                  ...getEventHandlers('Fully hosted systems with reduced internal reliance'),
                },
            },
            {
                id: 'global-support',
                meta: 'Standardised global support (Progress Indicator %)',
                styled: true,
                chart: {
                  data: (data: DashboardData[]): Record<string, React.ReactText>[] =>
                    getAggregatedDatasetSource(data, Array<string>().concat('Standardised global support')),
                  options: {
                    color: colours,
                    tooltip: {
                      show: true,
                      trigger: 'item',
                      formatter: (params: echarts.EChartOption.Tooltip.Format): string => {
                        const { value, seriesName } = params;
        
                        if (value && seriesName && (value as any)[seriesName]) { // eslint-disable-line
                          return `${(value as any)[seriesName]}`; // eslint-disable-line
                        }
        
                        return 'No Data';
                      },
                    },
                    legend: { show: false },
                    dataset: { dimensions: ['year'].concat('Standardised global support') },
                    grid,
                    toolbox: { feature: { saveAsImage: {} } },
                    xAxis: { type: 'category' },
                    yAxis: { type: 'value', show: true, splitNumber: 3, axisLabel: { formatter: '{value}%' } },
                    series: [{ type: 'bar' }],
                  },
                  ...getEventHandlers('Standardised global support'),
                },
            },
        ],
    },
];

