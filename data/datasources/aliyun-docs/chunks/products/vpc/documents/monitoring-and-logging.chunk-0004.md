合并降噪后的有效报警通知：云监控可以直接发送给报警联系人，如果报警在预定时间内未恢复，云监控自动将报警通知发送给下一个报警联系人组。
自定义通知方式：可以按照习惯定义通知渠道的级别和模板，还可以通过推送与集成，直接将所有报警数据推送到轻量消息队列（原 MNS）、日志服务SLS、函数计算FC和Webhook。
可监控指标

| 产品 | 指标类型 | 可监控指标 |
| --- | --- | --- |
| [VPC 对等连接](https://cms.console.aliyun.com/metric-meta/acs_vpcpeer/vpcpeer) | 实例维度 | 周期内入方向流量、周期内出方向流量、网络限速丢包速率、入方向带宽、出方向带宽 |
| [IPAM 作用范围](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_scope) | 实例维度 | 作用范围内合规 CIDR 数量、不合规 CIDR 数量、已忽略 CIDR 数量、托管 CIDR 数量、未托管 CIDR 数量、不重叠 CIDR 数量、重叠 CIDR 数量、子网 CIDR 数量、VPC CIDR 数量 |
| [IPAM 地址池](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_pool) | 实例维度 | 池整体利用率、池分配子池利用率、池分配资源利用率，地址池内合规 CIDR 数量、不合规 CIDR 数量、重叠 CIDR 数量、不重叠 CIDR 数量 |
| [IPAM](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vpc) [资源(VPC)](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vpc) | 实例维度 | VPC 利用率、VPC IPv4 网段利用率、VPC IPv6 网段利用率 |
| [IPAM](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vswitch) [资源(VSwitch)](https://cms.console.aliyun.com/metric-meta/acs_vpcipam/vpcipam_resource_vswitch) | 实例维度 | 子网利用率、子网 IPv4 网段利用率、子网 IPv6 网段利用率 |
