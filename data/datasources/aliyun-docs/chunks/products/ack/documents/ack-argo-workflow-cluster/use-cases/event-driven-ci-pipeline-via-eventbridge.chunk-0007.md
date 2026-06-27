- name: repo_url value: https://github.com/ivan-cai/echo-server.git - name: repo_name value: echo-server - name: target_branch value: release-v1 - name: container_image value: "YOUR-IMAGE-REGISTRY-ADDRESS" # 容器镜像库的地址，请根据您的实际信息替换. - name: container_tag value: "v1.0.0" - name: dockerfile value: ./Dockerfile - name: enable_suffix_commitid value: "true" - name: enable_test value: "true" workflowTemplateRef: name: ci-go-v1 clusterScope: true
网络访问：推荐使用专有网络，选择工作流集群的VPC，交换机和安全组。
根据上述配置，当您在GitHub仓库的release-v1分支上进行代码修改并提交时，该操作会触发自动化流程，您可以通过以下方式验证。
查看事件轨迹。
- 登录[事件总线](https://eventbridge.console.aliyun.com/)[EventBridge](https://eventbridge.console.aliyun.com/)[控制台](https://eventbridge.console.aliyun.com/)，在左侧导航栏，单击事件总线。
单击对应事件总线名称，在左侧导航栏，单击事件追踪。
进入事件追踪页面，可查看对应事件轨迹。
事件轨迹详情中，事件 ID 为b91299ae-355d-4f66-ac53-8d84e5d84b97，事件类型为eventbridge:Events:HTTPEvent，总线名称为ci-test，事件源为github.event。在事件投递区域，规则ttt成功将事件投递至目标https://8.217.97.153:6443，投递状态为成功，投递耗时 59 毫秒，投递响应为[200]NoMessage。
查看新建的Workflow的执行拓扑。
在工作流集群查看新建的Workflow的执行拓扑。具体操作，请参见[开启](../../distributed-cloud-container-platform-for-kubernetes/user-guide/enable-argo-server-for-a-workflow-cluster.md)[Argo Server](../../distributed-cloud-container-platform-
