# 如何选购日志服务资源包-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/purchase-a-resource-plan

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

# 选购资源包

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍选购日志服务资源包的操作步骤。

## （推荐）购买新版资源包

- 

打开[日志服务预付计划](https://common-buy.aliyun.com/?commodityCode=sls_plan_bag#/buy)[2.0](https://common-buy.aliyun.com/?commodityCode=sls_plan_bag#/buy)[购买页面](https://common-buy.aliyun.com/?commodityCode=sls_plan_bag#/buy)。

- 

在日志服务预付计划2.0页面，选择资源包的规格、购买数量和购买时长。

日志服务资源包提供多种规格。如何选择，请参见[如何选择资源包规格](products/sls/documents/how-do-i-select-a-quota-for-a-resource-plan.md)。

- 

单击立即购买。

- 

根据页面提示，完成支付。

## 购买旧版资源包

- 

打开[日志服务旧版资源包购买页面](https://common-buy.aliyun.com/?spm=5176.8066851.323083.pricedetail1111.4256252ekHO2aT&commodityCode=slsbagflow#/buy)。

- 

选择商品类型。

旧版资源包仅覆盖如下三种计费项，其余计费项需通过按量后付费方式进行付费。

重要

索引流量包、读写流量包和存储包仅支持日志数据（LogStore），不支持时序数据（MetricStore）。

- 

读写流量包用于抵扣读写流量计费项。

- 

索引流量包用于抵扣索引流量-日志索引计费项。

- 

存储包用于抵扣存储空间-日志存储计费项。

- 

选择规格、购买数量和购买时长。

- 

根据页面提示，单击立即购买，完成支付。

## 选购示例

某客户每天的日志服务使用量为2个Shard、100 GB读写流量、400 GB索引流量、存储数据稳定在10000 GB。具体费用如下：

| 计费项 | 说明 |
| --- | --- |
| 读写流量 | 100 GB×0.18 元/GB=18 元 |
| 索引流量-日志索引 | 400 GB×0.35 元/GB=140 元 |
| 存储空间-日志存储 | 10000 GB×0.0115 元/GB/天=115 元 |
| 活跃 Shard 租用 | 2 个*0.04 元=0.08 元 说明 当您在创建 LogStore 时配置 Shard 数量 为 2 时，表示您每天租用 2 个 Shard，每月（按 30 天计算）使用量为 60 Shard*天。 |


重要

资源包价格以控制台实际优惠价格为准。

| 计费周期 | 按量付费 | 一年期包月计划 | 节省费用 |
| --- | --- | --- | --- |
| 每月费用 | （18+140+115+0.08）元*30 天=8192.4 元 说明 根据每月费用，选择合适的包月计划。本案例推荐选择 8 个 1000 CU/月和 2 个 100 CU/月。 | 购买 8 个 1000 CU/月和 2 个 100 CU/月的一年期资源包，详细费用说明如下： 8*8520 元/12 个月+2*900 元/12 个月=5830 元 | 如果您购买一年期的资源包，则相比按量付费，每月可节省的费用：8192.4 元-5830 元=2362.4 元 |
| 一年总费用 | （18+140+115+0.08）元*30 天*12 个月=98308.8 元 | 购买 8 个 1,000 CU/月和 2 个 100 CU/月的一年期资源包，详细费用说明如下： 8*8520 元+2*900 元=69960 元 | 如果您购买一年期的资源包，则相比按量付费，每年可节省的费用：98308.8 元-69960 元=28348.8 元 |


[上一篇：资源包介绍](products/sls/documents/overview-11.md)[下一篇：资源包续费指南](products/sls/documents/renew-a-resource-plan.md)

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
