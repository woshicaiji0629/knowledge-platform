## 背景信息
压缩分为Gzip压缩和Brotli压缩，智能压缩功能主要针对Gzip压缩，智能压缩详情请参见[Gzip](use-the-gzip-compression-feature.md)[压缩](use-the-gzip-compression-feature.md)。
当源站文件的大小在1 KB~10 MB及之间时，才可以使用Gzip压缩或Brotli压缩，对1 KB以下和10 MB以上大小的文件不做压缩。
Brotli压缩支持的文件类型有text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、text/javascript、image/tiff、image/svg+xml、application/json、application/xml。
服务端响应携带响应头Content-Encoding: br：服务端响应的内容是经过Brotli压缩后的资源。
客户端请求携带请求头Accept-Encoding: br：客户端希望获取对应资源时进行Brotli压缩。
