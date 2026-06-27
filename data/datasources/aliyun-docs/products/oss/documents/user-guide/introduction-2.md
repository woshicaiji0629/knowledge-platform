# 对对象存储的音视频文件进行处理-音视频处理-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/introduction-2/

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

# 音视频处理概述

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

音视频处理是由智能媒体管理（IMM）提供的数据处理能力，支持多种视频格式转换。您可以将原始视频上传保存到对象存储（OSS）上，通过OSS的RESTful接口x-oss-async-process，您可以在任何时间、任何地点、任何互联网设备上发起视频转码等处理请求。另外您也可以通过OSS的x-oss-process接口，在源视频上传后立即播放。

## 使用场景

- 终端覆盖、网络适配

转换分辨率和码率，适应不同终端和网络环境播放。

- 高效编码、降低成本

在保证画质前提下，通过高效编码算法提质降码，减少卡顿并节省存储和流量费用。

- 智能生产、内容再造

利用视频AI和超分技术，实现低画质素材高清重生、截图、剪辑等内容再造。

- 实时转码、极速起播

利用边转边播技术，实现按需实时转码和极速起播，节省转码和存储费用，提升播放体验。

## 工作原理

离线转码：将视频文件上传到OSS存储空间，创建音视频处理任务，任务执行成功后，转码后的文件存储在OSS中。

边转边播：将视频文件上传到OSS存储空间，创建边转边播播放列表，立即播放，对视频实时按需转码并存储在OSS中。

## 处理参数

OSS支持直接使用一个或多个参数处理视频等音视频文件，也支持将多个参数封装在一个样式中批量处理视频等音视频文件。关于样式的更多信息，请参见[样式](products/oss/documents/user-guide/styles.md)。

当存在多个处理参数时，OSS将按照参数顺序对文件进行处理。处理参数说明如下表所示。

| 处理操作 | 参数 | 说明 |
| --- | --- | --- |
| [视频转码](products/oss/documents/user-guide/video-transcoding.md) | video/convert | 将 OSS 中的视频文件转换为需要的格式。 |
| [视频转动图](products/oss/documents/user-guide/convert-videos-to-animated-images.md) | video/animation | 将 OSS 中的视频文件转换为 GIF、Webp 等动图格式。 |
| [视频截雪碧图](products/oss/documents/user-guide/video-cut-sprite.md) | video/sprite | 将 OSS 中的视频文件截帧并拼成雪碧图转为需要的图片格式。 |
| [视频多帧截取](products/oss/documents/user-guide/video-frame-cutting.md) | video/snapshots | 将 OSS 中的视频文件截帧并转换为需要的图片格式。 |
| [视频拼接](products/oss/documents/user-guide/video-stitching.md) | video/concat | 将 OSS 中的多个视频拼接为一个视频并转换为需要的格式。 |
| [视频信息提取](products/oss/documents/user-guide/video-information-extraction.md) | video/info | 提取 OSS 中的视频文件的音视频格式信息和音视频流信息。 |
| [音频转码](products/oss/documents/user-guide/audio-transcoding.md) | audio/convert | 将 OSS 中的音频文件转换为需要的格式。 |
| [音频拼接](products/oss/documents/user-guide/audio-stitching.md) | audio/concat | 将 OSS 中的多个音频文件拼接为一个音频并转换为需要的格式。 |
| [音频信息提取](products/oss/documents/user-guide/audio-information-extraction.md) | audio/info | 提取 OSS 中的音频文件的音视频格式信息和音视频流信息。 |
| [生成边转边播播放列表](products/oss/documents/user-guide/generate-video-playlist.md) | hls/m3u8 | 将 OSS 中的视频文件生成可用于边转边播的播放列表。 |


## 操作方式

- 

您可以通过异步处理接口x-oss-async-process对视频文件进行处理。操作方式，请参见[异步处理](products/oss/documents/user-guide/asynchronous-processing.md)。

- 

您可以通过同步处理接口x-oss-process对视频文件进行处理。操作方式，请参见[同步处理](products/oss/documents/user-guide/synchronous-processing.md)。

- 

您可以通过批处理对存量视频文件进行处理。操作方式，请参见[批处理](products/oss/documents/user-guide/oss-batch-processing.md)。

- 

您可以通过触发器对增量视频文件进行处理。操作方式，请参见[触发器](products/oss/documents/user-guide/triggers.md)。

## 使用限制

音视频处理支持的格式如下表所示。

| 项目 | 音频格式 | 视频格式 |
| --- | --- | --- |
| 输入 | wav、 pcm、 tta、 flac、 au、 ape、 mp3、 wma、 ogg、 aac、 ra、 midi、 mpc、 mv、 aif、 aiff、 m4a、 mka、 mp2、 mpa、 wv、 ac3、 dts、 amr、 3gpp 等所有主流格式 | avi、 mpeg、 mpg、 dat、 divx、 xvid、 rm、 rmvb、 mov、 qt、 asf、 wmv、 vob、 3gp、 mp4、 flv、 avs、 mkv、 ts、 ogm、 nsv、 swf 等所有主流格式 |
| 离线转码输出 | mp3、aac、flac、oga、ac3、opus | mp4、mkv、mov、asf、avi、mxf、ts、flv |
| 边转边播输出 | ts | ts |


更多参数约束，请参见[CreateMediaConvertTask - 创建媒体转码任务](https://help.aliyun.com/zh/imm/developer-reference/api-imm-2020-09-30-createmediaconverttask)和[GenerateVideoPlaylist - 生成边转边播播放列表](https://help.aliyun.com/zh/imm/developer-reference/api-imm-2020-09-30-generatevideoplaylist)。

## 计费

音视频处理能力由智能媒体管理服务 (IMM) 进行计费，费用详情请参见[计费项](https://help.aliyun.com/zh/imm/product-overview/billable-items)。

[上一篇：管道](products/oss/documents/user-guide/pipeline.md)[下一篇：视频转码](products/oss/documents/user-guide/video-transcoding.md)

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
