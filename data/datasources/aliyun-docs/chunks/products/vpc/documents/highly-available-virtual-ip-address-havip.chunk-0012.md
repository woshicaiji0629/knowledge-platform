## 绑定 EIP 实现公网访问
HaVip 是交换机内的私网 IP 资源，如需公网访问，可以将 HaVip 与弹性公网IP（EIP）绑定。EIP 的使用会[产生费用](../../eip/documents/billing-overview.md)。
1、绑定的 EIP 地域需和 HaVip 的地域相同，且处于可用状态。2、ECS 实例借助 HaVip 绑定的 EIP 访问公网时，数据包的源 IP 为 HaVip 的私网IP，而非 ECS 实例的私网 IP。
