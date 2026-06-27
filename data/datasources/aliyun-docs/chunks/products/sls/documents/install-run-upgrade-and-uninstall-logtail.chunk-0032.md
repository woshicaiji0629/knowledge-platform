te-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [RAM](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [用户及授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) 。 |  |
| AccessKeySercret Project 所属账号的阿里云账号的 AccessKey Secret。推荐使用 RAM 用户的 AccessKey 并授予 RAM 用户 AliyunLogFullAccess 权限。相关操作，请参见 [创建](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [RAM](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) [用户及授权](create-a-ram-user-and-authorize-the-ram-user-to-access-log-service.md) 。 |  |
| ClusterID 自定义集群 ID，命名只支持大小写字母、数字、短划线(-)。该参数对应后面操作中的 ${your_k8s_cluster_id} 。不同的 Kubernetes 集群，请勿配置相同的集群 ID。 |  |
| SlsMonitoring 是否开启集群指标数据采集的开关，可选项： true（默认值）：开启。 false：不开启。 |  |
| Net Logtail 传输数据时的网络类型，若您的集群未打通阿里云内网访问，请使用公网。可选项： Internet（默认值）：公网。 Intranet：内网。 |  |
| SLS_CONTAINERD_USED 设定容器运行时是否为 containerd，可选项： true：是。 false（默认值）：否。 在使用 containerd 作为容器运行时的自建 Kubernetes 集群中，若未开启相关参数，可能导致日志无法被 Logtail 采集。 |  |
