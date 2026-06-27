# 如何配置告警写入事件库的权限-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/configure-permissions-for-writing-alarms-to-the-event-library

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

# 配置告警写入事件库的权限

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

将告警信息写入事件库时，需要具备角色权限。本文介绍默认角色及自定义角色的权限配置方法。

您在配置告警监控规则时，打开输出目标-事件库的开启开关后，需要对角色进行授权。

## 默认角色授权

当授权方式选择为默认角色时：

- 

单击前往授权，跳转至授权页面，根据界面提示完成授权。

系统将提示您授权角色AliyunLogETLRole。授权完成后，单击授权完成，请点刷新以刷新授权状态。

- 

授权完成后，单击授权完成，请点刷新，查看角色信息。

角色信息中，授权方式显示为默认角色，角色ARN显示为acs:ram::{账号ID}:role/aliyunlogetlrole。

## 自定义角色授权

当授权方式选择为自定义角色时，需要先配置权限策略，创建自定义角色，并为角色授权。

- 

使用阿里云账号（主账号）或RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。

- 

创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](products/ram/documents/create-a-custom-policy.md)。

{ { "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "log:PostLogStoreLogs", "Resource": "*" } ] }

- 

创建阿里云服务需要扮演的RAM角色。具体操作，请参见[创建可信实体为阿里云服务的](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[RAM](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)[角色](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-alibaba-cloud-service.md)。

重要

- 

创建RAM角色时，信任主体类型应选择云服务，且信任主体名称应选择日志服务。

- 

请检查角色的信任策略如下，Service内容至少包含"log.aliyuncs.com"。

{ "Statement": [ { "Action": "sts:AssumeRole", "Effect": "Allow", "Principal": { "Service": [ "log.aliyuncs.com" ] } } ], "Version": "1" }

- 

为RAM角色添加创建的自定义权限。具体操作，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)[角色的权限](products/ram/documents/user-guide/grant-permissions-to-a-ram-role.md)。

### 后续操作

获取RAM角色标识（ARN），具体操作，请参见[查看](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[RAM](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)[角色](products/ram/documents/user-guide/view-the-information-about-a-ram-role.md)。您在[创建告警监控规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)时，选择授权方式为自定义角色，并输入该角色的ARN。

[上一篇：跨Project监控数据授权](products/sls/documents/configure-access-control-policies.md)[下一篇：创建告警监控规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)

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
