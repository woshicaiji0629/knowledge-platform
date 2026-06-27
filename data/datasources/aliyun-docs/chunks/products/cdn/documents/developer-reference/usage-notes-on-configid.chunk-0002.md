## 生成ConfigId
配置单条规则：
调用[BatchSetCdnDomainConfig](../api-batchsetcdndomainconfig.md)给某个域名创建某个功能配置时生成ConfigId，该API调用成功后返回该配置项的ConfigId。
调用[SetCdnDomainStagingConfig](../api-setcdndomainstagingconfig.md)给某个域名创建某个功能配置时生成ConfigId，该API调用成功后不返回ConfigId，需要通过[DescribeCdnDomainStagingConfig](../api-describecdndomainstagingconfig.md)接口查询。
配置场景：假设加速域名为example.com，CDN节点在响应资源给客户端的时候，告知客户端该资源无需缓存。
示例：为域名example.com的功能set_resp_header配置规则：key=Cache-Control，value=no-cache。接口配置：
action: BatchSetCdnDomainConfig params: { "Functions": [{ "functionArgs": [{ "argName": "value", "argValue": "no-cache" }, { "argName": "key", "argValue": "Cache-Control" } ], "functionName": "set_resp_header" }], "domainNames": "example.com" } product: cdn
配置成功返回结果：返回ConfigId。
{ "code": "200", "data": { "DomainConfigList": { "DomainConfigModel": [ { "FunctionName": "set_resp_header", "DomainName": "example.com", "ConfigId": 19571990834**** } ] }, "RequestId": "4FF61A1D-E697-5E6C-9E5D-7D1E1529****" }, "httpStatusCode": "200", "requestId": "4FF61A1D-E697-5E6C-9E5D-7D1E1529****", "successResponse": true }
配置多条规则：有的功能支持配置多条规则，如果要一次配置多条规则，可以参考如下示例。
示例：为域名example.aliyundoc.com的功能set_resp_header（配置响应头）同时配置以下两条规则：
第一个规则：CDN节点在响应资源给
