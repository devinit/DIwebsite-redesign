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
      splitChunks: {
        chunks: 'async',
        minSize: 30000,
        maxSize: 0,
        minChunks: 1,
        maxAsyncRequests: 6,
        maxInitialRequests: 4,
        automaticNameDelimiter: '~',
        cacheGroups: {
          defaultVendors: {
            test: /[\\/]node_modules[\\/]/,
            priority: -10,
          },
          default: {
            minChunks: 2,
            priority: -20,
            reuseExistingChunk: true,
          },
        },
      },
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

  grunt.registerTask('default', ['watch']);
  grunt.registerTask('build', 'Compiles all the assets and copies the files to the dist directory.', ['webpack:build']);
};
