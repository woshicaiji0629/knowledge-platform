# 如何为日志服务K8s事件中心设置告警-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/configure-alerts-2-k8s

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

# 设置告警

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/sls)

[我的收藏](https://help.aliyun.com/my_favorites.html)

日志服务已内置告警规则模板，您只需添加对应的告警规则即可实时监控目标Kubernetes集群，并可通过钉钉等渠道接收到告警通知。本文介绍设置告警的相关操作。

## 前提条件

已创建K8s事件中心并接入Kubernetes集群数据。具体操作，请参见[创建并使用](products/sls/documents/create-and-use-an-event-center.md)[K8s](products/sls/documents/create-and-use-an-event-center.md)[事件中心](products/sls/documents/create-and-use-an-event-center.md)。

## 背景信息

K8s事件中心已内置告警规则模板、SLS ACK内置行动策略、SLS ACK内置用户组、SLS ACK Pod内置内容模板、SLS ACK内置内容模板、SLS ACK Node内置内容模板和SLS ACK Object内置内容模板。日志服务提供的内置资源可满足大部分告警场景，它们之间的关联如下：

- 

通过告警规则模板指定SLS ACK内置行动策略。

- 

通过SLS ACK内置行动策略指定SLS ACK内置用户组和内容模板（SLS ACK Pod内置内容模板、SLS ACK内置内容模板、SLS ACK Node内置内容模板和SLS ACK Object内置内容模板）。

触发告警后，日志服务会根据行动策略给指定用户发送告警通知。

## 步骤一：创建用户

- 

登录[日志服务控制台](https://sls.console.aliyun.com)。

- 

在日志应用区域的智能运维页签中，单击K8S事件中心。

- 

在左侧导航栏中，单击目标事件中心前面的图标，然后单击告警配置。

- 

在告警中心页面中，选择通知对象>用户管理。

- 

创建用户。

具体操作，请参见[创建用户](products/sls/documents/create-users-and-user-groups.md)。

## 步骤二：将用户添加到SLS ACK内置用户组

- 

在告警中心页面中，选择通知对象>用户组管理。

- 

在用户组列表中，单击sls.app.ack.builtin对应的修改。

- 

在修改用户组对话框中，将已创建的用户从待添加成员区域添加到已添加成员区域，然后单击确认。

## 步骤三：添加告警规则

日志服务已内置数十种K8s事件中心告警规则模板，您只需根据业务需求，添加对应的告警规则即可。此处以添加集群节点正常运行告警规则模板对应的告警规则为例。

- 

在告警中心页面中，单击告警规则>新建告警右侧的。

- 

单击从模板新建。

- 

在从模板新建面板中，单击SLS K8s事件中心。

- 

在告警规则模板列表中，单击目标告警规则模板。

- 

在新建告警面板中，cluster_id为集群ID，新建告警其他操作请参见[创建告警规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md)。

## 更多操作

为K8s事件中心设置告警后，您还可以进行如下操作。

| 操作 | 说明 |
| --- | --- |
| 关闭告警规则 | 关闭告警规则后，告警规则不会再触发告警， 状态 变更为 已关闭 。 该操作不会删除规则参数中已设置的信息。需要再次监控时，无需重新设置规则参数。 |
| 临时关闭告警规则 | 临时关闭告警规则后，在指定时间内不再触发告警。 |
| 删除告警规则 | 该操作会删除规则参数中已设置的信息。需要再次监控时，需要重新设置规则参数。 |
| 设置告警规则 | 设置告警规则的配置参数。 |
| 查看 | 查看告警规则概览信息和告警规则历史统计报表。 |
| 关注 | 将目标告警规则添加到关注列表中。 |
| 自定义告警 | 如果内置告警规则模板不满足您的业务需求，您可以单击 创建告警 ，创建自定义监控规则。具体操作，请参见 [创建日志告警规则](products/sls/documents/create-an-alert-monitoring-rule-for-logs.md) 。 |


[上一篇：创建并使用K8s事件中心](products/sls/documents/create-and-use-an-event-center.md)[下一篇：Kubernetes Ingress日志中心](products/sls/documents/kubernetes-ingress-log-center.md)

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
