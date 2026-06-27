Project列表，单击打开目标Project。
左侧导航栏中，选择资源>机器组。在打开的机器组页面中，选择机器组右侧的>创建机器组。
在创建机器组页面填写名称，机器组标识选择用户自定义标识，并在用户自定义标识中填入步骤一中参数${user_defined_id}的值，本例为user-defined-docker-1。

| 参数 | 说明 |
| --- | --- |
| 机器组 Topic | （可选） 机器组 Topic 用于区分不同服务器产生的日志数据。更多信息，请参见 [日志主题](log-topics.md) 。 |

检查机器组状态
在机器组列表中，单击目标机器组。在机器组配置页面，可查看机器组配置信息以及服务器状态。
如果心跳状态显示OK，说明配置成功，如果显示FAIL，请等待1分钟后单击刷新重试，若心跳状态仍为FAIL，请检查：
Logtail容器与Project是否同地域。
宿主机安全组是否放行Logtail出方向流量（默认端口80）。
处理操作请参见[如何排查容器日志采集异常](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
