## IPv4地址
VPC内的资源依赖公网IP地址与公网进行IPv4通信。公网IPv4地址类型分为固定公网IP与弹性公网IP。
固定公网IP只能在ECS/CLB等实例创建时分配，并且创建后无法更换绑定/解绑，只能随着实例删除。而[弹性公网](../../eip/documents/product-overview/what-is-eip.md)[IP](../../eip/documents/product-overview/what-is-eip.md)是独立的公网IP资源，可以单独创建与持有、动态绑定/解绑，满足灵活管理的要求，推荐您使用弹性公网IP。
公网ALB、公网NLB、公网NAT网关是通过绑定的弹性公网IP提供公网访问能力。公网ECS、公网CLB的固定公网IP，可以转为弹性公网IP。
弹性公网IP有不同类型：
弹性公网IP（BGP多线）：通过接入多条运营商线路并自动选择最优路径，为用户提供快速稳定的访问体验。
[弹性公网](../../eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md)[IP（BGP](../../eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md)[多线-精品）](../../eip/documents/use-boutique-eip-to-optimize-access-to-international-business-in-mainland-china.md)：为中国内地终端客户（不包括中国内地数据中心）专门优化的海外回中国内地流量的公网线路，通过运营商精品公网直连降低时延，提升国际业务访问质量。
[任播弹性公网](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip)[IP（Anycast EIP）](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip)：每一个Anycast EIP实例会被分配一个可在整个接入区域内发布、不受地域限制的公网IP地址。在将此IP地址与后端资源进行绑定后，接入区域内的用户流量将通过该IP地址从就近接入点进入阿里云网络。进入阿里云网络后，Anycast EIP可以智能选择路由并自动完成网络调度，将用户的网络访问请求送达至后端资源节点，提升用户的公网访问体验。
