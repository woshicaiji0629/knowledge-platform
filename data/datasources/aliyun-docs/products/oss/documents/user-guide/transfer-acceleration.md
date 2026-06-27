# 通过传输加速访问OSS-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/transfer-acceleration

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

# 通过传输加速访问OSS

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当需要远距离数据传输时，传输加速通过全球分布的云机房和智能路由解析，为上传、下载提供端到端的加速方案，优化跨地域访问延迟高、传输不稳定的问题，提升传输速度和用户体验。

## 工作原理

当用户通过传输加速域名访问Bucket时，系统将请求智能路由到离用户最近的阿里云接入点，再通过阿里云内部骨干网高速传输到目标Bucket所在地域，避免数据在公共互联网上长距离传输。

以北京用户访问成都Bucket为例：普通外网域名需经过多跳公共互联网路径；使用传输加速域名后，数据就近进入北京的阿里云接入点，再通过内部骨干网直达成都，减少公网传输距离，提升速度和稳定性。

说明

传输加速通过优化传输链路来提升速度和稳定性，但无法完全消除公共互联网和跨境网络波动的影响。实际加速效果受用户所在地区、运营商链路质量、网络拥塞状况等因素影响，跨境场景下尤为明显。

## 启用传输加速访问

### 步骤一：开启传输加速

- 

前往[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)，单击目标Bucket。

- 

在左侧菜单栏单击Bucket 配置>传输加速。

- 

单击开启传输加速右侧的开启图标，仔细阅读弹窗的开通提示，然后单击确定。

说明

传输加速开启后约需30分钟全网生效，请在生效后再进行验证测试。

开启传输加速后，原有的Bucket域名（如外网访问域名）保持正常使用，业务可根据用户地理位置和网络条件灵活选择最优访问方式。

### 步骤二：使用传输加速域名访问

开启传输加速后，需要将访问请求的Endpoint替换为传输加速域名（oss-accelerate.aliyuncs.com）才能获得加速效果。

说明

由于未备案域名无法解析到中国内地IP，如需将未备案的自定义域名通过CNAME实现传输加速访问，请将CNAME指向非中国内地加速域名（oss-accelerate-overseas.aliyuncs.com）。

## 公共读和公共读写Bucket

在浏览器中直接通过URL访问。如https://example-bucket.oss-accelerate.aliyuncs.com/example.jpg表示访问example-bucket中的文件example.jpg。

## 私有Bucket

访问私有读写权限的Bucket需要在文件URL中包含签名信息。以下操作演示如何通过控制台获取文件的签名URL，关于签名的详细信息和生成方式请参见[签名版本](products/oss/documents/developer-reference/add-signatures-to-urls.md)[4（推荐）](products/oss/documents/developer-reference/add-signatures-to-urls.md)。

- 

前往[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)，单击目标Bucket。

- 

单击需要访问的目标文件右侧操作列的详情。

- 

单击复制文件 URL，并将URL中的外网访问域名（如oss-cn-hangzhou.aliyuncs.com）替换为传输加速访问域名（oss-accelerate.aliyuncs.com）。

- 

在浏览器中访问修改后的URL。

重要

使用SDK、ossutil、ossbrowser等访问OSS时，Endpoint应配置为oss-accelerate.aliyuncs.com，不要包含Bucket名称。如果误将Endpoint配置为<BucketName>.oss-accelerate.aliyuncs.com，会导致域名解析失败。

## 测试加速效果

以下通过日本地域的ECS实例使用[ossutil](products/oss/documents/developer-reference/ossutil-overview.md)下载杭州地域文件的对比测试，验证传输加速的实际效果。

## 未开启加速

ossutil cp oss://example-bucket/ossutil-2.1.2-mac-arm64.zip ossutil-2.1.2-mac-arm64.zip -e oss-cn-hangzhou.aliyuncs.com

下载耗时如下：

Success: Total 1 object, size 9281195 B, Download done:(1 files, 9281195 B), avg 8.733 MiB/s 1.013983(s) elapsed

## 开启加速

ossutil cp oss://example-bucket/ossutil-2.1.2-mac-arm64.zip ossutil-2.1.2-mac-arm64.zip -e oss-accelerate.aliyuncs.com

下载耗时如下：

Success: Total 1 object, size 9281195 B, Download done:(1 files, 9281195 B), avg 20.155 MiB/s 0.440160(s) elapsed

## 应用于生产环境

最佳实践

- 

CDN结合传输加速：多层加速架构

支持同时配置[CDN](products/oss/documents/user-guide/cdn-acceleration.md)[加速](products/oss/documents/user-guide/cdn-acceleration.md)和传输加速。将CDN回源配置到传输加速域名，构建"CDN边缘缓存+OSS传输加速"的双重加速体系，CDN负责就近缓存响应用户请求，传输加速优化CDN回源链路，特别适合全球分发的静态资源场景，实现缓存命中和回源传输的全链路优化。

- 

大文件传输优化：分片传输与加速结合

对于GB、TB级大文件传输，结合使用传输加速与[分片上传](products/oss/documents/user-guide/multipart-upload.md)、[断点续传下载](products/oss/documents/user-guide/oss-resumable-download.md)形成完整的远距离大文件传输解决方案。传输加速优化网络链路质量，分片传输提高并发度和容错能力，两者协同显著降低传输超时风险并提升整体传输效率。

- 

成本优化：智能域名选择策略

针对不同用户群体和访问场景实施差异化域名策略。对于同地域或网络条件良好的用户，使用外网访问域名节约传输加速费用；对于跨地域、网络质量差的用户，使用传输加速域名提升体验。建议根据用户地理分布、业务重要性和成本预算制定域名选择策略。

容错策略

- 

域名降级机制

当传输加速域名出现访问问题时，应用程序应具备自动降级到外网访问域名的能力，确保业务连续性。传输加速服务与外网访问域名相互独立，一方故障不影响另一方正常使用，为业务提供双重保障。

## 配额与限制

| 限制项 | 说明 |
| --- | --- |
| 协议支持 | 传输加速域名仅支持 HTTP/HTTPS 协议的 API 接入，不支持 RTMP 等非 HTTP/HTTPS 协议。 |
| 生效时间 | 传输加速开启或关闭操作约需 30 分钟全网生效。 |
| 访问模式 | 传输加速域名仅支持携带 Bucket 名称的三级域名访问模式，无法用于列举 Bucket 等管理操作。管理操作请使用外网访问域名。 |
| 安全传输 | 传输加速后端可能选择使用 HTTPS 协议进行数据传输，客户端使用 HTTP 访问时，访问日志中可能显示为 HTTPS 协议。 |


## 计费说明

传输加速功能本身免费开启，仅在通过传输加速域名访问OSS时额外产生加速上传流量和加速下载流量，详见[传输加速费用](products/oss/documents/transfer-acceleration-fees.md)。

## 常见问题

### 通过加速域名访问时返回502或504错误怎么办？

此问题通常是OSS传输加速的自动路径切换机制导致的正常现象。为应对远距离传输中的网络波动和链路质量变化，该服务会动态选择最优传输路径，在路径切换瞬间可能导致少量请求中断并返回502/504错误。这种情况无法完全避免，建议在客户端代码中实现指数退避的重试逻辑来提升访问成功率。

### 开启传输加速后访问没有加速效果？

开启传输加速功能后，还需要将访问请求的Endpoint替换为传输加速域名（oss-accelerate.aliyuncs.com）才能获得加速效果。仅开启功能而不更换域名，仍通过普通外网域名访问。

### 开启传输加速后立即访问报错？

传输加速开启后约需30分钟全网生效。如果在开启后立即使用传输加速域名访问，可能会因为尚未生效而出现报错，请等待一段时间后重试。

### 使用传输加速域名后跨境访问仍然较慢？

传输加速通过优化传输链路来提升跨地域访问速度，但跨境场景下的实际效果受运营商跨境链路质量影响。当跨境链路出现拥塞或波动时，传输速度可能下降。建议：

- 

确认Endpoint配置正确，格式为oss-accelerate.aliyuncs.com，不包含Bucket名称。

- 

对于大文件，结合[分片上传](products/oss/documents/user-guide/multipart-upload.md)和[断点续传下载](products/oss/documents/user-guide/oss-resumable-download.md)提升传输可靠性。

- 

在应用层实现域名降级机制，当传输加速域名不稳定时自动切换到外网域名，保障业务连续性。

### 传输加速费用如何计算，是否与外网流量费用叠加？

传输加速费用与外网流出流量费用独立计算。

- 

使用传输加速域名访问时，会同时产生传输加速流量费用和外网流出流量费用。

- 

使用普通外网域名访问时，仅产生外网流出流量费用，不产生传输加速费用。

开启传输加速功能本身不收费，只有通过传输加速域名实际传输数据时才会产生费用。

[上一篇：通过CDN加速访问OSS](products/oss/documents/user-guide/cdn-acceleration.md)[下一篇：全球加速访问](products/oss/documents/user-guide/user-global-accelerated-access-to-oss.md)

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
