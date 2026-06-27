(../user-guide/create-and-manage-alb-instances.md)[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)。

| 参数 | 描述 |
| --- | --- |
| 地域 | 选择实例所属的地域。本文选择 华东 2（上海） 。 |
| 实例网络类型 | 选择实例网络类型，系统会根据您的选择分配私网或公网服务地址。本文选择 公网 。 说明 实例网络类型 选择 公网 类型只作用于 IPv4，IPv6 默认是私网类型。本文使用 IPv6 的公网类型，需执行 [步骤](implement-load-balancing-for-ipv6-services.md) [4](implement-load-balancing-for-ipv6-services.md) 变更 IPv6 的网络类型为公网类型。 |
| VPC | 选择实例所属的 VPC。 说明 请确保该 VPC 开启了 IPv6 功能。 |
| 可用区 | 选择至少 2 个可用区。本文选择 上海 可用区 E ， 上海 可用区 G 。 分别在所选可用区内选择交换机。本文选择可用区 E 下的 VSW1 和可用区 G 下的 VSW2。 |
| 协议版本 | 选择实例的 IP 协议版本。本文选择 双栈 。 |
| 功能版本（实例费） | 选择实例的功能版本。本文选择 标准版 。 |
| 实例名称 | 输入自定义实例名称。 |
| 服务关联角色 | 首次创建应用型负载均衡实例时，需要单击 创建服务关联角色 ，创建一个名称为 AliyunServiceRoleForAlb 的服务关联角色。系统会为该角色添加名称为 AliyunServiceRolePolicyForAlb 的权限策略，授予 ALB 拥有访问其他云产品实例的权限。更多操作，请参见 [负载均衡系统权限策略参考](../../security-and-compliance/application-oriented-load-balancing-system-permission-policy-reference.md) 。 |
