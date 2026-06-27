# 基于RAM的访问控制工作原理-专有网络VPC-阿里云

Source: https://help.aliyun.com/zh/vpc/how-vpc-and-ram-work-together

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/vpc/documents/vpc-user-guide.md)

- [开发参考](products/vpc/documents/developer-reference.md)

- [产品计费](products/vpc/documents/product-billing.md)

- [常见问题](products/vpc/documents/troubleshooting.md)

- [动态与公告](products/vpc/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 专有网络VPC如何与RAM协同工作

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/vpc)

[我的收藏](https://help.aliyun.com/my_favorites.html)

访问控制 RAM（Resource Access Management）是阿里云提供的一项服务，可以帮助您集中管理用户身份与资源访问权限。企业内有多名员工或应用程序需要访问专有网络 VPC（Virtual Private Cloud）的资源时，可以使用RAM服务做统一的权限管理，按需为他们分配不同的访问权限。在使用RAM管理阿里云产品的访问权限前，您需要了解云产品能与RAM的哪些功能结合使用，从而更好地设计满足业务需要的访问控制。本文介绍专有网络 VPC支持的RAM功能以及这些功能与RAM协同工作的原理。

## 概述

访问控制RAM使用权限来描述用户、用户组、角色对具体资源的访问能力，权限策略是一组访问权限的集合。RAM用户、用户组或RAM角色通过绑定权限策略，可以获得权限策略中指定的访问权限。

### 权限

云账号、RAM用户、资源创建者所拥有的权限说明如下：

- 云账号（资源属主）控制所有权限。

- 每个资源有且仅有一个资源属主，该资源属主必须是云账号，对资源拥有完全控制权限。

- 资源属主不一定是资源创建者。例如：一个RAM用户被授予创建资源的权限，该用户创建的资源归属于云账号，该用户是资源创建者但不是资源属主。

- RAM用户（操作员）默认无任何权限。

- RAM用户代表的是操作员，其所有操作都需被云账号显式授权。

- 新建的RAM用户默认没有任何操作权限，只有在被授权之后，才能通过控制台和RAM操作资源。

- 资源创建者（RAM用户）默认对所创建资源没有任何权限。

- RAM用户被授予创建资源的权限，用户将可以创建资源。

- RAM用户默认对所创建资源没有任何权限，除非资源属主对RAM用户有显式的授权。

### 权限策略

权限策略是用语法结构描述的一组权限的集合，可以精确地描述被授权的资源集、操作集以及授权条件。

RAM支持以下两种权限策略：

- 

系统策略：统一由阿里云创建，您只能使用不能修改，策略的版本更新由阿里云维护。更多信息，请参见[专有网络](products/vpc/documents/vpc-1694081077178.md)[VPC](products/vpc/documents/vpc-1694081077178.md)[系统权限策略参考](products/vpc/documents/vpc-1694081077178.md)。

- 

自定义策略：如果系统策略不能满足您的要求，您可以创建自定义策略实现精细化的权限管理。更多信息，请参见[专有网络](products/vpc/documents/vpc-custom-permission-policy-reference.md)[VPC](products/vpc/documents/vpc-custom-permission-policy-reference.md)[自定义权限策略参考](products/vpc/documents/vpc-custom-permission-policy-reference.md)。

### 为RAM主体绑定权限策略

权限策略创建后，RAM用户、用户组或RAM角色需绑定权限策略，才能获得权限策略中指定的访问权限。

- 

支持为RAM用户、用户组或RAM角色绑定一个或多个权限策略。

- 

绑定的权限策略可以是系统策略也可以是自定义策略。

- 

如果绑定的权限策略被更新，更新后的权限策略自动生效，无需重新绑定权限策略。

[上一篇：使用RAM进行访问控制](products/vpc/documents/identity-management-and-access-control.md)[下一篇：使用资源组进行精细化资源控制](products/vpc/documents/fine-grained-resource-control-using-resource-groups-64.md)

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
