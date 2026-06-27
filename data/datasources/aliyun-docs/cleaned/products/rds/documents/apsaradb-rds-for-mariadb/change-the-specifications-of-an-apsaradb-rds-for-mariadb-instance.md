# 变更RDS MariaDB配置：规格和存储空间-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance

# 变更配置
本文介绍如何变更RDS MariaDB实例配置，包括规格和存储空间。
## 变配方式
立即升降配：变配后，新的配置立即生效。包年包月实例和按量付费实例都支持立即升降配。
说明
RDS MariaDB目前不支持Serverless功能。
续费时升降配：是指对实例进行续费，并在续费时变更实例配置。仅包年包月实例支持续费时升降配，新的配置将在下一计费周期生效。例如，包月实例到期时间为2018年6月20日，您在2018年5月10日进行了实例的续费和升配的操作，则该续费和升配会在2018年6月20日生效。
说明
变配任务下达后，系统将磁盘数据同步到一个新实例，然后根据立即升降配或续费时升降配确定时间，到时间后系统将老实例的实例ID和连接地址等信息切换到新实例。
## 变更项
| 变更项 | 说明 |
| --- | --- |
| 规格 | 所有实例类型都支持变更规格。 |
| 存储空间 | 所有实例都支持增加存储空间，不支持减少存储空间。 说明 增加存储空间时不能超过该规格的存储空间限制，详情请参见 [主实例规格列表](../product-overview/primary-apsaradb-rds-instance-types.md) 。 若当前规格对应的存储空间范围无法满足您的需求，请选择其它实例规格。 |
说明
变更上述配置不会导致实例连接地址的改变。
## 计费规则
请参见[变配的计费规则](../product-overview/specification-changes.md)。
## 前提条件
您的阿里云账号没有未支付的续费订单。
## 注意事项
在变更配置生效期间，RDS服务可能会出现一次约30秒的闪断，而且与数据库、账号、网络等相关的大部分操作都无法执行，请尽量在业务低峰期执行变配操作，或确保您的应用有自动重连机制。
## 操作步骤
登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[管理控制台](https://rdsnext.console.aliyun.com/rdsList/basic)。
在页面左上角，选择实例所在地域。
找到目标实例，单击实例ID。
在配置信息区域，单击变更配置。
（仅包年包月实例需要执行此步骤）在弹出的对话框中，选择变更方式，单击下一步。在弹出的变更配置对话框中，根据需要选择立即升配或立即降配，然后单击下一步。
修改实例的配置。具体请参见[变更项](change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md)。
选择变更实例配置的执行时间。
数据迁移结束后立即切换：变更实例配置会涉及到底层的数据迁移，您可以选择在数据迁移后立即切换。
可维护时间内进行切换：在变更配置生效期间，可能会出现一次约30秒的闪断，而且与数据库、账号、网络等相关的大部分操作都无法执行，因此您可以选择在可维护时间段内执行切换的操作。
说明
若您要修改可维护时间，执行如下操作：
单击修改。
在配置信息区域修改可维护时间段，单击保存。
返回变更配置的页面，刷新页面，重新进行变更配置的操作。
在变更配置页面，勾选《关系型数据库RDS服务条款》，单击确认变更，并完成支付。
## 常见问题
仅扩容存储空间，需要迁移数据到新实例吗？
答：需要检查实例所在主机上是否有足够存储空间用于扩容。如果有则直接扩容，不需要迁移数据；如果没有，则需要迁移数据到拥有足够存储空间的主机上。
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
