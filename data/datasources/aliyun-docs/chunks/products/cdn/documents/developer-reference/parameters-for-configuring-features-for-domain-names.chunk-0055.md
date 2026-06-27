是否开启强制 HTTP 跳转： on：开启。 off：关闭。 | on |
| http_rewrite | String | 否 | 跳转方式，支持 301、308 状态码： 301：GET 请求方式不会发生变更，其他请求方式有可能会变更为 GET 请求方式。 308：请求方式和消息主体都不发生变化。 | 301 |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "enable", "argValue": "on" }, { "argName": "http_rewrite", "argValue": "301" }], "functionName": "http_force" }], "DomainNames": "example.com" }
https_force
功能说明：配置强制HTTPS跳转，该功能详细介绍请参见控制台配置说明[配置协议重定向](../user-guide/configure-url-redirection.md)。
功能冲突说明：强制HTTPS跳转功能与强制HTTP跳转功能（功能函数：http_force，功能ID：45）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另外一个功能添加配置。
功能ID（FunctionID/FuncId）：44。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| enable | String | 是 | 是否开启强制 HTTPS 跳转： on：开启。 off：关闭。 | on |
| https_rewrite | String | 否 | 跳转方式，支持 301、308 状态码： 301：GET 请求方式不会发生变更，其他请求方式有可能会变更为 GET 请求方式。 308：请求方式和消息主体都不发生变化。 | 301 |
