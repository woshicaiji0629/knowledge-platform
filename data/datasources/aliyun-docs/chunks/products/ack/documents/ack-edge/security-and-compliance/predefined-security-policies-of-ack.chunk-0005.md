CKPSPAppArmor | 限制在集群指定范围内部署的 Pod 配置 AppArmor。 | low |  |
| ACKPSPCapabilities | 限制在集群指定范围内部署的 Pod 配置 Linux Capabilities 能力。 | high |  |
| ACKPSPFSGroup | 限制在集群指定范围内部署的 Pod 配置 fsGroup。 | medium |  |
| ACKPSPFlexVolumes | 限制在集群指定范围内部署 Pod 的 FlexVolume 驱动配置。 | medium |  |
| ACKPSPForbiddenSysctls | 限制在集群指定范围内部署 Pod 的禁止的 Sysctl 范围。 | high |  |
| ACKPSPHostFilesystem | 限制在集群指定范围内部署的 Pod 允许挂载的主机 host 目录范围。 | high |  |
| ACKPSPHostNamespace | 限制在集群指定范围内部署的 Pod 是否允许共享主机 host 命名空间。 | high |  |
| ACKPSPHostNetworkingPorts | 限制在集群指定范围内部署的 Pod 使用主机网络和指定端口。 | high |  |
| ACKPSPPrivilegedContainer | 限制在集群指定范围内部署的 Pod 中启动特权容器。 | high |  |
| ACKPSPProcMount | 限制在集群指定范围内部署的 Pod 允许挂载的 Proc 类型。 | low |  |
| ACKPSPReadOnlyRootFilesystem | 限制在集群指定范围内部署的 Pod 使用只读的根文件系统。 | medium |  |
| ACKPSPSELinuxV2 | 限制在集群指定范围内部署的 Pod 必须使用 AllowedSELinuxOptions 参数中规定的 Selinux 配置。 | low |  |
| ACKPSPSeccomp | 限制在集群指定范围内部署的 Pod 使用指定的 Seccomp 配置文件。 | low |  |
| ACKPSPVolumeTypes | 限制在集群指定范围内部署的 Pod 使用指定的 Volume 挂载类型。 | medium |  |
| FinOps | ACKContainerRequests | 要求集群中某些应用 Pod 必须声明资源 requests 。 | low |
| ACKContainerResourcesWhitelist | 要求集群中某些应用 Pod 的 CPU 和内存资源配置必须从预设选项中选取。 | low |  |
| ACKContainerResourcesRange | 限
