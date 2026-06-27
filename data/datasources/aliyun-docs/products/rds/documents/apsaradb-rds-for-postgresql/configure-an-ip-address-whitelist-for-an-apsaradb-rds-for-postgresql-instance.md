# 设置RDS PostgreSQL的白名单-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-postgresql/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-postgresql-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-postgresql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-postgresql/getting-started.md)

- [DuckDB分析加速](products/rds/documents/apsaradb-rds-for-postgresql/duckdb-analytics-acceleration.md)

- [RDS for AI](products/rds/documents/apsaradb-rds-for-postgresql/rds-for-ai.md)

- [自研内核 AliPG](products/rds/documents/apsaradb-rds-for-postgresql/proprietary-alipg.md)

- [插件](products/rds/documents/apsaradb-rds-for-postgresql/plug-ins-1.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-postgresql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-postgresql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-postgresql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-postgresql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-postgresql/support.md)

[首页](https://help.aliyun.com/zh)

# 设置白名单

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

创建RDS PostgreSQL实例后，暂时还无法访问该实例，您需要设置RDS PostgreSQL实例的白名单，即IP白名单或安全组，本文介绍如何设置IP白名单。

## 操作场景

IP白名单指允许访问RDS实例的IP清单。设置IP白名单可以让RDS实例得到高级别的访问安全保护，建议您定期维护白名单。

通常需要设置IP白名单的场景如下：

- 

场景1：创建RDS实例后，您需要将外部IP地址添加至IP白名单中，外部设备才可以正常访问该RDS实例。

- 

场景2：当数据库连接异常时，您可以检查白名单设置是否正确。

不同连接场景下，IP白名单的设置请参见下表。

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 连接场景 | 网络类型 | IP 白名单设置 |
| --- | --- | --- |
| ECS 实例和 RDS 实例连接 | 处于相同 [专有网络](products/vpc/documents/what-is-vpc.md) [VPC](products/vpc/documents/what-is-vpc.md) 内（推荐） | 添加 ECS 实例私有 IP 地址。 |
| 处于不同专有网络 VPC 内 | 不同专有网络的实例无法内网互通，您可以参考如下方案： 切换 RDS 专有网络，选择和 ECS 实例相同的 VPC。 说明 ECS 实例和 RDS 实例需要处于相同地域才能切换到相同 VPC。如果地域不同，为业务稳定，建议您通过 DTS 将 RDS 实例迁移至 ECS 实例所属地域。详情请参见 [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/migrate-data-between-apsaradb-rds-for-postgresql-instances.md) [实例间数据迁移](products/rds/documents/apsaradb-rds-for-postgresql/migrate-data-between-apsaradb-rds-for-postgresql-instances.md) 。 在 IP 白名单中添加 ECS 实例私有 IP 地址。 |  |
| ACK 集群的容器和 RDS 实例连接 | 处于相同专有网络 VPC 内（推荐） | 当 ACK 集群的 [容器网络插件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md) 为 Flannel 时，添加应用程序所在的节点 IP。 当 ACK 集群的容器网络插件为 Terway 时，添加应用程序所在的 Pod IP。 您可以在目标 ACK 集群的 [容器组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-pods.md) 页面，查 Pod IP 和节点 IP。 |
| 处于不同专有网络 VPC 内 | 不同专有网络的实例无法内网互通，您可以参考如下方案： 切换 RDS 专有网络，选择和 ACK 集群相同的 VPC。 说明 ACK 集群和 RDS 实例需要处于相同地域才能切换到相同 VPC。如果地域不同，为业务稳定，建议您通过 DTS 将 RDS 实例迁移至 ACK 集群所属地域。详情请参见 [RDS PostgreSQL](products/rds/documents/apsaradb-rds-for-postgresql/migrate-data-between-apsaradb-rds-for-postgresql-instances.md) [实例间数据迁移](products/rds/documents/apsaradb-rds-for-postgresql/migrate-data-between-apsaradb-rds-for-postgresql-instances.md) 。 添加应用程序所在的 ACK 集群对应的 IP 地址。 当 ACK 集群的容器网络插件为 Flannel 时，添加应用程序所在的节点 IP。 当 ACK 集群的容器网络插件为 Terway 时，添加应用程序所在的 Pod IP。 |  |
| 云外主机连接 RDS 实例 | 无 | 在 IP 白名单中添加云外主机的公网 IP 地址。 云外主机的应用程序中使用 RDS 实例的外网连接地址。 通过 curl ipinfo.io/ip 可以查询云外主机公网 IP。 说明 如果云外主机没有固定 IP，或者 IP 地址经常变动，请参见 [常见问题](products/rds/documents/apsaradb-rds-for-postgresql/errors-and-faq-about-ip-address-whitelist-settings-in-apsaradb-rds-for-postgresql-1.md) 获取处理方案。 |


## 注意事项

- 

单个实例最多支持50个IP白名单分组。

- 

设置白名单不会影响RDS实例的正常运行。

- 

白名单分组仅用于IP地址管理，不会影响实际访问权限。所有分组中的IP地址对RDS实例的访问权限是一致的。

- 

默认的IP白名单分组（default ）不能删除，只能清空。

- 

请勿修改或删除系统自动生成的分组，避免影响相关产品的使用。例如ali_dms_group（[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)产品IP地址白名单分组）、hdm_security_ips（[DAS](https://help.aliyun.com/zh/das/product-overview/what-is-das#concept-2419191)产品IP地址白名单分组）。

重要

为防止误修改或删除白名单分组，2020年12月之后的新建实例，hdm_security_ips白名单分组对用户不可见。

- 

默认的IP白名单仅包含127.0.0.1，表示除了本地IP 127.0.0.1之外，任何其他IP均无法访问该RDS实例。

## 设置通用模式IP白名单

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏单击白名单与安全组。

- 

单击添加白名单分组，填写分组名称或单击已有分组的修改。

- 

填写需要访问该实例的IP地址或IP段，然后单击确定。

重要

- 

用英文逗号隔开多个IP地址或IP段，且逗号前后不能有空格，例如192.168.0.1,172.16.213.9。

- 

单个实例最多添加1000个IP地址或IP段。当IP地址较多时，建议将零散的IP合并为IP段，例如10.10.10.0/24。

- 

（可选）如果当前实例包含只读实例，可以通过参数白名单同步到只读实例配置白名单同步，将主实例的白名单同步至指定的只读实例。当有多个只读实例时，支持多选。

- 

（可选）单击加载ECS内网IP，将显示您当前阿里云账号下所有ECS实例的IP地址，可快速将ECS私有IP地址添加到白名单中。

## 高安全白名单模式IP白名单

说明

云盘实例不支持高安全白名单模式，[高性能本地盘存储类型已停止售卖](products/rds/documents/apsaradb-rds-for-postgresql/premium-local-ssds-are-no-longer-available-for-purchase-for-rds-for-postgresql-instances-since-september-1-2023.md)。

高安全白名单模式区分经典网络和专有网络，白名单分组需指定网络隔离模式，例如，经典网络的白名单IP地址不可从专有网络访问RDS实例，反之亦然。

如果高性能本地盘实例已经是高安全白名单模式，参见下文进行设置即可。如果需要切换为高安全白名单模式，请参见[切换为高安全白名单模式](products/rds/documents/apsaradb-rds-for-postgresql/switch-an-apsaradb-rds-for-postgresql-instance-to-the-enhanced-whitelist-mode.md)。

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏单击白名单与安全组。

- 

单击添加白名单分组，选择网络隔离模式。

- 

填写分组名称。

- 

在组内白名单中，填写需要访问该实例的IP地址或IP段，然后单击确定。

重要

- 

用英文逗号隔开多个IP地址或IP段，且逗号前后不能有空格，例如192.168.0.1,172.16.213.9。

- 

单个实例最多添加1000个IP地址或IP段。当IP地址较多时，建议将零散的IP合并为IP段，例如10.10.10.0/24。

- 

（可选）如果当前实例包含只读实例，可以通过参数白名单同步到只读实例配置白名单同步，将主实例的白名单同步至指定的只读实例。当有多个只读实例时，支持多选。

- 

（可选）单击加载ECS内网IP，将显示您当前阿里云账号下所有ECS实例的IP地址，可快速将ECS私有IP地址添加到白名单中。

说明

高安全白名单模式请注意选择网络隔离模式。

## 下一步

[创建账号和数据库](products/rds/documents/apsaradb-rds-for-postgresql/create-a-database-and-an-account-on-an-apsaradb-rds-for-postgresql-instance.md)

## 常见问题

通过RDS控制台添加白名单时报错InvalidSecurityIPListLength.Malformed？

## 问题描述

用户通过RDS控制台添加白名单时，可能会出现如下报错：

错误码：InvalidSecurityIPListLength.Malformed 报错信息（中文）：安全IP地址不在可用范围内或已被占用。 报错信息（英文）：The security ip address is not in the available range or occupied.

## 解决方案

- 

原因1：单个白名单分组中最多支持1000个IP地址/段，新增的IP超过了限制。

解决方案：确保单个白名单分组中的IP地址或IP段数量不超过1000个。建议将零散的IP地址合并为CIDR格式的IP段（如192.168.1.0/24），以减少占用数量。

- 

原因2：添加的IP白名单包含非法地址。

解决方案：确保输入的IP地址合法，推荐使用标准CIDR格式（如10.23.12.0/24），掩码范围为1~32。若需添加多个IP地址，请使用英文逗号（,）分隔。

- 

原因3：与已存在的白名单存在冲突。例如，在RDS MySQL中192.168.1.8会与192.168.1.1/8发生冲突。

解决方案：根据实际需求合理规划并添加白名单，避免与现有规则产生重叠或冲突。

说明

请勿删除默认分组default（包含127.0.0.1），也不要修改系统分组（如ali_dms_group或hdm_security_ips），以免影响系统功能或连接安全性。

## 相关API

- 

通过API（[DescribeDBInstanceIPArrayList](products/rds/documents/api-query-ip-address-whitelists.md)）查看RDS实例IP白名单。

- 

通过API（[ModifySecurityIps](products/rds/documents/api-modify-ip-address-whitelist.md)）修改RDS实例IP白名单。

[上一篇：设置白名单](products/rds/documents/apsaradb-rds-for-postgresql/set-the-whitelist-1.md)[下一篇：设置安全组](products/rds/documents/apsaradb-rds-for-postgresql/configure-a-security-group-for-an-apsaradb-rds-for-postgresql-instance-1.md)

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
