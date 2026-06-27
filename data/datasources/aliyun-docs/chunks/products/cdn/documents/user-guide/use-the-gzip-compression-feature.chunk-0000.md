## 背景信息
压缩分为Gzip压缩和Brotli压缩，Gzip压缩功能使用的是Gzip压缩算法，Brotli压缩详情请参见[Brotli](configure-brotli-compression.md)[压缩](configure-brotli-compression.md)。
当源站文件的大小在1 KB~10 MB及之间时，才可以使用Gzip压缩或Brotli压缩，对1 KB以下和10 MB以上大小的文件不做压缩。
Gzip压缩支持的文件类型有text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、text/javascript、image/tiff、image/svg+xml、application/json、application/xml。
客户端请求携带请求头Accept-Encoding: gzip：客户端希望获取对应资源时进行Gzip压缩。
服务端响应携带响应头Content-Encoding: gzip：服务端响应的内容为Gzip压缩的资源。
