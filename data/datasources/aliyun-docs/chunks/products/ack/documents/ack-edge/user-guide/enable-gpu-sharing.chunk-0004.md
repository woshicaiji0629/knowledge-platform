## 注意事项
针对纳入K8s集群管理的GPU节点，为业务应用申请和使用GPU资源时，请关注以下注意事项。
请勿直接在节点上运行GPU应用程序。
请勿通过docker、podman、nerdctl等工具命令创建容器并为容器申请GPU资源。例如，执行docker run --gpus all或docker run -e NVIDIA_VISIBLE_DEVICES=all并运行GPU程序。
请勿在Pod YAML的env中直接添加环境变量NVIDIA_VISIBLE_DEVICES=all或NVIDIA_VISIBLE_DEVICES=<GPU ID>等，通过容器的环境变量NVIDIA_VISIBLE_DEVICES直接为Pod申请GPU资源，并运行GPU程序。
在Pod YAML中未设置环境变量NVIDIA_VISIBLE_DEVICES，制作Pod所使用的镜像时，请勿将环境变量默认配置为NVIDIA_VISIBLE_DEVICES=all，并运行GPU程序。
请勿在Pod的securityContext中配置privileged: true，并运行GPU程序。
通过以上非标方式为业务应用申请的GPU资源，将存在如下安全隐患。
通过以上方式为业务应用申请的GPU资源，并未在调度器的设备资源账本中统计，有可能造成节点GPU资源的分配情况与调度器设备资源账本中记录的值不一致。调度器仍然会调度某些申请GPU资源的Pod到这个节点上，导致用户业务因为在同一张GPU卡上出现资源争抢（比如GPU显存申请）而运行失败的情况。
非标操作可能引发其他未知问题，例如[NVIDIA](https://github.com/NVIDIA/nvidia-docker/issues/1671)[社区的已知报错](https://github.com/NVIDIA/nvidia-docker/issues/1671)。
