## 使用限制
ALB实例绑定Anycast EIP使用限制：
ALB支持Anycast EIP的地域，请参见下表。

| 区域 | 地域 |
| --- | --- |
| 中国 | 中国香港 |
| 亚太 | 韩国（首尔）、日本（东京）、新加坡、马来西亚（吉隆坡）、印度尼西亚（雅加达）、菲律宾（马尼拉）、泰国（曼谷） |
| 欧洲与美洲 | 英国（伦敦）、美国（弗吉尼亚）、美国（硅谷）、德国（法兰克福） |

ALB实例绑定EIP使用限制：
ALB实例每个可用区绑定的EIP类型需保持一致。关于ALB支持绑定的EIP类型，请参见[ALB](../support/faq-about-alb.md)[支持绑定哪些类型的](../support/faq-about-alb.md)[EIP？](../support/faq-about-alb.md)。
绑定前，要求EIP未加入共享带宽。如有加入共享带宽的需求，ALB实例绑定EIP后，您可以在负载均衡控制台选择加入共享带宽。EIP的线路类型与共享带宽的线路类型需保持一致。关于如何加入共享带宽，请参见[调整公网实例带宽峰值](modify-the-configurations-of-alb-instances.md)。
