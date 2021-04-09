'use strict';
/* eslint-disable @typescript-eslint/no-var-requires */
const { dest, series, src } = require('gulp');
const clean = require('gulp-clean');
const webpack = require('webpack');
const webpackStream = require('webpack-stream');
const { merge } = require('webpack-merge');
const webpackConfig = require('./webpack.config');

const webpackConfigProduction = webpackConfig.map((config) =>
  merge(config, {
    devtool: false,
    mode: 'production',
    watch: false,
  }),
);

function cleaning(cb) {
  ['src/assets/**/*.js'].forEach((_path) => {
    src(_path, { read: false }).pipe(clean());
  });

  cb();
}

function streamWebpack(config) {
  if (typeof config.entry === 'object') {
    src(config.entry[Object.keys(config.entry)[0]]).pipe(webpackStream(config, webpack)).pipe(dest(config.output.path));
  } else {
    src(config.entry).pipe(webpackStream(config, webpack)).pipe(dest(config.output.path));
  }
}

function building(cb) {
  webpackConfigProduction.forEach(streamWebpack);

  cb();
}

function dev(cb) {
  webpackConfig.forEach(streamWebpack);

  cb();
}

exports.build = series(cleaning, building);
exports.default = series(cleaning, dev);
