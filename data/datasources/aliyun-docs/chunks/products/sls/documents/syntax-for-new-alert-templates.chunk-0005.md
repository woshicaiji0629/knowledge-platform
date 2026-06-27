### 条件语句
条件判断支持对参数或者逻辑比较表达式进行判断。通过条件判断，可以进行动态渲染。
如果if后面传入的是常量或者普通变量，则对该值进行真值判断。其中布尔值false、数字0、空字符串""、空值null、空数组[]、空对象{}都会被判定为假，其它值被判定为真。
如果if后面传入的是逻辑比较表达式，则按照比较结果进行判断。例如{{ if alert.severity >= 8 }}用于判断告警严重度是否大于等于8。
条件判断支持如下几种形式：

| 使用方式 | 示例 |
| --- | --- |
| if | {% if alert.severity >= 8 %} 严重告警 {% endif %} |
| if-else | {% if alert.severity >= 8 %} 严重告警 {% else %} 普通告警 {% endif %} |
| if-elif | {% if alert.severity >= 8 %} 严重告警 {% elif alert.severity >= 4 %} 普通告警 {% endif %} |
| if-elif-else | {% if alert.severity >= 8 %} 严重告警 {% elif alert.severity >= 4 %} 普通告警 {% else %} 通知 {% endif %} |
| 嵌套使用 | {% if alert.severity >= 8 %} 严重告警 {% else %} {% if alert.severity >= 4 %} 普通告警 {% else %} 通知 {% endif %} {% endif %} |
