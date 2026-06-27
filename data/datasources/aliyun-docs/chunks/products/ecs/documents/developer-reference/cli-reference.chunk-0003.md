## 创建ECS实例
创建ECS实例时，有很多必填参数，包括交换机ID、安全组、镜像等。您可以传入已经准备好的资源ID，或者调用以下OpenAPI创建对应资源。
创建VPC。
VPC是一种专有的云上私有网络，允许用户在公共云上配置和管理一个逻辑隔离的网络区域。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateVpc](../../../vpc/documents/api-createvpc.md) | RegionId | 地域： cn-hangzhou |
| CidrBlock | VPC 网段： 192.168.0.0/16 |  |

创建交换机。
交换机是一种在虚拟化环境中使用的网络交换设备，它模拟了物理交换机的功能，使虚拟机（VMs）之间以及虚拟机与物理网络之间可以进行通信。

| API | 参数 | 示例取值 |
| --- | --- | --- |
|  | RegionId | 地域： cn-hangzhou |
| [CreateVSwitch](../../../vpc/documents/api-createvswitch.md) | ZoneId | 可用区： cn-hangzhou-i |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3**** |  |
| CidrBlock | 交换机网段： 192.168.0.0/24 |  |

创建安全组。
安全组是一种虚拟防火墙，能够控制ECS实例的出入方向流量。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateSecurityGroup](../api-createsecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |

给安全组添加入防护规则。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [AuthorizeSecurityGroup](../api-authorizesecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| IpProtocol | 协议： tcp |  |
| SourceCidrIp | 源 CIDR： 0.0.0.0/0 |  |
| PortRange | 端口范围： Linux 实例： 22/22 Windows 实例： 3389/3389 |  |
