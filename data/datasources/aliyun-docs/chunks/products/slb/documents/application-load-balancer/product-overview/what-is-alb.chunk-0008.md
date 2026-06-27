## ALB类型
阿里云提供公网和私网两种类型的ALB。您可以根据业务场景选择配置对外公开或对内私有的ALB，系统会根据您的选择来决定是否使用共享带宽和弹性公网IP。

| 概念 | 说明 |
| --- | --- |
| VIP（Virtual IP address） | ALB 实施流量分发的实体。每个 VIP 都是专有网络 VPC（Virtual Private Cloud）中的一个私网 IP 地址。 |
| EIP | 您仅在创建公网 ALB 时需要使用 EIP，在创建私网 ALB 时无需配置。 ALB 对公网服务的 IP 地址，一个公网 ALB 可以有多个 EIP。为了实现高可用性，一个公网 ALB 至少应包含两个分布在不同可用区的 EIP。 |
| 共享带宽 | [共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/what-is-internet-shared-bandwidth) 提供地域级的带宽共享和复用能力，您可将同地域下的弹性公网 IP（EIP）添加到共享带宽实例中，复用共享带宽中的带宽，以节省公网带宽使用成本。 |
| 域名 | 一个在公网（私网）上可解析的域名解析至对应的 VIP。您也可以将所拥有的可读性强的域名通过 CNAME 方式解析到 ALB 的域名上来使用，具体操作，请参见 [为](../user-guide/configure-cname-resolution-for-alb.md) [ALB](../user-guide/configure-cname-resolution-for-alb.md) [配置](../user-guide/configure-cname-resolution-for-alb.md) [CNAME](../user-guide/configure-cname-resolution-for-alb.md) [解析](../user-guide/configure-cname-resolution-for-alb.md) 。 说明 自 北京时间 2024 年 11 月 15 日 00:00:00 起，对于新建的 ALB 实例默认使用新域名，阿里云平台将不允许用户直接使用平台侧提供的默认域名进行访问。 北京时间 2024 年 11 月 15 日 00:00:00 前，已创建的 ALB 实例不受影响。具体请参见 [负载均衡域名升级公告](../../product-overview/alb-and-nlb-domain-name-upgrade-announcement.md) 。 |
