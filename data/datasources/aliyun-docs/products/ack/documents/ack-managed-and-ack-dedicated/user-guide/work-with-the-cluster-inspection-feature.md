# 执行集群巡检以发现集群潜在风险并获取解决方案-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/work-with-the-cluster-inspection-feature

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 使用集群巡检

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

容器智能运维平台提供集群巡检功能，支持扫描集群运行状况，发现集群中存在的潜在风险并提供对应的解决方案，例如云资源配额余量、Kubernetes集群关键资源水位等检查。

## 操作步骤

在使用集群巡检功能前，请确保集群处于正常运行状态。集群巡检仅保留最近7天的结果。

在[容器服务管理控制台](https://cs.console.aliyun.com)的集群列表，查看目标集群的集群状态是否处于运行中。

重要

使用集群巡检功能时，系统将在您的集群中执行数据采集程序并收集检查结果。采集的信息包括系统版本、负载、运行时、kubelet等运行状态及系统日志中关键错误信息。数据采集程序不会采集您的业务信息及敏感数据。

- 

登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择巡检和诊断>集群巡检。

- 

在集群巡检页面的巡检规则区域，单击添加。

- 

在配置定时巡检规则面板，设置相应的时区和定时规则（每天），仔细确认集群信息和注意事项后，按照页面提示保存配置。

集群定时巡检配置完成后，将按照指定的时间巡检集群。您也可以在集群巡检页面的检查报告列表区域，单击执行巡检检查，手动巡检集群。

- 

巡检完成后，在集群巡检页面的检查报告列表区域右侧的操作列，单击目标检查报告右侧的查看详情。

- 

集群巡检会按照触发风险的程度分为低危、中危和高危，并高亮显示。

- 

巡检检查报告包含风险级别、风险项名称、异常影响及解决方案。您可以参见控制台指引了解并解决问题。

## 相关操作

订阅巡检报告

集群巡检支持订阅巡检结果。您可以在集群巡检页面的订阅巡检报告区域，访问[智能顾问控制台](https://advisor.console.aliyun.com/products?product=ack)，配置订阅巡检报告。

管理巡检规则

集群定时巡检配置完成后，您可以在巡检规则区域进行以下操作。

- 

单击编辑，设置新的巡检规则。

- 

单击删除，删除无需使用的巡检规则。规则删除后，集群将不再按此规则巡检。

## 相关文档

- 

[集群检查](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-cluster-check.md)功能支持在集群升级、迁移等操作前执行检查，确认集群是否符合要求。

- 

[集群诊断](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-cluster-diagnostics.md)功能支持节点诊断、Pod诊断、Service诊断、Ingress诊断、内存诊断、网络诊断等功能，辅助定位集群问题。

[上一篇：集群检查项及修复方案](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)[下一篇：使用集群诊断](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/work-with-cluster-diagnostics.md)

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
