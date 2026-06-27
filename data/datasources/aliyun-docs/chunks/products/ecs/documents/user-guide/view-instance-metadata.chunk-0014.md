| 基础网络配置 | network-type | 网络类型，只支持 VPC 类型实例。 | vpc |
| vpc-id | 实例所属 VPC ID。 | vpc-bp1e0g399hkd7c8q**** |  |
| vpc-cidr-block | 实例所属 VPC CIDR 段。 | 192.168.XX.XX/16 |  |
| vswitch-id | 实例所属虚拟交换机 ID。 | vsw-bp1ygryo03m39xhsy**** |  |
| vswitch-cidr-block | 实例所属虚拟交换机 CIDR 段。 | 192.168.XX.XX/24 |  |
| instance/max-netbw-egress | 实例规格的出方向内网最大带宽。单位：Kbit/s。 | 1228800 |  |
| dns-conf/nameservers | 实例的 DNS 配置。 | 100.100.XX.XX |  |
| ntp-conf/ntp-servers | NTP 服务器地址。 | ntp1.aliyun.com |  |
| 主网卡 IP 地址 | mac | 实例的 MAC 地址，如果实例存在多个网卡，则只显示 eth0 上的 MAC 地址。 | 00:16:3e:0f:XX:XX |
| private-ipv4 | 实例主网卡的私网 IPv4 地址。 | 192.168.XX.XX |  |
| public-ipv4 | 实例主网卡的公网 IPv4 地址。 | 120.55.XX.XX |  |
| eipv4 | 获取实例的固定公网 IPv4 地址或主网卡挂载的弹性公网 IPv4 地址。 | 120.55.XX.XX |  |
| 弹性网卡详细信息 | network/interfaces/macs/[mac]/network-interface-id | 网卡的标识 ID。 [mac]参数需要替换为实例的 MAC 地址（可通过元数据 mac 获取），下同。 | eni-bp1b2c0jvnj0g17b**** |
| network/interfaces/macs/[mac]/vpc-id | 网卡所属的 VPC ID。 | vpc-bp1e0g399hkd7c8q3**** |  |
| network/interfaces/macs/[mac]/vswitch-id | 网卡所属的虚拟交换机 ID。 | vsw-bp1ygryo03m39xhsy**** |  |
| network/interfaces/macs/[mac]/primary-ip-address | 网卡主私有 IP 地址。 | 192.168.XX.XX |  |
| network/interfaces/macs/[mac]/priva
