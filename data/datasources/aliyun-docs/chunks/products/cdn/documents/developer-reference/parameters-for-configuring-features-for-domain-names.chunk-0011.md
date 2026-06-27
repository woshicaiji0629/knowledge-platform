表示“等于”。 !=：表示“不等于”。 | == |
| value | String | 是 | 变量的取值。 | /image |
| origin | String | 是 | 回源查询 DNS 使用的域名（即用户请求中对应的变量值，匹配后需要回源到指定的源站地址）。 | origin.example.com |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "conditions", "argValue": "==" }, { "argName": "variable_type", "argValue": "uri" }, { "argName": "value", "argValue": "/image" }, { "argName": "origin", "argValue": "origin.example.com" }, { "argName": "variable", "argValue": "uri" }], "functionName": "advanced_origin" }], "DomainNames": "example.com", }
follow_302
功能说明：配置回源302跟随，该功能详细介绍请参见控制台配置说明[配置回源](../user-guide/configure-301-or-302-redirection.md)[301/302](../user-guide/configure-301-or-302-redirection.md)[跟随](../user-guide/configure-301-or-302-redirection.md)。
功能ID（FunctionID/FuncId）：219。
参数说明：
