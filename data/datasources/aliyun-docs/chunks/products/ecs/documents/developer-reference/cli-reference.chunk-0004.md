sg-bp1esyhwfbqeyudt **** |  |
| IpProtocol | 协议： tcp |  |
| SourceCidrIp | 源 CIDR： 0.0.0.0/0 |  |
| PortRange | 端口范围： Linux 实例： 22/22 Windows 实例： 3389/3389 |  |

创建ECS实例。
使用ECS，您可以快速部署和运行应用程序，灵活调整资源以应对业务变化，同时享受高性能、高安全性和低成本的计算能力，适用于网站托管、应用开发、数据处理等多种场景。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [RunInstances](../api-runinstances.md) | RegionId | 地域： cn-hangzhou |
| ImageId | 镜像：使用 Alibaba Cloud Linux 镜像 aliyun_3_x64_20G_alibase_20240819.vhd |  |
| InstanceType | 实例规格： ecs.e-c1m1.large |  |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| VSwitchId | 交换机 ID： vsw-bp1nzprm8h7mmnl8t **** |  |
| InstanceName | 实例名称： ecs_cli_demo |  |
| InstanceChargeType | 付费方式：实例按照按量付费的方式 PostPaid 说明 您需要确保账号余额能够完成支付。 |  |
| PASSWORD | 登录密码： ****** |  |
| InternetMaxBandwidthOut | 公网出带宽最大值。若大于 0，则自动为实例分配公网 IP。 |  |
| SystemDisk.Category | 系统盘的云盘种类： cloud_essd |  |
| SystemDisk.Size | 系统盘的大小：40 GiB |  |
