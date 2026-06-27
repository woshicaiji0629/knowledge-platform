## 注意事项
Gzip压缩兼容所有浏览器，Brotli压缩不兼容较老版本的浏览器，您可以根据业务需要[查询](https://caniuse.com)浏览器的兼容情况。
CDN对静态文件进行压缩时，会改变文件的MD5值，如果客户网站的业务逻辑里面有使用文件MD5校验（即客户端需要校验从CDN节点上拿到的文件的MD5值，如果文件校验的MD5值与响应头里面记录的MD5值不一致，则说明文件下载失败），请关闭Gzip压缩和Brotli压缩功能。
源站开启了压缩功能，且服务端响应中携带了响应头Content-Encoding，则CDN的压缩功能将不再生效。
同时开启Gzip压缩和Brotli压缩，且客户端请求头Accept-Encoding同时携带br和gzip时，仅Brotli压缩生效。
如果您同时开启了页面优化和压缩功能（Gzip压缩或者Brotli压缩），页面优化功能将会失效，CDN只会对文件进行压缩。
常见的图片文件类型（PNG、JPG、JPEG等）和视频文件类型（MP4、AVI、WMV等）已经做了内容的压缩处理，开启Gzip压缩或者Brotli压缩没有效果，建议您关闭Gzip压缩或者Brotli压缩功能。如果您需要进一步降低图片文件的体积可以使用[图像处理](image-editing-overview.md)功能；如果您需要进一步降低视频文件的体积可以使用[视频转码](https://help.aliyun.com/zh/mps/product-overview/features#concept-1960458)功能。
