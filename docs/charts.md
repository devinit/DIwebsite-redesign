# DI Charts
A library for creating interactive visualisations in a flexible way, abstracting common charting libraries like Plotly & D3

## Usage

The library can be accessed as a global `window.DICharts`

Since you may likely be dealing with multiple chart instances per page, the library works with CSS classes instead of IDs.

To add a new chart:

        window.DICharts.addChart({
            className: 'my-chart-element-class',
            plotly: {}, // optional: use to initialise a Plotly chart
            d3: {}, // optional: use to initialise a d3 chart
        })


## Plotly

        window.DICharts.addChart({
            className: 'my-chart-element-class',
            plotly: { // optional: use to initialise a Plotly chart
                layout: {}, // optional: Plotly layout options https://plotly.com/javascript/reference/layout/
                config: {}, // optional: Plotly config options https://plotly.com/javascript/configuration-options/
                data: [{}], // optional: Plotly data options for creating chart series - when provided, has precedences for rendering a chart
                csv: { // optional: abstracted fetching of CSV data
                    url: '', // URL for the CSV
                    onFetch: function(sourceData, config, manager) {} // callback to handle returned CSV. Also returns a manager instance of the DIPlotlyChart class which has several utils for handling Plotly charts
                },
                onClick: function(data, manager) {} // called when a data point is clicked,
                widgets: {
                    filters: [
                        {
                            className: '', // CSS class of the select element for this filter
                            multi: false, // if true, this filter will allow selection of multiple values
                            options: ['Option 1'], // optional: if provided, has a higher precendence for rendering filter options
                            getOptions: function(manager) {}, // optional: use for dynamic options i.e fetch the options within the fuction and return them
                            onChange: function(event, manager) {} // called when the option is changed
                        },
                        {} // add more filters
                    ],
                    legend: {
                        onClick: function(data, manager) {} // called when the legend is clicked
                    }
                }
            }
        });


## D3


        window.DICharts.addChart({
            className: 'my-chart-element-class',
            d3: { // optional: use to initialise a D3 chart
                onAdd: function(chartNodes) { // all the d3 actions happens here
                    Array.prototype.forEach.call(chartNodes, (chartNode) => { // iterate through the returned nodelist
                        const dichart = new window.DICharts.Chart(chartNode); // initialise a DICharts instance to gain access to the available utils
                        // do custom d3 coding here
                    });
                }
            }
        });


## Manager API

### DICharts.Chart()

**Init**

        const manager = new DICharts.Chart(*chartElement*)

**Loading**

        manager.showLoading();
        manager.hideLoading();

**Custom Widgets**

        const widgets = {
            filters: [
                {
                    className: '', // CSS class of the select element for this filter
                    multi: false, // if true, this filter will allow selection of multiple values
                    options: ['Option 1'], // optional: if provided, has a higher precendence for rendering filter options
                    getOptions: function(manager) {}, // optional: use for dynamic options i.e fetch the options within the fuction and return them
                    onChange: function(event, manager) {} // called when the option is changed
                }
            ]
        }
        manager.initCustomWidgets(widgets);


**Themes**

Supported themes are `default`, `sunflower`, `marigold`, `rose`, `lavendar`, `bluebell`, `leaf`, `rainbow`

        manager.getThemes() // returns all supported themes & their colours
        manager.getTheme(theme) // returns the theme and colours of either the specified theme or the currently applied theme


### Plotly Charts Manager

Extends `DICharts.Chart`, so all the functions & properties there are accessible here


**Plot**

        manager.setData(data) // sets the chart data
        manager.setLayout(layout) // sets the chart layout options
        manager.setConfig(config) // sets the chart config options
        manager.updatePlot() // creates a new plot or updates an existing one

Usage:

        manager.setData(data).setLayout(layout).setConfig(config).updatePlot();

        manager.getPlot() // returns the current plot


**Theme**

        manager.setTheme('theme') // sets the active theme


**Data**

        manager.csv(url) // fetches the CSV data and returns a promise
