# Project、LogStore、机器组、日志组、告警等资源的使用限制-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/basic-resources

# 基础资源使用限制
本文介绍项目（Project）、日志库（LogStore）、机器组（MachineGroup）、日志组（LogGroup）、告警等资源的使用限制。
说明
扩容操作本身不收取费用，但扩容后的资源将按照[标准价格](billing-overview.md)进行计费。
扩容操作请参见[管理资源配额](manage-a-project.md)。
## 基础资源上限
| Quota 指标 | 指标说明 | 默认值 | 可调整上限 |
| --- | --- | --- | --- |
| project 上限 | 一个阿里云账号下最多可创建 150 个 Project。 | 150 |  |
| LogStore 上限 | 一个 Project 中最多可创建的 LogStore 数量。 | 200 | 400 |
| shard 上限 | 一个 Project 中最多可创建 Shard 数量。 | 400 | 800 |
| logtail 采集配置上限 | 一个 Project 中最多可创建 Logtail 配置数量。 | 200 | 400 |
| 机器组上限 | 一个 Project 中最多可创建机器组数量。 | 200 | 400 |
| 仪表盘上限 | 一个 Project 中最多可创建仪表盘数量。 | 100 | 400 |
| 仪表盘中图表上限 | 一个仪表盘最多可包含统计图表数量。 | 200 | 400 |
| 快速查询上限 | 一个 Project 中最多可创建快速查询数量。 | 100 | 400 |
| 导出任务上限 | 一个 Project 中最多可创建导出任务数量。 | 100 | 400 |
| 导入任务上限 | 一个 Project 中最多可创建导入任务数量。 | 100 | 400 |
| 定时 SQL 上限 | 一个 Project 中最多可创建定时 SQL 数量。 | 100 | 400 |
| 加工任务上限 | 一个 Project 中最多可创建加工任务数量。 | 100 | 400 |
| 告警上限 | 一个 Project 中最多可创建告警数量。 | 100 | 400 |
| 订阅任务上限 | 一个 Project 中最多可创建订阅任务数量。 | 100 | 400 |
| project 写入流量上限（GB/min） | 一个 Project 在 1 分钟内所有 LogStore 写入流量的总和。 | 100 | 200 |
| project 写入次数上限（万次/min） | 一个 Project 在 1 分钟内所有 LogStore 写入次数的总和。 | 60 | 200 |
| project 读取次数上限（万次/min） | 一个 Project 在 1 分钟内所有 LogStore 读取次数的总和。 | 60 | 200 |
## LogStore使用限制
按写入数据量计费模式支持完整日志服务功能集合，增值功能如查询分析、数据加工、智能告警、消费投递等能力均不产生额外费用，但存在配额限制，具体说明如下。
| 配额限制 | 说明 |
| --- | --- |
| 数据加工量 | 单个 LogStore 每月支持的最大加工数据量为 100 TB。 |
| 定时 SQL 数据量 | 单个 LogStore 每月支持的定时 SQL 数据量为 20 TB。 |
| 投递数据量 | 单个 LogStore 每月支持的投递数据量为 100 TB。 |
| 消费数据量 | 单个 LogStore 每月支持的消费数据量为 100 TB。 |
| 告警作业计算数据量 | 单个 LogStore 每月支持的告警作业计算数据量为 100 TB。 |
## 读写数据限制
| 类别 | 限制项 | 说明 | 备注 |
| --- | --- | --- | --- |
| [Project](manage-a-project.md) | 写入流量 | 原始数据写入流量最大为 100GB/min。 | 超过限制时，返回状态码 403，提示 Inflow Quota Exceed。 |
| 写入次数 | 写入次数最大为 600000 次/min。 | 超过限制时，返回状态码 403，提示 Write QPS Exceed。 |  |
| 读取次数 | 读取次数最大为 600000 次/min。 | 超过限制时，返回状态码 403，提示 Read QPS Exceed。 |  |
| [Shard](manage-shards.md) | 写入流量 | 每个 Shard 支持 5MB/s 的数据写入。 | 非硬性限制。超过限制时，系统会尽可能提供服务，但不保证服务质量。 |
| 写入次数 | 写入次数最大为 500 次/s。 | 非硬性限制。超过限制时，系统会尽可能提供服务，但不保证服务质量。 |  |
| 读取流量 | 读取流量最大为 20 MB/s。 | 非硬性限制。超过限制时，系统会尽可能提供服务，但不保证服务质量。 |  |
| 读取次数 | 读取次数最大为 100 次/s。 | 非硬性限制。超过限制时，系统会尽可能提供服务，但不保证服务质量。 |  |
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
