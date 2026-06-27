HTTP 或 HTTPS 协议头部，则依然视为有效 referer 进行处理。示例： 取值为 on 时，referer 格式如下： referer: www.example.com 取值为 off（默认值）时，referer 格式如下： referer: https://www.example.com | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "allow_empty", "argValue": "off" }, { "argName": "refer_domain_deny_list", "argValue": "example.aliyundoc.com,demo.aliyundoc.com" }], "functionName": "referer_black_list_set" }], "DomainNames": "example.com" }
aliauth
功能说明：配置URL鉴权，该功能详细介绍请参见控制台配置说明[配置](../user-guide/configure-url-signing.md)[URL](../user-guide/configure-url-signing.md)[鉴权](../user-guide/configure-url-signing.md)。
功能ID（FunctionID/FuncId）：25。
参数说明：
