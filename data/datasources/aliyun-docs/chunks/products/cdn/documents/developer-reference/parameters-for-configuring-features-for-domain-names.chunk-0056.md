开启强制 HTTPS 跳转： on：开启。 off：关闭。 | on |
| https_rewrite | String | 否 | 跳转方式，支持 301、308 状态码： 301：GET 请求方式不会发生变更，其他请求方式有可能会变更为 GET 请求方式。 308：请求方式和消息主体都不发生变化。 | 301 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "https_rewrite", "argValue": "301" }], "functionName": "https_force" }], "DomainNames": "example.com" }
https_tls_version
功能说明：配置TLS协议版本，该功能详细介绍请参见控制台配置说明[配置](../user-guide/configure-tls-version-control.md)[TLS](../user-guide/configure-tls-version-control.md)[版本与加密套件](../user-guide/configure-tls-version-control.md)。
功能ID（FunctionID/FuncId）：110。
参数说明：
