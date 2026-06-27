# 配置自定义错误页面-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/create-a-custom-error-page

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

# 配置自定义页面

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

配置自定义错误页面后，当用户请求的内容不存在或出现错误时，CDN节点会返回自定义的错误页面，而不是默认的错误页面。自定义错误页面可以提高用户体验，让用户看到更友好的错误提示。

## 背景信息

阿里云CDN提供了在出现指定错误码的时候，能够让用户跳转到自定义页面的功能。

当客户端通过浏览器请求Web服务时，如果请求的URL不存在，Web服务器默认会返回404报错页面。Web服务器默认的报错页面通常不美观，为了提升访问者的体验，您可以配置自定义页面，根据所需自定义HTTP或HTTPS响应状态码跳转的完整URL地址。

说明

自定义页面如果使用的是CDN加速的资源，那么将会按照正常的CDN内容分发来计费。

### 支持的状态码

仅支持针对400、403、404、405、414、416、500、501、502、503、504这些状态码设置自定义页面。

| 状态码 | 描述 |
| --- | --- |
| 400 | 您访问的页面请求错误时，返回此代码。 |
| 403 | 服务器拒绝请求时，返回此代码。 |
| 404 | 请求服务器上不存在的网页时，返回此代码。 |
| 405 | 禁用请求中指定的方法时，返回此代码。 |
| 414 | 请求的 URL 过长服务器无法处理时，返回此代码。 |
| 416 | 页面无法提供请求的范围时，返回此代码。 |
| 500 | 服务器遇到错误无法完成请求时，返回此代码。 |
| 501 | 服务器不具备完成请求的功能时，返回此代码。 |
| 502 | 服务器作为网关或代理从上游服务器收到无效响应时，返回此代码。 |
| 503 | 服务器目前无法使用时，返回此代码。 |
| 504 | 服务器作为网关或代理无法及时从上游服务器收到请求时，返回此代码。 |


## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击缓存配置。

- 

单击自定义页面页签。

- 

单击添加，配置自定义页面的错误码和链接。

例如，错误码选择404，描述自动显示为对应说明，链接输入自定义错误页面地址如http://example.aliyundoc.com/error404.html，单击确定完成配置。

- 

单击确定，完成配置。

成功配置自定义页面后，您可以在自定义页面列表中，对当前的配置进行修改或删除操作。

## 配置示例

您希望将404页面显示为自定义页面，假设您已经将自定义404页面error404.html存放在源站的根目录下，并且通过加速域名example.aliyundoc.com可以访问到这个404页面，这个时候您可以通过以下配置来实现404状态码的自定义错误页面。

- 

错误码：404

- 

链接：您自定义的URL页面，例如：http://example.aliyundoc.com/error404.html。

- 

结果：访问返回404报错时，会跳转到http://example.aliyundoc.com/error404.html页面。

## 常见问题

### 配置自定义 403 页面时如何避免域名跳转或循环重定向？

为 403 状态码配置自定义错误页面时，如果直接在错误页面设置中配置跳转链接，可能出现域名跳转或循环重定向的问题。可通过以下方式避免：

- 

通过 CDN 控制台的[重写访问 URL](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)功能进行配置，而非直接在自定义错误页面中设置跳转链接。

- 

将待重写的 Path 设置为/，并将目标路径指向正确的 403 静态页面地址（例如/error/403.html）。

重要

请确保 403 错误页面本身不会再次触发 403 状态码的重定向，否则会导致循环重定向，无法正常访问页面。

## 相关API

[BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md)

[上一篇：响应过期缓存](products/cdn/documents/user-guide/serve-stale-content.md)[下一篇：重写访问URL](products/cdn/documents/user-guide/create-an-access-url-rewrite-rule.md)

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
