to-peer-connection.md) 。 |
| 访问规则配置 | 互访 ECS 所在安全组的出入方向规则是否放行对端 IP。 RDS 实例的访问白名单是否添加了对端 IP。 与交换机绑定的网络 ACL 的出入方向规则是否放行对端 IP。 | 确保安全组、网络 ACL、RDS 的访问白名单均放行对端 IP。 |

网段配置导致无法连通的原因
网段重叠：
两端VPC网段重叠时，如果配置对端VPC网段作为目标网段，流量会优先匹配系统路由，在VPC内部转发，无法抵达对端VPC。
如果交换机网段不重叠，可以配置对端交换机网段作为目标网段。但新建交换机需要使用与现有交换机网段不重叠的网段。因此，建议将业务迁移到网段不重叠的VPC中，重新建立对等连接。
交换机网段重叠，由于无法配置比系统路由更明细的路由，只能将业务迁移到网段不重叠的 VPC，重新建立对等连接。
使用非[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)标准私网网段：
VPC 将[RFC 1918](https://www.rfc-editor.org/rfc/rfc1918)之外的 IP 地址空间（如 198.19.0.0/16、30.0.0.0/16 等）视为公网网段。当 VPC 中的 ECS 绑定了公网 IP 或通过 NAT 网关具备公网访问能力时，访问这些网段的流量会走公网出口，无法通过对等连接到达目标 VPC。需要在 VPC 中[使用](using-ipv4-gateway-for-public-network-private-use.md)[IPv4](using-ipv4-gateway-for-public-network-private-use.md)[网关实现公网私用](using-ipv4-gateway-for-public-network-private-use.md)，将目标公网网段添加为私网路由，确保流量通过对等连接正确路由到目标 VPC。
