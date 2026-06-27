# 设置RDS MariaDB实例的IP白名单-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance

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

# 设置白名单

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

创建RDS实例后，暂时还无法访问，您需要设置RDS实例的白名单，以允许外部设备访问该实例。

## 背景信息

为了确保您的RDS实例的安全性，了解和设置IP白名单是至关重要的。以下是RDS的IP白名单详细说明：

- 

添加IP地址，允许这些IP地址访问该RDS实例。 默认IP白名单仅包含127.0.0.1，禁止外部访问。

- 

IP白名单支持通用白名单模式，适用于经典网络和专有网络。RDS MariaDB实例仅支持专有网络。

- 

设置白名单可以让RDS实例得到高级别的访问安全保护，建议您定期维护白名单。

## 注意事项

- 

您可以修改或清空默认的IP白名单，但是不能删除。

- 

单个实例最多支持50个IP白名单分组。

- 

单个实例最多添加1000个IP或IP段。建议将零散的IP合并为IP段，例如10.10.10.0/24（[CIDR](products/vpc/documents/faq-about-cidr-blocks.md)[模式](products/vpc/documents/faq-about-cidr-blocks.md)）。

- 

ali_dms_group（[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)产品IP地址白名单分组）、hdm_security_ips（[DAS](https://help.aliyun.com/zh/das/product-overview/what-is-das#concept-2419191)产品IP地址白名单分组）等分组为系统自动生成，请勿修改或删除，避免影响相关产品的使用。

重要

- 

请勿在这些分组里增加自己的业务IP，避免相关产品更新时覆盖您的业务IP，影响业务正常运行。

- 

为防止误修改或删除白名单分组，2020年12月之后的新建实例，hdm_security_ips白名单分组对用户不可见。

## 设置IP白名单

- 

访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏中单击白名单与安全组。

- 

在白名单设置页签中，单击default白名单分组中的修改。

说明

您也可以单击添加白名单分组新建自定义分组。

- 

在修改白名单分组对话框中，填写需要访问该实例的IP地址或IP段，然后单击确定。

说明

- 

当您在default分组中添加新的IP地址或IP段后，系统自动删除默认地址127.0.0.1。

- 

若您需要添加多个IP地址或IP段，请用英文逗号隔开（逗号前后都不能有空格），例如192.168.0.1,172.16.213.9。

- 

单击加载ECS内网IP后，将显示您当前阿里云账号下所有ECS实例的IP地址，可快速添加ECS内网IP地址到白名单中。

- 

当应用程序部署在ACK集群的容器中时，需要根据[容器网络插件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/comparison-between-terway-and-flannel.md)添加不同的IP地址。

- 

当ACK集群的容器网络插件为Flannel时，添加应用程序所在的节点IP。

- 

当ACK集群的容器网络插件为Terway时，添加应用程序所在的Pod IP。

您在目标ACK集群的[容器组](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-pods.md)页面，查Pod IP和节点IP。

## 常见IP白名单设置错误案例

- 

白名单与安全组 > 白名单设置中只有默认地址127.0.0.1。

该地址表示不允许任何设备访问RDS实例。因此需在白名单中添加对端的IP地址。

- 

白名单设置为0.0.0.0。

正确格式为0.0.0.0/0。

重要

0.0.0.0/0表示允许任何设备访问RDS实例，请谨慎使用。

- 

白名单中添加的设备公网IP地址并非设备真正的出口IP地址。

原因如下：

- 

公网IP地址不固定，可能会变动。

- 

IP地址查询工具或网站查询的公网IP地址不准确。

解决办法请参见[外网无法连接](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[RDS MySQL](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[或](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[MariaDB：如何正确填写本地设备的公网](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[IP](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)[地址](products/rds/documents/support/why-am-i-unable-to-connect-to-my-apsaradb-rds-for-mysql-or-apsaradb-rds-for-mariadb-instance-from-a-local-server-over-the-internet.md)。

## 常见问题

- 

Q：设置IP白名单后立刻生效吗？

A：设置白名单后约1分钟生效。

- 

Q：为什么多了几个不是我创建的白名单分组？

A：如果多出的分组内IP是内网IP，通常是阿里云其他产品（如DMS、DAS）自动生成的，不会操作您的业务数据。

- 

Q：不开放外网访问，仅在内网访问，会有安全风险吗？

A：建议将RDS实例切换为专有网络，这样只有相同VPC内的ECS实例才能访问RDS实例。

- 

Q：通过RDS控制台添加白名单时报错InvalidSecurityIPListLength.Malformed？

## 问题描述

用户通过RDS控制台添加白名单时，可能会出现如下报错：

InvalidSecurityIPListLength.Malformed The security ip address is not in the available range or occupied.

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

[上一篇：快速创建RDS MariaDB实例](products/rds/documents/apsaradb-rds-for-mariadb/create-an-apsaradb-rds-for-mariadb-instance.md)[下一篇：创建数据库和账号](products/rds/documents/apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance.md)

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
