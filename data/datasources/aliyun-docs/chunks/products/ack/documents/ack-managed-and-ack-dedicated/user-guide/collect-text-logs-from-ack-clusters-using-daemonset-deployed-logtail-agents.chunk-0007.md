### 新建ACK集群时安装Logtail组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
单击创建集群，在组件配置页面，选中使用日志服务。
本文只描述日志服务相关配置，关于更多配置项说明，请参见[创建](create-an-ack-managed-cluster-2.md)[ACK](create-an-ack-managed-cluster-2.md)[托管集群](create-an-ack-managed-cluster-2.md)。
当选中使用日志服务后，会出现创建项目（Project）的提示。
使用已有Project
可选择一个已有的Project来管理采集到的容器日志。
创建新Project
日志服务自动创建一个Project来管理采集到的容器日志。其中ClusterID为新建的Kubernetes集群的唯一标识。
重要
在组件配置页中，默认开启控制面组件日志，开启此配置会在Project中自动配置并采集集群控制面组件日志并遵循按量计费，因此请根据自身情况选择是否需要开启，相关信息请参考[管理控制面组件日志](collect-control-plane-component-logs-of-ack-managed-cluster.md)。
安装完成后，自动生成名为k8s-log-<YOUR_CLUSTER_ID>的Project，并在该Project下生成如下资源，可登录[日志服务控制台](https://sls.console.aliyun.com)查看资源。
