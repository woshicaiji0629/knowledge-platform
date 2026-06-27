描述 | 示例值 |
| --- | --- | --- | --- | --- |
| default_ttl_code | String | 是 | 状态码及其缓存时间，单位为秒，取值范围是 1~99999999（3 年多一些），多个状态码之间用半角逗号（,）分隔。 | 4xx=3,200=3600,5xx=1 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "default_ttl_code", "argValue": "4xx=3,200=3600,5xx=1" }], "functionName": "default_ttl_code" }], "DomainNames": "example.com" }
set_resp_header
功能说明：配置自定义HTTP响应头，该功能详细介绍请参见控制台配置说明[修改出站响应头](../user-guide/create-a-custom-http-response-header.md)。
功能ID（FunctionID/FuncId）：27。
参数说明：
