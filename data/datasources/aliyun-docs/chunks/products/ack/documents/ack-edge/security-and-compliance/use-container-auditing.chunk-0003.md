## 步骤一：启用容器内部操作审计功能
可通过以下步骤开启容器内部操作审计功能。启用此功能后，将安装以下两个组件。
[日志采集组件](../../ack-managed-and-ack-dedicated/user-guide/collect-text-logs-from-ack-clusters-using-daemonset-deployed-logtail-agents.md)：将审计日志收集到日志服务并创建默认的审计报表。
ack-advanced-audit组件：实现容器内操作审计。
默认将在日志采集组件使用的日志Project中创建一个名为advaudit-${cluster_id}的日志库，用于保存审计日志。该日志库数据的保存时间为180天。如需修改日志保存时间，请参见[管理](../../../../sls/documents/manage-a-logstore.md)[Logstore](../../../../sls/documents/manage-a-logstore.md)。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>审计。
在审计页面单击容器审计页签，然后单击开始安装。
