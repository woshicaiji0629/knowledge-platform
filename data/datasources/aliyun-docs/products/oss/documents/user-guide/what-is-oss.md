# 海量任意类型数据的存储访问-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/what-is-oss

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

# 什么是对象存储OSS

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

阿里云对象存储OSS（Object Storage Service）是一款海量、安全、低成本、高可靠的云存储服务，可提供99.9999999999%（12个9）的数据持久性，99.995%的数据可用性。多种存储类型供选择，全面优化存储成本。

OSS具有与平台无关的RESTful API接口，您可以在任何应用、任何时间、任何地点存储和访问任意类型的数据。

您可以使用阿里云提供的API、SDK包或者OSS迁移工具轻松地将海量数据移入或移出阿里云OSS。数据存储到阿里云OSS以后，您可以选择标准存储（Standard）作为移动应用、大型网站、图片分享或热点音视频的主要存储方式，也可以选择成本更低、存储期限更长的低频访问存储（Infrequent Access）、归档存储（Archive）、冷归档存储（Cold Archive）或者深度冷归档（Deep Cold Archive）作为不经常访问数据的存储方式。

OSS作为云上数据湖可提供高带宽的下载能力。在部分地域，可为单个阿里云账号提供高达100 Gbps的内外网总下载带宽，旨在满足AI和大规模数据分析的需求。关于各地域的带宽说明，请参见[OSS](products/oss/documents/user-guide/limits.md)[带宽](products/oss/documents/user-guide/limits.md)。

## 前置概念

阅读本文前，您可能需要了解如下概念：

- 

[什么是云存储？](https://www.aliyun.com/getting-started/what-is/what-is-cloud-storage)

- 

[什么是对象存储？](https://www.aliyun.com/getting-started/what-is/what-is-object-storage)

## 快速了解OSS

- 

短视频

观看以下视频，快速了解OSS。

- 

常见问题

查看[OSS](products/oss/documents/faq-15.md)[常见问题](products/oss/documents/faq-15.md)，了解其他用户经常咨询和关注的一些问题。

## OSS工作原理

数据以对象（Object）的形式存储在OSS的存储空间（Bucket ）中。如果要使用OSS存储数据，您需要先创建Bucket，并指定Bucket的地域、访问权限、存储类型等属性。创建Bucket后，您可以将数据以Object的形式上传到Bucket，并指定Object的文件名（Key）作为其唯一标识。

OSS以HTTP RESTful API的形式对外提供服务，访问不同地域需要不同的访问域名（Endpoint）。当您请求访问OSS时，OSS通过使用访问密钥（AccessKey ID和AccessKey Secret）对称加密的方法来验证某个请求的发送者身份。

Object操作在OSS上具有原子性和强一致性。

- 

存储空间

存储空间是用户用于存储对象（Object）的容器，所有的对象都必须隶属于某个存储空间。存储空间具有各种配置属性，包括地域、访问权限、存储类型等。用户可以根据实际需求，创建不同类型的存储空间来存储不同的数据。

- 

对象

对象是OSS存储数据的基本单元，也被称为OSS的文件。和传统的文件系统不同，对象没有文件目录层级结构的关系。对象由元数据（Object Meta）、用户数据（Data）和文件名（Key）组成，并且由存储空间内部唯一的Key来标识。对象元数据是一组键值对，表示了对象的一些属性，例如文件类型、编码方式等信息，同时用户也可以在元数据中存储一些自定义的信息。

- 

对象名称

在各语言SDK中，ObjectKey、Key以及ObjectName是同一概念，均表示对Object执行相关操作时需要填写的Object名称。例如向某一存储空间上传Object时，ObjectKey表示上传的Object所在存储空间的完整名称，即包含文件后缀在内的完整路径，如填写为abc/efg/123.jpg。

- 

地域

Region表示OSS的数据中心所在物理位置。用户可以根据费用、请求来源等选择合适的地域创建Bucket。一般来说，距离用户更近的Region访问速度更快。更多信息，请参见[OSS](products/oss/documents/user-guide/regions-and-endpoints.md)[已经开通的](products/oss/documents/user-guide/regions-and-endpoints.md)[Region](products/oss/documents/user-guide/regions-and-endpoints.md)。

- 

访问域名

Endpoint表示OSS对外服务的访问域名。OSS以HTTP RESTful API的形式对外提供服务，当访问不同的Region的时候，需要不同的域名。通过内网和外网访问同一个Region所需要的Endpoint也是不同的。例如杭州Region的外网Endpoint是oss-cn-hangzhou.aliyuncs.com，内网Endpoint是oss-cn-hangzhou-internal.aliyuncs.com。具体的内容请参见[各个](products/oss/documents/user-guide/regions-and-endpoints.md)[Region](products/oss/documents/user-guide/regions-and-endpoints.md)[对应的](products/oss/documents/user-guide/regions-and-endpoints.md)[Endpoint](products/oss/documents/user-guide/regions-and-endpoints.md)。

- 

访问密钥

AccessKey简称AK，指的是访问身份验证中用到的AccessKey ID和AccessKey Secret。OSS通过使用AccessKey ID和AccessKey Secret对称加密的方法来验证某个请求的发送者身份。AccessKey ID用于标识用户；AccessKey Secret是用户用于加密签名字符串和OSS用来验证签名字符串的密钥，必须保密。对于OSS来说，AccessKey的来源有：

- 

Bucket的拥有者申请的AccessKey。

- 

被Bucket的拥有者通过RAM授权给第三方请求者的AccessKey。

- 

被Bucket的拥有者通过STS授权给第三方请求者的AccessKey。

更多AccessKey介绍请参见[创建](https://help.aliyun.com/zh/document_detail/53045.html#task968)[AccessKey](https://help.aliyun.com/zh/document_detail/53045.html#task968)。

- 

原子性和强一致性

Object操作在OSS上具有原子性，操作要么成功要么失败，不存在中间状态的Object。当Object上传完成时，OSS即可保证读到的Object是完整的，OSS不会返回给用户一个部分上传成功的Object。

Object操作在OSS同样具有强一致性，当用户收到了上传（PUT）成功的响应时，该上传的Object进入立即可读状态，并且Object的冗余数据已经写入成功。不存在上传的中间状态，即执行read-after-write，却无法读取到数据。对于删除操作，用户删除指定的Object成功之后，该Object立即不存在。

关于OSS基本概念的完整介绍，请参见[基本概念](products/oss/documents/terms-2.md)。

## OSS重要特性

- 

版本控制

版本控制是针对存储空间（Bucket）级别的数据保护功能。开启版本控制后，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。您在错误覆盖或者删除文件（Object）后，能够将Bucket中存储的Object恢复到任意时刻的历史版本。更多信息，请参见[版本控制概述](products/oss/documents/user-guide/overview-78.md)。

- 

Bucket Policy

Bucket拥有者可通过Bucket Policy授权不同用户以何种权限访问指定的OSS资源。例如您需要进行跨账号或对匿名用户授权访问或管理整个Bucket或Bucket内的部分资源，或者需要对同账号下的不同RAM用户授予访问或管理Bucket资源的不同权限，例如只读、读写或完全控制的权限等。关于配置Bucket Policy的具体操作，请参见[通过](products/oss/documents/configure-bucket-policies-to-authorize-other-users-to-access-oss-resources.md)[Bucket Policy](products/oss/documents/configure-bucket-policies-to-authorize-other-users-to-access-oss-resources.md)[授权用户访问指定资源](products/oss/documents/configure-bucket-policies-to-authorize-other-users-to-access-oss-resources.md)。

- 

跨区域复制

跨区域复制（Cross-Region Replication）是跨不同OSS数据中心（地域）的Bucket自动、异步（近实时）复制Object，它会将Object的创建、更新和删除等操作从源存储空间复制到不同区域的目标存储空间。跨区域复制功能满足Bucket跨区域容灾或用户数据复制的需求。更多信息，请参见[跨区域复制概述](products/oss/documents/user-guide/cross-region-replication-overview.md)。

- 

数据加密

服务器端加密：上传文件时，OSS对收到的文件进行加密，再将得到的加密文件持久化保存；下载文件时，OSS自动将加密文件解密后返回给用户，并在返回的HTTP请求Header中，声明该文件进行了服务器端加密。更多信息，请参见[服务器端加密](products/oss/documents/user-guide/server-side-encryption-8.md)。

客户端加密：将文件上传到OSS之前在本地进行加密。更多信息，请参见[客户端加密](products/oss/documents/user-guide/client-side-encryption.md)。

- 

数据永久保存

除以下情况以外，OSS默认永久保存上传到Bucket的数据：

- 

通过OSS控制台、API、SDK、ossutil或者ossbrowser等工具手动删除数据。更多信息，请参见[删除文件](products/oss/documents/user-guide/delete-objects-18.md)。

- 

通过生命周期规则在指定时间内自动删除数据。更多信息，请参见[基于最后一次修改时间的生命周期规则](products/oss/documents/user-guide/lifecycle-rules-based-on-the-last-modified-time.md)。

- 

OSS停服后15天内未补足欠款。更多信息，请参见[欠费停服说明](products/oss/documents/overdue-payments.md)。

关于OSS功能特性的完整介绍，请参见[功能特性](products/oss/documents/functions-and-features.md)。

## OSS使用方式

OSS提供多种灵活的上传、下载和管理方式。

- 

通过控制台管理OSS

OSS提供了Web服务页面，您可以登录[OSS](https://oss.console.aliyun.com/overview)[控制台](https://oss.console.aliyun.com/overview)管理您的OSS资源。更多信息，请参见[OSS](products/oss/documents/overview-of-the-oss-console.md)[管理控制台概览](products/oss/documents/overview-of-the-oss-console.md)。

- 

通过API或SDK管理OSS

OSS提供RESTful API和各种语言的SDK开发包，方便您快速进行二次开发。更多信息，请参见[OSS API](products/oss/documents/developer-reference/list-of-operations-by-function.md)[参考](products/oss/documents/developer-reference/list-of-operations-by-function.md)和[OSS SDK](products/oss/documents/developer-reference/overview-21.md)[参考](products/oss/documents/developer-reference/overview-21.md)。

- 

通过工具管理OSS

OSS提供图形化管理工具ossbrowser、命令行管理工具ossutil、FTP管理工具ossftp等各种类型的管理工具。更多信息，请参见[OSS](products/oss/documents/developer-reference/oss-tools.md)[常用工具](products/oss/documents/developer-reference/oss-tools.md)。

- 

通过云存储网关管理OSS

OSS的存储空间内部是扁平的，没有文件系统的目录等概念，所有的对象都直接隶属于其对应的存储空间。如果您想要像使用本地文件夹和磁盘的方式来使用OSS存储服务，可以通过配置云存储网关来实现。更多信息，请参见[云存储网关产品详情页面](https://www.aliyun.com/product/hcs)。

## OSS计费

对象存储OSS支持以下计费方式。

- 

按量付费：所有计费项默认采用按量付费。按照各计费项的实际用量结算费用，先使用，后付费，适用于业务用量经常有变化的场景。更多信息，请参见[按量付费](products/oss/documents/pay-as-you-go-1.md)。

- 

资源包：针对部分常用计费项支持专用的资源包。预先购买针对不同的计费项推出的优惠资源包，在费用结算时，优先从资源包抵扣用量，先购买，后抵扣，适用于业务用量相对稳定的场景。更多信息，请参见[资源包概述](products/oss/documents/resource-plan.md)。

- 

预留空间：针对有地域属性Bucket产生的标准存储（本地冗余）容量费用以及ECS快照存储费用的预付费产品。预先购买预留空间，在费用结算时，优先从预留空间抵扣用量，先购买，后抵扣。更多信息，请参见[预留空间](products/oss/documents/reserved-capacity.md)。

- 

无地域属性预留空间：针对无地域属性Bucket产生的标准存储（本地冗余）容量费用的预付费产品。预先购买无地域属性的预留空间，在费用结算时，优先从无地域属性预留空间抵扣用量，先购买，后抵扣。更多信息，请参见[无地域属性预留空间](products/oss/documents/anywhere-reserved-capacity.md)。

- 

存储容量单位包SCU：针对存储费用支持SCU。SCU除了用于抵扣OSS的存储费用，还可用于抵扣多种云存储产品存储容量费用。更多信息，请参见[存储容量单位包](products/oss/documents/scu.md)[SCU](products/oss/documents/scu.md)。

说明

- 

相较于按量付费，资源包和SCU具有一定的优惠折扣。

- 

超出资源包、预留空间、无地域属性预留空间、存储容量单位包SCU抵扣额度的用量，计入按量付费，会产生后付费账单，请根据您的所需服务、业务体量，购买适合额度的资源包、预留空间、无地域属性预留空间、存储容量单位包SCU。

## 其他相关服务

将数据存储到OSS后，您可以使用阿里云提供的其他产品和服务对其进行相关操作。

以下是您会经常使用到的阿里云产品和服务：

- 

图片处理：对存储在OSS上的图片进行格式转换、缩放、裁剪、旋转、添加水印等各种操作。更多信息，请参见[快速使用](products/oss/documents/user-guide/img-implementation-modes.md)[OSS](products/oss/documents/user-guide/img-implementation-modes.md)[图片处理服务](products/oss/documents/user-guide/img-implementation-modes.md)。

- 

云服务器ECS：提供简单高效、处理能力可弹性伸缩的云端计算服务。更多信息，请参见[ECS](https://www.aliyun.com/product/ecs)[产品详情页面](https://www.aliyun.com/product/ecs)。

- 

内容分发网络CDN：将OSS资源缓存到各区域的边缘节点，利用边缘节点缓存的数据，提升同一个文件被边缘节点客户大量重复下载的体验。更多信息，请参见[CDN](https://www.aliyun.com/product/cdn)[产品详情页面](https://www.aliyun.com/product/cdn)。

- 

E-MapReduce：构建于ECS上的大数据处理的系统解决方案，基于开源的Apache Hadoop和Apache Spark，方便您分析和处理自己的数据。更多信息，请参见[E-MapReduce](https://www.aliyun.com/product/emapreduce)[产品详情页面](https://www.aliyun.com/product/emapreduce)。

- 

在线迁移服务：您可以使用在线迁移服务将第三方数据源，例如亚马逊AWS、谷歌云等数据轻松迁移到OSS。更多信息，请参见[在线迁移服务使用教程](https://help.aliyun.com/product/94157.html)。

- 

离线迁移服务：如果您有TB或PB级别的海量数据需要上传到OSS，但本地的网络带宽不够，扩容成本高，可以使用闪电立方离线数据迁移服务。更多信息，请参见[离线迁移（闪电立方）介绍](https://help.aliyun.com/zh/data-transport/product-overview/what-is-data-transport#topic574)。

- 

智能媒体管理IMM：场景化封装数据智能分析管理，为云上文档、图片、视频数据，提供一站式数据处理、分析、检索等管控体验。更多信息，请参见[智能媒体管理介绍](https://help.aliyun.com/zh/imm/product-overview/what-is-imm)。

## 其他阿里云存储服务

除了对象存储以外，阿里云还提供文件存储、块存储等类型的存储服务，满足您不同场景下的业务需求。更多信息，请参见[阿里云存储服务介绍](https://help.aliyun.com/zh/document_detail/207139.html#concept-1305535)和[阿里云存储产品文档](https://www.aliyun.com/help/docs/storage)。

关于阿里云存储服务的客户案例、解决方案等，请参见[阿里云存储产品家族](https://www.aliyun.com/storage/storage)。

[上一篇：开始使用](products/oss/documents/user-guide/product-introduction.md)[下一篇：功能特性](products/oss/documents/user-guide/product-function-node-oss.md)

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
