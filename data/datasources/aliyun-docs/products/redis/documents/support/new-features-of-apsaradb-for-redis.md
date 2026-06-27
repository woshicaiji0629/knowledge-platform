# Redis 开源版、Tair（企业版）大版本新特性和兼容性。-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/support/new-features-of-apsaradb-for-redis

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

# 大版本新特性与兼容性

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

在云数据库 Tair（兼容 Redis）中，您可以创建不同版本的实例，本文介绍各版本的新特性与兼容性变更。

说明

每部分包括社区和阿里云提供的特性及兼容性变更，您也可以参考Tair团队与社区共建的[Redis](https://github.com/tair-opensource/resp-compatibility/blob/main/compatibility_report_zh_CN.md)[大版本兼容性报告](https://github.com/tair-opensource/resp-compatibility/blob/main/compatibility_report_zh_CN.md)。

## Tair（企业版）

### 新特性

- 

扩展数据结构：Tair（企业版）5.0及以上版本支持 Tair 扩展数据结构，提供更丰富的数据模型和企业级功能。详情请参见[Tair](products/redis/documents/developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md)[扩展数据结构概览](products/redis/documents/developer-reference/extended-data-structures-of-apsaradb-for-redis-enhanced-edition.md)。

### 兼容性变更

Tair 扩展数据结构在从 5.0 版本升级至 6.0 版本时存在少量行为变更，6.0 和 7.0 版本之间无兼容性变更。各大版本的原生命令支持情况参见[Tair（企业版）命令支持与限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-apsaradb-for-redis-enhanced-edition.md)。

- 

- 

- 

- 

| 扩展数据结构 | 版本差异（5.0 vs 6.0） | 影响说明 |
| --- | --- | --- |
| TairHash ( [exHash](products/redis/documents/developer-reference/the-tairhash-command.md) ) | 在 EXHSCAN 命令中使用 pattern 参数时： • 5.0 版本 ：仅对匹配 pattern 的 field 进行过期检查。 • 6.0 版本 ：对所有扫描到的 field（无论是否匹配）均执行过期检查。 | 在存在大量过期 field 且扫描的 count 值较大时，6.0 版本的响应时间（RT）可能会上升。 |
| TairBloom ( [Bloom](products/redis/documents/developer-reference/tairbloom-command.md) ) | 底层使用的 Hash 算法更新。 | 可能会导致假阳率略微上升。 |
| TairTS ( [TS](products/redis/documents/developer-reference/the-tickets-command.md) ) | EXTS.S.ALTER ：在 6.0 版本中，传入部分无效属性（如 CHUNK_SIZE ）将被静默忽略，而在 5.0 版本中会报错。 EXTS.S.INFO ：在 6.0 版本中，返回值不再包含 maxDataPoints 字段。 EXTS.S.RANGE / EXTS.P.RANGE ：在 6.0 版本中，传入不支持的 withLabels 参数将被忽略，而在 5.0 版本中会报错。 查询 ：6.0 版本查询时 bucket 可以小于 1 秒，5.0 版本不可以。 | • 检查业务代码是否依赖 EXTS.S.ALTER 和 EXTS.S.RANGE 等命令的报错逻辑。 • 调整依赖 EXTS.S.INFO 返回值中 maxDataPoints 字段的客户端代码。 |


## Redis开源版7.0

### 新特性

- 

关于Redis7.0的新特性请参见[7.0 release note](https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES)。

- 

例如对于使用Background线程的module命令，慢日志功能会记录整个挂起的时间；对于普通的Block类命令（例如BLPOP），慢日志功能只会记录执行时间，不记录挂起时间。

### 兼容性

- 

关于社区演进的Breaking change请参见[7.0 release note](https://raw.githubusercontent.com/redis/redis/7.0/00-RELEASENOTES)。

- 

例如不再支持STRALGO命令，替换为LCS命令。

- 

不再支持Lua脚本中的allow-oom flag，更多信息请参见[redis/redis#10699](https://github.com/redis/redis/pull/10699)。

- 

关于其他命令的支持变化，请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。

## Redis开源版6.0

### 新特性

- 

关于Redis6.0的新特性请参见[6.0 release note](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES)。

- 

在集群架构直连模式中，PUBLISH命令会在集群中广播。

### 兼容性

- 

关于社区演进的Breaking change请参见[6.0 release note](https://raw.githubusercontent.com/redis/redis/6.0/00-RELEASENOTES)。

- 

账号管理与社区ACL账号权限存在部分差异，如下为云数据库 Tair（兼容 Redis）的账号管理说明：

- 

默认账号为default，实例名账号（例如r-bp1857n194kiuv****）为另外一个单独账号。

- 

通过AUTH命令连接Redis时，若未指定账号则使用default账号鉴权。

- 

关于其他命令的支持变化，请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。

## Redis开源版5.0

### 新特性

- 

关于Redis5.0的新特性请参见[5.0 release note](https://raw.githubusercontent.com/redis/redis/5.0/00-RELEASENOTES)。

- 

支持[时延洞察](products/redis/documents/user-guide/latency-insights.md)。

- 

支持[实时大](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)[Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)[统计](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)。

- 

支持[TLS](products/redis/documents/user-guide/enable-tls-encryption.md)[加密](products/redis/documents/user-guide/enable-tls-encryption.md)。

- 

优化了Blocking连接的唤醒时间精度。

- 

集群架构直连模式支持无感扩缩容。

### 兼容性

- 

关于社区演进的Breaking change，请参见[5.0 release note](https://raw.githubusercontent.com/redis/redis/5.0/00-RELEASENOTES)。

- 

例如Lua脚本执行的命令不再对结果进行排序。

- 

账号名称的大小写敏感。

- 

开通VPC免密后，免密连接可通过AUTH切换不同账号。

说明

若您的不同账号设置了不同权限，请确保应用程序在权限范围内执行命令，否则会出现权限不足的报错。

- 

开放READONLY和READWRITE命令。

- 

云原生版与经典版存在部分差异：云原生版实例开通VPC免密后，所有连接仍需进行白名单验证，且无法设置#no_loose_check-whitelist-always参数。

- 

关于其他命令的支持变化，请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。

## Redis开源版4.0（已停售）

展开查看详情

新特性

- 

关于Redis4.0的新特性请参见[4.0 release note](https://raw.githubusercontent.com/redis/redis/4.0/00-RELEASENOTES)。

- 

支持[审计日志](products/redis/documents/user-guide/enable-the-new-audit-log-feature.md)。

- 

支持[实时热](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)[Key](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)[统计](products/redis/documents/user-guide/use-the-real-time-key-statistics-feature.md)。

- 

开通VPC免密后，可通过设置#no_loose_check-whitelist-always参数，选择是否对同一VPC的网络连接进行白名单验证，更多信息请参见[参数支持](products/redis/documents/user-guide/supported-parameters.md)。

- 

支持[Sentinel](products/redis/documents/user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[兼容模式](products/redis/documents/user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)，需开通VPC免密，仅支持SENTINEL和get-master-addr-by-name两个子命令。

- 

支持创建多个账号（账号名称大小写不敏感），并可以对账号设置读写、只读权限，您可以通过AUTH user:password切换账号。

- 

默认账号为实例名（例如r-bp1857n194kiuv****）。

- 

若未指定账号或者账号不存在，则自动转为默认账号鉴权（实例名）。

- 

若开通VPC免密，免密连接无需鉴权，将使用默认账号，且无法切换账号。

- 

集群架构支持开通[直连模式地址](products/redis/documents/user-guide/enable-the-direct-connection-mode.md)。

- 

集群架构支持通过设置ptod_enabled参数，将客户端IP透传给DB节点，更多信息请参见[参数支持](products/redis/documents/user-guide/supported-parameters.md)。

兼容性

- 

关于社区演进的Breaking change请参见[4.0 release note](https://raw.githubusercontent.com/redis/redis/4.0/00-RELEASENOTES)。

- 

例如集群架构下需要记录Slot-to-Key的映射关系，所以相同数据的内存占用会比标准架构多。

- 

例如集群架构下SORT命令不支持BY和GET参数。

- 

不再支持[SSL](products/redis/documents/user-guide/configure-ssl-encryption.md)[加密](products/redis/documents/user-guide/configure-ssl-encryption.md)。

- 

集群架构直连模式不支持部分CLUSTER命令，更多信息请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。

- 

集群架构直连模式支持SELECT命令。

说明

您无法再使用SELECT命令来判断当前连接是否为Cluster mode，否则会导致误判。

- 

在集群架构直连模式中，PUBLISH命令不会广播至其他节点。

- 

关于其他命令的支持变化，请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。

## Redis开源版2.8（已停售）

展开查看详情

新特性

- 

关于Redis2.8的新特性请参见[2.8 release note](https://raw.githubusercontent.com/redis/redis/2.8/00-RELEASENOTES)。

- 

支持[设置白名单](products/redis/documents/getting-started/step-2-configure-whitelists.md)。

- 

支持[VPC](products/redis/documents/user-guide/enable-password-free-access.md)[免密](products/redis/documents/user-guide/enable-password-free-access.md)，开启该功能后：

- 

来自该VPC内的网络连接无需进行IP白名单验证。

- 

来自该VPC内的网络连接执行AUTH命令时，直接返回OK，无需进行密码验证。

- 

支持[SSL](products/redis/documents/user-guide/configure-ssl-encryption.md)[加密](products/redis/documents/user-guide/configure-ssl-encryption.md)。

- 

支持设置[禁用命令](products/redis/documents/user-guide/disable-high-risk-commands.md)。

- 

支持代理模式（Proxy）的集群架构。

兼容性

- 

关于社区演进的Breaking change请参见[2.8 release note](https://raw.githubusercontent.com/redis/redis/2.8/00-RELEASENOTES)。

- 

不支持部分调试类命令和管理类命令，更多信息请参见[Redis](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](products/redis/documents/developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)。

- 

提供有限的CONFIG SET/GET命令支持：

- 

CONFIG GET：仅返回部分配置项，不返回安全相关的配置项。

- 

CONFIG SET：仅返回OK，不会修改参数。

- 

提供有限的INFO命令支持，例如不返回Persistence、Replication等安全相关信息。

- 

集群架构代理模式不支持部分命令，更多信息请参见[集群架构与读写分离实例的命令限制](products/redis/documents/developer-reference/limits-on-commands-supported-by-cluster-and-read-write-splitting-instances.md)。

[上一篇：版本说明](products/redis/documents/support/version-description.md)[下一篇：Tair小版本发布日志](products/redis/documents/support/apsaradb-for-redis-enhanced-edition-1.md)

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
