## 查询某个客户端消息处理量
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标Logstore。
输入查询语句，然后单击最近15分钟，设置查询的时间范围。
本案例要查询某个客户端消息处理量，即输入客户端IP地址，查询语句格式为$ClientIP，例如10.10.10.0。
如果您要查询某个客户端的某类操作日志，可使用多个关键字组合方式，例如$ClientIP and (SendMessage or BatchSendMessage)。
查询结果如下图所示，当前查询时段内，该客户端处理了66条消息。
该文章对您有帮助吗？
反馈
