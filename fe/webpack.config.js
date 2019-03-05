const path = require('path');
const webpack = require('webpack');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
module.exports = {
	entry: './src/index.js',
	output: {
		path: path.resolve(__dirname, './dist'),
		filename: 'bundle.js',
	},
	mode: 'development',
	devtool: 'inline-source-map',
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				exclude: /node_modules/,
				use: {
					loader: 'babel-loader',
				},
			},
			{
				test: /.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
				use: [{
					loader: 'file-loader',
					options: {
						name: '[name].[ext]',
						outputPath: 'fonts/',
						publicPath: '/fonts/'
					}
				}]
			},
			{
				test: /\.(css|scss|sass)$/,
				use: ExtractTextPlugin.extract({
					fallback: 'style-loader',
					use: ['css-loader', 'resolve-url-loader', 'sass-loader?sourceMap']
				}),
			},		
		],
	},
	resolve: {
		extensions: ['.js', '.jsx'],
	},
	plugins: [
		new CopyWebpackPlugin([
			'./src/index.html',
		]),
		new ExtractTextPlugin('css/styles.css'),
	],
	devServer: {
		port: 3000,
		historyApiFallback: true,
	},
};
