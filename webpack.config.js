/* eslint-disable @typescript-eslint/no-var-requires */
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

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
        loader: 'babel-loader',
        include: path.resolve(__dirname, 'src'),
      },
      {
        enforce: 'pre',
        test: /\.js$/,
        loader: 'source-map-loader',
        include: path.resolve(__dirname, 'src'),
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js'],
  },
  performance: {
    maxEntrypointSize: 512000,
    maxAssetSize: 512000,
  },
  watch: true,
};

const wagtailAceEditorConfig = {
  ...sharedConfig,
  entry: './src/visualisation/widgets/ace-editor.ts',
  output: {
    path: path.resolve(__dirname, 'di_website/visualisation/static/visualisation/widgets/js'),
    filename: 'ace-editor.js',
    library: 'WagtailAceEditor',
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: './di_website/visualisation/static/visualisation/widgets/css/ace-editor.css',
    }),
  ],
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
  externals: ['jquery', 'echarts'],
};
chartsConfig.module.rules[0].loader = 'babel-loader';

const diChartsConfig = {
  ...sharedConfig,
  entry: './src/visualisation/library/index.ts',
  output: {
    path: path.resolve(__dirname, 'di_website/visualisation/static/visualisation/js'),
    filename: 'dicharts.js',
    library: 'DICharts',
  },
  externals: ['echarts'],
};

const appConfig = {
  ...sharedConfig,
  entry: {
    whatwedo: './src/whatwedo/index.ts',
    publications: './src/publications/index.ts',
    blog: './src/blog/index.ts',
    dashboard: './src/dashboard/index.ts',
  },
  output: {
    path: path.resolve(__dirname, 'di_website'),
    filename: '[name]/static/[name]/js/bundle.js',
    publicPath: '/assets/',
    chunkFilename: '[name]/js/[name][chunkhash].bundle.js',
  },
};

module.exports = [appConfig, wagtailAceEditorConfig, diChartsConfig, chartsConfig];
