alue": "example.com" }], "functionName": "rewrite_host" }], "DomainNames": "example.com" }
serving_stale_content
功能说明：响应过期缓存。
功能ID（FunctionID/FuncId）：260。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| origin_error_status_code | String | 否 | 自定义源站异常状态码。 功能说明：用于设置在源站返回哪些状态码时适用于此功能配置。 默认值：默认不填写。默认情况下，源站异常的定义是超时+所有的 5xx 状态码。 配置说明：支持直接输入 4xx、5xx 来模糊匹配，也支持输入 502、504 这样的状态码来精确匹配；支持输入多个状态码，输入多个状态码的情况下，各个状态码之间用英文逗号进行分隔。 | 502 |
| extend_expiration_time | Integer | 否 | 过期延长时间。 功能说明：缓存过期后，希望保留旧缓存的最长时间。 默认值：默认不填写。默认情况下，过期延长时间是 1 小时。 配置说明：输入值为大于等于 1 的正整数，单位为秒。 | 60 |
| origin_first | String | 否 | 源站策略优先。 功能说明：参数配置为 on 的情况下可以开启源站策略优先，这时候如果源站返回文件时携带了缓存策略 Cache-Control: stale-if-error=xx ，将优先遵循源站响应信息里面 stale-if-error 参数设置的时间来作为过期延长时间。 默认值：默认不填写。默认情况下，等同于 off，这时候使用的是通过参数 extend_expiration_time 设置的过期延长时间 配置说明：支持 on （开启）、 off （关闭）。 | on |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "origin_error_status_code", "argValue": "502" }, { "argName": "extend_expiration_time", "argValue": "60" }, { "argName": "origin_first", "argValue": "off" }], "functionName": "serving_stale_content" }], "DomainNames": "example.com" }
