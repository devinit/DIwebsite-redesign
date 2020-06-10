import $ from 'jquery';
import * as d3 from "d3";
import barChartVertical from './barChartVertical';
import barChartStackedVertical from './barChartStackedVertical';
import lineChartHorizontal from './lineChartHorizontal';
import lineChartVertical from './lineChartVertical';
import lineChartMultipleVertical from './lineChartMultipleVertical';
import lineChartStackedArea from './lineChartStackedArea';
import {createElement, dateParser, yearParser} from './utils';

export default function entry() {
    initChart('#bar-chart-vertical', barChartVertical);
    initChart('#bar-chart-stacked-vertical', barChartStackedVertical);
    initChart('#line-chart-vertical', lineChartVertical, dateParser);
    initChart('#line-chart-multiple-vertical', lineChartMultipleVertical, yearParser, {
        xAxis: d3.scaleTime,
        yAxisFormat: d => d + '%',
        yAxisLabel: '% changes in ODA loans since 2012'
    });
    initChart('#line-chart-stacked-area', lineChartStackedArea, yearParser, {
        xAxis: d3.scaleTime,
        yAxisLabel: 'US$ billions'
    });

    const el = $('#tester');
    d3.json(el.first().data('url')).then(d => {
        const plot = Plotly.newPlot('tester', d).then(p => {

            Plotly.relayout('tester', {
                updatemenus: [{
                    y: 0.8,
                    yanchor: 'top',
                    buttons: [{
                        method: 'restyle',
                        args: ['line.color', 'red'],
                        label: 'red'
                    }, {
                        method: 'restyle',
                        args: ['line.color', 'blue'],
                        label: 'blue'
                    }, {
                        method: 'restyle',
                        args: ['line.color', 'green'],
                        label: 'green'
                    }]
                }]
            });

        });

        // function makeTrace(i) {
        //     return {
        //         y: Array.apply(null, Array(10)).map(() => Math.random()),
        //         line: {
        //             shape: 'spline' ,
        //             color: 'red'
        //         },
        //         visible: i === 0,
        //         name: 'Data set ' + i,
        //     };
        // }

        // Plotly.newPlot('tester', [0, 1, 2, 3].map(makeTrace), {
        //     updatemenus: [{
        //         y: 0.8,
        //         yanchor: 'top',
        //         buttons: [{
        //             method: 'restyle',
        //             args: ['line.color', 'red'],
        //             label: 'red'
        //         }, {
        //             method: 'restyle',
        //             args: ['line.color', 'blue'],
        //             label: 'blue'
        //         }, {
        //             method: 'restyle',
        //             args: ['line.color', 'green'],
        //             label: 'green'
        //         }]
        //     }, {
        //         y: 1,
        //         yanchor: 'top',
        //         buttons: [{
        //             method: 'restyle',
        //             args: ['visible', [true, false, false, false]],
        //             label: 'Data set 0'
        //         }, {
        //             method: 'restyle',
        //             args: ['visible', [false, true, false, false]],
        //             label: 'Data set 1'
        //         }, {
        //             method: 'restyle',
        //             args: ['visible', [false, false, true, false]],
        //             label: 'Data set 2'
        //         }, {
        //             method: 'restyle',
        //             args: ['visible', [false, false, false, true]],
        //             label: 'Data set 3'
        //         }]
        //     }],
        // });

    }).catch(error => {
        console.log(error);
    });
    // https://api.plot.ly/v2
    // https://api.plot.ly/v2/plots#detail
}

const initChart = (selector, chart, accessor, {
    xAxis = d3.scaleLinear,     // use d3.scaleTime if date/year
    xAxisKey = 'year',          // key of the x axis data
    xAxisFormat = null,         // use d => d + '%' if precentage
    xAxisLabel = null,
    yAxis = d3.scaleLinear,     // use d3.scaleTime if date/year
    yAxisKey = 'value',         // key of the y axis data
    yAxisFormat = null,         // use d => d + '%' if precentage
    yAxisLabel = null,
} = {}) => {
    const config = { xAxis, xAxisKey, xAxisFormat, xAxisLabel, yAxis, yAxisKey, yAxisFormat, yAxisLabel};
    const el = $(selector).first();

    // load the data and create chart
    d3.csv(el.data('url'), accessor).then(d => {
        chart(selector, d, config);
    }).catch(error => {
        console.log(error);
    });
}
