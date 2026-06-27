### 新建ACK集群时安装Logtail组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在左侧导航栏中，单击集群列表。
在集群列表页面中，单击创建集群。
在组件配置配置项页中，选中使用日志服务。
说明
本操作仅介绍开启日志服务的关键步骤。关于创建集群的具体操作，请参见[创建](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
当选中使用日志服务后，会出现创建项目（Project）的提示。关于日志服务管理日志的组织结构，请参见[项目（Project）](project.md)。有以下两种创建Project方式。
使用已有 Project
您可以选择一个已有的Project来管理采集到的容器日志。
创建新 Project
日志服务自动创建一个Project来管理采集到的容器日志。其中ClusterID为您新建的Kubernetes集群的唯一标识。
在日志服务区域勾选使用日志服务，选择创建新 Project后，系统将自动创建名称为k8s-log-{ClusterID}的 Project。
安装完成后，在选择的Project下自动创建如下日志服务资源。
