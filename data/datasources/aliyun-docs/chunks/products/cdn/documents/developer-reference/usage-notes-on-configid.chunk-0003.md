1529****", "successResponse": true }
配置多条规则：有的功能支持配置多条规则，如果要一次配置多条规则，可以参考如下示例。
示例：为域名example.aliyundoc.com的功能set_resp_header（配置响应头）同时配置以下两条规则：
第一个规则：CDN节点在响应资源给客户端的时候，告知客户端该资源无需缓存。
参数配置如下：key=Cache-Control，value=no-cache
第二个规则：CDN节点在响应资源给客户端的时候，告知客户端该资源的内容类型是文本类型。
参数配置如下：key=Content-Type，value=text/plain
接口配置：
action: BatchSetCdnDomainConfig params: { "domainNames": "example.aliyundoc.com", "functions": [ { "functionArgs": [ { "ArgValue": "Cache-Control", "ArgName": "key" }, { "ArgValue": "no-cache", "ArgName": "value" } ], "functionName": "set_resp_header" }, { "functionArgs": [ { "ArgValue": "Content-Type", "ArgName": "key" }, { "ArgValue": "text/plain", "ArgName": "value" } ], "functionName": "set_resp_header" } ] } product: cdn
配置成功，返回结果，两条不同的规则分别返回了不同的ConfigId。
{ "code":"200", "data":{ "DomainConfigList":{ "DomainConfigModel":[ { "FunctionName":"set_resp_header", "DomainName":"example.aliyundoc.com", "ConfigId":20953663204**** }, { "FunctionName":"set_resp_header", "DomainName":"example.aliyundoc.com", "ConfigId":20953663204**** } ] }, "RequestId":"69A79ACE-FD8E-5993-9CEA-7AAB2F08****" }, "httpStatusCode":"200", "requestId":"69A79ACE-FD8E-5993-9CEA-7AAB2F08****", "successRespo
