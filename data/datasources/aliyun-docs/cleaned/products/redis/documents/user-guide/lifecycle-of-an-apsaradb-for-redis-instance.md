# 实例全生命周期管理流程与操作-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/lifecycle-of-an-apsaradb-for-redis-instance/

# 管理生命周期
本文介绍云数据库 Tair（兼容 Redis）实例的生命周期流程，即从实例创建（购买）到释放涉及的操作。
## 生命周期流程
图 1.生命周期流程
重要
对实例执行相关操作，会引发实例状态的变化并产生某些影响（例如产生秒级的连接闪断）。更多详情，请参见[实例状态与影响](instance-states-and-impacts.md)。
| 操作 | 说明 |
| --- | --- |
| [创建实例](../getting-started/step-1-create-an-apsaradb-for-redis-instance.md) | 云数据库 Tair（兼容 Redis） 分为 Tair（企业版） 和 Redis 开源版 ，其中 Tair（企业版） 包含多种形态： [内存型](../product-overview/dram-based-instances.md) 、 [持久内存型](../product-overview/persistent-memory-optimized-instances-1.md) 、 [磁盘型](../product-overview/essd-based-instances-1.md) 。您可以创建适应业务需求的实例。 |
| [变更实例配置](change-the-configurations-of-an-instance.md) | 通过变更实例的规格、架构和类型，适应不同场景对实例性能和兼容性的需求。 |
| [调整集群分片数](adjust-the-number-of-cluster-shards.md) | 分片数量越多，实例的整体性能越强。您可以根据业务对性能的需求，调整实例的分片数量。 |
| [开启读写分离](enable-read-write-splitting.md) | 当读请求流量非常大，超过节点性能上限时，您可以开启写分类功能。开启后，您无需修改业务代码，实例能够自动识别读、写请求并进行对应转发，满足高并发读写的业务场景。 |
| [增删备节点](node-management.md) | 增加实例的备节点数，可以提高实例的容灾能力。 |
| [重启实例](restart-one-or-more-apsaradb-for-redis-instances.md) | 当实例出现连接数满或性能问题时，您可以重启实例以释放所有连接。 |
| [升级大版本](upgrade-the-major-version-1.md) | 升级 Redis 开源版 实例的大版本，例如从兼容 Redis 5.0 升级到 7.0，升级后可体验新版本的相关特性与功能。更多信息请参见 [Redis](../support/new-features-of-apsaradb-for-redis.md) [开源版大版本新特性与兼容性](../support/new-features-of-apsaradb-for-redis.md) 。 |
| [升级小版本与代理版本](update-the-minor-version.md) | 云数据库 Tair（兼容 Redis） 会不断地对内核进行深度优化，修复安全漏洞，提升服务稳定性。建议定期检查并升级小版本。 |
| [转为云原生部署模式](change-to-the-cloud-native-deployment-mode.md) | 云原生 部署模式兼容更高的 Redis 版本，同时也具有更加灵活的架构配置。您可以将已创建的 经典 版实例转换为 云原生 版实例。 |
| [释放按量付费实例](release-pay-as-you-go-instances.md) | 对于闲置的实例资源，您可以释放按量付费实例或退订包年包月实例 。 |
| [实例回收站](manage-instances-in-the-recycle-bin.md) | 回收站用于保存到期、欠费、已释放的实例，您可以在回收站对这些实例进行续费解锁、重建、彻底销毁等操作。 |
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
