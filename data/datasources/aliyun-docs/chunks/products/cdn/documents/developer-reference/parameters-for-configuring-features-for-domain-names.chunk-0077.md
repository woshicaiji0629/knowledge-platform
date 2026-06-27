guide/configure-a-user-agent-blacklist-or-whitelist.md)[黑白名单](../user-guide/configure-a-user-agent-blacklist-or-whitelist.md)。
功能ID（FunctionID/FuncId）：58。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| ua | String | 是 | 填写 User-Agent，支持通配符*（匹配任意字符串）和多个值（多个值用|分割。例如： *curl*|*IE*|*chrome*|*firefox*） 。 | *curl*|*IE*|*chrome*|*firefox* |
| type | String | 是 | 名单类型，取值： black：黑名单。 white：白名单。 说明 黑、白名单互斥，同一时间只支持其中一种方式生效。 | black |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "ua", "argValue": "*curl*|*IE*|*chrome*|*firefox*" }, { "argName": "type", "argValue": "black" }], "functionName": "ali_ua" }], "DomainNames": "example.com" }
