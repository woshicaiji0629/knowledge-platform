,24]，小于限速结束时间，默认值为 0。 说明 表示时间点，24 小时制的整点，例如：0 表示 00:00:00，24 表示 24:00:00。 | 20 |
| ali_limit_end_hour | Integer | 否 | 限速结束时间，取值范围[0,24]，大于限速开始时间，默认值为 24。 | 23 |

配置示例一：设置单请求限速为1 MByte/s。
{ "Functions": [{ "functionArgs": [{ "argName": "ali_limit_rate", "argValue": "1m" }], "functionName": "limit_rate" }], "DomainNames": "example.com" }
配置示例二：默认情况下，单请求限速为1 MByte/s，如果用户请求URL中携带了参数rate，则会按照参数rate的实际数值来执行限速。例如：用户请求中携带了参数rate=200，则实际将会被限速为200 KByte/s。
{ "Functions": [{ "functionArgs": [{ "argName": "ali_limit_rate", "argValue": "1m" },{ "argName": "traffic_limit_arg", "argValue": "rate" },{ "argName": "traffic_limit_unit", "argValue": "k" }], "functionName": "limit_rate" }], "DomainNames": "example.com" }
