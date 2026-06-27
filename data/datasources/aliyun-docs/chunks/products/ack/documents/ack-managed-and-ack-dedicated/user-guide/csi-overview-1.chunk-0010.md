## 使用说明
使用CSI时需注意以下使用限制。
集群版本：需为1.14及以上。如需升级，请参见[手动升级集群](update-the-kubernetes-version-of-an-ack-cluster.md)。
集群环境：已在ACK集群中完成全面适配和验证。对于非ACK集群（非阿里环境集群、阿里云自建集群），由于配置、权限、网络等环境差异，CSI无法保证开箱即用。
建议参见[alibaba-cloud-csi-driver](https://github.com/kubernetes-sigs/alibaba-cloud-csi-driver/tree/master)源码并结合自身环境进行适配。
节点配置：kubelet运行参数--enable-controller-attach-detach为true。
操作系统：不支持Windows节点。
RBAC权限：PV是集群级别的资源，PVC是命名空间级别的资源。进行RBAC授权时，需注意不同角色对这两类资源的权限差异。
如果ACK默认提供的预置角色（管理员、运维人员等）无法满足需求，请配置自定义权限。例如，ACK默认的运维人员角色对PVC有读写权限，但对PV仅有只读权限，因此无法手动创建PV。详见[使用](grant-rbac-permissions-to-ram-users-or-ram-roles.md)[RBAC](grant-rbac-permissions-to-ram-users-or-ram-roles.md)[为集群内资源操作授权](grant-rbac-permissions-to-ram-users-or-ram-roles.md)。
