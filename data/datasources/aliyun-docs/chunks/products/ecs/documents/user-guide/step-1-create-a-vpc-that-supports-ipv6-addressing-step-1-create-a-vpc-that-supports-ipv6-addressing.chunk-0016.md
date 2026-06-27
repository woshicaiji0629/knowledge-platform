### 步骤四： 开通IPv6公网带宽
默认云服务器的IPv6地址仅具有私网通信能力，若您想要通过该IPv6地址访问公网或被公网访问，则需参照如下步骤开通IPv6公网带宽。
登录[专有网络管理控制台](https://vpcnext.console.aliyun.com)。
在左侧导航栏，选择公网访问>IPv6网关。
- 在顶部菜单栏处，选择IPv6网关的地域。
在IPv6网关页面，根据实例的专有网络ID找到对应IPv6网关，然后单击IPv6网关ID。
在IPv6网关的详情页面，单击IPv6公网带宽页签，找到目标IPv6地址，然后在操作列单击开通公网带宽。
在IPv6公网带宽（后付费）页面，根据以下信息配置公网带宽，然后单击立即购买并完成支付。

| 参数 | 描述 |
| --- | --- |
| 流量 | 选择公网带宽的计费类型。 公网带宽支持 按固定带宽计费 和 按使用流量计费 两种计费类型。更多信息，请参见 [IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) [网关计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) 。 |
| 带宽 | 根据需要调整公网带宽的带宽峰值。 |
| 计费周期 | 公网带宽的计费周期。有 按天 和 按小时 两种计费周期。 当公网带宽选择 按固定带宽计费 时，计费周期为 按天 。 当公网带宽选择 按使用流量计费 时，计费周期为 按小时 。 |

开通IPv6公网带宽完成后，即可测试IPv6的公网连通性。
说明
测试IPv6的网络连通性时，您需要确保服务端与客户端都支持并配置了IPv6。
ping -6 aliyun.com
系统返回信息如下图所示，表示网络连接正常。
说明
在此示例中，网站aliyun.com已支持IPv6，当您的ECS实例配置完成后，即可通过IPv6访问aliyun.com。
