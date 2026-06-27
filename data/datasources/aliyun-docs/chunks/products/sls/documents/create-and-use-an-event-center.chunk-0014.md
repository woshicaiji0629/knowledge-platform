### 如何查看事件对应容器的日志？
如果您使用的是阿里云Kubernetes集群，请参考如下步骤。
登录[容器服务控制台](https://cs.console.aliyun.com/)。
在集群列表页面中，单击目标集群。
在左侧导航栏中，选择工作负载>容器组。
将命名空间选择为kube-system。
在容器组列表中，单击目标容器组对应的日志。
如果您使用的是自建Kubernetes集群，请查看namespace为kube-system下文件名前缀为eventer-sls的Pod日志。
该文章对您有帮助吗？
反馈
