# 多样化应用场景全面解析-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/common-scenarios

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

# 应用场景

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

本文介绍对象存储OSS的主要应用场景。

## 图片和音视频等应用的海量存储

OSS可用于图片、音视频、日志等海量文件的存储。各种终端设备、Web网站程序、移动应用可以直接向OSS写入或读取数据。OSS支持流式写入和文件写入两种方式。

## 网页或者移动应用的静态和动态资源分离

利用海量互联网带宽，OSS可以实现海量数据的互联网并发下载。OSS提供原生的[传输加速](products/oss/documents/user-guide/transfer-acceleration.md)功能，支持上传加速、下载加速，提升跨国、跨洋数据上传、下载的体验。同时，OSS也可以结合CDN产品，提供静态内容存储、分发到边缘节点的解决方案，利用CDN边缘节点缓存的数据，提升同一个文件被同一地区客户大量重复并发下载的体验。更多信息，请参见[CDN](products/oss/documents/user-guide/cdn-acceleration.md)[访问加速](products/oss/documents/user-guide/cdn-acceleration.md)[OSS](products/oss/documents/user-guide/cdn-acceleration.md)。

## 云端数据处理

上传文件到OSS后，可以配合智能媒体管理服务和图片处理服务进行云端的数据处理。更多信息，请参见[图片处理](products/oss/documents/user-guide/latest-version-of-img-guide.md)和[媒体处理](products/oss/documents/media-processing.md)。

## 配置审计归档

为了全面监管您的云上资源，您可以通过配置审计服务高效地收集和存储来自多种云服务资源（包括但不限于云服务器ECS、专有网络VPC、关系型数据库RDS等）的定时快照及配置变更历史，并将数据投递到OSS指定Bucket。当配置审计投递到轻量消息队列SMQ的单个文件大小超过64 KB，或是投递到日志服务SLS的单个文件大小超过1 MB的限制时，需要将超出大小限制的文件投递到OSS指定Bucket。这样可以避免数据丢失，还能充分利用OSS的海量存储能力及低成本优势来保存详细的审计信息。更多信息，请参见[投递](https://help.aliyun.com/zh/document_detail/307022.html)。

## 操作审计归档

您可以使用操作审计服务的跟踪功能，记录和审计用户对云资源进行的操作，并通过创建跟踪将事件投递到OSS指定Bucket，用于长期存储。满足安全监控与保障、合规审计、资源变更管理以及故障诊断与运维等场景。更多信息，请参见[创建单账号跟踪](https://help.aliyun.com/zh/actiontrail/user-guide/create-a-single-account-trail)。

## 计算结果持久化存储

- 

OSS结合BatchCompute

批量计算（BatchCompute）是专为大规模并行批处理任务设计的高性能云服务，它能够轻松管理并执行涉及数以万计任务的并发作业。您只需上传您的计算任务至BatchCompute，系统将智能地在阿里云的众多虚拟机实例上并行执行这些任务。处理完成后，将计算结果直接保存在OSS中。OSS作为云端的持久化存储解决方案，安全可靠地保管着海量的原始数据或中间计算结果，其高度可扩展性和即时访问特性确保了数据的随时可用性。

- 

OSS结合E-HPC等多个云产品

OSS作为云原生的分布式存储服务，为各类数据和应用程序提供坚实的数据支撑。考虑到弹性高性能计算（E-HPC）场景下对数据管理和存储的高要求，OSS在该场景下扮演着关键角色。E-HPC构建了按需扩展的高性能计算集群，包括计算节点与GPU节点，专为处理物理仿真、气候模型构建、基因组学研究及大规模机器学习训练等重度计算任务设计。这些任务在执行过程中会产生和消耗大量数据，此时，OSS以其分布式存储的优势，不仅存储原始数据和计算结果等非结构化信息，还支持作业数据的导入与执行文件，确保数据的高效存取与管理。

在此基础上，ECS实例作为计算资源的核心载体，不仅运行多样化应用服务，还为E-HPC集群的计算节点提供支持。通过Elastic IP（EIP），每个ECS实例被分配静态公网IP，确保了服务的稳定可达性。为了构建一个既安全又高效的运行环境，通过VPC创建私有网络，为包括ECS、E-HPC在内的实例划分出独立、安全的网络空间，加强了资源之间的隔离与保护。

此外，NAS的引入，进一步增强了集群的数据共享能力。NAS作为一个集中式的文件存储服务，使得所有计算节点能够无缝访问共享文件，促进团队间的数据协作与交换。

综上所述，OSS结合E-HPC等多个云产品，共同构建了一个高度灵活、高效且安全的云计算生态环境，满足了从数据存储、计算资源调度到网络构建、数据共享等全方位需求。

## 镜像保存和分发

无影云电脑是一种云端虚拟电脑服务，允许用户通过互联网远程访问和使用配置好的虚拟桌面环境。OSS作为一种高可用、高持久性的对象存储服务，能够安全可靠地存储您的无影云电脑镜像。将镜像上传到OSS，可以作为一种备份手段，防止因意外情况导致镜像丢失，确保业务连续性。同时，方便其他用户或团队成员共享镜像，并基于镜像快速部署新的无影云电脑实例，提高工作效率并保持环境一致性。

## 录屏审计归档

无影云电脑支持录屏审计功能，该功能可以帮助记录和监控应用程序或者用户在云桌面的使用情况，确保数据安全和合规性。配置录屏审计管控策略后，生成的录屏文件将自动传输到指定的OSS Bucket中，实现审计记录的即时备份与安全存储，同时便于后期查阅、分析及合规审核，提升了管理效率与数据安全性。

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
