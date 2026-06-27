## 查询队列消息发送量
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询语句，然后单击最近15分钟，设置查询的时间范围。
本案例要查询队列消息发送量，即输入队列名称和发送操作，查询语句格式为$QueueName and (SendMessage or BatchSendMessage)，例如log and (SendMessage or BatchSendMessage)。
查询结果显示，当前查询时段内，生产者向log队列发送了3条队列消息。执行该查询语句后，查询结果显示结果精确，日志条数为 3。每条日志记录包含Action（如SendMessage，红色高亮）、QueueName、Time、MessageId、RequestId、RemoteAddress等字段信息。
