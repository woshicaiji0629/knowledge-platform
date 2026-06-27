h-ipv6-cidr-block | 网卡所属的虚拟交换机 IPv6 CIDR 段，仅支持已配置了 IPv6 的 VPC 类型实例。 | 2408:XXXX:325:a204::/64 |  |
| network/interfaces/macs/[mac]/vpc-ipv6-cidr-blocks | 网卡所属的 VPC IPv6 CIDR 段，仅支持已配置了 IPv6 的 VPC 类型实例。 | [2408:XXXX:325:a200::/56] |  |
| 云盘信息 | disks/ | 云盘序列号。 | bp131n0q38u3a4zi**** |
| disks/[disk-serial]/id | 云盘 ID。 | d-bp131n0q38u3a4zi**** |  |
| disks/[disk-serial]/name | 云盘名称。 | testDiskName |  |
| 安全与凭证 | public-keys/[keypair-id]/openssh-key | 公有密钥。仅在实例启动时提供了公有密钥的情况下可用。 | ssh-rsa ****3NzaC1yc2EAAAADAQABAAABAQDLNbE7pS****@****.com |
| ram/security-credentials/[role-name] | 与实例关联的 RAM 角色的临时安全凭证。[role-name]需替换为角色名称。凭证在 Expiration 字段指定时间后失效，需重新调用接口获取。 | { "AccessKeyId": "****", "AccessKeySecret": "****", "Expiration": "2024-11-08T09:44:50Z", "SecurityToken": "****", "LastUpdated": "2024-11-08T03:44:50Z", "Code": "Success" } |  |
| 实例高级属性 | instance/virtualization-solution | ECS 虚拟化方案，支持 Virt 1.0 和 Virt 2.0。 | ECS Virt |
| instance/virtualization-solution-version | 内部 Build 号。 | 2 |  |
| instance/spot/termination-time | 抢占式实例的操作系统设置的停机释放时间，时区标准为 UTC+0，格式为 yyyy-MM-ddThh:mm:ssZ。 | 2020-04-07T17:03:00Z |  |
| Windows 特定配置 | kms-server | Windows 实例的 KMS 激活服务器。 | kms.cloud.aliyuncs.com |
