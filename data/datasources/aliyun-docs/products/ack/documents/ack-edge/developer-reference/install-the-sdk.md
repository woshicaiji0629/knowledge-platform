# 使用容器服务SDK-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/install-the-sdk

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-edge/product-overview.md)

- [快速入门](products/ack/documents/ack-edge/quick-start.md)

- [操作指南](products/ack/documents/ack-edge/user-guide.md)

- [实践教程](products/ack/documents/ack-edge/use-cases.md)

- [安全合规](products/ack/documents/ack-edge/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-edge/developer-reference.md)

- [服务支持](products/ack/documents/ack-edge/support.md)

[首页](https://help.aliyun.com/zh)

# Java SDK调用示例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍如何通过SDK调用OpenAPI创建一个ACK托管集群。

## 步骤一：查看OpenAPI文档

在调用OpenAPI前，建议您先阅读对应的接口文档[通过](products/ack/documents/create-an-ack-managed-cluster.md)[OpenAPI](products/ack/documents/create-an-ack-managed-cluster.md)[创建](products/ack/documents/create-an-ack-managed-cluster.md)[ACK](products/ack/documents/create-an-ack-managed-cluster.md)[托管集群](products/ack/documents/create-an-ack-managed-cluster.md)，了解、学习调用该接口所需要的参数及权限等，更多参数请参见[API](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-overview.md)[概览](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-overview.md)。

## 步骤二：创建RAM用户并完成授权

您可以使用阿里云账号（主账号）、RAM用户、RAM角色调用该接口，有关各种身份的差异请参见[身份](https://help.aliyun.com/zh/openapi/identity)。

重要

阿里云账号拥有所有API的访问权限，建议您创建并使用RAM用户进行API访问或日常运维。

- 

[创建](products/ram/documents/user-guide/create-a-ram-user.md)[RAM](products/ram/documents/user-guide/create-a-ram-user.md)[用户](products/ram/documents/user-guide/create-a-ram-user.md)。

- 

使用阿里云账号登录[RAM](https://ram.console.aliyun.com/)[访问控制](https://ram.console.aliyun.com/)。

- 

在左侧导航栏，选择身份管理>用户。

- 

在用户页面，单击创建用户。

- 

在创建用户页面，设置登录名称和显示名称、访问方式为控制台访问。

- 

单击确定。

创建RAM用户成功后，请记录用户登录名称和密码。在调用OpenAPI时，需要使用该RAM用户登录阿里云OpenAPI开发者门户。

- 

为RAM用户授予AliyunCSFullAccess权限。具体操作，请参见[管理](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

说明

AliyunCSFullAccess：管理容器服务 Kubernetes 版的权限。

AliyunCSReadOnlyAccess：只读访问容器服务 Kubernetes 版的权限。

如果您需要新建自定义权限，请参见[授权信息](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-ram.md)。

- 

进入对应的RAM用户详情页，在认证管理页签，单击创建 AccessKey。具体操作，请参见[创建](products/ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](products/ram/documents/user-guide/create-an-accesskey-pair.md)。

## 步骤三：调用OpenAPI

本示例使用RAM用户调用CreateCluster创建一个ACK托管集群Pro版，通过Java语言SDK为例介绍，其他语言SDK的用法类似，更多信息请参见[容器服务](https://api.aliyun.com/api-tools/sdk/CS?version=2015-12-15&language=java-async-tea)[Kubernetes](https://api.aliyun.com/api-tools/sdk/CS?version=2015-12-15&language=java-async-tea)[版](https://api.aliyun.com/api-tools/sdk/CS?version=2015-12-15&language=java-async-tea)[SDK](https://api.aliyun.com/api-tools/sdk/CS?version=2015-12-15&language=java-async-tea)。您也可根据业务的实际需要选择其他调用方式，更多调用方法请参见[调用方式](https://help.aliyun.com/zh/openapi/developer-reference/overview-of-calling-methods)。

### 配置环境变量

调用接口前，您需要配置环境变量以获取访问凭证。环境变量配置操作，请参见[在](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Linux、macOS](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[和](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[Windows](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)[系统配置环境变量](https://help.aliyun.com/zh/sdk/developer-reference/configure-the-alibaba-cloud-accesskey-environment-variable-on-linux-macos-and-windows-systems)。

### 下载SDK示例代码

- 

访问[CreateCluster](https://next.api.aliyun.com/api/CS/2015-12-15/CreateCluster)。

- 

在左侧参数配置区域，填写需要的参数信息，然后单击发起调用。

- 

name示例值：test

- 

region_id示例值：cn-beijing

- 

cluster_type示例值：ManagedKubernetes

- 

cluster_spec示例值：ack.pro.small

- 

cluster_version示例值：1.30.1-aliyun.1

- 

vpcid示例值：vpc-2zedl8cyb7tnkaux1****

- 

container_cidr示例值：10.0.0.0/8

- 

service_cidr示例值：172.21.0.0/20

- 

vswitch_ids示例值：vsw-2ze7hfp0ah8rk1nz9****

- 

在右侧SDK示例页签，选择SDK版本为2.0和SDK语言，然后单击下载完整工程，下载后在本地完成解压。

说明

SDK版本推荐使用V2.0版本。关于V2.0和V1.0的区别，请参见[V1.0 SDK](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)[和](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)[V2.0 SDK](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)[区别](https://help.aliyun.com/zh/sdk/product-overview/differences-between-v1-and-v2-sdks)。

在页面左侧参数配置页签中填写请求参数（如name、region_id、cluster_type、cluster_spec、kubernetes_version等）后，右侧代码区域将实时生成对应语言的 SDK 示例代码。

### 运行SDK示例代码

- 

打开IntelliJ IDEA，单击File->Open，选择解压后的工程文件夹，等待Maven自动安装依赖信息。

- 

运行示例代码。

双击打开Sample，确认无报错后，运行代码。

- 

查看运行结果。

在底部控制台搜索statusCode，如果看到"statusCode":202表示调用成功已开始创建集群。您可以在[容器服务管理控制台](https://cs.console.aliyun.com)的集群列表页面看到新创建的集群。

{ "headers": { "content-type": "application/json;charset=utf-8", "access-control-expose-headers": "*", "x-acs-trace-id": "30c74bc83a7fae0a081e5f5846be703e" }, "statusCode": 202, "body": { "clusterId": "c6104ee21d6304ef8..." } }

[上一篇：SDK下载](products/ack/documents/ack-edge/developer-reference/sdk-description.md)[下一篇：CLI参考](products/ack/documents/ack-edge/developer-reference/cli-reference.md)

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
