# RDS实例变更配置的计费规则及升降配费用-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/product-overview/specification-changes

# 变更配置
本文说明RDS实例变更配置的费用。
## 按量付费实例变配费用
按量付费实例是每小时收费，变更配置后按照新的售价每小时收费。
## 包年包月实例变配费用
包年包月实例变配时会产生补差价或者退款。
升配：需选择立即升配，根据所选规格，需要支付差价。
降配：需选择立即降配，根据所选规格，系统会退还差价。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，选择地域并单击目标实例ID，在基本信息页的配置信息区域单击变更配置，根据需要选择立即升配或立即降配。
| 变配类型 | 费用说明 |
| --- | --- |
| 立即升配 | 支付费用 = 新配置剩余时长总价（新配置的月单价/30/24 × 包年包月剩余时长）- 老配置剩余时长总价（老配置的月单价/30/24 × 包年包月剩余时长） 示例：新配置月单价 14400 元，老配置月单价 7200 元，包年包月剩余天数 50 天，则需要支付（14400/30/24×50×24）-（7200/30/24×50×24）=12000 元。 |
| 立即降配 | 关于立即降配的退款金额，请参见 [降配退款规则说明](https://help.aliyun.com/zh/user-center/description-of-downgrade-refund-rules) 。 |
## 价格
购买实例的价格与所选地域、规格、存储等配置相关，请前往[购买页面](https://rdsbuy.console.aliyun.com/?spm=5176.2020520104.0.0.2b4b1450yLixqw#/create/rds/mysql)了解详情。
## 相关主题
[RDS MySQL](../apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)[变更配置](../apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md)
[RDS SQL Server](../apsaradb-rds-for-sql-server/change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md)[变更配置](../apsaradb-rds-for-sql-server/change-the-specifications-of-an-apsaradb-rds-for-sql-server-instance.md)
[RDS PostgreSQL](../apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)[变更配置](../apsaradb-rds-for-postgresql/change-the-specifications-of-an-apsaradb-rds-for-postgresql-instance.md)
[RDS MariaDB](../apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md)[变更配置](../apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md)
## 相关API
| API | 描述 |
| --- | --- |
| [ModifyDBInstanceSpec - 变更](../developer-reference/api-rds-2014-08-15-modifydbinstancespec.md) [RDS](../developer-reference/api-rds-2014-08-15-modifydbinstancespec.md) [实例](../developer-reference/api-rds-2014-08-15-modifydbinstancespec.md) | 该接口用于变更 RDS 实例的规格和存储空间等。 |
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
