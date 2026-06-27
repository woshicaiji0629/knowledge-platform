## 支持的资源列表
说明
Resource：资源，指新创建的资源，用于定义基础设施组件，例如一个ECS实例、一个虚拟机、一个网络安全组等。
Resource
[alicloud_auto_provisioning_group](https://help.aliyun.com/zh/terraform/alicloud-auto-provisioning-group)：用于ECS的自动配置组资源，它利用抢占式实例和按量付费实例快速部署集群。
[alicloud_ecs_disk_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-disk-attachment)：用于为ECS实例挂载数据盘或系统盘。
[alicloud_ecs_activation](https://help.aliyun.com/zh/terraform/alicloud-ecs-activation)：用于创建ECS激活码，允许用户配置描述、最大注册实例数、默认实例名称前缀、允许使用激活码的主机IP地址范围及激活码的有效期等参数，以批量注册受管实例。
[alicloud_ecs_auto_snapshot_policy](https://help.aliyun.com/zh/terraform/alicloud-ecs-auto-snapshot-policy)：用于创建ECS自动快照策略，允许用户配置自动创建快照的周期（如每周的哪几天）、一天中的哪些时间点创建快照、快照保留天数等参数，同时也支持跨区域复制快照及其加密设置。
[alicloud_ecs_auto_snapshot_policy_attachment](https://help.aliyun.com/zh/terraform/alicloud-ecs-auto-snapshot-policy-attachment)：用于将自动快照策略附加到指定的磁盘上，允许用户通过指定自动快照策略ID和磁盘ID来关联两者的配置，以实现对特定磁盘应用预设的自动快照策略。
[alicloud_ecs_capacity_reservation](https://help.aliyun.com/zh/terraform/alicloud-ecs-capacity-reservation)：用于在阿里云上创建容量预留，允许用户为特定实例类型预留资源，确保在需要时能够启动指定数量的实例。
[alicloud_ecs_command](https://help.aliyun.com/zh/terraform/alicloud-ecs-command)：资源用于在阿里云ECS实例上创建命令，允许用户通过指定命令内容（Base64编码）、描述、是否启用自定义参数、命令名称、超时时间及命
