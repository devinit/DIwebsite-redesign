/* eslint-disable @typescript-eslint/no-var-requires */
const path = require('path');
// const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const sharedConfig = {
  target: 'web',
  mode: 'development',
  resolve: {
    extensions: ['.js', '.jsx', '.json', '.ts', '.tsx'],
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        loader: 'ts-loader',
      },
      {
        enforce: 'pre',
        test: /\.js$/,
        loader: 'source-map-loader',
      },
      {
        test: /\.css$/,
        loader: 'css-loader',
      },
    ],
  },
};

const chartsConfig = {
  ...sharedConfig,
  entry: ['./src/visualisation/index.ts'],
  output: {
    path: path.resolve(__dirname, 'di_website/visualisation/static/visualisation/js'),
    filename: 'chart.js',
    publicPath: '/assets/visualisation/js/',
    chunkFilename: 'chart[chunkhash].js',
  },
  externals: ['jquery'],
};
chartsConfig.module.rules[0].loader = 'babel-loader';

module.exports = [chartsConfig];
