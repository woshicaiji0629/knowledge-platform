|
| --- | --- | --- | --- | --- |
| error_code | Integer | 是 | 错误码。 | 404 |
| rewrite_page | String | 是 | 重定向页面。 | http://example.aliyundoc.com/error404.html |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "error_code", "argValue": "404" }, { "argName": "rewrite_page", "argValue": "http://example.aliyundoc.com/error404.html" }], "functionName": "error_page" }], "DomainNames": "example.com" }
host_redirect
功能说明：配置URI重写规则，该功能详细介绍请参见控制台配置说明[重写访问](../user-guide/create-an-access-url-rewrite-rule.md)[URL](../user-guide/create-an-access-url-rewrite-rule.md)。
功能ID（FunctionID/FuncId）：43。
参数说明：
