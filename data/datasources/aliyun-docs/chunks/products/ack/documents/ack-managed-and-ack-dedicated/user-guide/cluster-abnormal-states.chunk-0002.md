| 状态码 | 异常状态 | 解决方案 |
| --- | --- | --- |
| KMSUnhealthy | 集群开启了使用阿里云密钥管理服务 KMS 进行 Secret 的落盘加密功能，且由于阿里云账号欠费或其他原因导致 KMS 服务暂停，使得集群控制面无法正常运行。 | 登录 [密钥管理服务控制台](https://kms.console.aliyun.com) 。 查看 KMS 服务暂停的原因，并恢复 KMS 服务。 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系技术支持人员恢复集群状态。 |
| NoNodeForLongTime | ACK 托管集群基础版 中没有节点，且集群中连续 14 天没有节点。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 恢复集群的状态，恢复后将集群升级为 ACK 托管集群 Pro 版 。 |
| AssumeRoleNotFound | 系统无法找到 容器服务 Kubernetes 版 的服务角色，导致集群控制面异常。 | 参见 [容器服务](ack-default-roles.md) [ACK](ack-default-roles.md) [服务角色](ack-default-roles.md) 排查 容器服务 Kubernetes 版 所需的角色。 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) ，联系技术支持人员恢复集群状态。 |
| AssumeUserNotFound | 系统无法找到 容器服务 Kubernetes 版 对应的 RAM 用户，导致集群控制面异常。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 获取技术支持。 |
| SecurityGroupNotFound | 系统无法找到 容器服务 Kubernetes 版 的安全组，导致集群控制面异常。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 获取技术支持。 |
| UnderMaintenance | 集群控制面处于后台维护中。 | [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 获取技术支持。 |
| ServiceInDebt | 当账号可用额度（含阿里云账户余额和代金券）小于待结算的账单时，会被判断为账号欠费。欠
