"use strict";
const webpack = require("webpack");
const webpackConfig = require("./webpack.config");
const merge = require("webpack-merge");

const webpackConfigProduction = webpackConfig.map(config => merge(config, {
    devtool: false,
    mode: 'production'
}));

module.exports = function(grunt) {
    grunt.initConfig({

        watch: {
            update: {
                files: [ "./src/**/*", "src/**/*" ],
                tasks: [ "webpack:develop" ],
                options: {
                    debounceDelay: 250
                }
            }
        },

        webpack: {
            develop: webpackConfig,
            build: webpackConfigProduction
        },
    });

    grunt.loadNpmTasks("grunt-contrib-watch");
    grunt.loadNpmTasks("grunt-webpack");

    grunt.registerTask("default", [ "watch" ]);
    grunt.registerTask(
        "build",
        "Compiles all the assets and copies the files to the dist directory.",
        [ "webpack:build" ]
    );
};
