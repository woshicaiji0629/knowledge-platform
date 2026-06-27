| 参数 | 示例取值 |
| --- | --- |
| RegionId | 地域： cn-hangzhou |
| ImageId | 镜像：推荐使用 Alibaba Cloud Linux 镜像 aliyun_3_x64_20G_alibase_20240528.vhd 。 |
| InstanceType | 实例规格： 个人应用：推荐选择 2 vCPU 2 GiB 的实例规格 ecs.e-c1m1.large 。 中小企业应用：推荐选择 2 vCPU 4 GiB 的实例规格 ecs.c7.large 。 |
| SecurityGroupId | 安全组 ID：根据 [CreateSecurityGroup](../api-createsecuritygroup.md) 返回结果。 示例： sg-bp18z2q1jg4gq95t**** |
| VSwitchId | 交换机 ID：根据 [CreateVSwitch](../../../vpc/documents/api-createvswitch.md) 返回结果。 示例： vsw-bp11hf5r945gewysp**** |
| InstanceName | 实例名称。 示例： ecs_cli_demo |
| InstanceChargeType | 付费方式：实例按照包年包月的付费方式 PrePaid 。 说明 您需要确保账号余额能够完成支付。 |
| PeriodUnit | 付费周期单位： Month |
| Period | 付费时长： 1 |
| InternetMaxBandwidthOut | 公网 IP 带宽： 1 |
| Password | 实例登录密码： <yourPassword> 说明 您需要自定义复杂密码以保护 ECS 实例的安全。 |
| SystemDisk.Category | 系统盘类型：cloud_essd |
| SystemDisk.Size | 系统盘大小：40 |
