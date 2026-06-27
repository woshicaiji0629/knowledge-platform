### 使用过alicloud_cs_kubernetes_autoscaler组件
如果您的集群之前已经使用alicloud_cs_kubernetes_autoscaler组件，在完成上述为当前集群添加弹性伸缩服务授权后，您需要执行以下步骤平滑切换alicloud_cs_kubernetes_autoscaler至alicloud_cs_kubernetes_node_pool，以创建开启自动伸缩功能的节点池。
修改集群的autoscaler-meta配置项。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择配置管理>配置项。
在配置项页面左上角的命名空间下拉框中，选择kube-system，然后在autoscaler-meta配置项右侧操作列下，单击编辑。
在编辑面板中，修改autoscaler-meta配置项的值。
您需将taints值的String类型改成数组类型，即在值文本框中，修改"taints":""为"taints":[]。
单击确定。
同步节点池。
在集群管理页左侧导航栏，选择节点管理>节点池。
在节点池页面右上方，单击同步节点池。
