# 通过控制台快捷创建RDS MariaDB实例-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mariadb/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mariadb/getting-started.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mariadb/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mariadb/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mariadb/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mariadb/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mariadb/support.md)

[首页](https://help.aliyun.com/zh)

# 快速创建RDS MariaDB实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以通过阿里云RDS管理控制台或API创建RDS实例。本文介绍如何通过控制台快速创建RDS MariaDB实例。

## 前提条件

通过RAM用户创建RDS实例时，该RAM用户必须拥有AliyunRDSFullAccess权限和AliyunBSSOrderAccess权限。如何授权，请参见[RAM](products/rds/documents/use-ram-for-resource-authorization.md)[资源授权](products/rds/documents/use-ram-for-resource-authorization.md)。

## 操作步骤

本文以快捷创建方式为例，介绍如何创建RDS MariaDB实例，该方式仅需设置关键参数即可完成创建，旨在帮助您快速入门，如需对创建实例时的其他参数进行特殊配置，请参见[创建](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)。

- 

访问[RDS](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)[管理控制台](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)，单击创建实例。

- 

在顶部选择快捷创建方式。

- 

选择付费类型。

当前支持如下付费类型，请根据实际需要选择。

| 付费类型 | 建议 | 优点 |
| --- | --- | --- |
| 包年包月 | 长期使用 RDS 实例，请选择 包年包月 （预付费）。 | 包年包月比按量付费更实惠，且购买时长越长，折扣越多。 |
| 按量付费 | 短期使用 RDS 实例，请选择 按量付费 （后付费）。 您可以先创建 按量付费 的实例，确认实例符合要求后变更计费方式为 包年包月 。更多信息，请参见 [按量付费转包年包月](products/rds/documents/apsaradb-rds-for-mariadb/change-the-billing-method-of-an-apsaradb-rds-for-mariadb-instance-from-pay-as-you-go-to-subscription.md) 。 | 可随时释放实例，停止计费。 |


- 

选择地域。

选择要在哪个地域创建RDS实例。

- 

如果您已购买[云服务器](products/ecs/documents/user-guide/what-is-ecs.md)[ECS](products/ecs/documents/user-guide/what-is-ecs.md)，并且期望ECS与RDS内网互通，请选择ECS实例所在地域。否则，ECS实例只能通过外网访问RDS实例，无法发挥最佳性能。

重要

RDS实例购买后，地域不支持更改，请慎重选择。

- 

如果您要通过ECS以外的设备（例如本地服务器或电脑）连接RDS实例，则选择将RDS实例创建在离该设备较近的地域，可以降低网络时延。后续通过外网地址连接RDS。

- 

选择引擎。

本文介绍快速创建RDS MariaDB实例，固定配置为MariaDB。

- 

选择实例规格。

根据不同系列实例我们提供不同规格，您可以根据实际业务需要进行选择。如此规格无法满足需要，也可在购买后进行[变更配置](products/rds/documents/apsaradb-rds-for-mariadb/change-the-specifications-of-an-apsaradb-rds-for-mariadb-instance.md)或在页面顶部选择标准创建进行自定义。更多信息，请参见[创建](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)。

- 

选择存储空间。

存储空间范围（最小值和最大值）与前面选择的实例规格和存储类型有关。您可以调整存储空间，增减幅度最少为5 GB。

- 

设置网络和交换机。

网络类型固定配置为专有网络，建议选择与ECS实例相同的VPC。ECS实例与RDS实例位于不同VPC时，无法内网互通。

说明

VPC相同，交换机不同，ECS实例与RDS实例也可以内网互通。

- 

（可选）查看更多配置项。

在快捷创建中，阿里云已自动帮您默认配置了其他参数，您可以单击更多配置查看其他信息。

重要

实例创建后暂不支持变更VPC，如果您需要通过ECS内网连接RDS实例，除了需要在相同地域外，还需要确保VPC一致，如不一致，请使用标准创建方式，各参数含义及具体方法，请参见[创建](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)。

- 

选择购买数量。

默认1个，支持一次性最多购买10个实例，根据实际需要选择。

- 

（可选）如果付费类型选择包年包月，则还需要设置购买时长，请根据实际需要选择。

您还可以选中启用自动续费，避免因忘记续费而导致业务中断。

- 

单击确认下单，并完成支付。

- 

查看实例。

进入[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择创建实例时选择的地域，根据创建时间找到刚刚创建的实例。

说明

实例创建需要约1~5分钟，请刷新页面查看。

## 下一步

- 

[设置白名单](products/rds/documents/apsaradb-rds-for-mariadb/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance.md)

- 

[创建数据库和账号](products/rds/documents/apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)

- 

[申请或释放外网地址](products/rds/documents/apsaradb-rds-for-mariadb/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-mariadb-instance.md)

- 

[连接](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)

## 常见问题

如何查看阿里云账号下的RDS实例总数量？

登录[RDS](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)[概览页](https://rdsnext.console.aliyun.com/dashboard/cn-hangzhou)，查看阿里云账号下所有数据库引擎的RDS实例总数量。在该页面您还可以看到实例分布在哪些地域，以及各地域下正在运行中的实例数量。

为什么创建实例后，实例列表看不到创建中的实例？

- 

- 

| 可能原因 | 说明 | 建议 |
| --- | --- | --- |
| 地域错误 | 您所在地域和您创建实例时选择的地域不一致。 | 在页面左上角切换地域。 |
| 可用区内资源不足 | 可用区内资源不足，导致创建失败。 创建失败您可以在 [订单列表](https://usercenter2.aliyun.com/order/list?pageIndex=1&pageSize=20) 里看到退款。 | 选择其它可用区后重试。 |
| RAM 权限策略禁止创建未加密的 RDS 实例 | 已配置 RAM 权限策略，禁止 RAM 用户创建未加密的 RDS 实例。 RAM 用户尝试创建高性能本地盘实例，实例创建失败（高性能本地盘实例无法在创建时设置磁盘加密）。 RAM 用户尝试创建云盘实例，但未设置云盘加密，实例创建失败。 更多信息，请参见 [通过](products/rds/documents/apsaradb-rds-for-mysql/use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [RAM](products/rds/documents/apsaradb-rds-for-mysql/use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [权限策略限制](products/rds/documents/apsaradb-rds-for-mysql/use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [RAM](products/rds/documents/apsaradb-rds-for-mysql/use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [用户权限](products/rds/documents/apsaradb-rds-for-mysql/use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) 。 | 创建实例时，存储类型选择云盘，选中 [云盘加密](products/rds/documents/apsaradb-rds-for-mysql/configure-the-disk-encryption-feature-for-an-apsaradb-rds-for-mysql-instance.md) 并设置密钥后重试。 |


## 相关文档

- 

标准创建方式：[创建](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance-1.md)

- 

通过API创建RDS实例：[创建一个](products/rds/documents/api-create-an-instance.md)[RDS](products/rds/documents/api-create-an-instance.md)[实例](products/rds/documents/api-create-an-instance.md)

- 

创建其它类型实例请参见：

- 

[快速创建](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS MySQL](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)

- 

[快速创建并使用](products/rds/documents/apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)[RDS SQL Server](products/rds/documents/apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)[实例](products/rds/documents/apsaradb-rds-for-sql-server/create-an-apsaradb-rds-for-sql-server-instance.md)

- 

[快速创建](products/rds/documents/apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)[实例](products/rds/documents/apsaradb-rds-for-postgresql/create-an-apsaradb-rds-for-postgresql-instance.md)

[上一篇：使用流程](products/rds/documents/apsaradb-rds-for-mariadb/general-workflow-to-use-apsaradb-rds-for-mariadb.md)[下一篇：设置白名单](products/rds/documents/apsaradb-rds-for-mariadb/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance.md)

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
