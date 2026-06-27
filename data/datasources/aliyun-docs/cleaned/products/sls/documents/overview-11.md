# 资源包类型与计费抵扣规则-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/overview-11

# 资源包介绍
预先购买资源包，在费用结算时，优先从资源包抵扣用量。本文介绍资源包的基本信息。
## 资源包
日志服务提供如下资源包。
重要
当您拥有新版资源包和旧版资源包（读写流量包、索引流量包和存储包）时，优先抵扣旧版资源包。
| 资源包 | 说明 |
| --- | --- |
| 新版 资源包-预付计划 2.0（推荐） | 支持抵扣日志服务中所有计费项。 说明 在有效期内，每月拥有相同的资源额度。每月月底清零，次月恢复。 |
| 旧版资源包-存储包 | 仅用于抵扣 存储空间-日志存储 计费项所产生的费用。 |
| 旧版资源包-索引流量包 | 仅用于抵扣 索引流量-日志索引 计费项所产生的费用。 |
| 旧版资源包-读写流量包 | 仅用于抵扣 读写流量 计费项所产生的费用。 |
## 新版资源包-预付计划2.0（推荐）
资源包支持抵扣日志服务中所有计费项。规格越大、包年期时长越长，价格优惠力度越大。系统每天会统计您使用的日志服务用量，在资源包额度范围内直接抵扣。在有效期内，每月有相同的资源额度。当月额度用完后，自动转为按量付费方式。
重要
新版资源包的优先级高于节省计划，如果同时拥有两者，则优先抵扣新版资源包。
同时支持按使用功能计费模式和按写入数据量计费模式。
日志服务新版资源包的包年计划（1年期及以上版本），根据规格大小给予不同的折扣优惠，具体折扣以购买页面为准。按量付费方式的定价无变化，只有购买新版资源包（1年期及以上版本），才享受预付计划2.0的优惠策略。
阿里云在您购买新版资源包时一次性收取费用。例如您要购买1年期、100 CU的新版资源包，则阿里云将在您购买当天一次性收取1年的费用。
新版资源包的规格单位为资源额度CU（Cost Unit）。
资源包支持按使用功能计费模式和按写入数据量计费模式。
每个计费项抵扣消耗资源包额度（CU）的比例，与该计费项的按量付费的单价完全一致。例如公共云日志服务的读写流量的按量付费价格为0.18元/GB，则每GB读写流量，抵扣0.18个CU，详细信息如下表所示：
## 按使用功能计费
| 计费项 | 公共云版本 | 金融云版本 |
| --- | --- | --- |
| 读写流量（每 GB） | 0.18 CU | 0.342 CU |
| 索引流量-日志索引（每 GB） | 0.35 CU | 0.665 CU |
| 索引流量-日志索引-查询型（每 GB） | 0.1 CU | 0.19 CU |
| 存储空间-日志热存储（每 GB/天） | 0.0115 CU | 0.02185 CU |
| 存储空间-日志低频存储（每 GB/天） | 0.005 CU | 0.0095 CU |
| 存储空间-日志归档存储（每 GB/天） | 0.0017CU | 0.00323 CU |
| 索引流量-时序索引（每 GB） | 0.2 CU | 0.38 CU |
| 存储空间-时序存储（每 GB/天） | 0.0035 CU | 0.00665 CU |
| 数据加工（每 GB） | 0.15 CU | 0.285 CU |
| 投递数据到 OSS 基础版（JSON 或 CSV 格式）（每 GB） | 0.05 CU | 0.095 CU |
| 投递数据到 OSS 高级版（Parquet 或 ORC 格式）（每 GB） | 0.2 CU | 0.38 CU |
| 投递数据到 MaxCompute（每 GB） | 0.2 CU | 0.38 CU |
| 投递数据到 AnalyticDB MySQL 版（每 GB） | 0.2 CU | 0.38 CU |
| 投递数据到云原生多模数据库 Lindorm（每 GB） | 0.200 元/GB | 0.380 元/GB |
| 电话告警通知（每次） | 0.15 CU | 0.285 CU |
| 短信告警通知（每次） | 0.05 CU | 0.095 CU |
| SQL 独享版（每核×小时） | 0.35 CU | 0.665 CU |
| 扫描流量 | 0.05 CU | 0.095 CU |
| 活跃 Shard 租用（每天） | 0.04 CU | 0.076 CU |
| 读写次数（每百万次） | 0.12 CU | 0.228 CU |
| 外网读取流量（每 GB） | 0.8 CU | 1.52 CU |
## 按写入数据量计费
| 计费项 | 公共云版本 | 金融云版本 |
| --- | --- | --- |
| 原始写入数据量（每 GB） | 0.4 CU | 0.76 CU |
| 存储空间-日志热存储（每 GB/天） | 0.0115 CU | 0.02185 CU |
| 存储空间-日志低频存储（每 GB/天） | 0.005 CU | 0.0095 CU |
| 存储空间-日志归档存储（每 GB/天） | 0.0017 CU | 0.00323 CU |
| 外网读取流量（每 GB） | 0.8 CU | 1.52 CU |
## 旧版资源包-存储包
存储包仅用于抵扣存储空间-日志存储计费项所产生的费用。系统每天会统计您使用的日志存储量，如果没有存储包的容量大小则不会产生费用，超出部分使用按量付费方式。
存储包支持叠加购买，存在多个存储包时，按照购买时间进行抵扣。
## 旧版资源包-索引流量包
索引流量包仅用于抵扣索引流量-日志索引计费项所产生的费用。系统每天会统计您使用的日志索引流量，如果没有超出索引流量包的容量大小则不会产生费用，超出部分使用按量付费方式。
索引流量包支持叠加购买，存在多个索引流量包时，按照购买时间进行抵扣。
## 旧版资源包-读写流量包
读写流量包仅用于抵扣读写流量计费项所产生的费用。系统每天会统计您使用的读写流量，如果没有超出读写流量包的容量大小，则不会产生费用，超出部分使用按量付费方式。
读写流量包支持叠加购买，存在多个读写流量包时，按照购买时间进行抵扣。
## 新旧版资源包对比
新版资源包
支持抵扣日志服务中所有计费项。包括存储、索引流量、读写流量、请求、加工、投递、告警通知（短信、电话）等。具有易管理、易使用、全覆盖等优势。
## 按使用功能计费
## 按写入数据量计费
旧版资源包
包括存储包、索引流量包和读写流量包。单计费项资源包模式存在难管理、覆盖不全、购买复杂等问题。
重要
日志存储空间包、日志索引流量包和读写流量包仅支持日志数据（Logstore），不支持时序数据（MetricStore）。
## 常见问题
### 购买资源包
[如何选择资源包规格？](how-do-i-select-a-quota-for-a-resource-plan.md)
[为什么购买资源包后，当月的日志服务消费额暴涨？](why-do-fees-significantly-increase-in-the-month-when-i-purchase-a-resource-plan.md)
[购买资源包后，多久生效？](when-does-a-resource-plan-take-effect-after-i-purchase-it.md)
[为什么购买了资源包仍会欠费？](why-do-i-have-overdue-payments-even-if-i-purchase-a-resource-plan.md)
[资源包额度不够用怎么办？](what-do-i-do-if-the-quota-of-a-resource-plan-is-insufficient.md)
[资源包购买页没有所需的资源包规格怎么办？](what-do-i-do-if-i-cannot-find-a-resource-plan-that-i-require.md)
### 使用资源包
[新旧版资源包的抵扣顺序是怎样的？](what-is-the-offset-order-of-the-new-and-old-resource-plans.md)
[为什么资源包的余量显示为-或者余量保持不变？](why-is-the-remaining-quota-of-a-resource-plan-displayed-as-or-remains-unchanged.md)
[已经产生的欠费是否可以购买资源包进行抵扣？](can-i-purchase-a-resource-plan-to-offset-overdue-payments.md)
[超出资源包使用额度后，如何计费？](how-am-i-charged-if-the-quota-of-a-resource-plan-is-exceeded.md)
[为什么](why-the-quota-of-a-one-year-resource-plan-is-used-up-in-one-month.md)[1](why-the-quota-of-a-one-year-resource-plan-is-used-up-in-one-month.md)[年期的资源包，1](why-the-quota-of-a-one-year-resource-plan-is-used-up-in-one-month.md)[个月就被用完了？](why-the-quota-of-a-one-year-resource-plan-is-used-up-in-one-month.md)
### 查看资源包明细
[如何查看资源包使用明细？](how-do-i-view-the-usage-details-of-my-resource-plans.md)
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
