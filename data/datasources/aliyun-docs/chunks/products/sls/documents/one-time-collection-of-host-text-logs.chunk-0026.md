### JSON数组解析
使用json_extract[函数](json-functions.md)，从JSON数组中提取JSON对象。
效果示例：

| 未经任何处理的原始日志 | 提取 JSON 数组结构 |
| --- | --- |
| [{"key1":"value1"},{"key2":"value2"}] | json1:{"key1":"value1"} json2:{"key2":"value2"} |

配置步骤：在Logtail配置页面的处理配置区域，将处理模式切换为SPL，配置SPL语句，使用[json_extract](json-functions.md)函数从JSON数组中提取JSON对象。
示例：从日志字段content中提取 JSON 数组中的元素，并将结果分别存储在新字段json1和json2中。
* | extend json1 = json_extract(content, '$[0]'), json2 = json_extract(content, '$[1]')
