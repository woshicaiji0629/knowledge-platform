## 查询主题消息发布量
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询语句，然后单击最近15分钟，设置查询的时间范围。
本案例要查询主题消息发布量，即输入主题名称和发布操作，查询语句格式为$TopicName and PublishMessage，例如logtest and PublishMessage。
查询结果显示，当前查询时段内，生产者向logtest主题发布了3条消息。执行查询后，返回3条精确匹配的日志记录，日志详情中包含TopicName（值为 logtest）、Action（值为 PublishMessage）、MessageId、RequestId、RemoteAddress等字段信息。
