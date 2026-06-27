# 变更ALB实例的网络类型-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/change-the-network-type-of-an-alb-instance

# 变更ALB实例的网络类型
您可以通过变更应用型负载均衡 ALB（Application Load Balancer）实例的网络类型来满足您的业务要求。
## 实例网络类型
ALB网络类型分为公网和私网。公网和私网的区别：
私网：ALB只有私网IP地址，只能被ALB所在VPC内的资源访问，无法从互联网访问。
公网：ALB具有公网IP和私网IP地址。公网ALB默认通过弹性公网IP（Elastic IP Address，简称EIP）提供公网能力，选择公网将会收取弹性公网IP的实例费、流量费用。
如需通过任播弹性公网IP（ Anycast Elastic IP Address，简称Anycast EIP）提供公网能力，您需要为ALB实例绑定Anycast EIP，具体操作，请参见[ALB](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[绑定](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[Anycast EIP](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[实现多地域业务就近接入](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)。
## 协议版本
ALB实例的协议版本分为IPv4和双栈。IPv4和双栈的区别：
| 协议版本 | 默认值 | 说明 |
| --- | --- | --- |
| IPv4 | 协议版本为 IPv4 的公网 ALB ，每个可用区提供一对 IP 地址，包括一个公网 IPv4 地址和一个私网 IPv4 地址。 协议版本为 IPv4 的私网 ALB ，每个可用区提供一个私网 IPv4 地址。 | 仅支持客户端使用 IPv4 地址（例如，192.0.2.1）访问。 仅支持将 IPv4 的客户端流量转发至 IPv4 的后端服务，且后端服务支持服务器类型（ECS、ENI、ECI）、IP 类型和函数计算类型。 |
| 双栈 | 协议版本为双栈的公网 ALB ，每个可用区提供三个 IP 地址，包括一个公网 IPv4 地址、一个私网 IPv4 地址和一个 IPv6 地址。 协议版本为双栈的私网 ALB ，每个可用区提供一对 IP 地址，包括一个私网 IPv4 地址和一个 IPv6 地址。 | 支持客户端同时使用 IPv4 地址（例如，192.168.0.1）和 IPv6 地址（例如，2001:db8:1:1:1:1:1:1）访问。 支持将 IPv4 和 IPv6 的客户端流量转发至 IPv4 或 IPv6 的后端服务。后端服务支持服务器类型（ECS、ENI、ECI）、IP 类型，不支持函数计算类型。 说明 如果您双栈 ALB 实例的服务器组类型为 IP 类型，且需要挂载 IPv6 的后端服务时，您需要使用 [ALB](../../product-overview/alb.md) [升级实例](../../product-overview/alb.md) 。 |
ALB对外通过DNS域名提供服务。ALB联动DNS，可实现自定义域名的解析，建议您使用CNAME解析的方式将自定义域名指向到ALB实例的DNS名称，使您更方便访问网络资源，配置可参考[为](configure-cname-resolution-for-alb.md)[ALB](configure-cname-resolution-for-alb.md)[配置](configure-cname-resolution-for-alb.md)[CNAME](configure-cname-resolution-for-alb.md)[解析](configure-cname-resolution-for-alb.md)。
## 公网IP介绍
ALB支持的公网类型：
EIP：EIP是可以独立购买和持有的公网IP地址资源。EIP可绑定到专有网络类型的CLB实例、私网ALB实例和公网NAT网关上。更多信息，请参见[什么是弹性公网](../../../../eip/documents/product-overview/what-is-eip.md)[IP](../../../../eip/documents/product-overview/what-is-eip.md)。
Anycast EIP：Anycast EIP是可以独立购买和持有的公网IP地址资源。每一个Anycast EIP实例会被分配一个可访问公网的IP地址。更多信息，请参见[什么是](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#concept-2494813)[Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/what-is-anycast-eip#concept-2494813)。
说明
关于Anycast EIP和EIP的差异，请参见[Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/comparison-between-anycast-eips-and-eips#concept-2082529)[和](https://help.aliyun.com/zh/anycast-eip/product-overview/comparison-between-anycast-eips-and-eips#concept-2082529)[EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/comparison-between-anycast-eips-and-eips#concept-2082529)[对比](https://help.aliyun.com/zh/anycast-eip/product-overview/comparison-between-anycast-eips-and-eips#concept-2082529)。
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
## 计费影响
ALB的计费项目前按小时收取，不足1小时按1小时计费。网络类型变更大约需要一分钟，如果您在1小时中间变更了网络类型，不足1小时的部分将按照变更前的计费规则收取1小时的费用。更多信息，请参见[ALB](../product-overview/alb-billing-rules.md)[计费规则](../product-overview/alb-billing-rules.md)。
公网和私网之间的变更，计费影响如下。
| 操作 | 使用场景 | 变更方式 | 计费影响 | 相关计费文档 |
| --- | --- | --- | --- | --- |
| IPv4 私网变更公网 | ALB 需要对外提供 IPv4 服务。 | 通过分配 EIP 或 Anycast EIP。 | 为 ALB 实例分配 EIP 或 Anycast EIP，会在对应的 EIP 或 Anycast EIP 上产生公网网络费。 | [弹性公网](../../../../eip/documents/pay-as-you-go.md) [IP](../../../../eip/documents/pay-as-you-go.md) [计费](../../../../eip/documents/pay-as-you-go.md) [Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing) [计费](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing) |
| IPv4 公网变更私网 | ALB 不再需要对外提供 IPv4 服务。 | 通过解绑 EIP 或 Anycast EIP。 | 变更后，具体的计费情况请以您的实际账单为准。 | 无 |
| IPv6 私网变更公网 | ALB 需要对外提供 IPv6 服务。 | 通过为 IPv6 网关开启公网带宽。 | IPv6 网关开启公网带宽会产生一定的费用。 | [IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) [网关计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb) |
| IPv6 公网变更私网 | ALB 不再需要对外提供 IPv6 服务。 | 通过为 IPv6 网关关闭公网带宽。 | 变更后，具体的计费情况请以您的实际账单为准。 | 无 |
## 前提条件
您已创建ALB。具体操作，请参见[创建和管理](create-and-manage-alb-instances.md)[ALB](create-and-manage-alb-instances.md)[实例](create-and-manage-alb-instances.md)。
## IPv4实例网络类型变更
### 私网变更公网
实例由私网变更为公网时，您需要为ALB实例分配公网IP，支持为ALB实例分配EIP或Anycast EIP，该操作将产生相关公网网络费，更多信息，请参见[弹性公网](../../../../eip/documents/pay-as-you-go.md)[IP](../../../../eip/documents/pay-as-you-go.md)[计费](../../../../eip/documents/pay-as-you-go.md)和[Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing)[计费](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing)。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标私网ALB实例，然后单击实例ID。
在实例详情页签，找到基本信息区域，在网络类型的IPv4右侧单击变更网络类型。
在变更网络类型对话框中，根据您的业务需求选择IP类型并分配公网IP，然后单击确定变更。
分配EIP
选择IP类型为弹性公网IP。
在列表中的分配弹性公网IP下拉框中选择新购弹性公网IP或指定可用的弹性公网IP。
说明
列表中的所有可用区都需要分配弹性公网IP。
如果您的业务需要ALB使用某个特定IP地址的EIP，您可以通过变更单个EIP实现。变更单个EIP需要增加或减少可用区来实现绑定或解绑EIP。关于如何变更可用区，请参见[更新实例可用区](modify-the-configurations-of-alb-instances.md)。
选择新购弹性公网IP时，请注意：
ALB网络类型变更会影响业务，之前随公网ALB创建的EIP会因网络类型的变更自动解绑或释放掉且无法找回。
您可以通过[弹性公网](https://vpc.console.aliyun.com/eip)[IP](https://vpc.console.aliyun.com/eip)[管理控制台](https://vpc.console.aliyun.com/eip)查看已购EIP的相关参数信息。
新购的EIP为按量付费（按使用流量计费）的BGP多线默认安全防护EIP。
分配Anycast EIP
关于ALB绑定Anycast EIP的相关限制和详细操作，请参见[ALB](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[绑定](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[Anycast EIP](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[实现多地域业务就近接入](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)。
选择IP类型为Anycast弹性公网IP。
在列表中的分配Anycast弹性公网IP下拉框中选择新购Anycast弹性公网IP或指定可用的Anycast EIP，然后单击确定变更。
说明
列表中的所有可用区都需要分配Anycast EIP。
选择新购Anycast弹性公网IP时，请注意：
ALB实例变更私网或释放后，关联的Anycast EIP会自动解绑并释放。
您可以通过[任播弹性公网](https://vpc.console.aliyun.com/eip/anycasts)[IP](https://vpc.console.aliyun.com/eip/anycasts)[管理控制台](https://vpc.console.aliyun.com/eip/anycasts)查看已购Anycast EIP的相关参数信息。
在实例详情页签，查看网络类型。
此变更生效大约需要一分钟，在实例详情页签查看IPv4的网络类型转变为公网后，代表转换成功。
### 公网变更私网
ALB实例由公网类型转换为私网类型，此操作会一次性解绑公网实例上所有EIP，并修改实例域名解析，将EIP变更为私网IP，请谨慎操作。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标公网ALB实例，然后单击实例ID。
在实例详情页签，找到基本信息区域，在网络类型的IPv4右侧单击变更网络类型。
在弹出的对话框中，确认转换后的影响，然后单击确定变更。
在实例详情页签，查看网络类型。
此变更生效大约需要一分钟，在实例详情页签查看IPv4的网络类型转变为私网后，代表转换成功。
## 双栈实例网络类型变更
### 私网变更公网
IPv4私网变更公网，请参见[IPv4](change-the-network-type-of-an-alb-instance.md)[实例网络类型变更](change-the-network-type-of-an-alb-instance.md)。
IPv6私网变更公网，请执行以下步骤完成变更。
说明
IPv6私网变更公网，将在VPC中的IPv6网关中开启公网带宽。开启公网带宽会产生一定的费用且会根据ALB公网和私网的切换，自动加入或删除。更多信息，请参见[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)[网关计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标私网ALB实例，然后单击实例ID。
在实例详情页签，找到基本信息区域，在网络类型的IPv6右侧单击变更网络类型。
在弹出的IPv6变更网络类型对话框中，确认提示信息，然后单击确定变更。
说明
如果ALB实例所在的VPC下没有IPv6网关，系统将提示您新建IPv6网关。请根据控制台提示信息完成操作。
在实例详情页签，查看网络类型。
此变更生效大约需要一分钟，在实例详情页签查看IPv6的网络类型转变为公网后，代表转换成功。
### 公网变更私网
IPv4公网变更私网，请参见[IPv4](change-the-network-type-of-an-alb-instance.md)[实例网络类型变更](change-the-network-type-of-an-alb-instance.md)。
IPv6公网变更私网，请执行以下步骤完成变更。
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标公网ALB实例，然后单击实例ID。
在实例详情页签，找到基本信息区域，在网络类型的IPv6右侧单击变更网络类型。
在弹出的关闭IPv6公网对话框中，确认转换后的影响，然后单击确定关闭。
在实例详情页签，查看网络类型。
此变更生效大约需要一分钟，在实例详情页签查看IPv6的网络类型转变为私网后，代表转换成功。
## 相关文档
[ALB](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[绑定](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[Anycast EIP](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)[实现多地域业务就近接入](../use-cases/associate-an-anycast-eip-with-an-alb-instance.md)
[ALB](../product-overview/alb-billing-rules.md)[计费规则](../product-overview/alb-billing-rules.md)
[弹性公网](../../../../eip/documents/pay-as-you-go.md)[IP](../../../../eip/documents/pay-as-you-go.md)[计费](../../../../eip/documents/pay-as-you-go.md)
[Anycast EIP](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing)[计费](https://help.aliyun.com/zh/anycast-eip/product-overview/product-billing)
[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)[网关计费说明](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)
[为](configure-cname-resolution-for-alb.md)[ALB](configure-cname-resolution-for-alb.md)[配置](configure-cname-resolution-for-alb.md)[CNAME](configure-cname-resolution-for-alb.md)[解析](configure-cname-resolution-for-alb.md)
[ALB](../use-cases/associate-an-eip-protected-by-anti-ddos-pro-or-premium-with-an-alb-instance.md)[通过](../use-cases/associate-an-eip-protected-by-anti-ddos-pro-or-premium-with-an-alb-instance.md)[DDoS](../use-cases/associate-an-eip-protected-by-anti-ddos-pro-or-premium-with-an-alb-instance.md)[防护（增强版）EIP](../use-cases/associate-an-eip-protected-by-anti-ddos-pro-or-premium-with-an-alb-instance.md)[实现公网访问](../use-cases/associate-an-eip-protected-by-anti-ddos-pro-or-premium-with-an-alb-instance.md)
[ALB](../support/faq-about-alb.md)[支持绑定哪些类型的](../support/faq-about-alb.md)[EIP？](../support/faq-about-alb.md)
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
