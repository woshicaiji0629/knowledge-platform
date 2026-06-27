| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启 IPv6 回源功能。 on：开启。 off：关闭。 说明 开启 IPv6 回源功能后，CDN 回源侧将提供 IPv6 服务。 CDN 节点和源站都具备可用的 IPv6 地址，则使用 IPv6 建立建连接 以下场景使用 IPv4 建立建连接 CDN 节点不具备可用的 IPv6 地址。 源站不具备可用的 IPv6 地址。 CDN 节点和源站都不具备可用的 IPv6 地址。 | on |
| follow | String | 是 | 是否开启回源跟随客户端 IP 协议版本功能。 on：开启。 off：关闭。 说明 开启回源跟随客户端 IP 协议版本功能后，CDN 回源将会跟随客户端请求使用的 IP 协议版本。 客户端请求使用 IPv6，则 CDN 优先回源 IPv6 源站，如果没有 IPv6 源站，则使用 IPv4 源站。 客户端请求使用 IPv4，则 CDN 优先回源 IPv4 源站，如果没有 IPv4 源站，则使用 IPv6 源站。 | on |
| ipv6_v4_mix_used | String | 否 | 是否开启“源站 IPv4 地址/IPv6 地址轮询”功能。 on：开启。 off：关闭。 说明 “源站 IPv4 地址/IPv6 地址轮询”功能与“IPv6 回源”、“回源跟随客户端 IP 协议版本”这两个功能是互斥的，“回源 v4/v6 轮询”功能一旦开启，“IPv6 回源”、“回源跟随客户端 IP 协议版本”这两个功能就会失效。 “源站 IPv4 地址/IPv6 地址轮询”功能的作用是不论客户端请求使用的是 IPv4 还是 IPv6，也不论源站有几个 IPv4 地址、几个 IPv6 地址，都会统一使用轮询方式回源到各个源站地址。 如果 IPv4、IPv6 地址配置了权重比例，那么还会按照权重比例回源。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" },{ "argName": "follow", "argValue": "on" }], "functionName": "ipv6_origin" }], "DomainNames": "example.com" }
cos_auth
功能说明：配置腾讯云COS云存储的鉴权Bucket。
功能ID（FunctionID/FuncId）：288。
参数说明：
