const webpack = require('webpack')
const path = require('path');

function resolve(dir) {
  return path.join(__dirname, dir);
}
console.log(55555)
module.exports = {
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery"
      })
    ],
  }
}
