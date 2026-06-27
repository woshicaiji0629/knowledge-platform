## 通过ConfigId删除配置项
调用[DeleteSpecificConfig](../api-deletespecificconfig.md)、[DeleteSpecificStagingConfig](../api-deletespecificstagingconfig.md)删除某个配置，删除配置的时候指定该配置项对应的ConfigId即可。
示例：为域名example.aliyundoc.com删除功能set_resp_header上指定的规则配置。接口调用：
action: DeleteSpecificConfig params: { "ConfigId": 19571990834****, "functionName": "set_resp_header", "domainName": "example.aliyundoc.com" } product: cdn
该文章对您有帮助吗？
反馈
