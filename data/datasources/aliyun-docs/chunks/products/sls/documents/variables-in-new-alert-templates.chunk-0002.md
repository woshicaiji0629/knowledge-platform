e | 首次触发时间。 | int | 1616059834 | 告警首次触发时间为 {{ alert.fire_time }} ，格式化显示为 {{ alert.fire_time | format_date }} 。 |
| status | 告警状态。 firing：触发告警。 resolved：恢复通知。 | string | firing | 告警状态为 {{ alert.status }} ，格式化显示为 {{ alert.status | format_status }} 。 |
| resolve_time | 告警恢复时间。 如果告警状态是 firing，取值为 0。 如果告警状态是 resolved，取值为具体恢复时间。 | int | 0 | 告警恢复的时间为 {{ alert.resolve_time }} ，格式化显示为 {{ alert.resolve_time | format_date }} 。 |
| severity | 告警严重度。 10：严重 8：高 6：中 4：低 2：仅报告 | int | 10 | 告警严重度为 {{ alert.severity }} ，格式化显示为 {{ alert.severity | format_severity }} 。 |
| labels | 标签列表。 | map | {"env":"test"} | 告警标签为 {{ alert.labels | to_list }} |
| annotations | 标注列表。 | map | { "title": "告警标题","desc": "告警描述" } | 告警标注为 {{ alert.annotations | to_list }} 。 |
| results | 查询参数和中间结果，数组类型。变量取值说明，请参见 [QueryData](variables-in-new-alert-templates.md) [结构](variables-in-new-alert-templates.md) 。 | array | 参见本文末尾附录。 | 第一个查询的开始时间为 {{ alert.results[0].start_time }} ；结束时间为 {{ alert.results[0].end_time }} ；count 的值为 {{ alert.results[0].fire_result.cnt }} ；查询和分析语句为 {{ alert.results[0].query }} 。 |
| fire_results | 触发告警的数据，即集合操作后的数据，最多 100 条。 fire_results 变量值超过 2KB，并且查询结果字段内容的长度超过 1KB 时，超出部分会被截断。数据被截断处理方式请参见 [触发告警的日志太
