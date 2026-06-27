用的域名是 example.com，重写后的 URL 使用新的域名 aliyundoc.com。 302 Location 地址支持使用其他协议，可以实现这样的效果：原始 URL 使用 HTTP 协议，重写后的 URL 使用 HTTPS 协议。 | redirect |
| rewrite_method | String | 否 | 重定向方式，支持 302、303、307 状态码： 302：默认重定向方式，GET 请求方式不会发生变更，其他请求方式有可能会变更为 GET 请求。 303：GET 请求方式不会发生变更，其他请求方式会变更为 GET 请求方式（消息主体会丢失）。 307：请求方式和消息主体都不发生变化。 | 302 |
