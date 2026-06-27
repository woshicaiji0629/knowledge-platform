: "example.com" }
forward_scheme
功能说明：配置回源协议，该功能详细介绍请参见控制台配置说明[配置回源协议](../user-guide/configure-the-origin-protocol-policy.md)。
功能ID（FunctionID/FuncId）：47。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启回源协议： on：开启。 off：关闭。 | on |
| scheme_origin | String | 否 | 回源类型，取值： http：CDN 以 HTTP 协议回源。 https：CDN 以 HTTPS 协议回源。 follow（跟随）：客户端以 HTTP 或者 HTTPS 协议请求 CDN，CDN 跟随客户端的协议请求源站。 说明 scheme_origin 不配置时，默认取值为 follow。 | follow |
| scheme_origin_port | String | 否 | 回源自定义端口，需要与 scheme_origin 参数搭配使用，取值： scheme_origin 取值为 http 时，只需要配置一个 HTTP 协议的回源端口，例如：80。 scheme_origin 取值为 https 时，只需要配置一个 HTTPS 协议的回源端口，例如：443。 scheme_origin 取值为 follow 时，需要同时配置 HTTP 协议和 HTTPS 协议的回源端口，中间用半角冒号（:）分隔，例如：80:443。 | 80:443 |
