## 网络连通性排查
建议优先使用[路径分析](vpc-peer-to-peer-connection.md)验证网络连通性。

| 检查项 | 检查内容 | 解决方案 |
| --- | --- | --- |
| 对等连接状态 | 查看目标对等连接实例的 状态 是否为 已激活 。 | 如果状态为对端接收中，需要联系接收端账号接受连接。 |
| 网段配置 | 查看发起端网段和接收端网段： 是否重叠。 是否使用了非 [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) 标准私网网段（如 198.19.0.0/16、30.0.0.0/8 等）。VPC 将这些网段视为公网地址，ECS 绑定公网 IP 时流量默认走公网出口。 当 ECS 实例部署 Docker 时，是否与 Docker 网卡地址冲突。 | 网段重叠时，需将业务迁移到网段不重叠的 VPC，重新建立对等连接。 使用非 RFC 标准私网网段时， [使用](using-ipv4-gateway-for-public-network-private-use.md) [IPv4](using-ipv4-gateway-for-public-network-private-use.md) [网关实现公网私用](using-ipv4-gateway-for-public-network-private-use.md) ，确保流量能够正确地到达目标 VPC。 [修改 Docker 网段](vpc-peer-to-peer-connection.md) 。 |
| 路由配置 | 查看对等连接详情页的 路由条目列表 ： 是否为两端 VPC 都配置了指向对方的路由。 目标网段是否正确填写对端的 VPC 网段。 路由条目是否添加到资源所在交换机绑定的路由表。 | 检查并修正 [双向路由配置](vpc-peer-to-peer-connection.md) 。 |
| 访问规则配置 | 互访 ECS 所在安全组的出入方向规则是否放行对端 IP。 RDS 实例的访问白名单是否添加了对端 IP。 与交换机绑定的网络 ACL 的出入方向规则是否放行对端 IP。 | 确保安全组、网络 ACL、RDS 的访问白名单均放行对端 IP。 |
