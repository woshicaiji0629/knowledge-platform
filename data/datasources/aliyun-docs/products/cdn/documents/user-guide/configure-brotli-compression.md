# 开启Brotli压缩-CDN-阿里云-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/configure-brotli-compression

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

# Brotli压缩

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Brotli是开源的一种新型压缩算法，Brotli压缩比Gzip压缩性能更好。开启Brotli压缩功能后，CDN节点会对资源进行智能压缩后返回，缩小传输文件大小，提升文件传输效率，减少带宽消耗。

## 背景信息

- 

压缩分为Gzip压缩和Brotli压缩，智能压缩功能主要针对Gzip压缩，智能压缩详情请参见[Gzip](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md)[压缩](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md)。

- 

当源站文件的大小在1 KB~10 MB及之间时，才可以使用Gzip压缩或Brotli压缩，对1 KB以下和10 MB以上大小的文件不做压缩。

- 

Brotli压缩支持的文件类型有text/xml、text/plain、text/css、application/javascript、application/x-javascript、application/rss+xml、text/javascript、image/tiff、image/svg+xml、application/json、application/xml。

- 

服务端响应携带响应头Content-Encoding: br：服务端响应的内容是经过Brotli压缩后的资源。

- 

客户端请求携带请求头Accept-Encoding: br：客户端希望获取对应资源时进行Brotli压缩。

## 注意事项

- 

CDN对静态文件进行压缩时，会改变文件的MD5值，如果源站文件配置了MD5校验机制，请关闭智能压缩和Brotli压缩功能。

- 

源站开启了压缩功能，且服务端响应中携带了content_encoding，则CDN的压缩功能将不再生效。

- 

同时开启Brotli压缩和智能压缩，且客户端请求头Accept-Encoding同时携带br和gzip时，仅Brotli压缩生效。

- 

如果您同时开启了页面优化和压缩功能（Gzip压缩或者Brotli压缩），页面优化功能将会失效，CDN只会对文件进行压缩。

- 

Brotli压缩只兼容部分浏览器，您可以根据业务需要[查询](https://caniuse.com)浏览器的兼容情况。

- 

常见的图片文件类型（PNG、JPG、JPEG等）和视频文件类型（MP4、AVI、WMV等）已经做了内容的压缩处理，开启智能压缩或者Brotli压缩没有效果，建议您关闭压缩功能。如果您需要进一步减小图片文件的体积可以使用[图像处理](products/cdn/documents/user-guide/image-editing-overview.md)功能，如果您需要进一步减小视频文件的体积可以使用[视频转码](https://help.aliyun.com/zh/mps/product-overview/features#concept-1960458)功能。“图像处理”和“视频转码”都会影响文件清晰度。

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

在Brotli压缩区域框中，打开Brotli压缩开关，完成配置。

成功开启Brotli压缩功能后，您可以对比查看原始请求收到的文件类型和开启Brotli压缩之后收到的文件类型，如果收到.br后缀的文件，说明文件已经被压缩了。

## 相关API

[BatchSetCdnDomainConfig](products/cdn/documents/api-batchsetcdndomainconfig.md)

[上一篇：Gzip压缩](products/cdn/documents/user-guide/use-the-gzip-compression-feature.md)[下一篇：图像处理](products/cdn/documents/user-guide/image-editing.md)

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
