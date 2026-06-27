### 1. 选择KubeConfig类型
KubeConfig包含访问集群所需的认证信息，请根据安全需求和使用场景选择KubeConfig类型。
重要
根据[安全责任共担模型](../security-and-compliance/shared-responsibility-model.md)，KubeConfig凭证需自行负责和维护，请谨慎维护其合理性和有效性，定期轮换KubeConfig并遵循最小化权限策略，避免KubeConfig泄露带来的安全风险。
根据KubeConfig有效期：
临时KubeConfig：支持配置KubeConfig有效期（30分钟～3天），过期后自动失效，以降低KubeConfig泄露的安全风险。适用于日常运维、故障排查、CI/CD流水线等无需长期连接API Server的场景。
长期KubeConfig：默认有效期为3年，适用于无法频繁更新KubeConfig的自动化系统或长期监控服务。
根据访问集群的方式：
内网访问：获取内网访问的KubeConfig，此时kubectl客户端机器必须与集群位于同一VPC。通过阿里云内网连接时，延迟更低，更安全。
公网访问：获取公网访问的KubeConfig，通过公网中的任意机器作为客户端来连接集群。依赖[EIP](../../../../eip/documents/product-overview/what-is-eip.md)连接 API Server，适用于本地开发或远程运维。
EIP 绑定后，相关费用请参见[按量付费](../../../../eip/documents/pay-as-you-go.md)。
如使用ACK专有集群且已开启公网访问，可通过 SSH 从 Master 节点获取 KubeConfig 后在本地使用 kubectl 管理集群。详情请参见[通过](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[SSH](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[连接](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[ACK](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[专有版集群的](use-ssh-to-connect-to-the-master-nodes-of-a-dedicated-kubernetes-cluster.md)[Master]
