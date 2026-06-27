# 核心应用场景与行业实践案例-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/product-overview/common-scenarios

# 应用场景
云数据库 Tair（兼容 Redis）适用于多种场景，尤其是请求并发量大场景中的数据存储。
## 游戏行业应用
游戏行业通常将Tair作为重要的部署架构组件，用于缓存或数据持久化。
场景一：Tair作为缓存加速应用访问
Redis作为缓存层，加速应用访问。数据存储在后端的数据库中（RDS）。
场景二：Tair作为存储数据库使用
游戏部署架构相对简单，主程序部署在ECS上，所有业务数据存储在Tair中，作为持久化数据库。Tair支持持久化功能，主备双机冗余数据存储。
Redis的服务可靠性至关重要，一旦Redis服务不可用，将导致后端数据库无法承载业务访问压力。Tair提供双机热备的高可用架构，保障极高的服务可靠性。主节点对外提供服务，当主节点出现故障，系统自动切换备用节点接管服务，整个切换过程对用户全部透明。
## 电商行业应用
电商行业通过Tair实现商品秒杀、购物推荐等功能。
场景一：秒杀类购物系统
大型促销秒杀系统，系统整体访问压力非常大，一般的数据库根本无法承载这样的读取压力。Tair支持持久化功能，可以直接选择Tair作为数据库系统使用。
场景二：带有计数系统的库存系统
使用RDS存储商品的所有信息，通过Tair存储商品的库存信息。在高并发、大流量场景下，Tair的极高性能可以轻松应对每一次来自用户的商品库存查询，避免所有查询请求全部进入RDS，导致业务响应变慢等问题，提升用户体验。
## 视频直播类应用
视频直播类业务通过Tair存储用户数据及好友互动关系。
双机热备保障高可用
Tair提供双机热备的方式，可以极大的提高服务可用性。
集群版解决性能瓶颈
Tair提供集群版实例，破除Redis单线程机制的性能瓶颈，可以有效的应对视频直播类流量突起，有效地支撑高性能的需求。
轻松扩容应对业务高峰
Tair可支持一键扩容，整个升级过程对用户全透明，可以从容应对流量突发对业务产生的影响。
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
