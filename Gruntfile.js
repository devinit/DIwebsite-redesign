'use strict';
/* eslint-disable @typescript-eslint/no-var-requires */
const webpackConfig = require('./webpack.config');
const merge = require('webpack-merge');
const TerserPlugin = require('terser-webpack-plugin');

const webpackConfigProduction = webpackConfig.map((config) =>
  merge(config, {
    devtool: false,
    mode: 'production',
    optimization: {
      minimize: true,
      minimizer: [
        new TerserPlugin({
          parallel: true,
          cache: true,
        }),
      ],
    },
  }),
);

module.exports = function (grunt) {
  grunt.initConfig({
    watch: {
      update: {
        files: ['./src/**/*', 'src/**/*'],
        tasks: ['webpack:develop'],
        options: {
          debounceDelay: 250,
        },
      },
    },

    webpack: {
      develop: webpackConfig,
      build: webpackConfigProduction,
    },
  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-webpack');

  grunt.registerTask('default', ['webpack:develop', 'watch']);
  grunt.registerTask('build', 'Compiles all the assets and copies the files to the dist directory.', ['webpack:build']);
};
