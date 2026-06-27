## 查询队列消息的消息轨迹
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询语句，然后单击最近15分钟，设置查询的时间范围。
本案例要查询队列消息的消息轨迹，即输入队列名称和消息ID，格式为$QueueName and $MessageId，例如log and EED287A265726135146E6A9CADC880FA。
查询结果记录了某条消息从发送到接收的过程。查询结果显示两条 MNSLogging 日志记录，MessageId 均为EED287A265726135146E6A9CADC880FA。其中一条记录的 Action 为SendMessage（时间 2020-10-21 16:50:53），另一条的 Action 为ReceiveMessage（时间 2020-10-21 16:50:57），表明该消息在队列sgw-express-sync-queue-gw-0008q1m4pv7qjse4na31-5796中完成了发送和接收的完整轨迹。
