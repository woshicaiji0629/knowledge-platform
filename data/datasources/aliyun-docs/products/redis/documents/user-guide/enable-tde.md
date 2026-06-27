# 开启透明数据加密TDE-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/user-guide/enable-tde

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/redis/documents/product-overview.md)

- [快速入门](products/redis/documents/getting-started.md)

- [Tair AI能力](products/redis/documents/tair-ai-ability.md)

- [操作指南](products/redis/documents/user-guide.md)

- [实践教程](products/redis/documents/use-cases.md)

- [安全合规](products/redis/documents/security-compliance.md)

- [开发参考](products/redis/documents/developer-reference.md)

- [服务支持](products/redis/documents/support.md)

- [视频专区](products/redis/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 开启透明数据加密TDE

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

云数据库 Tair（兼容 Redis）支持透明数据加密TDE（Transparent Data Encryption），可对RDB数据文件执行加密和解密。您可以通过控制台启用TDE功能，对RDB数据进行自动加密和解密，以满足提升数据安全性及合规需要。

## 前提条件

- 

实例存储介质为Tair（企业版）内存型。

- 

实例版本需在支持的版本范围内，升级方法请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。

- 

经典实例的小版本为1.7.1及以上。

- 

云原生实例大版本6.0及以上，小版本25.12.2.0及以上。

## 背景信息

云数据库 Tair（兼容 Redis）的TDE功能可以将RDB数据文件在写入磁盘之前进行加密，从磁盘读入内存时进行解密，具有不额外占用存储空间、无需更改客户端应用程序等优势。

图 1.TDE加密

## 影响

由于开启TDE功能后无法关闭，在开启前，需要评估对业务的影响，具体如下：

## 云原生实例

- 

支持转化为[全球多活](products/redis/documents/user-guide/overview-of-global-distributed-cache-for-tair.md)实例。

- 

支持通过[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)进行全量和增量数据同步。

- 

支持[迁移可用区](https://help.aliyun.com/zh/tair/user-guide/migrate-an-instance-across-zones#task-2224025)操作。

- 

暂不支持[离线全量](https://help.aliyun.com/zh/tair/user-guide/offline-key-analysis#concept-ufz-byl-jgb)[Key](https://help.aliyun.com/zh/tair/user-guide/offline-key-analysis#concept-ufz-byl-jgb)[分析](https://help.aliyun.com/zh/tair/user-guide/offline-key-analysis#concept-ufz-byl-jgb)操作。

- 

暂时不支持回收站恢复TDE实例。

## 经典实例

- 

暂不支持[迁移可用区](https://help.aliyun.com/zh/tair/user-guide/migrate-an-instance-across-zones#task-2224025)操作。

- 

暂不支持[离线全量](https://help.aliyun.com/zh/tair/user-guide/offline-key-analysis#concept-ufz-byl-jgb)[Key](https://help.aliyun.com/zh/tair/user-guide/offline-key-analysis#concept-ufz-byl-jgb)[分析](https://help.aliyun.com/zh/tair/user-guide/offline-key-analysis#concept-ufz-byl-jgb)操作。

- 

暂不支持将该实例[转换为全球分布式实例](https://help.aliyun.com/zh/tair/user-guide/create-a-distributed-instance#section-evg-7x6-t3b)。

- 

暂不支持通过[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)执行迁移或同步数据。

## 注意事项

- 

TDE的开启粒度为实例级别，不支持Key（键）或DB（库）粒度的控制。

- 

TDE加密对象为数据落盘文件（即RDB备份文件，如dump.rdb）。

- 

TDE所使用的密钥，由[密钥管理服务](products/kms/documents/key-management-service/support/what-is-key-management-service.md)[KMS](products/kms/documents/key-management-service/support/what-is-key-management-service.md)（Key Management Service）统一生成和管理，云数据库 Tair（兼容 Redis）不提供加密所需的密钥和证书。

- 

[实例回收站](products/redis/documents/user-guide/manage-instances-in-the-recycle-bin.md)不支持恢复已开启TDE的实例。

## 操作步骤

- 

访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。

- 

在左侧导航栏，单击TDE设置。

- 

打开TDE状态右侧的开关。

说明

如果小版本过低，该开关将处于不可单击状态，查看及升级小版本的方法，请参见[升级小版本与代理版本](products/redis/documents/user-guide/update-the-minor-version.md)。

- 

在弹出的对话框中，选择使用自动生成密钥或使用自定义密钥，然后单击确定。

说明

首次开启TDE时，需要您授权AliyunRdsInstanceEncryptionDefaultRole角色。

自定义密钥的创建方法，请参见[密钥管理服务](products/kms/documents/key-management-service/support/what-is-key-management-service.md)[KMS](products/kms/documents/key-management-service/support/what-is-key-management-service.md)。

设置完成后，实例状态改为TDE更变中，当实例状态转变为运行中表示操作完成。

## 相关API

| API 接口 | 说明 |
| --- | --- |
| [ModifyInstanceTDE](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-modifyinstancetde-redis.md) | 为实例开启透明数据加密 TDE 功能，支持自定义或自动生成密钥。 |
| [DescribeInstanceTDEStatus](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describeinstancetdestatus-redis.md) | 查询实例是否开启了 TDE 加密功能。 |
| [DescribeEncryptionKeyList](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describeencryptionkeylist-redis.md) | 查询实例的 TDE 加密功能可使用的自定义密钥列表。 |
| [DescribeEncryptionKey](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-describeencryptionkey-redis.md) | 查询实例的透明数据加密 TDE 自定义密钥的详情。 |
| [CheckCloudResourceAuthorized](products/redis/documents/developer-reference/api-r-kvstore-2015-01-01-checkcloudresourceauthorized-redis.md) | 查询实例是否已被授权使用 KMS 密钥服务。 |


## 常见问题

- 

Q：下载了加密后的RDB数据文件，如何进行解密？

A：目前无法解密，您可以将备份集恢复至新实例，恢复完成后，数据即完成自动解密。

- 

Q：为什么客户端读取到的数据还是明文显示的？

A：加密的对象是数据落盘文件（即RDB备份文件），而查询数据时读取的是内存数据（未被加密），所以是明文显示。

[上一篇：设置SSL加密](products/redis/documents/user-guide/configure-ssl-encryption.md)[下一篇：开启专有网络免密访问](products/redis/documents/user-guide/enable-password-free-access.md)

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
