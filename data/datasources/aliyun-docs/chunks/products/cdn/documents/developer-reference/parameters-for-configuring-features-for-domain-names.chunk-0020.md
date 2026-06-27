| String | 否 | 改写操作的执行规则，取值： 空：执行完该条规则后，后续 rewrite 规则会继续执行。 break：执行完该条规则后，后续 rewrite 规则不再执行。 enhance_break：类似 break，区别在于会带着参数一起进行处理，并且针对 flv 直播也会生效。 | break |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "flag", "argValue": "break" }, { "argName": "source_url", "argValue": "^/hello$" }, { "argName": "target_url", "argValue": "/hello/test" }], "functionName": "back_to_origin_url_rewrite" }], "DomainNames": "example.com", }
back_to_origin_argument_rewrite
功能说明：改写回源参数，该功能详细介绍请参见控制台配置说明[重写回源参数](../user-guide/rewrite-url-parameters-in-back-to-origin-requests.md)。
说明
回源参数改写，改写的是回源请求URL的查询参数，支持配置多个不同的改写规则，改写动作的优先级为添加参数＞删除参数＞仅保留＞修改参数。当不同的改写规则作用于同一个参数时，只有高优先级的规则会生效。
功能ID（FunctionID/FuncId）：224。
参数说明：
