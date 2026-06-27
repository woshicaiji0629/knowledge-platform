，参数 origin 的值设置为 all，代表所有源站）。 | example.com |
| host | String | 是 | 指定 HOST（也可以不指定 HOST，参数 host 的值设置为 ali_follow_origin 代表跟随源站地址作为 host 值）。 | host.example.com |

配置示例一：用户请求回源到源站example.com时，使用的host值为host.example.com。
{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "example.com" }, { "argName": "host", "argValue": "host.example.com" }], "functionName": "origin_host" }], "DomainNames": "example.com" }
配置示例二：用户回源到所有的源站（源站值用all来代表）都是用同一个host值host.example.com。
{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "host", "argValue": "host.example.com" }], "functionName": "origin_host" }], "DomainNames": "example.com" }
配置示例三：用户回源到所有的源站（源站值用all来代表）都跟随源站地址作为host值（用ali_follow_origin来表示）。
{ "Functions": [{ "functionArgs": [{ "argName": "origin", "argValue": "all" }, { "argName": "host", "argValue": "ali_follow_origin" }], "functionName": "origin_host" }], "DomainNames": "example.com" }
ali_origin_port_scheme
功能说明：配置回源端口和协议。
功能ID（FunctionID/FuncId）：276。
参数说明：
