### ACK托管集群如何修改LoongCollector配置以实现跨账号或跨地域采集？
如果您通过阿里云ACK容器服务控制台安装了loongcollector，默认将采集集群容器日志到同账号的日志服务Project下。此时您可以通过以下两种方式实现集群容器日志的跨账号或跨地域采集：
方法一：卸载后重新安装。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在日志与监控页签中，找到loongcollector，单击卸载。
参考[自建集群安装（DaemonSet](loongcollector-installation-kubernetes-1.md)[模式）](loongcollector-installation-kubernetes-1.md)重新安装即可。
方法二：更新Helm配置，重新部署loongcollector。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏，选择应用>Helm。
在Helm应用管理页面，找到loongcollector，单击其右侧操作列中的更新按钮，进入更新发布页面，参考如下表格修改相关配置，其他配置保持不变，单击确定：

| 集群与 Project | 需要修改的配置 |
| --- | --- |
| 同账号，不同地域 | region ：Project 所在地域对应的 [RegionID](loongcollector-installation-kubernetes-1.md) 。 |
| net ：Internet，不同地域之间无法通过内网互通，请使用公网传输数据。 |  |
| 不同账号，同地域 | aliUid ：日志服务所属的主账号 ID，多个账号之间使用半角逗号（,）相隔。 |
| net ：Intranet，同地域建议优先使用内网传输数据。 |  |
| 不同账号，不同地域 | aliUid ：日志服务所属的主账号 ID，多个账号之间使用半角逗号（,）相隔。 |
| region ：Project 所在地域的 [RegionID](loongcollector-installation-kubernetes-1.md) 。 |  |
| net ：Internet，不同地域之间无法通过内网互通，请使用公网传输数据。 |  |
