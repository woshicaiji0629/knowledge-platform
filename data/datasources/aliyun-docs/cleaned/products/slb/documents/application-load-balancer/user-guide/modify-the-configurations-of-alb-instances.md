# ALB实例变配-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/modify-the-configurations-of-alb-instances

# ALB实例变配
本文为您介绍ALB实例的变配规则和操作。
## 更新实例可用区
更新实例可用区的变配限制、生效时间、计费影响等相关信息请参见下表。
| 变配限制 | 生效时间 | 计费影响 | 适用场景 |
| --- | --- | --- | --- |
| 当前 ALB 实例可用区数量小于或等于 2 个时，不支持减少实例可用区。 公网 ALB 实例新增可用区限制： ALB 实例中的所有可用区绑定的 EIP 类型需保持一致。更多信息，请参见 [ALB](../support/faq-about-alb.md) [支持绑定哪些类型的](../support/faq-about-alb.md) [EIP？](../support/faq-about-alb.md) 。 绑定 EIP 前，要求 EIP 未加入共享带宽。如有加入共享带宽的需求， ALB 实例绑定 EIP 后，您可以在负载均衡控制台选择加入共享带宽。 不支持绑定包年包月 EIP，不支持绑定按量付费（按固定带宽计费）的 EIP。 | 通常更新实例可用区会立即生效，但可能由于网络等原因有一定的延时，请您耐心等待几分钟。 | 公网 ALB 修改可用区可能会涉及到弹性公网 IP 的变动，弹性公网 IP 会产生相应的费用，具体费用以实际结算为准。更多信息，请参见 [EIP](../../../../eip/documents/billing-overview.md) [计费概述](../../../../eip/documents/billing-overview.md) 。 | 当前实例可用区或公网 ALB 实例绑定的 EIP 不满足您的业务需求或超出您的业务需求时，您可以更新实例可用区。 |
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标实例，然后在操作列选择>编辑可用区/子网。
在编辑可用区/子网对话框中，选中目标可用区复选框并选择交换机，或取消选择目标可用区，然后单击确定。
选择交换机时，如果没有可选的交换机，您可以在下拉框中单击创建交换机。具体操作，请参见[创建和管理专有网络](../../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)。
公网ALB实例选中目标可用区复选框时，还需为该可用区分配EIP。
公网ALB实例分配EIP时选择新购创建的为按量付费（按使用流量计费）的BGP多线默认安全防护EIP。
公网ALB实例取消选择可用区时，支持保留ALB自动创建并绑定的EIP（Anycast EIP不支持保留），保留的EIP将按量计费；用户自行绑定的EIP自动保留。
## 变更可用区状态
### 可用区状态
| 可用区状态 | 说明 | 支持的可用区操作 |
| --- | --- | --- |
| 启用 | 该实例在当前可用区处于启用状态，VIP 正常转发流量。 | DNS 摘除 停止（仅支持通过 [CADT](https://bpstudio.console.aliyun.com/) [容灾管理](https://bpstudio.console.aliyun.com/) 服务操作。相关应用请参见教程 [通过](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [CADT](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [实现](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [ALB](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [可用区级容灾演练](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) 。） 说明 当前 ALB 实例处于 启用 状态的可用区数量等于 1 时，不支持 DNS 摘除和停止操作。 |
| 停止 | 该实例在当前可用区处于停止状态，VIP 不再转发流量。 该状态仅支持通过 [CADT](https://bpstudio.console.aliyun.com/) [容灾管理](https://bpstudio.console.aliyun.com/) 服务操作实现。 | 启用（仅支持通过 [CADT](https://bpstudio.console.aliyun.com/) [容灾管理](https://bpstudio.console.aliyun.com/) 服务操作。相关应用请参见教程 [通过](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [CADT](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [实现](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [ALB](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) [可用区级容灾演练](../use-cases/realize-alb-zone-level-disaster-recovery-drill-through-cadt.md) 。） |
| DNS 摘除 | 该实例在当前可用区处于 DNS 摘除状态，IP 已从 ALB 域名解析中摘除。 | DNS 恢复 |
### DNS摘除与恢复
负载均衡控制台支持ALB实例可用区的DNS摘除和DNS恢复操作。您可以通过DNS摘除和DNS恢复操作变更可用区状态，便于模拟可用区容灾等场景。
| 变配限制 | 生效时间 | 计费影响 | 适用场景 |
| --- | --- | --- | --- |
| [ALB](../../product-overview/alb.md) [升级实例](../../product-overview/alb.md) 默认支持 DNS 摘除与 DNS 恢复操作。 说明 升级前的 ALB 实例，仅固定 IP 模式支持 DNS 摘除与 DNS 恢复操作，动态 IP 模式不支持。 当前 ALB 实例处于 启用 状态的可用区数量等于 1 时，不支持 DNS 摘除操作。 | 通常摘除或恢复可用区 DNS 会即时生效，但可能由于网络等原因有一定的延时，请您耐心等待几分钟。 | 无 重要 DNS 摘除后，通过 VIP 访问该可用区的流量依然会正常转发并计算 LCU 消耗。 | 模拟多可用区容灾等场景，验证 ALB 高可用。 |
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择ALB实例所属的地域。
在ALB实例页面，单击目标实例ID。
在实例详情页签，在可用区区域，根据需要选择执行以下操作。
DNS摘除
在目标可用区的操作列单击DNS摘除，在弹出的对话框中确认摘除影响，然后单击已知晓影响，继续DNS摘除操作。
说明
该操作仅对当前ALB实例生效，可用区内其他实例不受影响。
可用区DNS摘除后，ALB域名解析中会删除该可用区IP的A记录，请充分评估对业务影响后谨慎操作。
可用区DNS摘除完成后，可用区状态变更为DNS摘除，同时该可用区VIP的可用性探测停止。
DNS恢复
如需恢复状态为DNS摘除的可用区，在该可用区的操作列单击DNS恢复，在弹出的对话框中确认恢复影响，然后单击已知晓影响，继续DNS恢复操作。
说明
可用区重新启用后，ALB域名解析中会增加该可用区IP的A记录，该可用区的IP将会正常转发访问ALB域名的流量。
可用区DNS恢复后，可用区状态变更为启用，同时该可用区VIP的可用性探测启动。
## 变配实例功能版本
ALB实例包含基础版、标准版、WAF增强版和扩展版。ALB实例功能版本支持平滑升级，升级期间仍可正常使用ALB实例，业务不受影响。
关于功能版本支持的功能特性，请参见[功能特性](../product-overview/functional-characteristics.md)。
关于资源使用的配额限制，请参见[配额与限制](../product-overview/quotas-and-limits.md)。
变配实例功能版本的变配限制、生效时间、计费影响等相关信息请参见下表。
| 变配限制 | 生效时间 | 计费影响 | 适用场景 |
| --- | --- | --- | --- |
| 标准版 ALB 实例不支持变配为基础版。 WAF 增强版 ALB 实例仅支持变配为标准版，不支持变配为基础版。 WAF 增强版的相关限制和管理操作，请参见 [为 ALB 开启 WAF 防护](../use-cases/enable-waf-protection-for-alb.md) 。 扩展版 ALB 实例不支持变配实例功能版本。 | 通常变配实例功能版本会立即生效，但可能由于网络等原因有一定的延时，请您耐心等待几分钟。 | ALB 实例功能版本变配，对应的实例费会变更，具体费用以实际结算为准。更多信息，请参见 [ALB](../product-overview/alb-billing-rules.md) [计费规则](../product-overview/alb-billing-rules.md) 。 升级为 ALB WAF 增强版实例后，会产生 WAF 3.0 的防护费用。更多信息，请参见 [WAF 3.0](../../../../waf/documents/web-application-firewall-3-0/billing-description.md) [包年包月计费说明](../../../../waf/documents/web-application-firewall-3-0/billing-description.md) 和 [WAF 3.0](../../../../waf/documents/web-application-firewall-3-0/billing-description-v3.md) [按量付费计费说明](../../../../waf/documents/web-application-firewall-3-0/billing-description-v3.md) 。若您的当前账号没有 WAF 实例，您购买 ALB WAF 增强版后，开通的是按量付费 WAF 3.0 实例。 | 当前 ALB 实例功能版本不满足您的业务需求或超出您的业务需求时，您可以变配实例功能版本。 |
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标实例，然后在操作列选择>变配功能版本。
在变配页面，选择功能版本（实例费）为标准版或WAF增强版，选中服务协议，然后单击立即购买。
返回实例页面，找到目标实例，在功能版本列查看实例的版本是否更新成功。
## 调整公网实例带宽峰值
公网ALB实例选择加入共享带宽后，公网ALB实例带宽峰值可通过已加入的共享带宽的带宽峰值来调整。
说明
未加入共享带宽时，公网ALB实例（双可用区）的带宽峰值，取决于各可用区所分配的EIP的带宽峰值。每个可用区的公网带宽峰值为对应EIP带宽峰值。
按使用流量计费的单个EIP的带宽峰值，仅作为参考值和上限，不作为业务承诺指标。因此，将所有EIP带宽峰值叠加作为ALB公网带宽峰值的理论值，也不作为业务承诺指标。
ALB实例加入共享带宽时，实例的带宽峰值以共享带宽的带宽峰值为准。
共享带宽的带宽峰值，仅作为参考值和上限，不作为业务承诺指标。
共享带宽的带宽峰值可通过新建共享带宽或修改已有的共享带宽来调整。新建或修改已有共享带宽的带宽峰值请登录[共享带宽管理控制台](https://vpc.console.aliyun.com/cbwp/cn-hangzhou/cbwps?spm=a2c4g.11186623.0.0.4a8154a16OGiG3)调整。
公网ALB实例绑定的EIP加入共享带宽的变配限制、生效时间、计费影响等相关信息请参见下表。
| 变配限制 | 生效时间 | 计费影响 | 适用场景 |
| --- | --- | --- | --- |
| EIP 的线路类型与共享带宽的线路类型需保持一致。 包年包月和按量付费的共享带宽均支持加入。 | 通常加入共享带宽会立即生效，但可能由于网络等原因有一定的延时，请您耐心等待几分钟。 | 加入共享带宽会产生相关费用，具体计费规则请参见 [产品计费](https://help.aliyun.com/zh/internet-shared-bandwidth/product-overview/billing-overview/#concept-844578) 。 | 当前 ALB 实例带宽峰值不满足您的业务需求时，可以在负载均衡控制台选择加入共享带宽。 |
- 登录[应用型负载均衡](https://slb.console.aliyun.com/alb)[ALB](https://slb.console.aliyun.com/alb)[控制台](https://slb.console.aliyun.com/alb)。
在顶部菜单栏，选择实例所属的地域。
在实例页面，找到目标实例，选择以下任一方式加入共享带宽。
在操作列选择>加入共享带宽，或在共享带宽列单击加入。
单击目标实例ID，在实例详情页签，找到付费信息区域，单击加入共享带宽。
在加入共享带宽对话框，选择目标共享带宽，单击确认加入。
如没有可选的共享带宽，您可以在下拉框单击新建共享带宽购买共享带宽。建议您[购买后付费共享带宽](https://help.aliyun.com/zh/internet-shared-bandwidth/user-guide/create-an-internet-shared-bandwidth-instance#task-hjr-jlk-z2b)。
## 相关文档
[UpdateLoadBalancerZones](../developer-reference/api-alb-2020-06-16-updateloadbalancerzones.md)：修改应用型负载均衡实例可用区属性。
[UpdateLoadBalancerEdition](../developer-reference/api-alb-2020-06-16-updateloadbalanceredition.md)：修改应用型负载均衡版本。
[StartShiftLoadBalancerZones](../developer-reference/api-alb-2020-06-16-startshiftloadbalancerzones.md)：可用区DNS摘除。
[CancelShiftLoadBalancerZones](../developer-reference/api-alb-2020-06-16-cancelshiftloadbalancerzones.md)：可用区DNS恢复。
[AttachCommonBandwidthPackageToLoadBalancer](../developer-reference/api-alb-2020-06-16-attachcommonbandwidthpackagetoloadbalancer.md)：将共享带宽包绑定到负载均衡实例。
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
