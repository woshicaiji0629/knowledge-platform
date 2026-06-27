| RegionId | 地域： cn-hangzhou |
| KeyPairName | 密钥对名称： sdk-key-pair |  |

创建ECS实例
使用ECS您可以快速部署和运行应用程序，灵活调整资源以应对业务变化，同时享受高性能、高安全性和低成本的计算能力，适用于网站托管、应用开发、数据处理等多种场景。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [RunInstances](../api-runinstances.md) | RegionId | 地域： cn-hangzhou |
| ImageId | 镜像：推荐使用 Alibaba Cloud Linux 镜像 aliyun_3_x64_20G_scc_alibase_20220225.vhd 。 |  |
| InstanceType | 实例规格： ecs.e-c1m2.xlarge 。 |  |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| VSwitchId | 交换机 ID： vsw-bp1nzprm8h7mmnl8t **** |  |
| InstanceName | 实例名称： sdk-test |  |
| InstanceChargeType | 付费方式：实例按照按量付费的方式 PostPaid 说明 您需要确保账号余额能够完成支付。 |  |
| KeyPairName | 密钥对名称： sdk-key-pair |  |
| SystemDisk.Category | 系统盘的云盘种类： cloud_essd |  |

查询ECS实例状态
在调用RunInstances后，ECS实例需要一定的启动时间。仅当ECS实例状态达到Running时，才能通过远程连接等方式登录到实例，以进行各种操作和应用程序的部署。您可以调用该OpenAPI查询ECS实例的状态。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DescribeInstanceStatus](api-ecs-2014-05-26-describeinstancestatus.md) | RegionId | 地域： cn-hangzhou |
| InstanceId | 实例 ID 集合： ["i-bp17f3kzgtzzj91r****"] |  |
