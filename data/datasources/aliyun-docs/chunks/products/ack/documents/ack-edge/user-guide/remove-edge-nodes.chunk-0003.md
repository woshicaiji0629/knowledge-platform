## 边缘节点池
在节点池页面，单击目标边缘节点池名称。
在基本信息页签最下方，选中目标节点，单击移除节点。
在移除节点面板，仔细阅读注意事项之后，选中我已了解上述说明，确认移除节点。然后单击确定。
边缘型节点池不支持同时释放ECS和自动排空节点。
移除边缘节点之后，为确保边缘节点上的K8s组件被清理。您需要在边缘节点上，使用边缘节点接入工具Edgeadm的Reset子命令重置节点，命令如下。
wget http://aliacs-k8s-[region].oss-[region].aliyuncs.com/public/pkg/run/attach/[clusterVersion]/[arch]/edgeadm -O edgeadm; chmod u+x edgeadm; ./edgeadm reset

| 参数 | 说明 | 示例 |
| --- | --- | --- |
| region | 集群地域。 | cn-hangzhou |
| clusterVersion | 集群版本。 | 1.22.15-aliyunedge.1 |
| arch | 边缘节点的 CPU 架构。 | amd64 |
