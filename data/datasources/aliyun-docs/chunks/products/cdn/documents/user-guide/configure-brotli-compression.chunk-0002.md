## 注意事项
CDN对静态文件进行压缩时，会改变文件的MD5值，如果源站文件配置了MD5校验机制，请关闭智能压缩和Brotli压缩功能。
源站开启了压缩功能，且服务端响应中携带了content_encoding，则CDN的压缩功能将不再生效。
同时开启Brotli压缩和智能压缩，且客户端请求头Accept-Encoding同时携带br和gzip时，仅Brotli压缩生效。
如果您同时开启了页面优化和压缩功能（Gzip压缩或者Brotli压缩），页面优化功能将会失效，CDN只会对文件进行压缩。
Brotli压缩只兼容部分浏览器，您可以根据业务需要[查询](https://caniuse.com)浏览器的兼容情况。
常见的图片文件类型（PNG、JPG、JPEG等）和视频文件类型（MP4、AVI、WMV等）已经做了内容的压缩处理，开启智能压缩或者Brotli压缩没有效果，建议您关闭压缩功能。如果您需要进一步减小图片文件的体积可以使用[图像处理](image-editing-overview.md)功能，如果您需要进一步减小视频文件的体积可以使用[视频转码](https://help.aliyun.com/zh/mps/product-overview/features#concept-1960458)功能。“图像处理”和“视频转码”都会影响文件清晰度。
