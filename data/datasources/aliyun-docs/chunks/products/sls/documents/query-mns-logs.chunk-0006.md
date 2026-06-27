## 查询主题消息的消息轨迹
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询语句，然后单击最近15分钟，设置查询的时间范围。
本案例要查询主题消息的消息轨迹，即输入主题名称和MessageId，查询语句格式为$TopicName and $MessageId，例如logtest and 8798453B65727FC6433E6AB4F746D4CE。
查询结果如下所示，记录了某条消息从发送到通知的过程。查询结果返回两条日志记录，其中 Action 字段分别为 PublishMessage 和 Notify，表示同一消息先被发布再被推送通知。
1 10-21 17:17:24 ... MNSLogging 1603271947 ProcessTime :1 TopicName :logtest Time :2020-10-21 17:17:24.679000 AccountId :xxx Action :PublishMessage MessageId :8798453B65727FC6433E6AB4F746D4CE RequestId :5F8FFCA4453241C3099B4BC9 RemoteAddress :xxx MessageTag : 1 10-21 17:17:24 ... MNSLogging 1603271947 ProcessTime :1 TopicName :logtest Time :2020-10-21 17:17:24.679000 AccountId :xxx Action : Notify MessageId :8798453B65727FC6433E6AB4F746D4CE RequestId :5F8FFCA4453241C3099B4BC9 RemoteAddress :xxx MessageTag :
