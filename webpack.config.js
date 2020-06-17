const path = require("path");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
  entry: "./src/visualisation/widgets/ace-editor.ts",
  target: "web",
  mode: "production",
  output: {
    path: path.resolve(__dirname, "di_website/visualisation/static/visualisation/widgets/js"),
    filename: "ace-editor.js",
    library: 'WagtailAceEditor'
  },
  resolve: {
    extensions: [".js", ".jsx", ".json", ".ts", ".tsx"],
  },
  module: {
    rules: [
      {
        test: /\.(ts|tsx)$/,
        loader: "ts-loader",
      },
      {
        enforce: "pre",
        test: /\.js$/,
        loader: "source-map-loader",
      },
      {
        test: /\.css$/,
        loader: "css-loader",
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "./di_website/visualisation/static/visualisation/widgets/css/ace-editor.css",
    }),
  ],
};
