# 在控制台通过会话管理连接实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/connect-to-an-instance-by-using-session-manager-1

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 在控制台通过会话管理连接实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以在控制台直接通过会话管理一键连接到ECS实例，支持免密连接无公网实例。相比于传统的SSH或RDP直连的方式更加安全方便。本文为您介绍如何在阿里云控制台通过会话管理连接实例。

重要

在通过会话管理连接实例时，不论实例是Windows系统还是Linux系统，都仅支持命令行界面。

如果您需要使用图形化界面以会话管理的方式连接Windows实例，可以通过端口转发功能，将Windows的远程访问端口映射到本机，通过RDP工具进行连接，具体操作，请参见[通过会话管理](products/ecs/documents/user-guide/perform-port-forwarding-by-using-ali-instance-cli.md)[CLI](products/ecs/documents/user-guide/perform-port-forwarding-by-using-ali-instance-cli.md)[的端口转发访问无公网实例](products/ecs/documents/user-guide/perform-port-forwarding-by-using-ali-instance-cli.md)。

## 前提条件

待连接实例状态为运行中

实例运行状态可以在ECS控制台中的实例模块查看，运行中的实例如图所示：

查看实例状态的操作说明，请参见[查看实例信息](products/ecs/documents/user-guide/view-instance-information.md)。

|  |  |
| --- | --- |


实例需安装云助手Agent

会话管理基于云助手的功能实现，需要在实例中安装云助手Agent。云助手Agent状态可以在ECS控制台的云助手模块查看，已经安装云助手的实例如图所示：

2017年12月01日之后使用官方公共镜像创建的ECS实例，默认预装了云助手Agent。如果您的实例是2017年12月01日之前购买的或使用自行上传的自定义镜像创建的实例，需自行安装云助手Agent，请参见[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

|  |  |
| --- | --- |


查看云助手Agent状态以及处理异常状态的具体操作，请参见[查看云助手状态及异常状态处理](products/ecs/documents/user-guide/check-the-status-of-cloud-assistant-and-handle-exceptions.md)。

确保网络连通（设置安全组）

通过会话管理连接ECS实例时，需要确保ECS中运行的云助手Agent与云助手服务端的网络连通性，即在安全组出方向设置以下规则：

与SSH、RDP等连接方式不同，由于会话管理是由云助手Agent主动与会话管理服务端建立WebSocket连接，因此仅需放行出方向的云助手服务端的WebSocket端口。关于会话管理的原理，请参见[会话管理工作原理](products/ecs/documents/user-guide/connect-to-an-instance-by-using-session-manager-2.md)。

重要

- 

如果使用普通安全组（包括默认安全组），默认情况下会放行所有的出方向流量，无需配置。

- 

如果使用企业安全组，默认情况下会禁用所有出方向的流量，需要配置以下规则。更多关于企业安全组的说明，请参见[普通安全组与企业级安全组](products/ecs/documents/user-guide/basic-security-groups-and-advanced-security-groups.md)。

添加安全组规则的具体操作，请参见[添加安全组规则](products/ecs/documents/user-guide/add-a-security-group-rule.md)。

| 授权策略 | 优先级 | 协议类型 | 端口范围 | 授权对象 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 允许 | 1 | 自定义 TCP | 443 | 100.100.0.0/16 | 用于访问云助手服务端。 |
| 允许 | 1 | 自定义 TCP | 443 | 100.0.0.0/8 | 访问 云助手 Agent 安装包所在服务器，用于安装或更新您的 云助手 Agent 。 |
| 允许 | 1 | 自定义 UDP | 53 | 0.0.0.0/0 | 用于解析域名。 |


此外，如果您计划仅通过会话管理连接实例，为了增加ECS实例的安全性，您可以取消放行安全组入方向上的SSH端口（默认22）或者RDP端口（默认3389）的规则。

RAM用户使用该功能需拥有相关权限

如果RAM用户需要在控制台使用会话管理连接实例，根据最小授权原则，需要具有以下权限。

- 

ecs:StartTerminalSession：通过会话管理连接实例的权限，此外，可以通过Resource字段，限制RAM用户可连接（会话管理）的ECS实例。

- 

ecs:DescribeCloudAssistantStatus：查询ECS实例是否需要安装云助手，该权限用于控制台在连接前进行校验。

- 

ecs:DescribeUserBusinessBehavior：查询会话管理功能是否已经开启，该权限用于控制台在连接前进行校验。

- 

ecs:ModifyCloudAssistantSettings（可选）：打开或关闭会话管理的权限，如果当前阿里云账号已经开通会话管理，无需分配该权限。

自定义权限策略示例如下：

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" }, { "Effect": "Allow", "Action": [ "ecs:DescribeUserBusinessBehavior", "ecs:DescribeCloudAssistantStatus", "ecs:ModifyCloudAssistantSettings" ], "Resource": "*" } ] }

为RAM用户授权，请参见[为](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

## 操作步骤

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

单击目标实例ID进入实例详情页，单击远程连接。

- 

单击展开其他登录方式，找到通过会话管理远程连接，确保会话管理已开启（全地域），如果显示会话管理已关闭，请先打开功能开关。

重要

打开会话管理功能开关前，请确保RAM用户具有查看会话管理配置的DescribeUserBusinessBehavior权限和打开或关闭会话管理功能的ModifyUserBusinessBehavior权限，详细的权限策略示例，请参见[前提条件](products/ecs/documents/user-guide/connect-to-an-instance-by-using-session-manager-1.md)。

- 

单击免密登录。

连接成功后，Linux实例默认以ecs-assist-user用户登录实例，Windows实例默认以system用户登录。以Linux实例为例，效果如图所示。

## 相关阅读

除了在控制台使用会话管理连接实例外，您还可以在个人计算机上通过命令行使用会话管理的功能连接实例，具体操作，请参见[通过会话管理](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)[CLI（ali-instance-cli）连接实例](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)。

[上一篇：通过会话管理连接实例](products/ecs/documents/user-guide/connect-to-an-instance-by-using-session-manager-2.md)[下一篇：为会话管理开启会话加密](products/ecs/documents/user-guide/turn-on-session-encryption-for-session-management.md)

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
