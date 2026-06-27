### 为已有节点池开启
开启或关闭节点池容器镜像加速开关后，仅对新增节点生效。如需针对存量节点生效，需要将节点移除出节点池后，重新添加回节点池，相关操作，请参见[移除节点](../../ack-managed-and-ack-dedicated/user-guide/remove-a-node-11.md)并[添加已有节点](../../ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster.md)。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池列表页面，单击目标节点池所在行操作列的编辑，在高级选项中，勾选容器镜像加速，按照页面提示更新节点池的配置项。
在节点池列表，如果节点池状态显示更新中，表明节点池正在变更中。显示已激活，表明变更已完成。
