## 事件

| 事件类型 | 事件名称 | 事件内容示例 | 事件说明 | 处理措施 |
| --- | --- | --- | --- | --- |
| Normal | SecurityInspectorConfigAuditStart | Start to running config audit | 开始执行巡检任务。 | 无需处理。 |
| Normal | SecurityInspectorConfigAuditFinished | Finished running once config audit | 巡检任务执行完成。 | 无需处理。 |
| Warning | SecurityInspectorConfigAuditHighRiskFound | 2 high risks have been found after running config audit | 巡检执行完之后，发现部分工作负载存在未修复的高风险检查项。 | 在集群的 配置巡检 页面的 巡检详情 页签，查看详细的巡检结果。 按需过滤选项中的 是否有风险 、 命名空间 和 工作负载类别 ，过滤查看有风险的工作负载。 单击 详情 ，查看该工作负载中每个检查项的检查结果。 对于确认无需修复的检查项，单击 加白名单 ，将该检查项加入白名单。 对于确认需要修复的检查项，单击 详情 ，参考加固建议进行修复。 |
