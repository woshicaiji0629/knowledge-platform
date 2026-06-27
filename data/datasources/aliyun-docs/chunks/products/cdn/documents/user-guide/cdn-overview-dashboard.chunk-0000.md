### 【正在运行】域名看板
在所有正在运行状态的域名中，以CNAME、缓存过期时间、SSL证书三个配置为维度，统计每个配置未配置和已配置的数量。鼠标悬浮于统计数字上时，会显示对应配置状态的域名。

| 配置项 | 是否为必要配置 | 说明 |
| --- | --- | --- |
| CNAME | 必配 | [CNAME](../getting-started/quick-access-to-alibaba-cloud-cdn.md) 是一种 DNS 记录类型，在阿里云 CDN 中是保证加速域名正常运行的必要配置。 |
| 缓存过期时间 | 推荐 | [缓存过期时间](configure-the-cdn-cache-expiration-time.md) 指源站资源在阿里云 CDN 节点缓存的时长，达到预设时间，资源将会被节点标记为失效资源。合理的配置缓存过期时间可以提高阿里云 CDN 的缓存命中率，提升用户体验。 |
| SSL 证书 | 推荐 | [SSL](configure-an-ssl-certificate.md) [证书](configure-an-ssl-certificate.md) 是可以实现客户端与阿里云 CDN 节点之间的数据加密，使加速域名可以使用 HTTPS 协议访问。 |
