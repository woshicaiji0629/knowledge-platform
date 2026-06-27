# 命令支持范围与使用限制-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/overview-3

# 命令概览
云数据库 Tair（兼容 Redis）存在多个版本、系列和架构，各种类型的实例对于Redis命令的支持度有所不同。根据本章节的导航信息，您可以快速找到云数据库 Tair（兼容 Redis）各版本支持的命令和限制使用的命令。
## 命令支持概览
| 文档标题 | 简介 |
| --- | --- |
| [Redis](commands-supported-by-apsaradb-for-redis-community-edition.md) [开源版命令支持](commands-supported-by-apsaradb-for-redis-community-edition.md) | Redis 开源版 支持多个引擎版本和架构类型，不同的引擎版本和架构类型对 Redis 命令的支持度有所不同。本文以 Redis 的相关命令为基准，介绍详细的命令支持情况和使用限制，为您的实例选型提供相关参考。 |
| [Tair](extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) [扩展数据结构概览](extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md) | Tair（企业版） 除支持原生 Redis 的命令以外，还支持下述数据结构， 包括 [exString](tairsting-command.md) （包含 [Redis String](cas-cad-command.md) [命令增强](cas-cad-command.md) ）、 [exHash](the-tairhash-command.md) 、 [exZset](tairzset-command.md) 、 [GIS](tairgis-command.md) 、 [Bloom](tairbloom-command.md) 、 [Doc](tairdoc-command.md) 、 [TS](the-tickets-command.md) 、 [Cpc](taircpc-command.md) 、 [Roaring](tairroaring-command.md) 、 [Search](tairsearch.md) 和 [Vector](tairvector.md) 。 说明 [内存型](../product-overview/dram-based-instances.md) （兼容 Redis 7.0、6.0）兼容所有数据结构。 [内存型](../product-overview/dram-based-instances.md) （兼容 Redis 5.0）兼容除 TairVector 以外的所有数据结构。 [持久内存型](../product-overview/persistent-memory-optimized-instances-1.md) 兼容 [exString](tairsting-command.md) （包含 [Redis String](cas-cad-command.md) [命令增强](cas-cad-command.md) ）、 [exHash](the-tairhash-command.md) 和 [Cpc](taircpc-command.md) 。 |
| [Tair（企业版）命令支持与限制](limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md) | Tair（企业版） 兼容大多数的 Redis 命令，为保障服务性能，部分命令的使用受到限制。 |
| [阿里云自研的](in-house-commands-for-tair-instances-in-proxy-mode.md) [Proxy](in-house-commands-for-tair-instances-in-proxy-mode.md) [命令](in-house-commands-for-tair-instances-in-proxy-mode.md) | 在兼容 Redis 命令之外， 云数据库 Tair（兼容 Redis） 还支持多个自研命令，可以在集群架构或读写分离架构中使用，帮助您更方便地管理实例。 |
## 不同架构下的命令限制
由于部署架构的不同，集群架构和读写分离架构实例在Redis命令的支持上有一定的区别，更多信息请参见[集群架构与读写分离架构实例的命令限制](limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。
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
