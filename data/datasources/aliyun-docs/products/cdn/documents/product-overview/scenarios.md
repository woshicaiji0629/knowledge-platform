# 典型应用场景业务加速详解-CDN-阿里云-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/product-overview/scenarios

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

# 应用场景

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

CDN具有广泛的应用场景，可实现图片小文件、大文件下载和视音频点播业务类型的加速，本文介绍阿里云CDN产品的应用场景。

## 场景概述

阿里云CDN的应用场景如下表所示。

| 应用场景 | 场景概述 |
| --- | --- |
| [图片小文件](products/cdn/documents/product-overview/scenarios.md) | 适用于各类网站或应用中小文件的加速分发，例如各种门户网站、电子商务类网站、新闻资讯类网站或应用、娱乐游戏类网站等。 |
| [大文件下载](products/cdn/documents/product-overview/scenarios.md) | 适用于各类大文件的下载和分发加速，例如游戏安装包、应用更新、手机 ROM 升级、应用程序包下载等，平均单个文件大小在 20 MB 以上。 |
| [视音频点播](products/cdn/documents/product-overview/scenarios.md) | 适用于各类视音频网站的文件分发和访问加速，例如影视类视频网站、在线教育类视频网站、新闻类视频网站、短视频社交类网站以及音频类相关网站和应用，支持 MP4、FLV 等主流视频格式。 |


业务类型主要影响CDN的调度优化策略，例如大文件下载场景会启用分片回源和预加载等优化。选择与实际业务不完全匹配的类型不会导致加速不可用，CDN仍会正常进行内容分发和缓存，但建议您根据实际文件大小和业务特征选择对应的业务类型，以获得最佳的加速效果。

## 图片小文件

图片小文件适用于网站或应用中小文件的加速分发，例如各种门户网站、电子商务类网站、新闻资讯类网站、娱乐游戏类网站等。您需要将源站内容进行动静态分离，静态内容使用阿里云CDN加速，例如图片、CSS、JS小文件等；动态内容使用[阿里云全站加速](https://www.aliyun.com/product/dcdn)[DCDN](https://www.aliyun.com/product/dcdn)产品。

说明

- 

静态内容是指在不同请求中访问到的数据都相同的静态文件。例如：图片、视频、网站中的文件（html、css、js）、软件安装包、apk文件、压缩包等。

- 

动态内容是指在不同请求中访问到的数据不相同的动态内容。例如：网站中的文件（asp、jsp、php、perl、cgi）、API接口、[数据库](https://www.aliyun.com/getting-started/what-is/what-is-cloud-database)交互请求等。

关于动态和静态资源的详细介绍，请参见[什么是静态内容和动态内容？](products/cdn/documents/support/what-are-static-content-and-dynamic-content.md)。

CDN加速图片小文件业务可以帮您解决以下问题：

- 

终端用户访问慢：网站小文件内容多、打开速度太慢。

- 

跨区域访问质量差：终端用户分布在不同区域，不同区域的访问速度和质量高低不一。

- 

高并发压力大：运营推广期间，源站服务器压力大，服务器容易崩溃，造成服务不可用。

- 

图片格式分辨率处理复杂：无法根据适合的终端情况进行图片压缩和优化。

## 大文件下载

大文件下载适用于各类大文件的下载和分发加速，例如游戏安装包、应用更新、手机ROM升级、应用程序包下载等，平均单个文件大小在20 MB以上。

CDN加速大文件下载业务可以帮您解决以下问题：

- 

终端用户无法下载或者下载太慢。

- 

网络环境不稳定时，下载容易中断，重新下载会耗费额外的资源。

- 

网站内容不安全，容易被劫持或者盗链，对业务造成额外的损失。

- 

高并发下载或者下载突增场景下对源站性能要求非常高，且源站的带宽成本也较高。

## 视音频点播

视音频点播适用于各类视音频网站，例如影视类视频网站、在线教育类视频网站、新闻类视频网站、短视频社交类网站以及音频类相关网站和应用，您可以使用阿里云CDN产品实现对音视频内容的文件分发和访问加速。

CDN加速视音频点播业务可以帮您解决以下问题：

- 

终端用户访问视频时打不开视频或容易卡顿，观看不流畅。

- 

视频资源容易被劫持或盗用，版权得不到有效保护。

- 

高并发访问或者访问突增场景下对源站性能要求非常高，且源站的带宽成本也较高。

如果您需要同时完成对音视频内容的上传、转码、存储、分发等处理，您可以使用阿里云的视频点播产品，该产品集音视频上传、自动化转码处理、媒体资源管理、分发加速于一体，提供完整地一站式视频点播解决方案。视频点播相关介绍，请参见[什么是视频点播](https://help.aliyun.com/zh/vod/product-overview/what-is-apsaravideo-vod#concept-2526011)。

[上一篇：阿里云CDN的五大竞争力](products/cdn/documents/product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)[下一篇：功能特性](products/cdn/documents/product-overview/product-function-node-cdn.md)

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
