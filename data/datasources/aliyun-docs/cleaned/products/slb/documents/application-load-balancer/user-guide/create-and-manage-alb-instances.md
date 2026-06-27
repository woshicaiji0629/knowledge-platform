# 创建和管理ALB实例-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/create-and-manage-alb-instances

# 创建和管理ALB实例
ALB是专门面向七层的负载均衡服务，提供应用层处理能力和多种高级转发规则。通过购买一个ALB实例，可以将来自客户端的请求转发给后端服务器。
## 创建实例
规划与准备
账号权限：首次创建ALB实例时，系统会引导创建服务关联角色AliyunServiceRoleForAlb。该角色为必需，用于授权ALB访问弹性网卡、安全组、弹性公网IP、共享带宽等云资源。
账号余额：ALB实例采用按量付费（后付费）计费模式，账号欠费时无法创建实例。创建前请确保账号有足够现金余额。
网络准备：
已在目标地域[创建专有网络](../../../../vpc/documents/vpc-and-vswitch.md)[VPC](../../../../vpc/documents/vpc-and-vswitch.md)。
为实现高可用，在地域支持多可用区的前提下，ALB实例需部署在至少两个可用区。请确保在计划使用的每个可用区内创建至少一个交换机。
IP地址规划：
ALB实例会从每个指定的交换机中分配3个IP地址，包含1个VIP（对外提供服务）和2个Local IP（用于与后端服务器通信）。
为确保ALB实例各项弹性能力可用，建议在ALB实例所在的每个交换机内预留至少8个IP地址。且 IPv4 交换机的首个和末尾3个IP地址为系统保留地址，故交换机的 IPv4 网段前缀长度需要配置为/28或更短（如/27）。
安全规划：为确保ALB实例与后端服务正常连通，如访问链路中存在安全策略（如 iptables 或其他第三方安全软件），建议提前放通ALB实例所属交换机网段。
## 控制台
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击创建应用型负载均衡。
在购买页完成以下配置，点击立即创建。
地域：建议选择最靠近客户端的地域以降低访问延迟。
参考[ALB](../product-overview/supported-regions-and-zones.md)[功能特性支持的地域与可用区](../product-overview/supported-regions-and-zones.md)。
实例网络类型：
私网：仅分配私网IP地址，用于阿里云内部网络访问。
公网：同时分配公网IP和私网IP，支持互联网访问和内网访问。ALB默认由弹性公网IP（EIP）提供公网能力。
选择公网将收取EIP的[配置费和流量费](../../../../eip/documents/billing-overview.md)。双栈公网实例默认使用IPv4地址提供公网服务，无IPv6公网能力。如需IPv6公网能力，请[变更](change-the-network-type-of-an-alb-instance.md)[ALB](change-the-network-type-of-an-alb-instance.md)[实例的网络类型](change-the-network-type-of-an-alb-instance.md)，这将产生[IPv6](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)[公网费用](https://help.aliyun.com/zh/ipv6-gateway/product-overview/ipv6-gateway-billing/#concept-gvc-fyt-zfb)。
VPC：实例和服务器组需位于同一个VPC。ALB实例创建后，所属VPC无法修改。
可用区：
如地域支持多可用区，至少选择2个可用区及对应交换机。
（仅当实例网络类型为公网）可选择绑定已有EIP或自动分配公网IP。如选择后者，系统将创建按量付费（按使用流量计费）的EIP并绑定至ALB实例。
仅支持绑定暂未加入共享带宽的按量付费（按使用流量计费）的已购EIP；同一个ALB实例不同可用区绑定的[EIP](../support/faq-about-alb.md)[类型](../support/faq-about-alb.md)需保持一致。
协议版本：如需支持IPv6访问，选择[双栈](alb-instance-overview.md)；否则选择IPv4。
购买双栈ALB实例前，请为实例所在交换机[开启](../../../../vpc/documents/vpc-and-vswitch.md)[IPv6](../../../../vpc/documents/vpc-and-vswitch.md)。仅支持新建双栈实例，不支持升级已有IPv4实例为双栈。
[功能版本](../product-overview/functional-characteristics.md)（实例费）：
基础版：提供应用型负载均衡的基本功能，可支持基于域名、URL、HTTP Header等路由转发。
标准版：在基础版之上，还支持自定义TLS安全策略、链路追踪等特性，以及重定向、重写等高级路由功能。
WAF增强版：在标准版之上，集成Web应用防火墙（WAF 3.0），为Web业务提供应用层安全防护。
若账号未开通WAF实例，购买WAF增强版ALB实例将自动开通WAF 3.0按量付费实例。若账号已开通WAF 3.0包年包月实例，购买WAF增强版ALB实例后，不会额外产生WAF费用。若账号下已开通WAF 2.0实例，需先[释放](../../../../waf/documents/web-application-firewall-2-0/user-guide/terminate-the-waf-service.md)[WAF 2.0](../../../../waf/documents/web-application-firewall-2-0/user-guide/terminate-the-waf-service.md)[实例](../../../../waf/documents/web-application-firewall-2-0/user-guide/terminate-the-waf-service.md)或者[迁移至](../../../../waf/documents/product-overview/migrate-a-waf-instance-to-waf-3.md)[WAF 3.0](../../../../waf/documents/product-overview/migrate-a-waf-instance-to-waf-3.md)。ALB 默认不开启 X-Forwarded-Proto 头字段。释放 WAF 2.0 实例后，直接访问 ALB 可能会因后端服务无法正确识别协议（HTTP/HTTPS）而导致业务异常（例如，无限重定向）。为避免此问题，务必在 ALB 监听配置中手动开启X-Forwarded-Proto请求头。
（仅当实例网络类型为公网）加入共享带宽：双可用区ALB实例默认公网带宽峰值为400Mbps，可加入[共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/user-guide/create-an-internet-shared-bandwidth-instance#ea9cb55b4ambt)以获取更大带宽峰值。
（仅当实例网络类型为公网，且未选择加入共享带宽）公网计费方式：默认为[按流量计费](../../../../eip/documents/pay-as-you-go.md)且无法修改。
按流量计费模式下，带宽峰值不作为业务承诺指标，仅作为参考值和带宽上限峰值。当出现资源争抢时，带宽峰值可能会受到限制。
实例名称和[资源组](https://help.aliyun.com/zh/resource-management/resource-group/product-overview/resource-group-overview)：建议合理设置以简化管理。购买实例后，支持在[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面修改实例名称及使用[标签](https://help.aliyun.com/zh/resource-management/tag/product-overview/tag-overview)管理实例。
## API
调用[CreateLoadBalancer](../developer-reference/api-alb-2020-06-16-createloadbalancer.md)创建应用型负载均衡实例。
后续操作
[创建服务器组](create-and-manage-a-server-group.md)：创建一组ALB实例转发请求的目标服务器。
添加监听：为ALB实例添加接收请求的入口，支持创建[HTTP](../../add-an-http-listener.md)、[HTTPS](add-an-https-listener.md)、[QUIC](add-a-quic-listener.md)监听。
[添加](configure-cname-resolution-for-alb.md)[CNAME](configure-cname-resolution-for-alb.md)[解析](configure-cname-resolution-for-alb.md)：[负载均衡域名已升级](../../product-overview/alb-and-nlb-domain-name-upgrade-announcement.md)，新建ALB实例不支持直接使用DNS名称访问。请使用自有域名，将其以CNAME形式解析到实例的DNS名称进行访问。
## 释放实例
从实例创建完成到实例释放结束，无论是否使用，将收取[实例费](../product-overview/alb-billing-rules.md)。为避免不必要的开销，当不再需要实例时，可以将其释放以停止计费。
释放公网ALB实例时，支持保留ALB自动创建并绑定的EIP（Anycast EIP不支持保留），保留的EIP将按量计费；用户自行绑定的EIP自动保留。
警告
释放实例会删除其所有配置且不可恢复，请谨慎操作。
如果实例由其他云服务（如容器服务 Kubernetes 版）管理，释放实例将导致关联服务异常且不可恢复。
释放前，请确保已将解析到该实例的业务域名指向其他地址，避免业务中断。
释放实例前，请确认实例未开启删除保护。
## 控制台
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，在目标实例操作列选择>释放并确认。
## API
调用[DisableDeletionProtection](../developer-reference/api-alb-2020-06-16-disabledeletionprotection.md)关闭实例的删除保护。
调用[DeleteLoadBalancer](../developer-reference/api-alb-2020-06-16-deleteloadbalancer.md)删除负载均衡实例。
## 删除保护和配置修改保护
删除保护和配置修改保护功能用于防止误操作导致实例被删除或修改。
配置修改保护仅对控制台生效。
## 控制台
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID进入实例详情页，在实例属性区域开启或关闭删除保护和配置修改保护。
## API
调用[EnableDeletionProtection](../developer-reference/api-alb-2020-06-16-enabledeletionprotection.md)和[DisableDeletionProtection](../developer-reference/api-alb-2020-06-16-disabledeletionprotection.md)开启和关闭删除保护。
调用[UpdateLoadBalancerAttribute](../developer-reference/api-alb-2020-06-16-updateloadbalancerattribute.md)时，设置ModificationProtectionConfig下的Status字段开启或关闭配置修改保护。
## 计费说明
ALB支持按量付费（后付费）和资源包（预付费）两种付费方式，计费组成等信息详见[ALB](../product-overview/billing-overview.md)[计费概述](../product-overview/billing-overview.md)。
## 配额
详见[ALB](alb-quotas-2.md)[配额](alb-quotas-2.md)。
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
