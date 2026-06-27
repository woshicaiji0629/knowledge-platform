## 配置访问云产品内网Endpoint
ack-kubernetes-webhook-injector默认使用云产品公网Endpoint。如果您的集群未开启公网访问能力，可以通过修改配置，选择访问云产品内网Endpoint。
说明
部分云产品在特定地域没有内网Endpoint。配置前，请在[OpenAPI](https://next.api.aliyun.com/home)[门户](https://next.api.aliyun.com/home)查询目标产品的地域下是否提供内网Endpoint。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。
在页面顶部命名空间下拉列表中，选择kube-system命名空间，找到kubernetes-webhook-injector对应的Deployment，然后单击目标Deployment右侧操作列下的更多 > 查看Yaml。
在spec.template.spec.containers.command下方增加- '--intranet-access'一行，然后单击更新。
