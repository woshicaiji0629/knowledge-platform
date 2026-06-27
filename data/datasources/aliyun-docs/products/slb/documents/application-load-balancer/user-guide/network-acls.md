# 访问控制-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/network-acls

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/slb/documents/application-load-balancer/product-overview.md)

- [快速入门](products/slb/documents/application-load-balancer/getting-started.md)

- [操作指南](products/slb/documents/application-load-balancer/user-guide.md)

- [实践教程](products/slb/documents/application-load-balancer/use-cases.md)

- [开发参考](products/slb/documents/application-load-balancer/developer-reference.md)

- [服务支持](products/slb/documents/application-load-balancer/support.md)

[首页](https://help.aliyun.com/zh)

# 访问控制

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/slb)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ALB访问控制通过在监听上配置IP黑白名单，实现对客户端请求的精细化过滤。用户可以创建访问控制策略组，添加IP条目，并将策略组关联到监听来限制或放行特定来源的访问。

## 访问控制（ACL）与安全组如何选择

ALB提供两种访问控制机制：访问控制ACL和[安全组](products/slb/documents/application-load-balancer/user-guide/add-an-alb-instance-to-a-security-group.md)。

| 对比项 | 访问控制 ACL（本文） | ALB 安全组 |
| --- | --- | --- |
| 控制粒度 | 基于源 IP，作用于单个监听。 | 基于源 IP + 协议 + 端口，作用于整个 ALB 实例。 |
| IPv6 支持 | 不支持，仅可添加 IPv4 条目。 | 支持 IPv4 和 IPv6 地址。 |
| 默认行为 | 白名单模式自动拒绝未列入的 IP；黑名单模式自动放行未列入的 IP。 | 默认放通所有流量 ，必须显式添加拒绝规则（0.0.0.0/0）才能限制访问。 |
| 适用场景 | 简单 IP 黑白名单。配置简便，无需理解优先级规则。 | 需端口粒度控制、IPv6 控制、或 ICMP 协议控制的场景。 |


## 前提条件

已[创建](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[ALB](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)[实例](products/slb/documents/application-load-balancer/user-guide/create-and-manage-alb-instances.md)并[配置监听](products/slb/documents/application-load-balancer/user-guide/create-and-manage-listeners.md)。

## 创建访问控制策略组

访问控制策略组是IP条目的集合。创建策略组并添加IP条目后，可将其关联到监听以实现黑名单或白名单访问控制。

## 控制台

- 

前往ALB控制台的[访问控制](https://slb.console.aliyun.com/alb/cn-hangzhou/acls)页面，在顶部菜单栏选择目标实例所属地域，然后单击创建访问控制策略组。

- 

在创建访问控制策略组对话框，输入策略组名称，单击确定。

- 

策略组创建完成后，在访问控制页面，单击目标策略组ID进入详情页。在条目页签，通过以下方式添加IP条目：

- 

单个添加：单击添加条目，在对话框输入地址/地址段和备注，单击添加。

- 

批量添加：单击批量添加条目，按以下格式批量输入：

- 

每个条目一行，以回车分隔。

- 

IP地址或IP地址段与备注之间用竖线（|）分隔，例如192.168.1.0/24|备注。

- 

单次最多支持添加20个条目。

- 

如果批量添加的条目中包含策略组内已存在的条目，批量添加将失败，需移除重复条目后重新提交。

添加完成后，可在条目列表中删除或导出条目。

## API

- 

调用[CreateAcl](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-createacl.md)创建访问控制策略组。

- 

调用[AddEntriesToAcl](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-addentriestoacl.md)添加IP条目。

- 

调用[RemoveEntriesFromAcl](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-removeentriesfromacl.md)删除IP条目。

## 开启/关闭访问控制

用户可以为监听设置访问白名单或黑名单：

- 

白名单：仅允许策略组内的IP访问监听，拒绝其他所有请求。

- 

黑名单：拒绝策略组内的IP访问监听，放行其他所有请求。

重要

无论设置白名单还是黑名单，如果关联的策略组中没有任何IP条目，访问控制不会生效，监听将转发全部请求。设置白名单前请确认策略组内已包含需要放行的IP，避免阻断正常业务流量。

## 控制台

- 

前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，在顶部菜单栏选择目标实例所属地域，单击目标实例ID。

- 

在监听页签，找到目标监听，在访问控制列单击启用或关闭。

- 

启用：在对话框选择访问控制方式（白名单或黑名单）和访问控制策略组，单击保存。

- 

关闭：在确认对话框单击确定。

也可以在监听详情页的访问控制区域开启或关闭访问控制。

## API

- 

调用[AssociateAclsWithListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-associateaclswithlistener.md)将访问控制策略组关联到监听。

- 

调用[DissociateAclsFromListener](products/slb/documents/application-load-balancer/developer-reference/api-alb-2020-06-16-dissociateaclsfromlistener.md)解除访问控制策略组与监听的关联。

## 常见问题

配了白名单，任意IP仍能访问

原因：策略组未关联到监听；或策略组中没有添加任何IP条目（空策略组等同于全部放通）。

解决方案：进入ALB实例的监听页签，确认目标监听的访问控制列显示已开启，并确认关联的策略组中包含IP条目。

想临时全放通，添加0.0.0.0/0到白名单不生效

原因：访问控制策略组不支持添加0.0.0.0/0，控制台会提示格式错误。

解决方案：正确做法是直接[关闭访问控制](products/slb/documents/application-load-balancer/user-guide/network-acls.md)，需要时再开启。

配了黑名单，目标IP仍能访问

原因：请求经CDN/WAF转发到ALB，ALB看到的源IP是CDN/WAF的回源IP，而非客户端真实IP。

解决方案：ALB访问控制在四层生效，匹配的是请求报文的源IP地址。当请求经CDN/WAF转发时，源IP是CDN/WAF的回源IP，因此ALB层的黑名单无法拦截客户端IP。需要在WAF或CDN层配置黑名单。

黑名单无法拦截X-Forwarded-For中的IP

原因：ALB访问控制在四层生效，仅匹配请求报文的源IP地址，不解析七层HTTP头部中的X-Forwarded-For字段。

解决方案：可在 WAF 中通过[自定义规则](products/waf/documents/web-application-firewall-3-0/user-guide/configure-custom-rules-to-defend-against-specific-requests.md)实现：将匹配字段设为 X-Forwarded-For、逻辑符设为包含、匹配内容填写目标IP，规则动作设为拦截。参考[配置自定义规则中的匹配条件说明](products/waf/documents/web-application-firewall-3-0/user-guide/match-conditions.md)。

在后端Nginx配了allow/deny不生效

原因：经过ALB代理后，后端服务器收到的请求来源IP是ALB的Local IP（从ALB实例所在交换机分配的私网地址），Nginx的allow/deny基于来源IP判断，因此无法匹配客户端IP。

解决方案：

- 

（推荐）改用ALB访问控制功能，在ALB层直接配置IP黑白名单。

- 

在Nginx中通过X-Forwarded-For请求头[获取客户端真实](products/slb/documents/application-load-balancer/use-cases/preserve-client-ip-addresses.md)[IP](products/slb/documents/application-load-balancer/use-cases/preserve-client-ip-addresses.md)，再基于真实IP配置allow/deny规则。

想对单个域名或URL路径做访问限制

说明：访问控制ACL作用于监听级别，无法按域名或路径区分。开启后该监听下所有域名均受影响。

替代方案：标准版或WAF增强版ALB可通过转发规则实现——在转发条件中同时配置域名/路径和SourceIp条件，对匹配的请求返回固定响应（如403）。单条转发规则的SourceIp条件最多支持5个IP/CIDR段，且不支持0.0.0.0/x格式。如IP数量较多或使用基础版ALB，建议接入WAF，通过[自定义规则](products/waf/documents/web-application-firewall-3-0/user-guide/configure-custom-rules-to-defend-against-specific-requests.md)实现域名/路径与IP组合的访问控制。

想封禁国外IP

说明：ALB访问控制不提供地域封禁功能，无法自动识别IP所属国家。

替代方案：可以手动将已知国外IP段加入黑名单，但无法自动更新且条目数有上限。建议使用WAF的[区域封禁](products/waf/documents/web-application-firewall-3-0/user-guide/configure-region-blacklist-rules-to-block-requests-from-specific-regions.md)功能实现。

## 多层代理场景的访问控制

当ALB前存在七层代理时，ALB访问控制（四层生效）只能看到上一跳代理的回源IP，无法识别客户端真实IP，需在正确的层级配置访问控制。以CNAME接入WAF的场景为例（客户端 → CDN → WAF → ALB → ECS），各层的源IP和访问控制建议如下。

WAF增强版ALB通过SDK集成实现防护，WAF不参与流量转发，因此不存在WAF回源环节。如果ALB前无CDN等七层代理，则不存在本节描述的问题。

- 

- 

| 层级 | 看到的源 IP | 访问控制建议 |
| --- | --- | --- |
| WAF | 无 CDN 时为客户端真实 IP。 有 CDN 时为 CDN 回源 IP，需在 WAF 接入配置中设置 [客户端](products/waf/documents/web-application-firewall-3-0/user-guide/add-a-domain-name-to-waf-in-cname-record-mode.md) [IP](products/waf/documents/web-application-firewall-3-0/user-guide/add-a-domain-name-to-waf-in-cname-record-mode.md) [判定方式](products/waf/documents/web-application-firewall-3-0/user-guide/add-a-domain-name-to-waf-in-cname-record-mode.md) 以获取真实客户端 IP。 | 推荐在此层做 IP 黑白名单 。WAF 正确配置后可基于客户端真实 IP 进行拦截，同时支持地域封禁功能。 |
| ALB | WAF 的回源 IP。 | 在 ALB 配置白名单，仅允许 WAF 的回源 IP 段访问，防止攻击者绕过 WAF 直接访问 ALB 公网 IP。 [WAF](products/waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) [回源](products/waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) [IP](products/waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) [段](products/waf/documents/web-application-firewall-3-0/user-guide/faq-about-the-cloud-native-mode.md) 可在 WAF 控制台的 接入管理 页面查看。 |
| 后端 ECS | ALB 的 Local IP（从 ALB 实例所在交换机分配的私网地址）。 | 请确保后端 ECS 的 iptables 或其他第三方安全软件未屏蔽 ALB 的 Local IP 网段，否则健康检查和请求转发会失败。 |


## 计费

访问控制功能本身不产生额外费用。ALB实例的计费规则请参见[ALB](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)[计费说明](products/slb/documents/application-load-balancer/product-overview/alb-billing-rules.md)。

## 配额

| 限制项 | 功能版本 | 上限 |
| --- | --- | --- |
| 一个访问控制策略组可关联的监听数 | 基础版/标准版/WAF 增强版 | 50 |
| 一个监听可关联的访问控制策略组数 | 基础版/标准版/WAF 增强版 | 3 |
| 一个地域可支持的访问控制策略组数 | 基础版/标准版/WAF 增强版 | 1000 |
| 一个访问控制策略组可添加的条目数 | 基础版/标准版/WAF 增强版 | 500 |
| 一个 ALB 实例可关联的访问控制条目数 | 基础版/标准版/WAF 增强版 | 800 |
| 一个监听可关联的访问控制条目数 | 基础版 | 300 |
| 标准版/WAF 增强版 | 500 |  |


上述指标为硬限制，无法提升，详见[ALB](products/slb/documents/application-load-balancer/product-overview/quotas-and-limits.md)[配额与限制](products/slb/documents/application-load-balancer/product-overview/quotas-and-limits.md)。

[上一篇：ALB加入安全组](products/slb/documents/application-load-balancer/user-guide/add-an-alb-instance-to-a-security-group.md)[下一篇：使用资源组进行精细化资源控制](products/slb/documents/application-load-balancer/user-guide/fine-grained-resource-control-using-resource-groups-2.md)

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
