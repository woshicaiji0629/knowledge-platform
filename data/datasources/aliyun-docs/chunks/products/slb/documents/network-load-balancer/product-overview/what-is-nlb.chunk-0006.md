### 网络类型
阿里云提供公网和私网两种网络类型的NLB。您可以根据业务场景选择配置对外公开或对内私有的NLB，系统会根据您的选择来决定是否使用共享带宽和弹性公网IP。上图中半透明框中所有元素分别实现了一个面向公网（私网）的NLB。

| 概念 | 说明 |
| --- | --- |
| 域名 | 一个在公网（私网）上可解析的域名解析至对应的 VIP。您也可以将所拥有的可读性强的域名通过 CNAME 方式解析到 NLB 的域名上来使用。 说明 自 北京时间 2024 年 11 月 15 日 00:00:00 起，对于新建的 NLB 实例默认使用新域名，阿里云平台将不允许用户直接使用平台侧提供的默认域名进行访问。 北京时间 2024 年 11 月 15 日 00:00:00 前，已创建的 NLB 实例不受影响，具体请参见 [负载均衡域名升级公告](../../product-overview/alb-and-nlb-domain-name-upgrade-announcement.md) 。 |
| 共享带宽 | 您仅在创建公网 NLB 时需要使用共享带宽。共享带宽提供 [地域](https://www.aliyun.com/getting-started/what-is/what-is-a-region) 级的带宽共享和复用能力，以及按带宽计费和按增强型 95 计费等多种计费模式，可有效节省公网带宽使用成本。公网 NLB 中将使用共享带宽来提供增强型 95 计费和按带宽计费能力。 |
| EIP | 您仅在创建公网 NLB 时需要使用 EIP，在创建私网 NLB 时无需配置。 NLB 对公网服务的 IP 地址，一个公网 NLB 可以有多个 EIP。为了实现 [高可用](https://www.aliyun.com/getting-started/what-is/what-is-high-availability) 性，一个公网 NLB 至少应包含两个分布在不同可用区的 EIP。 |
| VIP（Virtual IP address） | NLB 实施流量分发的实体。每个 VIP 都是专有网络 VPC（Virtual Private Cloud）中的一个私网 IP 地址。 |
