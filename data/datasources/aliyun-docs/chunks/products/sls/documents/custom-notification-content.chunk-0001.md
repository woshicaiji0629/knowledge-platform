## 新旧版内容模板对比
新版告警支持两个版本的内容模板语法。相对于旧版的内容模板语法，新版提供更加灵活且高级的自定义渲染逻辑。

| 功能 | 新版 | 旧版 |
| --- | --- | --- |
| 引用方式 | 普通字段： {{ alert.project }} 嵌套字段： {{ alert.policy.alert_policy_id }} 数组元素： {{ alert.results[0] }} 数组元素字段： {{ alert.results[0].query }} | 普通字段： ${project} 嵌套字段： ${policy.alert_policy_id} 数组元素： ${results[0]} 数组元素字段： ${results[0].query} |
| 模板变量 | 内容和样式分离。由告警变量提供内容，通过控制流和函数实现多样化的样式。更多信息，请参见 [内容模板变量说明（新版）](variables-in-new-alert-templates.md) ）。 | 内容和样式不分离，都由告警变量提供。更多信息，请参见 [内容模板变量说明（旧版）](variables-in-original-alert-templates.md) 。 |
| 控制流（条件判断、迭代等） | 支持。更多信息，请参见 [内容模板语法（新版）](syntax-for-new-alert-templates.md) 。 | 不支持。 |
| 过滤器处理 | 支持。更多信息，请参见 [内置模板函数](built-in-functions-in-alert-templates.md) 。 | 不支持。 |
