| 匹配类型名称 | 域名配置功能函数 [condition](../developer-reference/parameters-for-configuring-features-for-domain-names.md) 中对应的配置参数 | 匹配类型含义 | 匹配对象 | 匹配运算符 | 匹配值 | 大小写敏感 | 对应 nginx/tengine |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 协议类型 | scheme | 客户端请求使用的协议类型，例如：HTTP、HTTPS。 | 不涉及 | 等于 不等于 | http https | 不涉及 | $scheme |
| 请求方法 | method | 客户端请求使用的请求方法，例如：GET、PUT。 | 不涉及 | 等于 不等于 | get put post delete head | 不涉及 | $request_method |
| URI（路径） | uri | 客户端请求 URL 中的路径，不含请求参数，例如： /favicon.ico 。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 支持通配符 ? 和 * , 例如：填写 /*/my_path/* ，支持输入多个值。 | 区分大小写 忽略大小写 | $raw_uri 或$uri |
| 文件名 | basename | 客户端请求的文件的名称，例如：name1。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 支持通配符 ? 和 * ，支持输入多个值。 | 区分大小写 忽略大小写 | - |
| 文件扩展名 | extension | 客户端请求的文件的后缀名，从右向左识别，识别到第一个"."，例如： .mp4 。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 支持通配符 ? 和 * ，支持输入多个值。 | 区分大小写 忽略大小写 | - |
| Hostname | hostname | 客户端请求携带的 hostname，匹配顺序：请求 URL 中的 host>请求头 HOST 中的 host。 | 不涉及 | 包含其中任意一个 不包含其中任意一个 | 用户请求的 host，支持输入多个值。 | 区分大小写 忽略大小写 | $host 或$http_host |
| 客户端 IP | clientip | 客户端的 IP。 支持 IPv4（例如 1.1.X.X ）、IPv6（例如 240e:95c:3004:2:3:0:0:XXX ）、支持网段（例如 20.209.XXX.XXX/31 ）。 | 建联 IP XFF IP 说明 建联 IP、XFF IP 详细说明，请参见 [IP](rules-engine.md) [地址校验模式](rule
