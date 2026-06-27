value123 |
| match_all | String | 否 | 设置匹配模式。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置匹配模式： on：匹配所有（所有匹配上的值都会被替换）。 off：仅匹配第一个（只有第一个匹配上的值会被替换）。 | off |

配置示例：为加速域名example.com添加自定义回源请求头，请求头名称=Accept-Encoding，请求头值=gzip。
{ "Functions": [{ "functionArgs": [{ "argName": "header_operation_type", "argValue": "add" }, { "argName": "header_name", "argValue": "Accept-Encoding" }, { "argName": "header_value", "argValue": "gzip" }, { "argName": "duplicate", "argValue": "off" }], "functionName": "origin_request_header" }], "DomainNames": "example.com" }
origin_response_header
功能说明：配置回源HTTP响应头，该功能详细介绍请参见控制台配置说明[修改入站响应头](../user-guide/rewrite-http-response-headers.md)。
功能ID（FunctionID/FuncId）：229。
参数说明：
