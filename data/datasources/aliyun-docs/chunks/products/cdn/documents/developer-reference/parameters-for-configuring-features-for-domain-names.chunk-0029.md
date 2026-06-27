ow_origin 。 跟随回源 host 作为 SNI，设置为 ali_follow_host 。 | example.org |
| keepalive_sni | String | 否 | 是否开启长连接 SNI 匹配： on：开启。 off：关闭。 说明 开启后，不同回源 SNI 将使用不同长连接。 | / |

配置示例一：用户请求回源到源站origin.example.com时，使用的SNI值为host.example.com。
{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "origin.example.com" }, { "argName": "sni_host", "argValue": "host.example.com" }], "functionName": "origin_sni" }], "DomainNames": "example.com" }
配置示例二：用户回源到所有的源站（源站值用all来表示）都使用同一个SNI值host.example.com。
{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "sni_host", "argValue": "host.example.com" }], "functionName":"origin_sni" }], "DomainNames":"example.com" }
配置示例三：用户回源到所有的源站（源站值用all来表示）都跟随源站地址作为SNI值（使用参数值ali_follow_origin来表示）。
{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "sni_host", "argValue": "ali_follow_origin" }], "functionName": "origin_sni" }], "DomainNames": "example.com" }
配置示例四：用户回源到所有的源站（源站值用all来表示）都跟随回源host作为SNI值（使用参数值ali_follow_host来表示）。
{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "sni_host", "argValue": "ali_follow_host" }], "functionName": "origin_sni" }], "DomainNames": "example.com" }
source_group
功能说明：源站组设置。
功能ID（FunctionID/FuncId）：294。
参数说明：
