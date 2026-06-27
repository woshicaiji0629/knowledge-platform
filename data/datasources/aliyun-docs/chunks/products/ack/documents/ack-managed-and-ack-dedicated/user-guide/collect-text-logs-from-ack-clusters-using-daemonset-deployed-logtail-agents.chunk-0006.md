### 已有的ACK集群中安装Logtail组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在日志与监控页签中，找到logtail-ds，然后单击安装。如未找到logtail-ds组件，请[安装](../../../../sls/documents/collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md)[LoongCollector](../../../../sls/documents/collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md)[组件](../../../../sls/documents/collect-text-logs-of-the-ack-cluster-deploy-loongcollector-in-the-daemonset-mode.md)。
LoongCollector组件为logtail-ds组件的升级版，两个组件不能同时存在，推荐使用LoongCollector组件。
