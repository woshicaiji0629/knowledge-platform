# 切换RDS PostgreSQL实例的虚拟交换机-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/switch-an-apsaradb-rds-for-postgresql-instance-to-a-different-vswitch

# 切换RDS PostgreSQL实例的虚拟交换机
如果您需要变更RDS PostgreSQL实例虚拟交换机，您可以在控制台或通过API修改虚拟交换机配置。
## 前提条件
实例为RDS PostgreSQL云盘版。
## 使用限制
如果当前可用区没有可用的交换机，请前往[专有网络控制台创建](https://vpc.console.aliyun.com/)交换机。
RDS PostgreSQL不支持切换VPC。
如果需要更换VPC，您可以购买新的实例（购买时选择目标VPC），然后将数据迁移到新的实例。详情请参见[使用一键上云迁移实例](use-the-cloud-migration-feature-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)或[使用](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)[DTS](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)[迁移实例](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)。
如果不便进行实例迁移，您可以[使用](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[VPC](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[对等连接实现](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[VPC](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[私网互通](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)。同一地域的VPC对等连接不收取任何费用，而跨地域的VPC对等连接则需支付相应费用。
## 影响
切换过程会有30秒闪断，请确保应用程序具有重连机制。
切换虚拟交换机会造成虚拟IP（VIP）的变更，请您在应用程序中尽量使用[连接地址](configure-endpoints-2.md)进行连接，不要使用IP地址。
VIP的变更会短暂影响到[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms)、[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)的使用，变更结束后会自动恢复正常。
客户端的DNS缓存会导致只能读取数据，无法写入数据，请及时清理缓存。
## 操作步骤
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏单击数据库连接。
单击切换交换机。
选择虚拟交换机，并单击确定。
如果当前可用区没有可用的交换机，请前往[专有网络控制台创建](https://vpc.console.aliyun.com/)交换机。
在弹出的风险提示框中单击确定切换。
## 常见问题
Q：如何切换VPC？
A：RDS PostgreSQL不支持切换VPC。
如果需要更换VPC，您可以购买新的实例（购买时选择目标VPC），然后将数据迁移到新的实例。详情请参见[使用一键上云迁移实例](use-the-cloud-migration-feature-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)或[使用](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)[DTS](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)[迁移实例](use-dts-to-migrate-data-between-apsaradb-rds-for-postgresql-instances.md)。
如果不便进行实例迁移，您可以[使用](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[VPC](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[对等连接实现](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[VPC](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)[私网互通](../../../vpc/documents/create-and-manage-vpc-peering-connection.md)。同一地域的VPC对等连接不收取任何费用，而跨地域的VPC对等连接则需支付相应费用。
## 相关文档
如果需要将实例的交换机切换为其他可用区的交换机，请参见[迁移可用区](migrate-an-apsaradb-rds-for-postgresql-instance-across-zones-in-the-same-region.md)。
## 相关API
| API | 描述 |
| --- | --- |
| [SwitchDBInstanceVpc](api-rds-2014-08-15-switchdbinstancevpc-postgresql.md) | 切换 RDS PostgreSQL 实例的虚拟交换机。 重要 RDS PostgreSQL 不支持切换 VPC，请求参数中的 VPCId 请配置为当前实例的 VPC。 |
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
