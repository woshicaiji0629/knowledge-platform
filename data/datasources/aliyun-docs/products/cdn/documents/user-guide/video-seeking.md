# 拖拽播放介绍-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/video-seeking

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

# 配置拖拽播放

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

拖拽播放功能指在视音频点播中，拖拽播放进度时客户端向服务器发送URL请求。接下来为您介绍在CDN中如何开启拖拽播放功能。

说明

开启拖拽播放功能后，首字节延迟约增加30ms。即对首帧加载延迟平均30ms，但一般不易感知。

## 功能介绍

开启拖拽播放后，用户调整播放位置时都会向服务器端发送一个请求。CDN会识别该请求最近的前一个关键帧，以加载用户希望播放的视频片段，从而实现无缝切换的播放体验。

## 前提条件

- 

源站服务器支持HTTP Range请求。

- 

关闭[忽略参数](products/cdn/documents/user-guide/ignore-parameters.md)功能。

## 文件格式说明

例如：FLV文件的URL请求为www.aliyun.com/test.flv?start=10，服务端会响应从第10字节前一个关键帧的数据。 拖拽播放功能支持的文件和URL格式如下表所示。

- 

- 

- 

- 

| 文件格式 | Meta 信息 | Start 参数 | 举例 |
| --- | --- | --- | --- |
| MP4 | 源站视频的 meta 信息必须在文件头部，不支持 meta 信息在尾部的视频。 | start 参数表示时间（秒），最多支持三位小数。例如 start=1.01，表示 1.01 秒开始播放。 start 不是关键帧， CDN 会自动定位到前一个关键帧。 start 是关键帧， CDN 会自动定位到当前关键帧。 | URL 请求为 domain/video.mp4?start=10 ，表示从第 10 秒开始播放视频。 |
| FLV | 源站视频必须带有 meta 信息。 | start 参数表示字节，不支持小数，虽然参数可以写小数，但是拖拽模块会向下取整把小数转为正整数。如果开启 FLV 按时间拖拽 ，则开始和结束参数的单位为秒。 说明 按字节寻址适合用于精确的数据处理或处理原始视频数据，而按秒寻址则通过直接跳转到请求的精确秒数提供用户友好的体验。 start 不是关键帧， CDN 会自动定位到前一个关键帧。 start 是关键帧， CDN 会自动定位到当前关键帧。 | URL 请求为 domain/video.flv?start=10 ，表示从第 10 字节的前一个关键帧开始播放视频。 |


## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击视频相关。

- 

在拖拽播放区域，打开拖拽播放开关。

- 

（可选）开启FLV按时间拖拽和修改自定义参数。

## 拖拽参数处理说明

以时间拖拽为例，拖拽参数为默认的start和end参数，参数取值在不同场景下处理逻辑说明如下：

### MP4文件请求

| start/end 取值 | 示例 | 拖拽处理逻辑 |
| --- | --- | --- |
| 无效 start ，无效 end | start=foo&end=bar | 忽略拖拽参数，响应完整视频。 |
| 有效 start ，无效 end | start=10 | 拖拽处理 10 文件时长。 |
| 无效 start ，有效 end | end=10 | 拖拽处理 0-10 。 |
| 有效 start ，有效 end | start=0&end=10 | 拖拽处理 0-10 。 |
| start 和 end 同时为 0 | start=0&end=0 | 忽略拖拽参数，响应完整视频。 |
| start 大于 end | start=10&end=0 | 拖拽处理 10 文件时长。 |
| start 等于 end | start=10&end=10 | 拖拽处理 10 文件时长。 |
| start 大于视频时长 | start 大于视频时长 | 返回 400 。 |


### FLV文件请求

| start/end 取值 | 示例 | 拖拽处理逻辑 |
| --- | --- | --- |
| 无效 start ，无效 end | start=foo&end=bar | 忽略拖拽参数，响应完整视频。 |
| 有效 start ，无效 end | start=10 | 拖拽处理 10 文件时长。 |
| 无效 start ，有效 end | end=10 | 拖拽处理 0-10 。 |
| 有效 start ，有效 end | start=0&end=10 | 拖拽处理 0-10 。 |
| start 和 end 同时为 0 | start=0&end=0 | 忽略拖拽参数，响应完整视频。 |
| start 大于 end | start=10&end=0 | 拖拽处理 10 文件长度。 |
| start 等于 end | start=10&end=10 | 拖拽处理 10 文件长度。 |
| start 大于视频时长 | start 大于视频时长 | 返回完整视频。 |


## 相关文档

[批量配置域名](products/cdn/documents/api-batchsetcdndomainconfig.md)来实现视频点播功能，更多信息请参考[域名配置功能函数](products/cdn/documents/developer-reference/parameters-for-configuring-features-for-domain-names.md)。

[上一篇：配置Range回源](products/cdn/documents/user-guide/object-chunking.md)[下一篇：配置听视频](products/cdn/documents/user-guide/audio-extraction.md)

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
