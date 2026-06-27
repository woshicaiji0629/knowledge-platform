# 资源流控超限报错的解决方案-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/expansion-of-resources

# 资源流控及解决方案
日志服务包含Project、Logstore、Shard等资源概念，为保证云上多租户更可靠的QoS服务质量，每种资源会设置相关的资源流控限制。当您使用的日志服务资源出现流控报错时，您可能会遇到一些非预期行为，例如API返回错误、资源创建失败、数据上传失败等。本文介绍主要的日志服务资源流控报错及对应的解决方案。
## 发现流控
您可以使用日志服务CloudLens for SLS监控各种资源的使用水位和流控异常事件，当触发告警后，您可以及时进行相应地处理。具体操作，请参见[使用](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[CloudLens for SLS](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[监控](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[Project](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)[资源配额](use-cloudlens-for-sls-to-monitor-project-resource-quotas.md)。
## 应对方案
当您遇到如下资源流控报错时，请根据对应的解决方案进行处理。
| 分类 | 超限说明 | 解决方案 |  |
| --- | --- | --- | --- |
| 写入超限 | WriteQuotaExceed（Project 级别超限） | Project 写流量：Project write quota exceed: inflow: xxx Project 写次数：Project write quota exceed: qps: xxx | 在 [日志服务控制台](https://sls.console.aliyun.com) 调整资源配置。具体操作，请参见 [调整资源配额](adjust-resource-quotas.md) 。 |
| ShardWriteQuotaExceed（Shard 级别超限） | Shard 写：shard write quota exceed, please split shard（所有可用 Shard 写入都超过限制） Shard 写：shard write quota exceed, shard: xxx | 使用手动或自动分裂方式新增 Shard。具体操作，请参见 [管理](manage-shards.md) [Shard](manage-shards.md) 。 |  |
| 读取超限 | ShardReadQuotaExceed（Shard 级别超限，Project 级别没有限制读） | Shard 读次数：shard read qps exceed quota limits Shard 读流量：shard read bytes exceed quota limits | 使用手动或自动分裂方式新增 Shard。具体操作，请参见 [管理](manage-shards.md) [Shard](manage-shards.md) 。 |
| 资源创建超限 | ProjectQuotaExceed | Logstore 数量：project xxx logstore count quota exceed Project 数量： Account <aliuid> most has <project quota> project Shard 数量： project <project name>, shard count quota exceed | 在 [日志服务控制台](https://sls.console.aliyun.com) 调整资源配置。具体操作，请参见 [调整资源配额](adjust-resource-quotas.md) 。 |
| 请求类超限 | 仪表盘数量超限 | dashboard quota exceed | 在 [日志服务控制台](https://sls.console.aliyun.com) 调整资源配置。具体操作，请参见 [调整资源配额](adjust-resource-quotas.md) 。 |
| SQL 分析请求超过并发限制 | user can only run 15 query concurrently Too many queued queries | 检查业务本身压力是否有异常或因实现逻辑出现的无效忙请求。 如果确实有更高并发需求，请 [提工单](https://selfservice.console.aliyun.com/ticket/category/sls/today) 申请，日志服务将协助提升 SQL 并发能力。 |  |
| 其他配置资源创建超限 | QuotaExceed | Logtail 采集配置数量：project config count exceed quota 机器组数量：project machine group count exceed quota 告警数量：Alert count exceeds the maximum limit | 在 [日志服务控制台](https://sls.console.aliyun.com) 调整资源配置。具体操作，请参见 [调整资源配额](adjust-resource-quotas.md) 。 |
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
