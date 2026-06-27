# 通过删除域名和管理日志停止CDN计费-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/support/how-do-i-shut-down-the-cdn-service-or-stop

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 如何关闭CDN服务或停止计费？

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文将给您介绍停用阿里云CDN的操作。如果您有停用阿里云CDN的需求，请您仔细按照文档的介绍进行操作，避免在停用后产生额外费用。

考虑到CDN服务开通之后将会关联许多系统逻辑，直接关闭可能会导致客户的业务受到影响，因此阿里云暂时没有提供一键关闭CDN服务功能。但是只要不添加CDN加速域名或者边缘程序等相关功能，那么CDN服务是不会产生计费的（基本等同于关闭CDN服务），具体参考以下操作方法：

## 关闭实时日志推送

如果您之前开通了实时日志推送服务，请在删除域名之前，先关闭实时日志推送功能，并且清空已经转存到日志服务产品上日志。您可以参考[什么是实时日志](products/cdn/documents/user-guide/overview-1.md)，了解更多实时日志的信息。

操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，选择日志管理>实时日志。

- 

在实时日志推送页签，单击Project 的修改域名按钮，在修改域名页签中，点击清空按钮，随后点击修改按钮。

- 

选择第三步操作的Project，点击操作列的，选择删除服务。

## 关闭离线日志转存

如果您之前开通了离线日志转存服务，请在删除域名之前，先关闭离线日志转存功能，并且清空已经转存到OSS产品上日志。您可以[【CDN](products/cdn/documents/user-guide/use-function-compute-to-deliver-logs.md)[控制台】通过函数计算转存离线日志](products/cdn/documents/user-guide/use-function-compute-to-deliver-logs.md)来了解更多原理离线日志的信息。

操作步骤

- 

在CDN控制台取消关联域名。

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，选择日志管理>离线日志。

- 

单击通过函数计算转存离线日志页签。

- 

单击关联域名，在弹窗右侧勾选需要取消的域名，单击。

- 

单击确认，取消关联域名。

- 

可选：在函数计算控制台删除函数和服务。

说明

开通离线日志功能时，在函数计算中指定或者创建了函数和服务为离线日志功能服务，如果您不再需要可同步删除该函数和服务，可选择删除函数和服务，避免残留过多配置。

- 

删除函数：请参考[删除函数](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/manage-functions#multiTask3514)。

- 

删除服务：请参考[删除服务](https://help.aliyun.com/zh/functioncompute/fc-2-0/user-guide/manage-services#multiTask427)。

- 

在OSS控制台删除对应的存储Bucket数据。

说明

日志只要存储在OSS的存储Bucket就会收取少量费用，建议您主动删除存储Bucket数据。

删除对应的存储Bucket数据：请参考[删除存储空间](products/oss/documents/basic-settings-delete-buckets.md)。

## 删除加速域名

如果您之前添加了CDN加速域名，请删除所有已添加的CDN加速域名，删除加速域名可以彻底停止指定域名的CDN加速服务，CDN不会再产生任何有关该域名的费用。请参见[停止加速服务](products/cdn/documents/user-guide/disable-or-remove-an-accelerated-domain-name.md)。

操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，定位目标域名，在操作列中，选择>删除。

- 

在确认删除域名对话框中，单击确定。

警告

删除加速域名之后，CDN将会删除该域名及其对应的配置，该行为属于风险操作，系统将会根据用户账号的权限设置进行二次身份验证，详情请参见[风险操作二次身份验证](products/cdn/documents/user-guide/risk-operation-secondary-authentication.md)。

[上一篇：CDN节点与镜像站点的区别是什么？](products/cdn/documents/support/differences-between-a-cdn-pop-and-a-mirror.md)[下一篇：回源/源站](products/cdn/documents/support/51a989.md)

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
