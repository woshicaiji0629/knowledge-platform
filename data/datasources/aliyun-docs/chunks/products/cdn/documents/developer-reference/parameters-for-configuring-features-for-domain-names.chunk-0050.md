配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "flag", "argValue": "redirect" }, { "argName": "regex", "argValue": "^/hello$" }, { "argName": "replacement", "argValue": "/hello/test" }, { "argName": "rewrite_method", "argValue": "302" }], "functionName": "host_redirect" }], "DomainNames": "example.com" }
self_defined_cachekey
功能说明：配置自定义Cachekey，该功能详细介绍请参见控制台配置说明[自定义](../user-guide/create-custom-cache-keys.md)[Cachekey](../user-guide/create-custom-cache-keys.md)。
功能ID（FunctionID/FuncId）：227。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| uri | Array of String | 否 | 将请求中的源 URI 改写为目标 URI，然后存为 cachekey。 uri_to_rewrite 用于指定源 uri。 ai_uri_regex 用于指定目标 uri。 | [{"uri_to_rewrite":"/hello","ai_uri_regex":"/hello/test"}] |
| args | Array of String | 否 | 请求中的参数进行增、删、改和保留操作，然后后存为 cachekey，取值： args_operation_type：指定参数操作类型，支持 add（修改）、delete（删除）、modify（变更）和 keep（保留）。 args：指定参数操作对应的参数值。 | [{"args":"test=123","args_operation_type":"add"}] |
| headers | String | 否 | 用于增加多个 HTTP header，并且拼接到 cachekey 中，多个 HTTP header 之间使用空格分隔。 | example |
| variable | Array of String | 否 | 自定义变量，可使用正则表达式从请求 URL 中的请求参数、HTTP header、cookie 和 URI 中截取出任意字段，然后拼接到 cachekey 中。 | [] |
