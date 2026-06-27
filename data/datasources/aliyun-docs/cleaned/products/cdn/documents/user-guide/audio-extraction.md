# 如何开启音视频分离-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/audio-extraction

# 配置听视频
开启听视频功能后，CDN节点会将视频文件中的音频分离，并返回给客户端，实现听视频的同时降低带宽的使用，有效节省流量。通过本文您可以了解开启音视频分离的操作方法。
## 背景信息
当客户端请求访问视频文件时，向服务器端发送URL请求，例如：http://www.aliyun.com/test.flv?ali_audio_only=1，CDN服务器端仅向客户端发送纯音频数据。客户端必须支持Transfer-Encoding:chunked传输方式。
说明
听视频功能不支持Range请求，但是播放视频时许多客户端都会发起Range请求（包括但不限于Safari、iOS设备上的浏览器），建议您使用自研的客户端对接该功能。
听视频过程中如果需要拖动进度条播放，需同时配置拖拽功能。进行拖拽时，会先读取原音视频文件的meta信息获取播放时长，将播放时长作为播放进度来实现播放进度的拖拽具体操作。更多信息，请参见[配置拖拽播放](video-seeking.md)。
目前听视频功能不支持 MP4 Box Header Size 等于 16 的场景（64 位），仅支持 MP4 Box Header Size 等于 8 的场景。关于 Header Size 的详细说明和查看方法，请参见下方 MP4 Box Header Size 说明。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击视频相关。
在听视频区域，打开听视频开关。
开启听视频功能后，需要配合请求参数ali_audio_only使用。支持的文件格式如下表所示。
| 文件格式 | meta 信息 | ali_audio_only 参数 | 举例 |
| --- | --- | --- | --- |
| MP4 | 源站视频的 meta 信息必须在文件头部，不支持 meta 信息在尾部的视频。 | ali_audio_only 参数表示该请求为音视频分离请求，服务端只返回 meta 信息和音频信息，视频信息会被过滤掉。如果不带该参数或参数值非 1，则该功能失效。 | 请求 http://domain/video.mp4?ali_audio_only=1 。 |
| FLV | 无要求。 | ali_audio_only 参数表示该请求为音视频分离请求，服务端只返回 meta 信息和音频信息，视频信息会被过滤掉。如果不带该参数或参数值非 1，则该功能失效。 | 请求 http://domain/video.flv?ali_audio_only=1 。 |
## MP4 Box Header Size 说明
如果 MP4 文件在使用听视频功能时无法正常提取音频，可能是文件的 mdat Box 使用了扩展 Header（16 字节），不符合当前听视频功能的要求。
说明
此限制主要针对 mdat Box（存储实际音视频数据的容器）。moov 等其他 Box 通常默认使用 8 字节 Header，不受此限制影响。
通过本节可以了解 Header Size 的概念，并检查文件是否兼容。
### 什么是 MP4 Box Header Size
MP4 文件由多个 Box（容器单元）组成，例如 moov box、mdat box 等。每个 Box 包含一个 Header，用于描述该 Box 的大小和类型。Header 有以下两种规格：
| 规格 | Header 大小 | 说明 |
| --- | --- | --- |
| 标准 Header | 8 字节（32 位） | 包含 size（4 字节）和 box type（4 字节）。size 字段直接存储 Box 的实际大小。适用于 Box 数据量可用 4 字节表示的场景。 |
| 扩展 Header | 16 字节（64 位） | 包含 size（4 字节，固定值为 1）、box type（4 字节）和 largesize（8 字节）。当 size 值为 1 时，表示启用 largesize 机制，真实大小存储在 largesize 字段中。常见于 mdat Box 数据量较大的场景。 |
### 查看 MP4 文件的 Box Header Size
可以使用以下工具查看 MP4 文件的 Box Header Size。
方式一：使用 MP4Box.js 在线工具（推荐）
打开[MP4Box.js ISOBMFF Box Structure Viewer](https://gpac.github.io/mp4box.js/test/filereader.html)。
上传 MP4 文件。
在左侧 Box View 的 Tree View 中，单击mdat (MediaDataBox)。
在右侧Box Property View中查看original_size字段，判断 Header Size：
original_size显示为 1：mdat Box Header Size 为 16 字节，不支持听视频功能。
original_size不显示或不为 1：mdat Box Header Size 为 8 字节，支持听视频功能。
以下为两种情况的属性对比：
| 属性字段 | Header Size = 8 字节（支持） | Header Size = 16 字节（不支持） |
| --- | --- | --- |
| size | 实际大小数值 | 实际大小数值 |
| box_name | MediaDataBox | MediaDataBox |
| start | 偏移字节数 | 偏移字节数 |
| original_size | 不显示 | 显示为 1 |
方式二：使用 Bento4 命令行工具
运行以下命令：
./mp4dump 文件名.mp4 | grep -E "\[mdat\]|\[moov\]"
根据输出结果判断：
[mdat] size=8+xxxxxx：Header Size 为 8 字节，支持听视频功能。
[mdat] size=16+xxxxxx：Header Size 为 16 字节，不支持听视频功能。
## 相关文档
相关API接口请见[批量配置域名](../developer-reference/api-cdn-2018-05-10-batchsetcdndomainconfig.md)。
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
