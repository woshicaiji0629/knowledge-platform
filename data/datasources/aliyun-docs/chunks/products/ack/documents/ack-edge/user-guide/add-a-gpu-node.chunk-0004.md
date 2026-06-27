登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，选择目标节点池右侧操作列的> 添加已有节点。
进入添加节点页面，单击手动添加，添加现有实例。
单击下一步进入实例信息页面，您可以在此处填写节点接入配置，具体的配置参数，请参见[参数列表](add-an-edge-node.md)。
{ "gpuVersion": "Nvidia_Tesla_T4", "enableIptables": true, "quiet": true, "manageRuntime": true, "allowedClusterAddons": [ "kube-proxy", "flannel", "coredns" ] }
说明
生成节点接入脚本时，需配置gpuVersion参数。当前支持的GPU版本如下请参见[使用限制](add-a-gpu-node.md)。
该参数配置完成后，接入工具会自动安装nvidia-containerd-runtime，关于nvidia-containerd-runtime更多信息，请参见[nvidia-containerd-runtime](https://developer.nvidia.com/nvidia-container-runtime)。
配置完成后单击下一步，进入添加完成页面，单击复制，到您的边缘节点上粘贴并执行该脚本。
添加节点成功的结果如下所示。
I0410 10:54:25.801554 19419 join-node.go:241] [join-node] Config the kubelet service configuration successfully. I0410 10:54:25.801590 19419 join-node.go:246] [join-node] Adding edge hub static yaml I0410 10:54:25.801662 19419 join-node.go:279] [join-node] Add edge hub static yaml is ok I0410 10:54:25.801666 19419 join-node.go:384] [join-node] Start to joining node to cluster. I0410 10:54:27.338166 19419 join-node.go:393] [join-node] Join node to cluster successfully. I0410 10:54:27.338214 19419 install.go:151] [install-
