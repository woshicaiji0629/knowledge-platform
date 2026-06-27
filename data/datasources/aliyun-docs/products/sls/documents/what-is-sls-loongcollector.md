# 采集处理路由发送可观测性数据-LoongCollector-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/what-is-sls-loongcollector/

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# LoongCollector介绍

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

LoongCollector 是日志服务推出的一款集性能、稳定性和可编程性于一身的新一代数据采集器，专为构建下一代可观测 Pipeline 设计。LoongCollector扩展融合了可观测性技术栈，改变传统日志采集器的单一场景限制，支持Logs、Metrics、Traces、Events、Profiles 的采集、处理、路由、发送等功能。

重要

LoongCollector目前支持在公有云的所有地域安装，但金融云和政务云暂不支持。

## LoongCollector采集场景

LoongCollector采集根据不同的采集数据源，主要分为以下使用方式：

- 

[持续采集主机文本日志](products/sls/documents/host-text-log-collection-auto-install.md)：采集主机中的文件日志。

- 

[Kubernetes](products/sls/documents/container-log-collection-in-a-kubernetes-cluster.md)[集群容器日志采集](products/sls/documents/container-log-collection-in-a-kubernetes-cluster.md)：采集集群中的日志。

- 

[采集](products/sls/documents/collect-http-data.md)[HTTP](products/sls/documents/collect-http-data.md)[数据](products/sls/documents/collect-http-data.md)：采集HTTP前端数据Body内容。

- 

[采集](products/sls/documents/retrieving-sql-query-results.md)[SQL](products/sls/documents/retrieving-sql-query-results.md)[查询结果](products/sls/documents/retrieving-sql-query-results.md)：采集SQL查询结果。

更多采集场景请参考[日志数据采集（Log）](products/sls/documents/sls-log-collection.md)。

## 核心优势

### 端上采集融合

LoongCollector支持所有的采集工作只用一个Agent实现，包括Logs、Metrics、Traces、Events、Profiles 的采集、处理、路由、发送等功能。且对于K8s，LoongCollector 基于标准 CRI API 与 Pod 的底层定义进行交互，让您无需变更容器配置，即可自动为采集的可观测性数据附加 K8s 元数据标签（如 Namespace、Pod、Container、Labels 等），实现数据与基础设施的精准关联。

### 灵活的可编程管道

LoongCollector 通过 SPL 与多语言 Plugin 引擎加持，构建完善的可编程体系。不同引擎可以相互打通，通过灵活的组合实现预期的计算能力。

您可根据自身需求灵活选择引擎。如果看重执行效率，可以优先选择原生插件，辅以扩展插件；如果看重算子覆盖全面性，需要处理复杂数据，可以选择 SPL 引擎。

| 可编程引擎 | 分类 | 特点 |
| --- | --- | --- |
| [多语言 Plugin 引擎](products/sls/documents/processing-plug-ins.md) | 原生插件 | C++实现，性能高，资源开销低，较完善的算子能力。 |
| 扩展插件 | Golang 实现，较高的性能，资源开销低，较完善的算子能力。 |  |
| [SPL](products/sls/documents/spl-overview.md) [引擎](products/sls/documents/spl-overview.md) | SPL 引擎 | C++实现，列式模型，向量化执行，性能高，资源开销低，全面的算子能力，100+算子，管道式设计，灵活组合，可以处理复杂数据。 |


### 高性能与高可靠

LoongCollector的底层设计支持高性能与高可靠，为大规模分布式系统提供稳固、高效的可观测性数据统一采集。

- 

高性能：核心流程无锁设计、事件驱动机制、核心场景单线程百M/s吞吐量。

- 

高可靠：基于时间片公平调度、队列高低水位反压控制、实现Pipeline之间多租户隔离、数据流免拷贝机制保障内存资源。

- 

大规模生产级标准：商业版千万级部署规模，广泛应用于阿里集团、蚂蚁集团及公有云客户，经受各类线上大促销、极端场景考验。

[上一篇：LoongCollector数据采集器（原Logtail）](products/sls/documents/loongcollector-management.md)[下一篇：LoongCollector发布历史](products/sls/documents/loongcollector-release-history.md)

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
