",\"negate\":false}]},\"name\":\"example\",\"status\":\"enable\"} 实现效果： 规则名称：example 状态：enable 逻辑判断：and 条件表达式：客户端建联 IP 的协议版本等于 v6 |

条件表达式的格式（即argValue的格式）说明如下：

| 参数 | 说明 |
| --- | --- |
| \"match\": | match 表示条件匹配表达式。 |
| \"logic\":\"and\" | logic 表示条件匹配表达式的逻辑判断参数，取值为 and 和 or。 |
| \"criteria\" | criteria 表示条件表达式的判断内容。 |
| \"matchType\":\"clientipVer\" | matchType 表示对用户请求中携带的某一类型信息进行匹配。 |
| \"matchObject\":\"CONNECTING_IP\" | matchObject 表示对匹配类型进行进一步的细分，例如：客户端 IP 可以进一步细分为“建联 IP”和“XFF IP”。 |
| \"matchOperator\":\"equals\" | matchOperator 表示匹配操作执行的具体动作。 |
| \"matchValue\":\"v6\" | matchValue 表示预先设定的匹配值，将会与用户请求中携带的信息进行匹配。 |
| \"negate\":false | negate 表示是否对条件表达式的结果取反，取值为 true 和 false。 |
| \"name\":\"example\" | name 表示规则条件的名称。 |
| \"status\":\"enable\" | status 表示规则条件的生效状态。 |
