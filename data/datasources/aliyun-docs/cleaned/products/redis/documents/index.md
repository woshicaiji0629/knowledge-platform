# 云数据库 Tair（兼容 Redis®）-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/

# 云数据库 Tair（兼容 Redis®）
云数据库 Tair（兼容 Redis）是一种全托管、兼容Redis协议且具备超高性能的数据库服务，能够保证亚毫秒级的稳定时延，为应用程序起到加速作用。
云数据库 Tair提供Redis开源版和Tair（企业版）两种内核供您选择：
Redis开源版内核基于开源代码进行强化，而Tair内核则在此基础上增加了大量企业级特性，能够覆盖Redis开源版难以应对的场景，并提供稳定可靠的服务。
[免费试用](https://free.aliyun.com/?searchKey=redis)[立即购买](https://common-buy.aliyun.com/?commodityCode=kvstore_pretair_public_cn)[优惠活动](https://www.aliyun.com/database/dbfirstbuy)[常见问题](https://help.aliyun.com/knowledge_detail/146768.html)[相关技术圈](https://developer.aliyun.com/group/hbasespark/)
## 学习路径
由浅入深，带您玩转云数据库 Tair（兼容 Redis）！
### 了解
云数据库 Tair（兼容 Redis）
- [产品简介](product-overview/what-is-apsaradb-for-redis.md)
- [Tair（企业版）介绍](product-overview/overview-1.md)
- [架构介绍](product-overview/overview-6.md)
- [规格性能](product-overview/overview-4.md)
- [功能特性](product-overview/features.md)
- [应用场景](product-overview/common-scenarios.md)
- [灾备方案](product-overview/disaster-recovery.md)
- [Redis开源版命令支持](developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)
- [Tair（企业版）命令支持](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)
产品定价
- [收费项目](product-overview/billable-items.md)
- [计费详情](product-overview/billing-methods.md)
- [变配说明](product-overview/configuration-changes.md)
新特性
- [Redis开源版Release note](support/apsaradb-for-redis-community-edition.md)
- [Tair（企业版）Release note](support/apsaradb-for-redis-enhanced-edition-1.md)
- [Proxy（代理节点）Release note](support/apsaradb-for-redis-proxy-nodes.md)
### 上手
快速入门
- [启航：了解控制台](getting-started/manage-instances-1.md)
- [第1步：创建实例](getting-started/step-1-create-an-apsaradb-for-redis-instance.md)
- [第2步：设置白名单](getting-started/step-2-configure-whitelists.md)
- [第3步：连接实例](user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)
### 使用
连接
- [redis-cli连接教程](user-guide/change-the-endpoint-or-port-number-of-an-instance.md)
- [客户端程序连接教程](user-guide/use-a-client-to-connect-to-an-apsaradb-for-redis-instance.md)
- [直连地址连接教程](user-guide/use-a-private-endpoint-to-connect-to-an-apsaradb-for-redis-instance.md)
安全
- [账号管理](user-guide/create-and-manage-database-accounts.md)
- [设置SSL加密](user-guide/configure-ssl-encryption.md)
- [TED加密](user-guide/enable-tde.md)
运维
- [设置可维护时间](user-guide/set-a-maintenance-window.md)
- [备份恢复](user-guide/backup-and-restoration-solutions.md)
- [变更配置](user-guide/change-the-configurations-of-an-instance.md)
问题排查
- [发现并处理大Key和热Key](user-guide/identify-and-handle-large-keys-and-hotkeys.md)
- [实例CPU使用率高](user-guide/troubleshoot-high-cpu-utilization-on-an-apsaradb-for-redis-instance.md)
- [实例内存使用率高](user-guide/troubleshoot-the-high-memory-usage-of-an-apsaradb-for-redis-instance.md)
- [离线全量Key分析](user-guide/offline-key-analysis.md)
- [实时Top Key统计](user-guide/use-the-real-time-key-statistics-feature.md)
- [如何处理集群数据倾斜](user-guide/deal-with-data-skew-issues.md)
### 实践
最佳实践
- [电商秒杀系统](use-cases/use-apsaradb-for-redis-to-build-a-business-system-that-can-handle-flash-sales.md)
- [管道传输（Pipeline）教程](use-cases/use-pipelining-to-batch-issue-commands.md)
- [事务处理教程](use-cases/process-transactions.md)
- [消息发布与订阅](use-cases/publish-and-subscribe-to-messages.md)
- [商品相关性分析](use-cases/correlation-analysis-on-e-commerce-store-items.md)
- [高性能分布式锁](https://help.aliyun.com/document_detail/443679.htm)
### 开发
开发者文档
- [API参考](api-overview.md)
- [SDK参考](download-and-use-sdks.md)
- [Tair扩展数据结构概览](developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md)
- [Lua脚本使用规范](support/usage-of-lua-scripts.md)
- [客户端重连指南](use-cases/retry-mechanisms-for-redis-clients.md)
- [JedisPool资源池优化](use-cases/jedispool-optimization.md)
## 热门视频
创建Tair实例
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
