li_follow_origin" }], "functionName": "origin_host" }], "DomainNames": "example.com" }
ali_origin_port_scheme
功能说明：配置回源端口和协议。
功能ID（FunctionID/FuncId）：276。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| port | String | 是 | 回源端口。 说明 当 scheme 设置为 follow 时，需填写 http:80|https:443 这样的格式。 | 80 |
| scheme | String | 是 | 回源协议：自定义回源协议（支持 http、https、follow、https_sm、follow_sm）。 http：按照 HTTP 协议回源。 https：按照 HTTPS 协议回源，采用国际算法。 follow：回源协议跟随（使用 HTTPS 协议回源时，仅支持国际算法）。 客户端采用 HTTP 协议，按照 HTTP 协议回源。 客户端采用 HTTPS 协议。 客户端为国际算法，按照 HTTPS 协议回源，采用国际算法。 客户端为国密算法，按照 HTTPS 协议回源，采用国际算法。 https_sm：按照 HTTPS 协议回源，采用国密算法。 follow_sm：回源协议跟随（使用 HTTPS 协议回源时，既支持国际算法，也支持国密算法）。 客户端采用 HTTP 协议，按照 HTTP 协议回源。 客户端采用 HTTPS 协议。 客户端为国际算法，按照 HTTPS 协议回源，采用国际算法。 客户算作国密算法，按照 HTTPS 协议回源，采用国密算法。 说明 国际算法指的是国际标准的加密算法，国密算法指的是中国国家密码管理局认定的国产加密算法。 | http |
