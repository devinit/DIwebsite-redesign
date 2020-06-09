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
        Plotly.plot(el[0], d);
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
