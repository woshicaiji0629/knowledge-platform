## 提高CDN的访问性能
结合您的实际业务需求，通过配置页面优化、Range回源、智能压缩功能，可缩小访问文件的体积，提升资源加速效率和页面可读性。

| 场景 | 说明 | 配置 |
| --- | --- | --- |
| 提高访问性能 | CDN 会自动删除页面的冗余内容，例如 HTML 页面、内嵌 JavaScript 和 CSS 中的注释以及重复的空白符，可有效去除页面的冗余信息，缩小文件体积，提高加速分发效率。 | [页面优化](user-guide/enable-html-optimization.md) |
| 客户端通知源站服务器只返回指定范围的部分内容，适用于音视频等较大文件的内容分发加速，可减少回源流量消耗，并提升资源的响应时间。 | [配置](user-guide/object-chunking.md) [Range](user-guide/object-chunking.md) [回源](user-guide/object-chunking.md) |  |
| CDN 节点向您返回请求的资源时，会对文本文件进行 Gzip 压缩，可有效缩小传输文件的大小，提升文件传输效率，减少带宽消耗。 | [Gzip](user-guide/use-the-gzip-compression-feature.md) [压缩](user-guide/use-the-gzip-compression-feature.md) |  |

该文章对您有帮助吗？
反馈
