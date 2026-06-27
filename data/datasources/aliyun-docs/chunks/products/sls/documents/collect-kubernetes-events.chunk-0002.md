### 阿里云Kubernetes
如果是ACK集群，则对应阿里云Kubernetes组件中的ack-node-problem-detector组件已集成eventer和node-problem-detector功能，您只需要部署该组件。更多信息，请参见[事件监控](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md)。如果是ACK Serverless集群，您需要部署kube-eventer组件。
NPD根据配置与第三方插件检测节点的问题或故障并生成相应的集群事件。而Kubernetes集群自身也会因为集群状态的切换产生各种事件，例如Pod驱逐、镜像拉取失败等异常情况。日志服务SLS（Log Service）的Kubernetes事件中心实时汇聚Kubernetes中的所有事件并提供存储、查询、分析、可视化、告警等能力。将集群事件接入日志服务的Kubernetes事件中心操作步骤如下：
如果在创建集群时，已选中安装node-problem-detector并创建事件中心，可直接按照[步骤二](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/event-monitoring.md)查看Kubernetes事件中心。关于如何通过创建集群时安装NPD组件，请参见[创建](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
若创建集群时未选中安装node-problem-detector并创建事件中心，则需手动安装，具体的操作步骤如下。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择运维管理>组件管理。
在日志与监控页签，查找并安装ack-node-problem-detector。
