## 查询队列消息删除量
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询语句，然后单击最近15分钟，设置查询的时间范围。
本案例要查询队列消息删除量，即输入队列名称和删除操作，查询语句格式为$QueueName and (DeleteMessage or BatchDeleteMessage)，例如log and (DeleteMessage or BatchDeleteMessage)。
当前查询时段内，61条log队列消息被删除。执行查询后，在查询结果区域查看日志条数，该数值即为队列消息删除量。
