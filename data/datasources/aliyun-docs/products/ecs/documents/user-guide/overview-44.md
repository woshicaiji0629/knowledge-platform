# 什么是安全组.安全组能力介绍,普通安全组,企业级安全组,默认安全组,托管安全组,安全组使用建议-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/overview-44

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

# 安全组概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

安全组是一种虚拟防火墙，能够控制ECS实例的出入站流量。您可以将具有相同安全需求并相互信任的ECS实例放入相同的安全组，以划分安全域，保障云上资源的安全。本文介绍安全组的功能、分类、最佳实践和操作指引等。

## 功能介绍

创建ECS实例时，您需要指定一个或多个安全组。ECS 实例关联的多个安全组的规则将按固定的策略排序，共同决定是否放行实例出入站的流量。

您可以为安全组新增规则，修改或删除已有规则，这些规则变动会自动作用于安全组中的所有ECS实例。安全组规则由授权对象、目的端口、协议类型、授权策略（允许或拒绝）和优先级组成。安全组的入方向规则控制ECS实例入站的流量，出方向规则控制ECS实例出站的流量，详情请参见[安全组规则](products/ecs/documents/user-guide/security-group-rules.md)。

ECS实例关联的安全组，其规则作用于主网卡。专有网络ECS实例的其他弹性网卡，可以指定与主网卡不同的安全组。

配置安全组时，您还需要了解如下信息：

- 

在专有网络VPC下，安全组仅能在所属的VPC下使用，在创建专有网络VPC的ECS实例时，您指定的虚拟交换机和安全组，必须属于同一个VPC。

- 

ECS实例或者弹性网卡可以关联一个或者多个安全组，但必须至少关联一个安全组。ECS实例和弹性网卡关联安全组的数量限制，请参见[安全组使用限制](products/ecs/documents/user-guide/limitations.md)。

- 

在创建ECS实例时，如果您未指定安全组，系统会将该ECS实例的主网卡关联到默认安全组，详情请参见[默认安全组](products/ecs/documents/user-guide/default-security-groups.md)。

例如下图所示，专有网络VPC包含ECS 1和ECS 2，两个ECS的主网卡都关联安全组1。假设安全组1是普通安全组，组内连通策略默认为组内互通，那么ECS 1和ECS 2的内网是互通的，这种互通策略不受您配置的自定义规则的影响。ECS 1和ECS 2的其他出入方向流量受到安全组1的自定义规则控制。根据安全组1的入方向规则，使用任意IP都可以ping通安全组1内ECS 1和ECS 2，安全组1未配置出方向规则，默认允许所有出方向的流量。

## 安全组分类

普通安全组和企业级安全组

根据特性不同，安全组分为普通安全组和企业级安全组，两者均免费，适用于不同的使用场景。

- 

普通安全组：支持组内互通功能，支持添加授权安全组访问的规则，但可容纳的私网IP数量小于企业级安全组。

- 

企业级安全组：可以容纳更多的私网IP地址数量，但不支持组内互通功能，也不支持添加授权安全组访问的规则。

在ECS实例关联到多个安全组时，同一块弹性网卡只能使用一种类型的安全组。建议您根据自己的使用需求来选择安全组类型，详情请参见[普通安全组与企业级安全组](products/ecs/documents/user-guide/basic-security-groups-and-advanced-security-groups.md)。

自定义安全组和托管安全组

根据操作权限归属不同，安全组分为自定义安全组和托管安全组。自定义安全组和托管安全组都可以是普通安全组或者企业级安全组。

- 

自定义安全组：由阿里云账号直接在ECS控制台上创建的安全组为自定义安全组，您拥有自定义安全组的操作权限。默认安全组也属于自定义安全组，详情请参见[创建安全组](products/ecs/documents/user-guide/create-a-security-group-1.md)。

- 

托管安全组：云产品可以为您创建托管安全组，操作权限属于云产品，您仅能查看不能操作，详情请参见[托管安全组](products/ecs/documents/user-guide/managed-security-groups.md)。

在您使用[DescribeSecurityGroups](products/ecs/documents/api-describesecuritygroups.md)接口查询到安全组的ServiceManaged属性为True，或使用控制台看到安全组有类似云产品托管的安全组不支持修改操作的提示时，表示该安全组为托管安全组。

## 安全组使用的最佳实践

关于安全组的使用，为您提供以下最佳实践建议：

- 

规划

您可以为安全组设置名称、描述，也可以设置安全组的标签、资源组，便于进行分类运维。建议您合理设置这些信息，方便快速识别安全组的用途，在管理较多安全组时更加清晰。

- 

以白名单的方式使用安全组

即默认拒绝所有访问，添加允许规则来放通指定的端口范围和授权对象。

- 

添加安全组规则时遵循最小授权原则

例如，开放Linux实例的22端口用于远程登录时，建议仅允许特定的IP访问，而非所有IP（0.0.0.0/0）。

- 

遵循最小权限原则

在不需要普通安全组内ECS实例互相内网互通时，将普通安全组的组内连通策略设置为组内隔离。

- 

尽量保持单个安全组内规则的简洁

按照用途将规则维护在多个安全组中，并将实例关联到这些安全组。单个安全组的规则数量过多，会增加管理复杂度。安全组规则的健康检查，提供了检测单个安全组冗余规则的能力，详情请参见[检查安全组是否存在冗余规则](products/ecs/documents/user-guide/manage-security-group-rules.md)。

- 

不同类型应用的实例加入不同的安全组，分别维护安全组规则

例如，将允许公网访问的实例关联到同一个安全组，仅放通对外提供服务的端口，例如80、443等，默认拒绝其他所有访问。避免在允许公网访问的实例上提供其他服务，例如MySQL、Redis等，建议将内部服务部署在不允许公网访问的实例上，并关联其他的安全组。

- 

避免直接修改线上环境使用的安全组

可以先克隆一个安全组在测试环境调试，确保修改后实例流量正常，再对线上环境的安全组规则进行修改。

说明

如果您需要检测ECS常用端口是否被安全组规则放行，或者检测安全组规则是否允许特定IP与ECS网卡单向访问，您可以在诊断下的安全组规则检测页签完成操作。具体操作，请参见[安全组规则检测](products/ecs/documents/user-guide/safety-set-of-rules-to-detect.md)。

## 相关文档

- 

[管理安全组和规则](products/ecs/documents/user-guide/start-using-security-groups.md)，可提供精细化的网络安全隔离与访问控制。

- 

安全组配额相关信息，详情请参见[安全组使用限制](products/ecs/documents/user-guide/limitations.md)。

- 

想要给ECS实例绑定多张弹性网卡，详情请参见[弹性网卡概述](products/ecs/documents/user-guide/eni-overview.md)。

- 

合理使用安全组可以有效提高实例的安全性，但提高实例安全性是一项系统的工作，您还可以结合更多其他做法，详情请参见[云服务器](products/ecs/documents/user-guide/best-security-practices.md)[ECS](products/ecs/documents/user-guide/best-security-practices.md)[安全性](products/ecs/documents/user-guide/best-security-practices.md)。

[上一篇：安全组](products/ecs/documents/user-guide/security-groups-1.md)[下一篇：安全组规则](products/ecs/documents/user-guide/security-group-rules.md)

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
