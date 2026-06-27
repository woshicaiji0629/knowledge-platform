# 将RDS PostgreSQL基础系列实例升级为高可用系列-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/upgrade-an-apsaradb-rds-for-postgresql-instance-from-basic-edition-to-high-availability-edition

# PostgreSQL基础系列升级高可用系列
您可以将RDS PostgreSQL的基础系列实例升级为高可用系列，获得更高可靠性。
## 前提条件
实例需要满足如下要求：
实例大版本：PostgreSQL 10或以上版本。
实例系列：基础系列。
说明
您可以在实例的基本信息页面查看实例的系列。
## 背景信息
高可用系列是适用性较广的云数据库系列。采用一主一备的经典高可用架构，适合80%以上的用户场景，包括互联网、物联网、零售电商、物流、游戏等行业。
详情请参见[高可用系列](../apsaradb-rds-for-mysql/rds-high-availability-edition.md)。
## 费用说明
升级版本的费用请参见[变更配置](../product-overview/specification-changes.md)。
## 影响
RDS变更配置可能涉及底层数据迁移，请您耐心等待。在迁移完成后会根据您设置的切换时间自动进行切换，切换时会出现30秒左右的闪断，请确保应用具备重连机制。
升级后无法回退到基础系列。
## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在基本信息页面的配置信息，单击变更配置。
（仅包年包月实例需要执行此步骤）在弹出的对话框中，选择立即升配，单击下一步。
设置如下参数。
| 参数名称 | 说明 |
| --- | --- |
| 产品系列 | 选择 高可用系列 。 |
| 存储类型 | 选择实例的存储类型。详情请参见 [存储类型介绍](storage-types-of-apsaradb-rds-for-postgresql.md) 。 说明 仅当原实例的存储类型为 ESSD 云盘时，支持此参数。 |
| 实例规格 | 选择实例规格。每种规格都有对应的 CPU 核数、内存、最大连接数和最大 IOPS。详情请参见 [主实例规格列表](../product-overview/primary-apsaradb-rds-instance-types.md) 。 |
| 存储空间 | 设置存储空间。存储空间只能增加，不能降低。 |
| 切换时间 | 选择升级的切换时间： 立即执行 可维护时间内进行切换 |
阅读服务协议后，单击确认下单并完成支付。
## 相关API
| API | 描述 |
| --- | --- |
| [变更](../api-change-instance-configuration.md) [RDS](../api-change-instance-configuration.md) [实例](../api-change-instance-configuration.md) | 变更 RDS 实例配置。 |
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
