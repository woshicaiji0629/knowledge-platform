# 权限与访问控制概述-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/permissions-and-access-control-overview

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/oss/documents/user-guide.md)

- [开发参考](products/oss/documents/developer-reference.md)

- [产品计费](products/oss/documents/billing.md)

- [常见问题](products/oss/documents/oss-faq.md)

- [动态与公告](products/oss/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 权限与访问控制概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

对象存储OSS提供多层次权限控制机制，确保数据在存储和访问过程中的安全性。以下介绍OSS权限与访问控制的整体架构，帮助理解各控制方式的定位和差异，根据业务需求选择合适的方案。

## 快速选择

| 场景 | 推荐方案 |
| --- | --- |
| 数据私有，阻止非授权用户和匿名访问 | [Bucket ACL](products/oss/documents/user-guide/bucket-acl-2.md) 设为私有（默认配置） |
| 对外提供公开可读的静态资源 | [Bucket ACL](products/oss/documents/user-guide/bucket-acl-2.md) 设为公共读，配合 [防盗链](products/oss/documents/user-guide/hotlink-protection.md) 防止资源盗用 |
| 授权多个用户访问特定 Bucket | [Bucket Policy](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) ，仅需单条策略即可指定允许的用户列表 |
| 统一管理某个用户可访问的所有资源 | [RAM Policy](products/oss/documents/user-guide/ram-policy.md) 绑定到该用户 |
| 将资源共享给其他阿里云账号 | [Bucket Policy](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) 或 [基于](products/oss/documents/user-guide/cross-account-access-by-ram-role.md) [RAM](products/oss/documents/user-guide/cross-account-access-by-ram-role.md) [角色实现跨账号访问](products/oss/documents/user-guide/cross-account-access-by-ram-role.md) [OSS](products/oss/documents/user-guide/cross-account-access-by-ram-role.md) |
| 同一 Bucket 为多个应用或团队提供差异化访问 | [接入点](products/oss/documents/user-guide/access-point.md) ，每个应用或团队独立的入口和策略 |
| 防止误配置导致数据公开泄露 | [阻止公共访问](products/oss/documents/user-guide/block-public-access.md) |
| 浏览器端 JavaScript 访问 OSS | [跨域设置](products/oss/documents/user-guide/configure-cross-origin-resource-sharing.md) |
| 多账号场景下统一配置权限边界，例如强制开启阻止公共访问功能 | [Control Policy](products/oss/documents/user-guide/control-policy.md) |


## 鉴权机制

OSS根据请求类型采用不同的鉴权流程：

- 

签名请求：OSS验证签名有效性后，分别评估Control Policy（如有）、RAM Policy、Bucket Policy、ACL，综合判定是否允许访问。

- 

匿名请求：OSS评估Control Policy（如有）、Bucket Policy和ACL是否允许公开访问。

鉴权结果分为三类：Allow（策略明确授权）、Explicit Deny（策略明确拒绝，优先级最高）、Implicit Deny（无授权则拒绝）。

完整的鉴权流程请参见[鉴权流程详解](products/oss/documents/user-guide/authentication.md)。

## 权限控制方式

### ACL

ACL（访问控制列表）通过预定义的权限等级控制资源的公开或私有状态，是最简单的权限控制方式。

[Bucket ACL](products/oss/documents/user-guide/bucket-acl-2.md)控制存储空间的默认访问权限，[Object ACL](products/oss/documents/user-guide/object-acl.md)控制单个对象的权限（优先级更高），Object ACL未指定时默认继承Bucket ACL。支持以下权限等级：

| 权限等级 | 效果 |
| --- | --- |
| 私有（private） | 数据私有，仅资源拥有者或被授权用户可访问 |
| 公共读（public-read） | 任何人可读取，仅资源拥有者或被授权用户可写入 |
| 公共读写（public-read-write） | 任何人可公开读取和写入 |


ACL仅支持预定义等级，无法指定授权对象或条件限制。如需精细控制，请使用Bucket Policy或RAM Policy。

### Bucket Policy

[Bucket Policy](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md)是配置在Bucket上的授权策略，定义谁可以访问此Bucket中的资源。支持授权给RAM用户、其他阿里云账号或匿名用户，并可设置IP地址、VPC、时间等条件限制。

当需要授权多个用户访问同一Bucket时，单条Bucket Policy即可完成，无需为每个用户单独配置。

实践教程：[基于](products/oss/documents/user-guide/dual-access-control-with-vpc-and-bucket-policy.md)[VPC Policy](products/oss/documents/user-guide/dual-access-control-with-vpc-and-bucket-policy.md)[和](products/oss/documents/user-guide/dual-access-control-with-vpc-and-bucket-policy.md)[Bucket Policy](products/oss/documents/user-guide/dual-access-control-with-vpc-and-bucket-policy.md)[实现双重访问控制](products/oss/documents/user-guide/dual-access-control-with-vpc-and-bucket-policy.md)｜[基于](products/oss/documents/user-guide/cross-departmental-data-sharing-based-on-bucket-policy.md)[Bucket Policy](products/oss/documents/user-guide/cross-departmental-data-sharing-based-on-bucket-policy.md)[实现跨部门数据共享](products/oss/documents/user-guide/cross-departmental-data-sharing-based-on-bucket-policy.md)

### RAM Policy

[RAM Policy](products/oss/documents/user-guide/ram-policy.md)是绑定到用户身份上的授权策略，定义该用户可以访问哪些OSS资源，适合统一管理某个用户或应用在多个Bucket上的权限。

OSS提供系统策略（如AliyunOSSFullAccess、AliyunOSSReadOnlyAccess）可直接使用，也支持自定义策略。通过RAM角色可实现跨账号访问和STS临时授权。

实践教程：[基于](products/oss/documents/user-guide/cross-account-access-by-ram-role.md)[RAM](products/oss/documents/user-guide/cross-account-access-by-ram-role.md)[角色实现跨账号访问](products/oss/documents/user-guide/cross-account-access-by-ram-role.md)[OSS](products/oss/documents/user-guide/cross-account-access-by-ram-role.md)｜[基于](products/oss/documents/user-guide/access-control-base-on-ram-policy.md)[RAM Policy](products/oss/documents/user-guide/access-control-base-on-ram-policy.md)[控制](products/oss/documents/user-guide/access-control-base-on-ram-policy.md)[OSS](products/oss/documents/user-guide/access-control-base-on-ram-policy.md)[的访问权限](products/oss/documents/user-guide/access-control-base-on-ram-policy.md)

### Control Policy

资源目录[Control Policy](products/oss/documents/user-guide/control-policy.md)是一种基于资源结构（资源夹或成员）的访问控制策略，主要用于定义权限边界。在多账号管理场景中，可通过自定义管控策略统一强制限制各成员账号中的Bucket安全策略，例如强制开启阻止公共访问等。

### Bucket Policy、RAM Policy与Control Policy区别

| 维度 | Bucket Policy | RAM Policy | Control Policy |
| --- | --- | --- | --- |
| 配置位置 | Bucket 上 | RAM 身份主体上 | 资源目录的各级资源结构（资源夹、成员）上 |
| 管理视角 | 以资源为中心：谁可以访问此资源 | 以身份为中心：身份主体可访问哪些资源 | 以组织治理为中心：在整个资源目录范围内统一限制权限边界 |
| 匿名访问 | 支持 | 不支持 | 不支持 |


选择建议：授权多个用户访问同一资源时Bucket Policy更高效；管理单个用户的所有资源权限时RAM Policy更直观；需要匿名访问时只能用Bucket Policy；在多账号场景下，可使用Control Policy统一限制权限边界。三者可同时使用，OSS会综合评估，都允许时请求才通过。

### 接入点

[接入点](products/oss/documents/user-guide/access-point.md)（Access Point）为Bucket提供独立的访问入口。当一个Bucket需要被多个应用或团队以不同权限访问时，可为每个访问方创建独立的接入点，通过接入点策略（AP Policy）分别管理各自的权限，避免在单一Bucket Policy中维护复杂的规则。

每个接入点拥有独立的访问域名、AP Policy和网络限制配置。用户通过接入点访问时，需要RAM Policy与Bucket Policy的合并结果为Allow，且AP Policy也为Allow，请求才通过。

## 安全防护

### 阻止公共访问

[阻止公共访问](products/oss/documents/user-guide/block-public-access.md)开启后，即使ACL或Bucket Policy配置了公开授权也不会生效，防止因误配置导致数据泄露。可在账号级别（作用于所有Bucket）、Bucket级别或接入点级别独立配置，优先级依次递减。

存储敏感数据且无匿名访问需求时，建议在账号级别开启此功能。

### 防盗链

[防盗链](products/oss/documents/user-guide/hotlink-protection.md)通过校验HTTP请求头中的Referer字段，阻止未授权站点引用OSS资源。支持白名单模式（仅允许指定域名）和黑名单模式（拒绝指定域名）。适用于防止图片、视频等资源被盗用。

说明

Referer可被伪造，如需更高安全性建议使用签名URL。

### 跨域设置

浏览器默认禁止网页JavaScript访问不同域名的资源。通过[配置](products/oss/documents/user-guide/configure-cross-origin-resource-sharing.md)[CORS](products/oss/documents/user-guide/configure-cross-origin-resource-sharing.md)[规则](products/oss/documents/user-guide/configure-cross-origin-resource-sharing.md)，OSS会在响应中返回允许跨域的头信息，使浏览器放行请求。适用于前端直传文件、获取资源等场景。

## 授权策略语法

Bucket Policy、RAM Policy、Control Policy和AP Policy均使用JSON格式定义，核心元素包括：

| 元素 | 说明 |
| --- | --- |
| Effect | 授权效果： Allow 或 Deny |
| Principal | 授权对象（RAM Policy 和 Control Policy 不需要） |
| Action | 授权操作，如 oss:GetObject |
| Resource | 授权资源范围 |
| Condition | 生效条件（可选） |


完整的语法说明和Action列表请参见[授权语法与元素](products/oss/documents/user-guide/authorization-syntax-and-elements.md)。

## 相关文档

- 

[对象存储系统权限策略参考](products/oss/documents/user-guide/oss.md)

- 

[使用资源组进行精细化资源控制](products/oss/documents/user-guide/fine-grained-resource-control-using-resource-groups-49.md)

[上一篇：权限与访问控制](products/oss/documents/user-guide/permissions-and-access-controls.md)[下一篇：鉴权流程详解](products/oss/documents/user-guide/authentication.md)

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
