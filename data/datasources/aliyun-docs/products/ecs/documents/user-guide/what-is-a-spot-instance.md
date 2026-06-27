# 使用闲置库存的实例-抢占式实例-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/what-is-a-spot-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 什么是抢占式实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

抢占式实例（旧称竞价实例）是一种使用阿里云闲置库存的实例，性能与常规ECS实例无异，价格根据市场供需关系实时变化，相对于按量付费实例规格最高能节约90%的成本。抢占式实例在库存资源充足时可以被获取并使用，在库存资源不足时被中断回收。

## 适用场景

抢占式实例旨在为短期任务和高容错性应用提供经济高效的计算资源，如果您可以灵活控制应用程序的运行时间或者应用程序可以容忍中断，那么抢占式实例对您来说是经济实惠的选择，抢占式实例适用于无状态、容错能力强、中断容忍度高的业务场景。例如：

- 

实时分析业务

- 

大数据业务

- 

地理空间勘测分析业务

- 

图像和媒体编码业务

- 

科学计算业务

- 

可弹性伸缩的业务站点、网络爬虫业务

- 

测试业务

- 

其他无状态业务场景

重要

对于有状态、需要长时间作业或稳定性要求较高的业务场景，如数据库服务、持续运行的任务等，不建议使用抢占式实例。

## 运行流程

创建抢占式实例时，您需要对资源进行出价，当出价≥市场价格且库存充足时，您将成功获取实例并使用。在一段时间内，您可以稳定使用实例，实例的稳定使用时长和您设置的实例使用时长有关，超出稳定使用时长后，当出价<市场价格或库存不足时，触发中断回收，实例将在5分钟后被释放。

出价：跟设置的单台实例上限价格（即出价模式）有关，是您愿意为所选购的抢占式实例支付的最高价格（非实际计费价格）。

出价模式：

- 

使用自动出价：出价=市场价格，即实例使用期间的价格始终和市场价格保持一致，随市场价格实时波动，可以保证实例不会因价格浮动因素被中断回收，但不能保证实例因库存不足的因素被中断回收。

- 

设置单台上限价：出价=设置的单台价格上限，即设置单台可接受的最高价，价格越高，持有抢占式实例机会越大，当出价低于市场价或库存不足时，实例被中断回收。

实例使用时长：

- 

设定使用实例1小时：阿里云保障您的实例在创建后1小时之内不被中断回收，即创建实例后1小时内不受检测机制影响。

- 

无确定使用时长：没有使用时长保障，实例创建后会受检测机制影响，这意味着您的实例可能随时会被中断回收。

## 三大特点

### 中断回收

抢占式实例的中断回收不可避免，您可以根据自身业务场景设置实例使用时长和单台实例上限价格，以平衡成本与实例的持续运行时间，同时您也可以选择不同的实例中断模式来决定如何恢复或处理实例。

实例中断模式

- 

直接释放：触发中断回收时，您的实例将被直接释放，包括计算资源（vCPU、GPU和内存）、固定公网IP、固定带宽以及云盘（系统盘和数据盘）。

- 

节省停机：触发中断回收时，实例进入节省停机模式，计算资源（vCPU、GPU和内存）、固定公网IP和固定带宽被回收，云盘（系统盘和数据盘）、弹性公网IP、快照等资源保留并继续收费。抢占式实例进入节省停机模式后，可能会因为库存不足或者价格浮动超过出价而重启失败。

说明

实例中断模式在抢占式实例创建后不支持修改。

中断回收相关建议

- 

数据保留：您可以在新购抢占式实例时，设置实例中断模式为节省停机或者设置云盘（系统盘和数据盘）不随实例释放，抢占式实例中断回收后数据会保留。更多信息，请参见[抢占式实例数据保留和恢复](products/ecs/documents/user-guide/preemptible-instance-data-retention-and-data-recovery-after-interrupt-reclamation.md)。

- 

感知中断与响应：您可以通过云监控订阅中断回收事件或者通过OpenAPI查询实例状态等方式来感知中断回收。更多信息，请参见[感知抢占式实例中断事件与响应](products/ecs/documents/user-guide/query-the-interruption-events-of-preemptible-instances.md)。

### 市场价格浮动

市场价格：指的是实例规格的价格，不包括云盘、公网带宽等资源的价格。

说明

下文以华东1（杭州）地域的实例ecs.hfg5.8xlarge为例，按量付费实例原价和抢占式实例折扣力度可能变化，价格以购买页面为准，此处仅为示例。

- 

- 

| 抢占式实例的市场价格会随供需变化而浮动。 同一地域，不同可用区下，同一实例规格的抢占式实例市场价格存在差异。 |  |
| --- | --- |


### 折扣低至1折

说明

下文以华东1（杭州）地域的实例ecs.hfg5.8xlarge为例，按量付费实例原价和抢占式实例折扣力度可能变化，价格以购买页面为准，此处仅为示例。

- 

- 

| 抢占式实例有折扣，价格最低为按量付费实例规格的 10%，最高为按量付费实例规格原价。 相比于 设定实例使用 1 小时，无确定使用时长 的抢占式实例更优惠。 |  |
| --- | --- |


## 如何创建抢占式实例

您可以通过ECS控制台、API或Terraform等方式创建抢占式实例。更多信息，请参见[创建抢占式实例](products/ecs/documents/user-guide/create-a-spot-instance.md)。

## 使用限制

- 

抢占式实例不支持转换为按量付费和包年包月实例。

- 

抢占式实例不支持变更实例规格。

- 

抢占式实例不支持备案服务。

## 计费相关

计费规则：请参见[抢占式实例](products/ecs/documents/spot-instance.md)。

账单查询：请参见[查看抢占式实例账单](products/ecs/documents/view-billing-details.md)。

## 进阶使用

考虑到实际资源使用场景，在提升资源自动运维层面，建议您搭配阿里云的弹性伸缩、弹性供应组或者容器服务ACK使用抢占式实例。

- 

弹性伸缩：根据业务需求和策略自动调整计算能力（即实例数量）。请参见[在伸缩组使用抢占式实例降低成本](https://help.aliyun.com/zh/auto-scaling/use-cases/cost-reduction-by-using-preemptible-instances)。

- 

弹性供应组：弹性供应组是一种快速交付ECS实例集群的方案，简单配置后即可自动在多个可用区内交付不同计费方式（按量付费和抢占式实例）、多种实例规格的实例集合，提升批量交付大量实例的效率。请参见[弹性供应组配置示例](products/ecs/documents/user-guide/configure-an-auto-provisioning-group.md)。

- 

容器服务 ACK：提供高性能可伸缩的容器应用管理服务，支持企业级Kubernetes容器化应用的生命周期管理。请参见以下文档：

- 

[使用抢占式](products/ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[ECI](products/ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[实例运行](products/ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[Job](products/ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)[任务](products/ack/documents/serverless-kubernetes/use-cases/run-jobs-on-a-preemptible-instance-1.md)

- 

[抢占式实例节点池最佳实践](https://help.aliyun.com/zh/document_detail/410889.html)

- 

[基于抢占式实例的弹性训练](products/ack/documents/cloud-native-ai-suite/user-guide/elastic-training-based-on-preemptive-instances.md)

- 

[抢占式实例节点池最佳实践](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/best-practices-for-preemptible-instance-based-node-pools.md)

## 常见问题

更多有关抢占式实例问题，请参见[实例](products/ecs/documents/user-guide/instance-faq.md)[FAQ](products/ecs/documents/user-guide/instance-faq.md)。

[上一篇：抢占式实例](products/ecs/documents/user-guide/preemptible-instances.md)[下一篇：抢占式实例Advisor](products/ecs/documents/user-guide/spot-instance-advisor.md)

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
