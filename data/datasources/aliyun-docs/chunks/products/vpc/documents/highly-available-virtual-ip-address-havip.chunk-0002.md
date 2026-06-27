## 使用 HaVip 实现主备切换
HaVip 支持绑定同一交换机内的ECS实例或弹性网卡，结合Keepalived等软件实现主备切换时的服务 IP 不变。
配额：使用前，需登录[配额中心控制台](https://quotas.console.aliyun.com/products/vpc/quotas?spm=a2c4g.11186623.0.0.610ecda16wO953&query=vpc_privilege_allow_buy_havip_instance&keyword=buy_havip_instance)申请创建 HaVip 的权限。配额为1，代表可创建 HaVip，而单账号支持创建 HaVip 的数量为 50 个。
IP 版本：HaVip 仅支持 IPv4。
绑定资源：
HaVip 只能同时绑定同一类型资源。如需绑定其他类型资源，需先解绑已经绑定的资源。
HaVip 绑定弹性网卡时，需确保弹性网卡绑定在ECS实例上。
如果已绑定的 ECS 实例或弹性网卡被删除，系统会自动解除 HaVip 和对应 ECS 实例或弹性网卡的绑定关系。
如果从 ECS 实例上解绑已绑定 HaVip 的辅助弹性网卡，不会影响 HaVip 和该辅助弹性网卡的绑定关系。
