## 生效验证
配置完成后，可通过curl命令或浏览器开发者工具查看资源的HTTP响应标头，以判断缓存是否按预期工作。
1. 执行验证命令
在终端上执行以下命令进行测试。
curl -I "https://your.domain.com/path/to/file.jpg"
2. 解读关键响应头

| 响应标头 | 常见值与解读 |
| --- | --- |
| X-Cache | 指示请求是否命中 CDN 缓存。 - HIT ：命中缓存。 - MISS ：未命中缓存，请求已回源获取资源。 |
| Cache-Control | 开启"客户端跟随 CDN 缓存策略"后，此标头会显示 CDN 传递给浏览器的缓存指令，如 max-age=3600 。 |
| X-Swift-CacheTime | 资源在 CDN 节点上配置的缓存总时长，单位为秒。 |
