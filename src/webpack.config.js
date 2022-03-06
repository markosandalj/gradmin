const path = require("path");
const webpack = require("webpack");
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const FixStyleOnlyEntriesPlugin = require("webpack-fix-style-only-entries");
const CopyPlugin = require("copy-webpack-plugin");

const devMode = process.env.NODE_ENV !== "production";
const outputDir = devMode ? 'build_dev' : 'build';

module.exports = {
  entry: {
    main: "./frontend/src/index.js",
    print: "./frontend/src/print.scss"
  },
  output: {
    path: path.resolve(__dirname, "./frontend/static/assets"),
    filename: "[name].js",
    clean: true,
  },
  devtool: "source-map",
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
      {
          test: /\.s?css$/,
          use: [
              MiniCssExtractPlugin.loader,
              'css-loader',
              "resolve-url-loader",
              'sass-loader',
          ],
      },
      {
          test: /\.(png|svg|jpg|jpeg|gif)$/i,
          type: 'asset/resource',
      },
      {
          test: /\.(woff|woff2|eot|ttf|otf)$/i,
          type: 'asset/resource',
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
    }),
  new FixStyleOnlyEntriesPlugin(),
  ],
};