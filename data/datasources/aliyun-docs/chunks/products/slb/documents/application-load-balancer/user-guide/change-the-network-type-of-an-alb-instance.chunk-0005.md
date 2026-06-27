间变更了网络类型，不足1小时的部分将按照变更前的计费规则收取1小时的费用。更多信息，请参见[ALB](../product-overview/alb-billing-rules.md)[计费规则](../product-overview/alb-billing-rules.md)。
公网和私网之间的变更，计费影响如下。

| 操作 | 使用场景 | 变更方式 | 计费影响 | 相关计费文档 |
| --- | --- | --- | --- | --- |
| IPv4 私网变更公网 | ALB 需要对外提供 IPv4 服务。 | 通过分配 EIP 或 Anycast EIP。 | 为 ALB 实例分配 EIP 或 Anycast EIP，会在对应的 EIP 或 Anycast EIP 上产生公网网络费。 | [弹性公网](../../../../eip/documents/pay-as-you-go.md) [IP](../../../../eip/documents/pay-as-you-go.md) [计费](../../../../eip/documents/pay-as-you-go.md) [Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing) [计费](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing) |
| IPv4 公网变更私网 | ALB 不再需要对外提供 IPv4 服务。 | 通过解绑 EIP 或 Anycast EIP。 | 变更后，具体的计费情况请以您的实际账单为准。 | 无 |
| IPv6 私网变更公网 | ALB 需要对外提供 IPv6 服务。 | 通过为 IPv6 网关开启公网带宽。 | IPv6 网关开启公网带宽会产生一定的费用。 | [IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) [网关计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) |
| IPv6 公网变更私网 | ALB 不再需要对外提供 IPv6 服务。 | 通过为 IPv6 网关关闭公网带宽。 | 变更后，具体的计费情况请以您的实际账单为准。 | 无 |
