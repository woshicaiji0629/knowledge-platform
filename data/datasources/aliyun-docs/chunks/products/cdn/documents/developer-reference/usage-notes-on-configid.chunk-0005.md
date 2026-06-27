## 查询ConfigId
调用[DescribeCdnDomainConfigs](../api-describecdndomainconfigs.md)、[DescribeCdnDomainStagingConfig](../api-describecdndomainstagingconfig.md)，查询结果返回对应配置的ConfigId。
示例：查询域名example.aliyundoc.com的功能set_resp_header的配置。接口调用：
action: DescribeCdnDomainConfigs params: { "domainName": "example.aliyundoc.com", "functionNames": "set_resp_header" } product: cdn
返回结果：显示ConfigId。
{ "code": "200", "data": { "RequestId": "51B7DF03-A7AE-56ED-BF1E-D16F6A6B****", "DomainConfigs": { "DomainConfig": [{ "Status": "configuring", "FunctionName": "set_resp_header", "FunctionArgs": { "FunctionArg": [{ "ArgValue": "no-cache", "ArgName": "value" }, { "ArgValue": "Cache-Control", "ArgName": "key" } ] }, "ConfigId": 19572306654**** }] } }, "httpStatusCode": "200", "requestId": "51B7DF03-A7AE-56ED-BF1E-D16F6A6B****", "successResponse": true }
