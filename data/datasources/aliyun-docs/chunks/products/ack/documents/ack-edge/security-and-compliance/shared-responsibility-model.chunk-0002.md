## 客户负责
客户的安全管理运维人员需要负责部署在云上的业务应用安全防护以及对云上资源的安全配置和更新，包含以下内容：
基于阿里云公告和提供的补丁或版本升级方式及时进行OS、集群侧系统组件、运行时等漏洞的修复和版本更新。
遵循安全原则进行ACK集群、节点池和网络等参数配置，避免因为不当的参数或权限配置给攻击者可乘之机。
基于使用需求，遵循权限最小化原则进行应用或账号、角色的授权，凭据的管理，相关安全策略的部署实施以及应用自身参数配置安全。
负责应用制品的供应链安全。
负责应用敏感数据和应用运行时刻的安全。
对于离职员工或非受信人员，删除RAM用户或RAM角色并不会同步删除该用户或角色拥有的集群KubeConfig中的RBAC权限。因此，在删除RAM用户或RAM角色之前，请吊销离职员工或非受信用户的KubeConfig权限。具体操作，请参见[吊销集群的](../../ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)[KubeConfig](../../ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)[凭证](../../ack-managed-and-ack-dedicated/user-guide/revoke-a-kubeconfig-credential.md)。
针对容器服务ACK Edge集群，负责边缘节点稳定性和OS层面安全漏洞的修复和版本更新。
