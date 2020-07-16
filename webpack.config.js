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
        include: path.resolve(__dirname, 'src'),
      },
      {
        enforce: 'pre',
        test: /\.js$/,
        loader: 'source-map-loader',
        include: path.resolve(__dirname, 'src'),
      },
      {
        test: /\.css$/,
        loader: 'css-loader',
        include: path.resolve(__dirname, 'src'),
      },
    ],
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
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
    libraryTarget: 'umd',
  },
  externals: ['jquery'],
};
chartsConfig.module.rules[0].loader = 'babel-loader';

module.exports = [chartsConfig];
