# 跨Project、地域或阿里云账号监控日志时，配置相应的授权-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/configure-access-control-policies

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

# 跨Project监控数据授权

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当告警监控规则跨Project、地域和阿里云账号监控目标时，日志服务需要通过扮演RAM角色的方式访问日志库或时序库，您需要进行相应的授权。

## 使用场景

| 授权方式 | 适用场景 |
| --- | --- |
| 默认 | 对告警监控规则所在的同一个 Project 内，不同日志库和时序库进行协同告警监控。 |
| 内置角色 | 对告警监控规则所在同一个阿里云账号内，不同 Project 的日志库和时序库进行协同告警监控。 |
| 自定义角色 | 对告警监控规则所在不同阿里云账号进行监控，或者对 RAM 角色的访问控制权限有更精细的要求。 |


## 操作视频

## 步骤一：配置授权

- 

添加查询统计。具体步骤，请参见[创建告警监控规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)。

- 

配置授权方式。

## 默认授权

对同一个Project内的不同日志库和时序库进行告警监控时，使用默认授权方式。

在高级配置页签中，选择授权方式为默认。

## 内置角色授权

对同一个阿里云账号的不同日志库和时序库进行告警监控时，使用内置角色授权。

在高级配置页签中，将授权方式配置为内置角色。如果是首次配置，需要使用阿里云主账号[按照页面提示完成授权](https://ram.console.aliyun.com/role/authorization?request=%7B%22Services%22%3A%5B%7B%22Service%22%3A%22Log%22%2C%22Roles%22%3A%5B%7B%22RoleName%22%3A%22AliyunSLSAlertMonitorRole%22%2C%22TemplateId%22%3A%22AliyunSLSAlertMonitorRole%22%7D%5D%7D%5D%2C%22ReturnUrl%22%3A%22https%3A%2F%2Fsls.console.aliyun.com%2Flognext%2Fproject%2Flog-service-1984268643269815-cn-wulanchabu%2Falertcenter%22%7D)。授权后，日志服务将创建名称为AliyunSLSAlertMonitorRole的RAM角色，日志服务将扮演此角色以读取源日志库中的数据。单击高级配置页签，在授权方式下拉框中选择内置角色。

## 自定义角色授权（同账号）

对同一个阿里云账号下的不同日志库或指标库进行告警监控时，您可以通过自定义角色实现告警监控。

- 

[创建可信实体为阿里云服务的](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[RAM](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[角色](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)，其中受信服务请选择日志服务。

- 

创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)。

重要

Project名称需根据实际情况替换。如果您需要更细粒度的授权，例如只允许在指定Project下创建监控规则，则可以在下述策略的Resource中指定具体的Project，例如acs:log:*:*:project/my-project。

{ "Statement": [ { "Action": [ "log:ListProject" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:*" ] }, { "Action": [ "log:ListLogStores", "log:GetLogStoreLogs", "log:GetIndex" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:project/Project名称/*" ] } ], "Version": "1" }

- 

为RAM角色添加创建的自定义权限。具体操作，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

### 后续操作

- 

获取RAM角色标识（ARN），具体操作，请参见[查看](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[RAM](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[角色](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)。

- 

在使用自定义角色授权时，输入该RAM角色标识。更多信息，请参见[创建告警监控规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)。

在高级配置页签中，将授权方式选择为自定义角色后，在角色 ARN输入框中填写对应的角色标识。

## 自定义角色授权（跨账号）

对跨阿里云账号下的不同日志库或指标库进行告警监控时，您可以通过自定义角色实现告警监控。例如在阿里云账号A中创建告警，监控阿里云账号B下的日志库或指标库。

在阿里云账号B进行以下操作：

- 

[创建可信实体为阿里云服务的](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[RAM](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[角色](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)，其中受信服务请选择日志服务。

- 

修改RAM角色的信任策略。具体操作，请参见[修改](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[RAM](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)[角色的信任策略](products/ram/documents/user-guide/edit-the-trust-policy-of-a-ram-role.md)。

重要

请根据实际情况替换阿里云账号A的ID。您可以在[账号中心](https://account.console.aliyun.com/v2/#/basic-info/index)中查看阿里云账号ID。

{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "阿里云账号A的ID@log.aliyuncs.com", "log.aliyuncs.com" ] } } ], "Version": "1" }

- 

创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)。

重要

将配置框中的原有脚本替换为如下内容。其中，Project名称需根据实际情况替换。如果您想要更细粒度的授权，例如只允许在指定Project下创建监控规则，则可以在下述策略的Resource中指定具体的Project，例如acs:log:*:*:project/my-project。

{ "Statement": [ { "Action": [ "log:ListProject" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:*" ] }, { "Action": [ "log:ListLogStores", "log:GetLogStoreLogs", "log:GetIndex" ], "Effect": "Allow", "Resource": [ "acs:log:*:*:project/Project名称/*" ] } ], "Version": "1" }

- 

为RAM角色添加创建的自定义权限。具体操作，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

- 

获取RAM角色标识（ARN），具体操作，请参见[查看](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[RAM](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[角色](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)。

### 后续操作

- 

获取RAM角色标识（ARN），具体操作，请参见[查看](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[RAM](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[角色](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)。

- 

在阿里云账号A中创建告警时，选择自定义角色授权，角色ARN使用在阿里云账号B中创建的RAM角色标识。更多信息，请参见[创建告警监控规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)。

## 步骤二：为RAM用户授权

设置内置角色或自定义角色后，如果需要使用RAM用户查询时序库或日志库，必须使用阿里云主账号为RAM用户添加如下权限策略，用于扮演相应的角色。为RAM用户授权的操作步骤，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

{ "Action": "ram:PassRole", "Effect": "Allow", "Resource": "acs:ram::阿里云账号ID:角色ARN" }

[上一篇：授权RAM用户操作告警](products/sls/documents/authorized-ram-user-operation-alarm.md)[下一篇：配置告警写入事件库的权限](products/sls/documents/configure-permissions-for-writing-alarms-to-the-event-library.md)

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
