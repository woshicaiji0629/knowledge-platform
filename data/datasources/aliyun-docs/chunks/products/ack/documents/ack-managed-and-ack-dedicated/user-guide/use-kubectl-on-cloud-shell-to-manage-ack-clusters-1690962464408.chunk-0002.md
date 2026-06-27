## Workbench
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择集群信息。
在集群信息页面，单击右上方的通过 Workbench 管理集群。
在终端界面，执行kubectl命令以验证集群的连通性。
此命令以查询命名空间为例。
kubectl get namespace
预期输出：
NAME STATUS AGE default Active 3h14m kube-node-lease Active 3h14m kube-public Active 3h14m kube-system Active 3h14m
