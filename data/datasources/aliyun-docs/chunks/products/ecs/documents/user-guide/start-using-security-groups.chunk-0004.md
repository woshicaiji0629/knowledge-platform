业务端口 | TCP | 跨安全组内网互访（如 8080、3306） | 在 目标 安全组入方向授权 源安全组 ID | [案例](security-groups-for-different-use-cases.md) [5](security-groups-for-different-use-cases.md) |

在安全组详情页，选择规则方向后单击增加规则添加规则；已有规则可在访问规则区域编辑或删除。
警告
最小权限：80/443可按需对公网开放；SSH（22）、RDP（3389）与面板端口应限定可信 IP，避免使用0.0.0.0/0或::/0。
规则优先级：同优先级下，拒绝规则优先生效。对于[部分特定网络流量](security-group-rules.md)，安全组会默认放行。
变更管理：避免直接修改生产环境的安全组，建议先[克隆安全组](start-using-security-groups.md)在测试环境验证后再调整线上规则。
单击确定创建。
API
调用[CreateSecurityGroup](../developer-reference/api-ecs-2014-05-26-createsecuritygroup.md)，创建安全组。
创建安全组后，调用以下 API 管理安全组规则：
调用[AuthorizeSecurityGroup](../developer-reference/api-ecs-2014-05-26-authorizesecuritygroup.md)，添加入方向规则。
调用[AuthorizeSecurityGroupEgress](../developer-reference/api-ecs-2014-05-26-authorizesecuritygroupegress.md)，添加出方向规则。
调用[ModifySecurityGroupRule](../developer-reference/api-ecs-2014-05-26-modifysecuritygrouprule.md)，修改入方向规则。
调用[ModifySecurityGroupEgressRule](../developer-reference/api-ecs-2014-05-26-modifysecuritygroupegressrule.md)，修改出方向规则。
调用[RevokeSecurityGroup](../developer-reference/api-ecs-2014-05-26-revokesecuritygroup.md)，删除入方向规则。
调用[RevokeSecurityGroupEgress](../developer-reference/api-ecs-2014-05-26-revokesecuritygroupegress.md)，删除出方向规则。
创建的普通安全组若未配置规则时，入方向默认会允许同安全组内其他ECS的流量，拒绝其他所有入方向流量，出方向允许所有流量。
