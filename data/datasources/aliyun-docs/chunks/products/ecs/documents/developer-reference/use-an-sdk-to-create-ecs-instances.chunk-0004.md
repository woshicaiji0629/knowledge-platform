## 创建ECS实例
创建ECS实例时有很多必填参数，包括交换机ID、安全组、镜像等。您可以传入已经准备好的资源ID，或者调用以下OpenAPI创建对应资源。
创建VPC
VPC是一种专有的云上私有网络，允许用户在公共云上配置和管理一个逻辑隔离的网络区域。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateVpc](../../../vpc/documents/api-createvpc.md) | RegionId | 地域： cn-hangzhou |
| CidrBlock | VPC 网段： 192.168.0.0/16 |  |

查询VPC信息
在调用CreateVpc之后，VPC需要一段配置时间，您可以调用该OpenAPI查询VPC的状态。当VPC的状态处于Available（可用）时，请再调用后续OpenAPI。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DescribeVpcs](../../../vpc/documents/api-describevpcs.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC 的 ID： vpc-bp1aag0sb9s4i92i3**** |  |

创建交换机
交换机是一种在虚拟化环境中使用的网络交换设备，它模拟了物理交换机的功能，使虚拟机（VMs）之间以及虚拟机与物理网络之间可以进行通信。

| API | 参数 | 示例取值 |
| --- | --- | --- |
|  | RegionId | 地域： cn-hangzhou |
| [CreateVSwitch](../../../vpc/documents/api-createvswitch.md) | ZoneId | 可用区： cn-hangzhou-i |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3**** |  |
| CidrBlock | 交换机网段： 192.168.0.0/24 |  |

创建安全组
安全组是一种虚拟防火墙，能够控制ECS实例的出入方向流量。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateSecurityGroup](../api-createsecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |

给安全组添加防护规则
