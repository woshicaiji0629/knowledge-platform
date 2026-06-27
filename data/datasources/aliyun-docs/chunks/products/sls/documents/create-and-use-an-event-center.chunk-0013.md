### K8s事件中心实例无数据
部署好K8s事件中心后，新产生的事件会自动采集到K8s事件中心，您可以在自定义查询页面进行搜索（建议将右上角时间范围调整到1天）。如果无数据，一般有两个原因：
部署K8s事件中心后，K8s集群还未产生事件。
您可以通过kubectl get events --all-namespaces命令检查集群内是否有新事件产生。
部署eventer和node-problem-detector时，参数填写错误。
如果您使用的是阿里云Kubernetes集群，请参考如下步骤。
登录[容器服务控制台](https://cs.console.aliyun.com/)。
在集群列表页面中，单击目标集群。
在左侧导航栏中，选择应用>Helm。
在Helm页面中，单击ack-node-problem-detector后的更新。
检查并修改参数配置。更多信息，请参见[步骤一：部署](create-and-use-an-event-center.md)[eventer](create-and-use-an-event-center.md)[和](create-and-use-an-event-center.md)[node-problem-detector](create-and-use-an-event-center.md)。
如果您使用的是自建Kubernetes集群，参数配置请参见[采集](collect-kubernetes-events.md)[Kubernetes](collect-kubernetes-events.md)[事件](collect-kubernetes-events.md)。
