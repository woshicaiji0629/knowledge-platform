ption | String | 否 | 扩展字段。 | 空 |
| grammar | String | 否 | 规则语法，取值：es2（默认值）和 js。 | / |
| jsmode | String | 否 | JS 执行模式，取值： redirect：拦截模式。 bypass（默认值）：旁路模式。 | / |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "name", "argValue": "test" }, { "argName": "rule", "argValue": "if eq($uri, '/') {\n rewrite('https://example.com/index.html', 'redirect')\n}" }, { "argName": "pri", "argValue": "0" }, { "argName": "pos", "argValue": "head" }, { "argName": "enable", "argValue": "on" }, { "argName": "brk", "argValue": "off" }, { "argName": "option", "argValue": "" }], "functionName": "edge_function" }], "DomainName": "example.com" }
