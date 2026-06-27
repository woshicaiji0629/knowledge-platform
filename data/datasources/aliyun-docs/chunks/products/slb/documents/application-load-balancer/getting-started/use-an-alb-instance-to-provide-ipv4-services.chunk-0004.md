## 步骤一：创建ALB实例
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在实例页面，单击创建应用型负载均衡。
在应用型负载均衡（按量付费）购买页面，根据需要配置实例。
此处仅列出和本文强相关的配置项，其他未列出的配置项使用默认值。关于参数的更多信息，请参见[创建和管理](../user-guide/create-and-manage-alb-instances.md)[ALB](../user-guide/create-and-manage-alb-instances.md)[实例](../user-guide/create-and-manage-alb-instances.md)。

| 配置 | 说明 |
| --- | --- |
| 地域 | 选择实例所属的地域。本文选择 华东 2（上海） 。 |
| 实例网络类型 | 选择实例网络类型，系统会根据您的选择分配私网或公网服务地址。本文选择 公网 。 |
| VPC | 选择实例所属的 VPC。 |
| 可用区 | 至少选择 2 个可用区。本文选择 上海 可用区 E 及该可用区下的交换机 VSW1， 上海 可用区 G 及该可用区下的交换机 VSW2。 |
| 协议版本 | 选择实例的协议版本。本文选择 IPv4 。 |
| 功能版本（实例费） | 选择实例的功能版本，本文选择 标准版 。 |
| 实例名称 | 输入自定义实例名称。 |
| 服务关联角色 | 首次创建应用型负载均衡实例时，需要单击 创建服务关联角色 ，创建一个名称为 AliyunServiceRoleForAlb 的服务关联角色。系统会为该角色添加名称为 AliyunServiceRolePolicyForAlb 的权限策略，授予 ALB 拥有访问其他云产品实例的权限。更多操作，请参见 [负载均衡系统权限策略参考](../../security-and-compliance/application-oriented-load-balancing-system-permission-policy-reference.md) 。 |

单击立即购买，根据控制台提示完成实例开通。
返回实例页面，选择对应的地域即可看到新建的实例。
