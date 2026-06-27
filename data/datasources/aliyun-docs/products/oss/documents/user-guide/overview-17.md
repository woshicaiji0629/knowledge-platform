# 如何使用GetObject处理新版图片-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/overview-17/

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

# 图片处理

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

针对OSS内存储的图片文件（Object），您可以在GetObject请求中携带图片处理参数对图片文件进行处理。例如添加图片水印、转换格式等。

## 操作视频

观看以下视频了解如何快速处理图片：

## 处理参数

OSS支持直接使用一个或多个参数处理图片，也支持将多个参数封装在一个样式中批量处理图片。有关图片样式的详情，请参见[图片样式](products/oss/documents/user-guide/image-styles.md)。

当存在多个图片处理参数时，OSS将按照参数顺序对图片进行处理。处理参数说明如下：

| 图片处理 | 参数 | 说明 |
| --- | --- | --- |
| [图片缩放](products/oss/documents/user-guide/resize-images-4.md) | resize | 将图片缩放至指定大小。 |
| [图片水印](products/oss/documents/user-guide/add-watermarks.md) | watermark | 为图片添加图片或文字水印。 |
| [自定义裁剪](products/oss/documents/user-guide/custom-crop.md) | crop | 裁剪指定大小的矩形图片。 |
| [质量变换](products/oss/documents/user-guide/adjust-image-quality.md) | quality | 调整 JPG 和 WebP 格式图片的质量。 |
| [格式转换](products/oss/documents/user-guide/convert-image-formats-2.md) | format | 转换图片格式。 |
| [HEIF](products/oss/documents/user-guide/advanced-compression-of-heif-or-avif-images.md) [或](products/oss/documents/user-guide/advanced-compression-of-heif-or-avif-images.md) [AVIF](products/oss/documents/user-guide/advanced-compression-of-heif-or-avif-images.md) [图片高级压缩](products/oss/documents/user-guide/advanced-compression-of-heif-or-avif-images.md) | format | 将图片转换为 HEIF 或 AVIF 高压缩比格式。 |
| [获取信息](products/oss/documents/user-guide/query-the-exif-data-of-an-image-4.md) | info | 获取图片信息，包括基本信息、EXIF 信息。 |
| [自适应方向](products/oss/documents/user-guide/auto-rotate-4.md) | auto-orient | 将携带旋转参数的图片进行自适应旋转。 |
| [内切圆](products/oss/documents/user-guide/circle-crop.md) | circle | 以图片中心点为圆心，裁剪出指定大小的圆形图片。 |
| [索引切割](products/oss/documents/user-guide/indexed-slice.md) | indexcrop | 按指定 x 或 y 轴的大小切分图片，之后选取其中一张图片。 |
| [圆角矩形](products/oss/documents/user-guide/rounded-rectangle-4.md) | rounded-corners | 按指定圆角大小将图片裁剪成圆角矩形。 |
| [模糊效果](products/oss/documents/user-guide/blur.md) | blur | 对图片进行模糊处理。 |
| [旋转](products/oss/documents/user-guide/rotate.md) | rotate | 按指定角度以顺时针方向旋转图片。 |
| [设置图片显示方式](products/oss/documents/user-guide/gradual-display.md) | interlace | 将 JPG 格式的图片调整为渐进显示。 |
| [获取图片主色调](products/oss/documents/user-guide/query-the-average-tone.md) | average-hue | 获取图片主色调。 |
| [亮度](products/oss/documents/user-guide/brightness.md) | bright | 调整图片亮度。 |
| [锐化](products/oss/documents/user-guide/sharpen.md) | sharpen | 对图片进行锐化处理。 |
| [对比度](products/oss/documents/user-guide/contrast.md) | contrast | 调整图片对比度。 |


例如，对原图example.jpg添加图片缩放resize以及质量变换quality参数后，文件URL为https://oss-console-img-demo-cn-hangzhou.oss-cn-hangzhou.aliyuncs.com/example.jpg?x-oss-process=image/resize,w_300/quality,q_90。您可以通过配置不同的规则，实现CDN回源原图或者经图片处理参数后的图片。

- 

回源原图

通过CDN开启过滤参数后，文件URL请求中问号（?）之后的参数将全部去除，即直接命中原图example.jpg。

- 

回源处理后的图片

通过CDN开启保留回源参数后，文件URL请求中问号（?）之后的所有参数将全部保留，即直接命中经图片处理参数后的图片。

关于CDN回源规则的配置详情，请参见[忽略参数](products/cdn/documents/user-guide/ignore-parameters.md)。

## 操作方式

您可以通过文件URL、API、SDK对图片进行处理。操作方式，请参见[图片处理操作方式](products/oss/documents/user-guide/img-implementation-modes.md)。

## 使用限制

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 项目 | 说明 |
| --- | --- |
| 图片格式 | 原图只支持 JPG、PNG、BMP、GIF、WebP、TIFF 、HEIC 、AVIF。 动态图片（例如 GIF 格式图片）仅支持缩放、裁剪、旋转以及添加图片水印的操作，不支持其它图片处理操作。 如果需要对 WebP 格式的动态图片进行编解码，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。 |
| 图片大小 | 原图大小不能超过 20 MB。 |
| 原图尺寸 | 除图片旋转对应的原图高或者宽不能超过 4,096 px 外，其他图片操作对应的原图高或者宽不能超过 30,000 px，且总像素不能超过 2.5 亿 px。 动态图片（例如 GIF 图片）的总像素计算方式为 宽*高*图片帧数 ；非动态图片（例如 PNG 图片）的总像素计算方式为 宽*高 。 |
| 目标图尺寸 | WebP 格式宽高不能超过 16,383 px。 HEIC 格式宽高不能超过 4,096 px。 AVIF 格式宽不能超过 4,096 px，总像素数不能超过 9,437,184 px。 |
| 图片缩放 | 缩放后图片，宽或高不能超过 16,384 px，且总像素不能超过 16,777,216 px。 |
| 图片样式 | 每个存储空间下最多能创建 50 个样式。如您的业务有更多样式的需求，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请。 说明 您可以在一个样式（Style）中包含多个图片处理参数，快速实现复杂的图片处理操作。更多信息，请参见 [图片样式](products/oss/documents/user-guide/image-styles.md) 。 |
| 处理能力 | 每秒图片处理量（按原图大小计） 华东 1（杭州）、华东 2（上海）、华北 2（北京）、华北 3（张家口）、华南 1（深圳）：20 MB/s。 其他地域：2 MB/s。 每秒请求数 QPS（Query Per Second） 华东 1（杭州）、华东 2（上海）、华北 2（北京）、华北 3（张家口）、华南 1（深圳）：50。 其他地域：5。 说明 如有计算量较大场景（如编码 WebP/AVIF/HEIF 超过 1080p 分辨率大图或超过上述限制），需要联系 [技术支持](https://selfservice.console.aliyun.com/ticket/createIndex) 评估实际使用限制。 |


## 费用说明

使用图片处理服务时，会产生如下费用：

- 

图片处理费用

未超出免费额度时，不产生费用；超出免费额度后，按处理的原图实际大小计费。计费详情，请参见[数据处理费用](products/oss/documents/data-processing-fees.md)。

- 

请求费用

处理图片时会产生一次GetObject请求，按请求次数收费。计费详情，请参见[请求费用](products/oss/documents/api-operation-calling-fees.md)。

- 

流量费用

根据处理后的图片大小收取外网流出流量费用。计费详情，请参见[流量费用](products/oss/documents/traffic-fees.md)。

## 版本说明

图片处理服务目前提供新版和旧版两个版本的API接口，本文档介绍新版接口的使用，旧版接口的功能今后不再更新。有关新旧版本接口使用兼容性的详细说明，请参见[新旧版本图片处理服务及使用说明](products/oss/documents/user-guide/differences-between-the-old-and-new-versions-of-img.md)。

[上一篇：图片标签检测迁移到新版](products/oss/documents/user-guide/image-tag-detection-migrated-to-the-new-version.md)[下一篇：图片处理操作方式](products/oss/documents/user-guide/img-implementation-modes.md)

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
