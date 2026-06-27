## 方式一：通过控制台配置Service流量拓扑
若您需要创建一个限制在本节点池内被访问的Service，只需要给Service添加注解即可。例如将名称配置为openyurt.io/topologyKeys，值配置为kubernetes.io/zone。关于创建服务的更多信息，请参见[Service](../../ack-managed-and-ack-dedicated/user-guide/service-management.md)[管理](../../ack-managed-and-ack-dedicated/user-guide/service-management.md)。
