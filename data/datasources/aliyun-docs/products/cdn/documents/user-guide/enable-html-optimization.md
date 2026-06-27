# 配置页面优化用于删除页面冗余信息-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/enable-html-optimization

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

# 页面优化

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

开启页面优化功能，CDN会自动删除页面的冗余内容，例如HTML页面、内嵌JavaScript和CSS中的注释以及重复的空白符，可以有效去除页面的冗余信息，缩小文件体积，提高加速分发效率，同时也可以提升页面的可阅读性。

## 注意事项

- 

如果源站文件配置了MD5校验机制，请不要开启页面优化功能。

开启页面优化功能，CDN进行页面优化时，会改变文件的MD5值，导致优化后文件的MD5值和源站文件的MD5值不一致。

- 

如果源站开启了Gzip压缩或Brotli压缩，CDN的页面优化功能将会失效，CDN会将源站压缩后的文件透传给客户端。

在不关闭源站的Gzip或Brotli压缩的情况下，如果想使用CDN的页面优化功能，您可以在CDN的回源HTTP头中进行配置，删除Accept-Encoding头。CDN回源删除Accept-Encoding后，CDN页面优化功能即可正常执行。删除Accept-Encoding头，请参见[修改出站请求头](products/cdn/documents/user-guide/configure-custom-request-headers.md)。

- 

如果您同时开启了页面优化和压缩功能（Gzip压缩或者Brotli压缩），页面优化功能将会失效，CDN只会对文件进行压缩。

- 

在某些特殊情况下，开启页面优化功能，改写网站页面中的HTML文件、CSS文件、JS文件可能会影响到网站的业务逻辑，客户端访问改写以后的网站页面可能会出现类似Hydration completed but contains mismatches.这样的报错，这个时候关闭页面优化功能即可解决问题。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击性能优化。

- 

在页面优化区域框中，您可以选择开启HTML优化、CSS优化或JavaScript优化。

说明

“HTML优化”这个开关是页面优化功能的总开关，如果仅打开“HTML优化”开关，则只会开启HTML优化功能；如果要开启CSS优化或JavaScript优化，需要先打开“HTML优化”开关，然后再打开“CSS优化”或者“JavaScript优化”开关，CSS优化或者JavaScript优化才会生效。

- 

开启HTML优化：即可实现对HTML页面的优化。

- 

开启CSS优化：即可实现对CSS的优化。

- 

开启JavaScript优化：即可实现对JavaScript的优化。

## 常见问题

[同时开启页面优化和](https://developer.aliyun.com/article/776017)[Gzip](https://developer.aliyun.com/article/776017)[压缩功能，页面优化不生效？](https://developer.aliyun.com/article/776017)

## 相关API

[BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md)

[上一篇：性能优化概述](products/cdn/documents/user-guide/performance-optimization-overview.md)[下一篇：Gzip压缩](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md)

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
