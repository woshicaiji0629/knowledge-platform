## 步骤二：安装ack-kserve组件
ack-kserve组件默认采用RawDeployment模式部署，并与Nginx Ingress Controller组件集成。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择应用>Helm。
单击左上方创建，在基本信息页面填写应用名，在Chart区域搜索选中ack-kserve，然后单击下一步。
在参数配置页面，确认Chart 版本和参数信息后，单击确定。
部署成功后，可以在Helm页面查看ack-kserve的Helm组件信息。
修改kserve中inferenceservice-config配置项。
在Helm页面，单击kserve，然后单击inferenceservice-config，单击YAML 编辑，修改YAML文件中的ingressClassName字段，使其与[安装](edge-cluster-ingress-overview.md)[Nginx Ingress Controller](edge-cluster-ingress-overview.md)时指定的ingressClassResource.name一致。
校验ack-kserve是否运行。
执行以下命令，查看Pod运行状态。
kubectl get pod -n kserve
如果预期输出的STATUS为running状态，表明ack-kserve组件已经安装成功。
