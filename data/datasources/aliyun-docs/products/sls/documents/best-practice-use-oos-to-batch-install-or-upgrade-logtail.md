# 如何使用OOS批量安装或升级Logtail-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/best-practice-use-oos-to-batch-install-or-upgrade-logtail

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [开始使用](products/sls/documents/start-using-sls.md)

- [资源管理](products/sls/documents/resource-management.md)

- [数据采集](products/sls/documents/data-collection-1.md)

- [数据处理](products/sls/documents/data-processing-sls.md)

- [数据存储](products/sls/documents/data-storage.md)

- [查询与分析](products/sls/documents/index-and-query.md)

- [数据监控](products/sls/documents/data-monitoring.md)

- [数据输出与集成](products/sls/documents/sls-log-output-and-integration.md)

- [技术解决方案](products/sls/documents/sls-technical-solutions.md)

- [开发参考](products/sls/documents/developer-reference.md)

- [安全合规](products/sls/documents/security-compliance.md)

- [常见问题](products/sls/documents/faq-15.md)

[首页](https://help.aliyun.com/zh)

# 使用OOS批量安装或升级Logtail

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何通过阿里云运维编排服务批量安装或升级Logtail。

## 使用场景

运维编排服务（Operation Orchestration Service，简称OOS）是阿里云提供的自动化运维平台。您可以使用自定义模板或阿里云提供的公共模板，对ECS、RDS、SLB、VPC等资源进行自动化运维。更多信息，请参见[什么是系统运维管理](https://help.aliyun.com/zh/oos/product-overview/introduction-to-oos)。

当您需要在大量的阿里云ECS实例中安装、更新或卸载Logtail时，可以使用运维编排OOS进行批量自动操作。如果您的服务器是与日志服务属于不同账号的ECS、其他云厂商的服务器或自建IDC，您需要手动安装Logtail。具体操作，请参见[安装](products/sls/documents/install-logtail-on-a-linux-server.md)[Logtail（Linux](products/sls/documents/install-logtail-on-a-linux-server.md)[系统）](products/sls/documents/install-logtail-on-a-linux-server.md)或[安装](products/sls/documents/install-logtail-on-a-windows-server.md)[Logtail（Windows](products/sls/documents/install-logtail-on-a-windows-server.md)[系统）](products/sls/documents/install-logtail-on-a-windows-server.md)。

## 前提条件

- 

至少拥有一台阿里云ECS服务器。

- 

使用RAM用户操作时，该RAM用户需具备如下权限。

- 

AliyunOOSFullAccess权限：为RAM用户授予AliyunOOSFullAccess权限的具体操作，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

- 

自定义权限：为RAM用户授予如下自定义权限时，需要先创建自定义策略并为RAM用户授权。具体操作，请参见[创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)、[管理](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeTagKeys", "ecs:DescribeTags", "ecs:DescribeInstances", "ecs:DescribeInvocationResults", "ecs:RunCommand", "ecs:DescribeInvocations" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "oos:ListTemplates", "oos:StartExecution", "oos:ListExecutions", "oos:GetExecutionTemplate", "oos:ListExecutionLogs", "oos:ListTaskExecutions" ], "Resource": "*" } ] }

## 操作步骤

- 

登录[运维编排](https://oos.console.aliyun.com/)[OOS](https://oos.console.aliyun.com/)[控制台](https://oos.console.aliyun.com/)。

- 

在左侧导航栏中，选择自动化任务>公共任务模板。

- 

在公共任务模板页面中，搜索LogAgent，找到批量安装日志服务插件模板，然后单击创建执行。

- 

在创建页面，完成如下配置。

- 

在基本信息步骤中，保持默认配置，然后单击下一步：设置参数。

- 

在设置参数步骤中，完成如下配置，然后单击下一步：确定。

重要参数说明如下：

- 

是否覆盖LogAgent：打开是否覆盖LogAgent开关后，如果ECS实例内已存在Logtail，则将被覆盖。详细说明如下表所示。

重要

当ECS实例为Windows操作系统且使用upgrade操作时，仅支持覆盖原有的Logtail更新，是否覆盖LogAgent配置不会生效。

| 是否覆盖 LogAgent | install（安装） | upgrade（更新） | uninstall（卸载） |
| --- | --- | --- | --- |
| 覆盖 LogAgent | 卸载 Logtail，安装最新版本。 | 卸载 Logatil，安装最新版本。 | 卸载 Logtail |
| 不覆盖 LogAgent | 返回 Logtail 已存在，不会覆盖。 | 保留原有 Logtail 配置，安装最新版本，安装完成后按照之前进度继续采集。 | 卸载 Logtail |


- 

目标实例：选择目标ECS实例。更多信息，请参见[实例选取方式](products/sls/documents/install-logtail-on-ecs-instances.md)。

- 

确认信息无误后，单击创建。

- 

查看执行结果。

您可以在执行结果区域，查看在每台ECS上执行Logtail安装命令的执行状态。执行详情页面显示执行状态为成功，模板名称为ACS-ECS-BulkyInstallLogAgent，执行模式为自动执行。执行结果流程依次经过输入、获取ECS实例、runCommand、输出四个节点，所有节点均已执行成功。您还可以通过查看输出、日志等内容，获取Logtail的安装目录等信息。

[上一篇：日志采集失败的 6 大经典雷区](products/sls/documents/6-log-collection-failures.md)[下一篇：数据处理](products/sls/documents/data-processing-sls.md)

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
