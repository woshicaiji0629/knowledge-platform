配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "max_tries", "argValue": 2 }, { "argName": "retain_args", "argValue": "off" }, { "argName": "retain_header", "argValue": "off" }, { "argName": "response_header", "argValue": "X-Alicdn-Redirect" }, { "argName": "retain_header", "argValue": "off" }, { "argName": "modify_host", "argValue": "example.com" }, { "argName": "cache", "argValue": "off" }, { "argName": "expired_time", "argValue": "7200" }, { "argName": "follow_origin_host", "argValue": "off" }, { "argName": "follow_5xx_retry_origin", "argValue": "off" }], "functionName": "follow_302" }], "DomainNames": "example.com" }
set_req_header
功能说明：配置自定义回源HTTP头，该功能详细介绍请参见控制台配置说明[修改入站请求头](../configure-custom-request-headers-old.md)。
说明
set_req_header是v1版本，建议您使用v2版本：origin_request_header，v2版本支持更丰富的自定义回源HTTP头功能。
功能ID（FunctionID/FuncId）：39。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| key | String | 是 | 回源头名称。 | Accept-Encoding |
| value | String | 是 | 回源头的值。如果要删除某个回源头，设置回源头的值为 null。 | gzip |
