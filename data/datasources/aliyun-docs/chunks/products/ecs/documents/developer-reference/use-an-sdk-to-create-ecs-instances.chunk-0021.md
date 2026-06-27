## 释放资源
当您不再需要所创建的资源时，可以调用以下OpenAPI接口以释放该资源。
说明
根据您的实际需求，选择相应的OpenAPI释放资源 。本示例释放上述步骤创建的所有资源。
释放ECS实例

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteInstances](../api-deleteinstances.md) | RegionId | 地域： cn-hangzhou |
| InstanceId | 实例 ID： i-bp17f3kzgtzzj91r**** |  |

删除SSH密钥对

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteKeyPairs](../api-deletekeypairs.md) | RegionId | 地域： cn-hangzhou |
| KeyPairNames | SSH 密钥对名称： ["sdk-key-pair"] |  |

删除安全组

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteSecurityGroup](api-ecs-2014-05-26-deletesecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |

删除交换机

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteVSwitch](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevswitch.md) | RegionId | 地域： cn-hangzhou |
| VSwitchId | 交换机 ID： vsw-bp1nzprm8h7mmnl8t **** |  |

删除VPC

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteVpc](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |
