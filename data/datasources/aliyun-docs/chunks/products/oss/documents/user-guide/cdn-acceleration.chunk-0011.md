### 最佳实践
安全传输：启用HTTPS
为加速域名[配置](access-oss-by-https-protocol.md)[HTTPS](access-oss-by-https-protocol.md)[证书](access-oss-by-https-protocol.md)，并启用强制HTTPS跳转，实现客户端到CDN节点间的数据加密传输。HTTPS不仅能有效防止数据在传输过程中被窃取或篡改，还能避免浏览器地址栏出现不安全警告，提升用户信任度与品牌形象。
证书配置位置说明

| 访问方式 | 证书配置位置 | 说明 |
| --- | --- | --- |
| 直接访问 OSS 域名 | OSS 控制台 | 在 Bucket 的 Bucket 配置 > 域名管理 中配置 |
| 通过 CDN 加速域名访问 | CDN 控制台 | 在加速域名的 HTTPS 配置 中配置 |

说明
泛域名证书（如*.example.com）只能匹配二级域名，三级域名（如img.cdn.example.com）需要单独申请证书。
OSS不支持HTTP/2协议，如需使用HTTP/2，请通过CDN加速访问。
性能优化：配置综合缓存策略
缓存策略是CDN性能的核心要素，应包含缓存有效期和参数处理两个维度。
设置缓存有效期
通过[配置](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[CDN](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[缓存过期时间](../../../cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)，最大化缓存命中率：

| 文件类型 | 建议缓存时间 | 说明 |
| --- | --- | --- |
| 不常更新的静态文件（图片、音视频、安装包） | 1 个月以上 | 减少不必要的回源请求 |
| 频繁更新的静态文件（JS、CSS） | 数小时~数天 | 配合版本号（如 style.v1.1.css ）管理 |
| 动态文件或 API（PHP、JSP） | 0 秒（不缓存） | 确保每次请求获取最新内容 |
