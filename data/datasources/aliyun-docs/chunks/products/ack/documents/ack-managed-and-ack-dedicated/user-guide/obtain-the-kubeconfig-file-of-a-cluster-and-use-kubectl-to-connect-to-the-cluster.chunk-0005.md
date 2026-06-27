## 应用于生产环境
确保 KubeConfig 有效性：为防止 KubeConfig 过期导致集群访问中断，请及时更新。
长期 KubeConfig 有效期为3年，建议在临近过期的180天内，通过[容器服务管理控制台](https://cs.console.aliyun.com)或[DescribeClusterUserKubeconfig](../developer-reference/api-cs-2015-12-15-describeclusteruserkubeconfig.md)获取新KubeConfig。
新KubeConfig有效期仍为3年，旧 KubeConfig 在证书过期前仍然有效。
快速吊销KubeConfig：当KubeConfig疑似泄露时，应立即[吊销集群的](revoke-a-kubeconfig-credential.md)[KubeConfig](revoke-a-kubeconfig-credential.md)[凭证](revoke-a-kubeconfig-credential.md)。吊销后，系统会生成新的 KubeConfig 和授权绑定，所有基于旧KubeConfig的连接都将失效。
清理权限：在项目结束、员工离职等用户不再需要访问权限的场景中，使用“清理”功能来批量回收KubeConfig权限。清理后，系统不会生成新KubeConfig。具体操作请参见[清除](clear-kubeconfig.md)[KubeConfig](clear-kubeconfig.md)、[通过](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)[ack-ram-tool](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)[清理集群中指定用户的权限](revoke-the-permissions-of-the-specified-user-by-using-ack-ram-tool.md)。
为避免权限误删除，可[使用](using-the-kubeconfig-recycle-bin.md)[KubeConfig](using-the-kubeconfig-recycle-bin.md)[回收站](using-the-kubeconfig-recycle-bin.md)，恢复已清除的指定KubeConfig权限。
