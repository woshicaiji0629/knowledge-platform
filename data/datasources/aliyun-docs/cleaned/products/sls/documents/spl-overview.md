# SPL语言概述工作原理与使用限制-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/spl-overview

# SPL语法
本文介绍日志服务SPL语言的基本信息，包括工作原理、语法、指令表达式等。
## SPL概述
对于读取出的原始数据，日志服务提供SPL语句（SLS Processing Language）做结构化信息提取、字段操作和数据过滤等操作。另外，日志服务还提供多级管道级联功能，第一级管道是索引过滤条件，后面的多级管道是SPL指令，最终输出经过SPL处理后的结果数据。如果您了解SQL语言的使用，您在不同数据处理需求场景中使用日志服务SPL时，可以参考[SPL](spl-usage-scenario-vs-sql.md)[与](spl-usage-scenario-vs-sql.md)[SQL](spl-usage-scenario-vs-sql.md)[的使用场景对照](spl-usage-scenario-vs-sql.md)。
## 工作原理
日志服务SPL支持在[Logtail](use-logtail-spl-to-parse-logs.md)[采集](use-logtail-spl-to-parse-logs.md)、[写入处理器](ingest-processor-quick-start.md)、[基于规则消费](overview-of-rule-based-consumption.md)、[数据加工（新版）](data-processing-new-edition-overview.md)、[扫描模式查询与分析（Scan）](query-and-analyze-logs-in-scan-mode.md)等日志服务功能中使用，工作原理如下图：
说明
关于SPL在各个场景中的功能定义，请参见[通用参考](spl-general-reference.md)。
## 使用限制
| 类别 | 限制项 | Logtail 采集 | 写入处理器 | 实时消费 | 数据加工（新版） | 扫描查询 |
| --- | --- | --- | --- | --- | --- | --- |
| SPL 复杂度 | 脚本管道级数 | 16 级 | 16 级 | 16 级 | 16 级 | 16 级 |
| 脚本长度 | 64KB | 64KB | 10KB | 10KB | 64KB |  |
| SPL 运行时 | 运行内存大小 重要 处理方案请参见 [错误处理](spl-general-reference.md) 。 | 50MB | 1GB | 1GB | 1GB | 2GB |
| 运行超时 重要 处理方案请参见 [错误处理](spl-general-reference.md) 。 | 1 秒 | 5 秒 | 5 秒 | 5 秒 | 2 秒 |  |
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
