## 通过ConfigId更新配置项
调用[BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md)、[SetCdnDomainStagingConfig](../api-setcdndomainstagingconfig.md)更新已有的配置，更新配置的时候指定该配置项对应的ConfigId即可。
配置场景：假设加速域名为example.com，CDN节点响应给客户端的资源由不缓存改为缓存1小时。
示例：为域名example.com的功能set_resp_header更新规则配置为：key=Cache-Control，value=max-age=3600。接口调用：
action: BatchSetCdnDomainConfig params: { "Functions": [ { "functionArgs": [ { "argName": "value", "argValue": "max-age=3600" }, { "argName": "key", "argValue": "Cache-Control" } ], "functionName": "set_resp_header", "ConfigId": 19571990834**** } ], "domainNames": "example.com" } product: cdn
