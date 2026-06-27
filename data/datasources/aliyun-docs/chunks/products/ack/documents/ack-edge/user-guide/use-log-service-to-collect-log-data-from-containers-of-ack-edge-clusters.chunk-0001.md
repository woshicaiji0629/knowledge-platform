### 创建集群时启用Logtail
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面单击创建集群。
以下仅介绍开启日志服务的关键步骤。关于创建集群的具体操作，请参见[创建](create-an-ack-edge-cluster-1.md)[ACK Edge](create-an-ack-edge-cluster-1.md)[集群](create-an-ack-edge-cluster-1.md)。
在组件配置配置向导中，选中使用日志服务。
当选中使用日志服务后，会出现创建项目（Project）的提示。关于日志服务管理日志的组织结构，请参见[项目（Project）](../../../../sls/documents/project.md)。有以下两种创建Project方式。
单击使用已有 Project，选择一个现有的Project来管理采集的日志。
单击创建新 Project，自动创建一个新的Project来管理采集的日志，Project会自动命名为k8s-log-{ClusterID}，ClusterID是新建的ACK Edge集群的唯一标识。 单击创建新 Project，将自动创建名称为k8s-log-{ClusterID}的 Project。
配置完成后，单击右下角创建集群，在弹出的窗口中单击确认，完成创建。
完成创建后，可在集群列表页面看到开启了Logtail的ACK Edge集群。
