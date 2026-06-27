### 条件表达式包含的参数
最小粒度的条件表达式包含以下参数：

| 参数名称 | 域名配置功能函数 [condition](../developer-reference/parameters-for-configuring-features-for-domain-names.md) 中对应的配置参数 | 参数说明 | 是否必填 |
| --- | --- | --- | --- |
| 条件匹配 | match | 表示条件匹配表达式。 | 是 |
| 逻辑判断 | logic | 表示条件匹配表达式的逻辑判断参数，取值为 and 和 or 。 | 是 |
| 条件判断内容 | criteria | 表示条件表达式的判断内容。 | 是 |
| 匹配类型 | MatchType | 表示对用户请求中携带的某一类型信息进行匹配。 | 是 |
| 匹配对象 | MatchObject | 表示对匹配类型进行进一步的细分，例如：客户端 IP 可以细分为“建联 IP”和“XFF IP”。 | 否 |
| 匹配运算符 | MatchOperator | 表示匹配操作执行的具体动作。 | 是 |
| 匹配值 | MatchValue | 表示预先设定的匹配值，将会与用户请求中携带的信息进行匹配。 | 是 |
| 条件判断值取反 | negate | 表示是否对条件表达式的结果取反，取值为 true 和 false。 | 是 |
| 大小写敏感 | caseSensitive | 表示对匹配值中的字符是否大小写敏感。 | 否 |
| 规则条件名称 | name | 表示规则条件的名称。 | 是 |
| 生效状态 | status | 表示规则条件的生效状态。 | 是 |
