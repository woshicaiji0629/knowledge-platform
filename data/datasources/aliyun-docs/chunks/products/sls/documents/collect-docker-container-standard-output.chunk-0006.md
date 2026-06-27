## 步骤二：创建Logtail采集配置
在日志存储>日志库页签中，单击目标Logstore。
展开LogStore菜单栏，单击Logtail配置，然后单击添加Logtail配置。
在快速数据接入页面，单击Docker标准输出-旧版。
由于步骤一创建了机器组，此处请单击使用现有机器组。
在机器组配置步骤中，选择步骤一中创建的机器组，单击>添加机器组到应用机器组中，并单击下一步。
在Logtail配置步骤中，输入配置名称，单击下一步。
在查询分析配置步骤中，单击刷新，可预览采集到的日志。若无日志，请确认容器是否持续产生标准输出日志，一般来说，标准输出默认在/var/lib/docker/containers/容器ID/容器ID-json.log中。若确认后仍无预览日志，请查看[如何排查容器日志采集异常](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
