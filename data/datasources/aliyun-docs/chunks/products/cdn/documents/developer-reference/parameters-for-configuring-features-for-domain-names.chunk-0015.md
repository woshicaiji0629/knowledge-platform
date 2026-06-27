否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| key | String | 是 | 回源头名称。 | Accept-Encoding |
| value | String | 是 | 回源头的值。如果要删除某个回源头，设置回源头的值为 null。 | gzip |

配置示例一：添加一个回源HTTP请求头。
{ "Functions": [{ "functionArgs": [{ "argName": "value", "argValue": "gzip" }, { "argName": "key", "argValue": "Accept-Encoding" }], "functionName": "set_req_header" }], "DomainNames": "example.com" }
配置示例二：删除一个回源HTTP请求头（将value值设置为null）。
{ "Functions":[{ "functionArgs":[{ "argName":"value", "argValue":"null" }, { "argName":"key", "argValue":"User-Agent" }], "functionName":"set_req_header" }], "DomainNames":"example.com" }
origin_request_header
功能说明：配置回源HTTP请求头（新），该功能详细介绍请参见控制台配置说明[修改出站请求头](../user-guide/configure-custom-request-headers.md)。
功能ID（FunctionID/FuncId）：228。
参数说明：
