## 默认配置
快速购买ECS实例时，为了减少配置参数时间，部分参数由系统自动分配。默认分配的参数如下表所示。

| 参数 | 默认配置 |
| --- | --- |
| 可用区 | 系统随机分配，不能修改。 |
| 网络类型 | 默认专有网络，不能修改。更多信息，请参见 [默认专有网络和交换机](../../../vpc/documents/user-guide/default-vpcs-and-default-vswitches.md) 。 |
| 安全组 | 默认安全组，实例创建后可修改，具体操作，请参见 [为实例（主网卡）关联安全组](manage-ecs-instances-in-security-groups.md) 。 |
| 专有网络 | 默认专有网络交换机，更多信息，请参见 [默认专有网络和交换机](../../../vpc/documents/user-guide/default-vpcs-and-default-vswitches.md) 。 |
| 密码 | 无密码，您需要在实例创建成功后重置密码，具体操作，请参见 [重置实例登录密码](reset-the-logon-password-of-an-instance.md) 。 |
| 实例名称 | 系统命名，实例创建后可修改。 |
