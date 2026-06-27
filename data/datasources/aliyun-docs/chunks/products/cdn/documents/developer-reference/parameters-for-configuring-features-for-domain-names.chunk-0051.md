，多个 HTTP header 之间使用空格分隔。 | example |
| variable | Array of String | 否 | 自定义变量，可使用正则表达式从请求 URL 中的请求参数、HTTP header、cookie 和 URI 中截取出任意字段，然后拼接到 cachekey 中。 | [] |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "uri", "argValue": [{ "uri_to_rewrite": "/hello", "ai_uri_regex": "/hello/test" }] }, { "argName": "args", "argValue": [{ "args": "test=123", "args_operation_type": "add" }] }, { "argName": "headers", "argValue": "" }, { "argName": "variable", "argValue": [] }], "functionName": "self_defined_cachekey" }], "DomainNames": "example.com" }
rewrite_host
功能说明：共享缓存。
功能ID（FunctionID/FuncId）：54。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| share_host | String | 是 | 可以与当前域名共享缓存的目标域名。该配置不修改用户请求的回源 HOST，只是在查询缓存资源的时候，使用 share_host 值来生成查询用的 cachekey。 | example.com |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "share_host", "argValue": "example.com" }], "functionName": "rewrite_host" }], "DomainNames": "example.com" }
serving_stale_content
功能说明：响应过期缓存。
功能ID（FunctionID/FuncId）：260。
参数说明：
