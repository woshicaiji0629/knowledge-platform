## 查询队列消息消费量
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询语句，然后单击最近15分钟，设置查询的时间范围。
本案例要查询队列消息消费量，即输入队列名称和消费操作，查询语句格式为$QueueName and (ReceiveMessage or BatchReceiveMessage)，例如log and (ReceiveMessage or BatchReceiveMessage)。
查询结果显示，当前查询时段内，log队列中有12条消息被消费。执行查询后，查询结果显示共 12 条日志记录。每条原始日志包含Action（如ReceiveMessage）、QueueName（如log）、MessageId、RequestId、NextVisibleTime、ProcessTime、RemoteAddress等字段信息。
