| value123 |
| match_all | String | 否 | 匹配模式。当 header_operation_type 使用 rewrite 时（即执行替换操作），需要设置匹配模式： on：匹配所有（所有匹配上的值都会被替换）。 off：仅匹配第一个（只有第一个匹配上的值会被替换）。 | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "header_operation_type", "argValue": "add" }, { "argName": "header_name", "argValue": "Cache-Control" }, { "argName": "header_value", "argValue": "no-cache" }, { "argName": "duplicate", "argValue": "off" }], "functionName": "origin_response_header" }], "DomainNames": "example.com" }
back_to_origin_url_rewrite
功能说明：改写回源URI，该功能详细介绍请参见控制台配置说明[重写回源路径](../user-guide/rewrite-urls-in-back-to-origin-requests.md)。
功能ID（FunctionID/FuncId）：225。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| source_url | String | 是 | 被重写的 URI。 | ^/hello$ |
| target_url | String | 是 | 重写的目标 URI。 | /hello/test |
| flag | String | 否 | 改写操作的执行规则，取值： 空：执行完该条规则后，后续 rewrite 规则会继续执行。 break：执行完该条规则后，后续 rewrite 规则不再执行。 enhance_break：类似 break，区别在于会带着参数一起进行处理，并且针对 flv 直播也会生效。 | break |
