# 产品核心优势多维度解析-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/benefits

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

# 产品优势

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

对象存储OSS是阿里云提供的海量、安全、低成本、高持久性的云存储服务。本文将OSS与传统的自建存储进行对比，让您更好地了解OSS。

下表列举了与自建存储相比，OSS在易用性、持久性、数据安全等方面的优势。

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

- 

- 

- 

- 

- 

- 

- 

| 对比项 | 对象存储 OSS | 自建服务器存储 |
| --- | --- | --- |
| 易用性 | 提供标准的 RESTful API 接口、丰富的 SDK 包、客户端工具、控制台。您可以像使用文件一样方便地上传、下载、检索、管理用于 Web 网站或者移动应用的海量数据。 不限制存储空间大小。您可以根据所需存储量无限扩展存储空间，解决了传统硬件存储扩容问题。 支持流式写入和读取。适合视频等大文件的同步读写业务场景。 支持数据生命周期管理。您可以通过设置生命周期规则，将到期数据批量删除或者转储为更低成本的低频访问、归档存储、冷归档存储或者深度冷归档存储。 | 存储受硬盘容量限制，需人工扩容。 不支持流式写入和读取。 手动删除数据。 |
| 持久性 | OSS 作为阿里巴巴全集团数据存储的核心基础设施，多年支撑双 11 业务高峰，历经高可用与高可靠的严苛考验。OSS 的多重冗余架构设计，为数据持久存储提供可靠保障。同时，OSS 基于高可用架构设计，消除单点故障，确保数据业务的持续性。 服务可用性最高可达 99.995%。 数据设计持久性最高可达 99.9999999999%（12 个 9）。 规模自动扩展，不影响对外服务。 OSS 会通过计算网络流量包的校验和，验证数据包在客户端和服务端之间传输中是否出错，保证数据完整传输。 OSS 针对对象的操作具有强一致性。当对象上传或复制成功时，即可立即读取，且冗余写入多个设备。 采用数据冗余存储机制，将每个对象的不同冗余存储在同一个区域内多个设施的多个设备上，确保硬件失效时的数据持久性和可用性。 当数据存入 OSS 后，OSS 会检测和修复丢失的冗余，确保数据持久性和可用性。 OSS 会周期性地通过校验等方式验证数据的完整性，及时发现因硬件失效等原因造成的数据损坏。当检测到数据有部分损坏或丢失时，OSS 会利用冗余数据重建并修复损坏数据。 | 受限于硬件持久性，易出问题，当出现磁盘坏道时，容易出现不可逆转的数据丢失。 人工数据恢复困难、耗时、耗力。 |
| 数据安全 | 提供企业级多层次安全防护，包括服务端加密、客户端加密、防盗链、通过 Bucket Policy 限制 IP 黑白名单访问、细粒度权限管控、STS 和 URL 鉴权与授权机制、WORM 特性、日志审计等。 提供用户级别资源隔离机制和多集群同步机制，支持异地容灾机制。 支持基于 SSL 和 TLS 的 HTTPS 加密传输，有效防止数据在云端的潜在安全风险。 提供版本控制功能，防止文件被误删除或覆盖而造成数据丢失。 获得多项合规认证，包括 SEC、FINRA 等，满足企业数据安全与合规要求。 | 需要另外购买清洗和黑洞设备。 需要单独实现安全机制。 |
| 成本 | 带宽资源充足，上行流量免费。 无需运维人员与托管费用，0 成本运维。 | 存储受硬盘容量限制，需人工扩容。 单线或双线接入速度慢，有带宽限制，峰值时期需人工扩容。 需专人运维，成本高。 |
| 智能存储 | 提供多种数据处理能力，例如图片处理、视频截帧、文档预览、图片场景识别、SQL 查询等，并无缝对接 Hadoop 生态以及阿里云函数计算、EMR、DataLakeAnalytics、BatchCompute、MaxCompute、Data Disaster Recovery 等产品，满足企业数据分析与管理的需求。 | 需要额外采购，单独部署。 |
| 加速访问 | 互联网访问加速：提供传输加速服务，可优化互联网传输链路和协议栈，大幅减少数据远距离传输超时的比例，极大地提升用户上传和下载体验。更多信息，请参见 [传输加速](products/oss/documents/user-guide/transfer-acceleration.md) 。 内容加速分发：OSS 作为源站，搭配 CDN 进行内容分发，提升同一个文件被重复下载的体验。 | 不支持。 |


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
