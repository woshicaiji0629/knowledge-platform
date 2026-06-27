### 函数
内置模板函数便于您对数据进行各种操作，丰富了通知内容的格式和展示样式。更多信息，请参见[内置模板函数](built-in-functions-in-alert-templates.md)。
例如您要通过Webhook方式发送JSON格式的内容，相关信息如下：
告警的查询语句（包含一个换行）
* | select count(*) as cnt
不同使用方式的对比说明

| 对比项 | 内容模板 | 结果 | 说明 |
| --- | --- | --- | --- |
| 不使用函数 | { "query": "{{ alert.results[0].query }}" } | { "query": "* | select count(*) as pv" } | JSON 格式不合法 |
| 使用 quote 函数 | { "query": {{ quote(alert.results[0].query) }} } | { "query": "* | \nselect count(*) as pv" } | JSON 格式合法 |
