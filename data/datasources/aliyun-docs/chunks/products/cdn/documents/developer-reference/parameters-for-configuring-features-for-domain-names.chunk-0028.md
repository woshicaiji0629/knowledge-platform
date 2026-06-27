户端采用 HTTP 协议，按照 HTTP 协议回源。 客户端采用 HTTPS 协议。 客户端为国际算法，按照 HTTPS 协议回源，采用国际算法。 客户算作国密算法，按照 HTTPS 协议回源，采用国密算法。 说明 国际算法指的是国际标准的加密算法，国密算法指的是中国国家密码管理局认定的国产加密算法。 | http |

配置示例一：回源协议设置为http，回源端口设置为80。
{ "Functions": [{ "functionArgs": [{ "argName": "port", "argValue": "80" }, { "argName": "scheme", "argValue": "http" }], "functionName": "ali_origin_port_scheme" }], "DomainNames": "example.com" }
配置示例二：回源协议follow用户请求使用的协议，使用HTTP协议回源时，回源到源站的80端口，使用HTTPS协议回源时，回源到源站的443端口。
{ "Functions":[{ "functionArgs": [{ "argName": "port", "argValue": "http:80|https:443" }, { "argName": "scheme", "argValue": "follow" }], "functionName":"ali_origin_port_scheme" }], "DomainNames":"example.com" }
origin_sni
功能说明：配置指定源站回源SNI，可以对指定源站设置指定的回源SNI。
功能ID（FunctionID/FuncId）：262。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| origin | String | 是 | 源站地址（也可以不指定源站地址，不指定源站地址的时候，参数 origin 的值设置为 all）。 | example.com |
| sni_host | String | 是 | sni host 值： 可以设置为固定值，例如： example.org 。 跟随源站地址作为 SNI，设置为 ali_follow_origin 。 跟随回源 host 作为 SNI，设置为 ali_follow_host 。 | example.org |
| keepalive_sni | String | 否 | 是否开启长连接 SNI 匹配： on：开启。 off：关闭。 说明 开启后，不同回源 SNI 将使用不同长连接。 | / |
