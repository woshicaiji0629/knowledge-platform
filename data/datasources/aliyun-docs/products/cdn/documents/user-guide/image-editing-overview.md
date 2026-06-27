# 在CDN节点上对图片进行处理-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/image-editing-overview

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

# 图片处理概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在一些内容分享网站，一张原始图片可能会根据业务的需要被缩放、裁剪、旋转、压缩等，若每次处理都需要回源，则会增加回源次数及CDN节点缓存。阿里云CDN提供图像处理功能，可直接在CDN的L2节点对图片进行处理，同时缓存处理后的图片，能够有效提升内容返回速度，减轻源站压力，减少回源流量等。

说明

- 

阿里云CDN、DCDN和OSS的图片处理都是独立的功能，不能相互混用。

- 

图像处理为付费服务，公测期间暂不收费，收费时间另行通知。

- 

当您使用图像处理功能时，由于不同图片格式在压缩算法上存在较大差异，因此不同图片格式之间相互转换可能会导致图片体积变大，例如：jpeg转webp、jpeg转png、png转webp。如果您需要降低图片文件的体积，建议您通过调整质量参数quality降低图片质量来实现。

## 适用场景

通过CDN进行图片处理，所有的图片处理和缓存都通过CDN节点完成，源站无感知。

下表为您列出了图片处理常见的适用场景，适用场景较多，不仅限于以下场景。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 适用场景 | 说明 |
| --- | --- |
| 电商平台 | 多种样式图片处理满足多终端图片显示场景，图片编辑更加高效便捷。 可对商品图、图片评论等进行压缩，减少图片文件大小，达到省流量的目的。 支持添加水印，用于版权保护，具有品牌标识、宣传推广作用。 |
| 社交软件 | 简单、灵活的图片编辑方式满足社交图片标准的图片处理需求。 支持添加水印，保护个人信息不被盗用。 |
| 在线教育 | 简单、灵活的图片编辑方式满足在线教育课件图等标准图片处理的需求。 您可以根据不同场景需求使用不同压缩功能，平衡压缩收益与视觉体验。 |
| 素材网站 | 多种样式图片处理满足多终端图片显示场景，图片编辑更加高效便捷。 针对需要使用高清大图的素材网站及平台，您可以使用图片自动瘦身进行视觉无损压缩，在不损失视觉观感的情况下最大化压缩比，提升图片加载速度。 |


## 功能优势

图片处理功能的优势如下：

- 

更快分发

原图在回源节点缓存后，直接在回源节点处理和分发多尺寸图片，减少回源链路，更快到达边缘。

- 

减轻源站压力

通过CDN处理图片，减少源站的存储和计算压力，降低维护成本，源站无感知。

- 

提升刷新预热效率

当原图失效后，处理后的目标图也会全部失效且无法访问，对图片进行处理可以减少图片的大小，降低刷新预热时回源的带宽，加速新图片的更新。

- 

边缘需求定制

通过图片处理参数控制，根据不同浏览器和客户端版本定制图片处理需求，满足不同业务能力。

## 使用限制

使用图片处理功能时有如下限制：

- 

原图限制

- 

图片格式只支持JPEG、JPG、PNG、WebP（静态，帧数等于1）、BMP、GIF（动态仅支持缩放和格式转换）、TIFF、JPEG 2000。

- 

原图大小不能超过10 MB。

- 

原图的宽×高不能超过16,777,216 px。

说明

若图片为GIF格式时，GIF图片的原图宽×高为所有帧相加之和，您可以使用ImageMagick等工具查看GIF图片的帧信息。

- 

如果原图为动态 WebP（帧数大于1），则不支持任何形式的图片处理操作。图片处理参数不会生效，CDN 将直接返回原图。

- 

处理后的图片限制

- 

图片的宽×高不能超过16,777,216 px。

- 

转WebP格式时，图片的宽×高不能超过16,777,216 px，且宽和高单边均不能超过16,384 px。

- 

缓存预热限制：图像转换功能不支持对缓存预热的内容生效，即CDN节点在缓存预热时只回源获取原始图片文件，不会做图像转换处理。

## 图片处理开通与操作方法

图片处理开通与操作方式，具体操作，请参见[图片处理操作方法](products/cdn/documents/user-guide/image-processing-operation-method.md)。

[上一篇：图像处理](products/cdn/documents/user-guide/image-editing.md)[下一篇：图片处理操作方法](products/cdn/documents/user-guide/image-processing-operation-method.md)

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
