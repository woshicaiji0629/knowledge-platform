操作），需要设置匹配模式： on：匹配所有（所有匹配上的值都会被替换）。 off：仅匹配第一个（只有第一个匹配上的值会被替换）。 | / |
| access_origin_control | String | 否 | 是否开启跨域校验： on：开启 CDN 节点对用户请求的跨域校验。 off：关闭该功能。 | / |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "header_operation_type", "argValue": "add" }, { "argName": "key", "argValue": "Cache-Control" }, { "argName": "value", "argValue": "no-cache" }, { "argName": "duplicate", "argValue": "off" }], "functionName": "set_resp_header" }], "DomainNames": "example.com" }
error_page
功能说明：配置自定义页面，该功能详细介绍请参见控制台配置说明[配置自定义页面](../user-guide/create-a-custom-error-page.md)。
功能ID（FunctionID/FuncId）：15。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| error_code | Integer | 是 | 错误码。 | 404 |
| rewrite_page | String | 是 | 重定向页面。 | http://example.aliyundoc.com/error404.html |
