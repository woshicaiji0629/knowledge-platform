# exString数据结构命令详解-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/tairsting-command

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

# exString

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

TairString（exString）是一种带版本号的String类型数据结构，本文介绍TairString数据支持的命令。

## TairString简介

Redis的String仅由key和value组成，而TairString不仅包含key和value，还携带了版本（version），可用于乐观锁等场景。除此之外，TairString在Redis String加减功能的基础上支持了边界设置，可以将INCRBY、INCRBYFLOAT的结果限制在一定的范围内，超出范围则提示错误。

主要特性

- 

value携带版本号。

- 

使用INCRBY、INCRBYFLOAT递增数据时可设置变更范围。

该Module已开源，更多信息请参见[TairString](https://github.com/alibaba/TairString)。

## 最佳实践

- 

[基于](products/redis/documents/use-cases/implementation-of-high-performance-distributed-lock-based-on-tairstring.md)[TairString](products/redis/documents/use-cases/implementation-of-high-performance-distributed-lock-based-on-tairstring.md)[实现高性能分布式锁](products/redis/documents/use-cases/implementation-of-high-performance-distributed-lock-based-on-tairstring.md)

- 

[基于](products/redis/documents/use-cases/implementation-of-high-performance-optimistic-lock-based-on-tairstring.md)[TairString](products/redis/documents/use-cases/implementation-of-high-performance-optimistic-lock-based-on-tairstring.md)[实现高性能乐观锁](products/redis/documents/use-cases/implementation-of-high-performance-optimistic-lock-based-on-tairstring.md)

- 

[基于](products/redis/documents/use-cases/implementation-of-high-efficiency-current-limiter-based-on-tairstring.md)[TairString](products/redis/documents/use-cases/implementation-of-high-efficiency-current-limiter-based-on-tairstring.md)[实现高效限流器](products/redis/documents/use-cases/implementation-of-high-efficiency-current-limiter-based-on-tairstring.md)

## 前提条件

实例为Tair[内存型](products/redis/documents/product-overview/dram-based-instances.md)或[持久内存型](products/redis/documents/product-overview/persistent-memory-optimized-instances-1.md)（小版本为1.2.3及以上）。

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群实例或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

本文的操作对象为Tair实例中的TairString数据。

说明

Tair实例中可同时设置Redis String（即Redis原生String）和TairString，本文的命令无法对Redis String使用。

## 命令列表

表 1.TairString命令

| 命令 | 语法 | 简介 |
| --- | --- | --- |
| [EXSET](products/redis/documents/developer-reference/tairsting-command.md) | EXSET key value [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [KEEPTTL] | 若 key 不存在，则创建新的 key，并将 value 保存到 key 中；若 key 已存在，则覆盖原来 value 的值。 |
| [EXGET](products/redis/documents/developer-reference/tairsting-command.md) | EXGET key | 获取 TairString 的 value 和 version。 |
| [EXSETVER](products/redis/documents/developer-reference/tairsting-command.md) | EXSETVER key version | 设置目标 key 的 version。 |
| [EXINCRBY](products/redis/documents/developer-reference/tairsting-command.md) | EXINCRBY key num [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 对 TairString 的 value 进行自增自减操作，num 的范围为 long。 |
| [EXINCRBYFLOAT](products/redis/documents/developer-reference/tairsting-command.md) | EXINCRBYFLOAT key num [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 对 TairString 的 value 进行自增自减操作，num 的范围为 double。 |
| [EXCAS](products/redis/documents/developer-reference/tairsting-command.md) | EXCAS key newvalue version | 当目标 key 的 version 值与指定的 version 相等时，则更新 key 的 value 值；version 不相等，则返回旧的 value 和 version。 |
| [EXCAD](products/redis/documents/developer-reference/tairsting-command.md) | EXCAD key version | 当目标 key 的 version 值与指定的 version 相等时，则删除 Key。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairString 数据。 |


说明

本文的命令语法定义如下：

- 

大写关键字：命令关键字。

- 

斜体：变量。

- 

[options]：可选参数，不在括号中的参数为必选。

- 

A|B：该组参数互斥，请进行二选一或多选一。

- 

...：前面的内容可重复。

## EXSET

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

| 类别 | 说明 |
| --- | --- |
| 语法 | EXSET key value [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 若 key 不存在，则创建新的 key，并将 value 保存到 key 中；若 key 已存在，则覆盖原来 value 的值。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 value ：为 key 设置的 value。 EX ：指定 key 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 key 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 key 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 key 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 NX ：只在 key 不存在时写入。 XX ：只在 key 存在时写入。 VER ：版本号。 如果 key 存在，和当前版本号做比较： 如果相等，写入，且版本号加 1。 如果不相等，返回异常。 如果 key 不存在或者 key 当前版本为 0，忽略传入的版本号直接设置 value，成功后版本号变为 1。 ABS ：绝对版本号。设置后，无论 key 当前的版本号是多少，完成写入并将 key 的版本号覆盖为该选项中设置的值。 KEEPTTL ：延用该 key 原本设置的过期时间（Time to live，TTL 信息），该参数不能与 EX 、 PX 、 EXAT 、 PXAT 参数同时设置。 说明 若未设置 KEEPTTL 参数，也未设置 EX 、 PX 等设置过期时间的参数，则该 key 的过期时间将被删除，即表示该 key 不会过期。 |
| 返回值 | 执行成功：OK。 指定了 XX 且 key 不存在：nil。 指定了 NX 且 key 已经存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXSET foo bar EX 10 NX ABS 100 返回示例： OK |


## EXGET

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXGET key |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 TairString 的 value 和 version。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 |
| 返回值 | 执行成功：value 与 version。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXGET foo 返回示例： 1) "bar" 2) (integer) 1 |


## EXSETVER

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXSETVER key version |
| 时间复杂度 | O(1) |
| 命令描述 | 设置目标 key 的 version。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 version ：需要设置的版本号。 |
| 返回值 | 执行成功：1。 若 key 不存在：0。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXSETVER foo 2 返回示例： (integer) 1 |


## EXINCRBY

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

| 类别 | 说明 |
| --- | --- |
| 语法 | EXINCRBY key num [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [MIN minval] [MAX maxval] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 对 TairString 的 value 进行自增自减操作，num 的范围为 long。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 num ：TairString 进行自增自减操作的数值，必须为整数。 EX ：指定 key 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 key 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 key 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 key 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 NX ：只在 key 不存在时写入。 XX ：只在 key 存在时写入。 VER ：版本号。 如果 key 存在，和当前版本号做比较： 如果相等，进行自增，且版本号加 1。 如果不相等，返回异常。 如果 key 不存在或者 key 当前版本为 0，忽略传入的版本号并进行自增操作，成功后版本号变为 1。 ABS ：绝对版本号。设置后，无论 key 当前的版本号是多少，完成写入并将 key 的版本号覆盖为该选项中设置的值。 MIN ：设置 TairString value 的最小值。 MAX ：设置 TairString value 的最大值。 KEEPTTL ：延用该 key 原本设置的过期时间，该参数不能与 EX 、 PX 、 EXAT 、 PXAT 参数同时设置。 说明 若未设置 KEEPTTL 参数，也未设置 EX 、 PX 等设置过期时间的参数，则该 key 的过期时间将被删除，即表示该 key 不会过期。 |
| 返回值 | 执行成功：操作后 value 的值。 若设置了 MAX 或 MIN，而操作后的 value 超过了该范围：(error) ERR increment or decrement would overflow。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXSET foo 1 命令。 命令示例： EXINCRBY foo 100 MAX 300 返回示例： (integer) 101 |


## EXINCRBYFLOAT

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

| 类别 | 说明 |
| --- | --- |
| 语法 | EXINCRBYFLOAT key num [EX|PX|EXAT|PXAT time] [NX|XX] [VER|ABS version] [MIN minval] [MAX maxval] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 对 TairString 的 value 进行自增自减操作，num 的范围为 double。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 num ：TairString 进行自增自减操作的数值，类型为浮点数。 EX ：指定 key 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 key 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 key 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 key 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 NX ：只在 key 不存在时写入。 XX ：只在 key 存在时写入。 VER ：版本号。 如果 key 存在，和当前版本号做比较： 如果相等，进行自增，且版本号加 1。 如果不相等，返回异常。 如果 key 不存在或者 key 当前版本为 0，忽略传入的版本号并进行自增操作，成功后版本号变为 1。 ABS ：绝对版本号。设置后，无论 key 当前的版本号是多少，完成写入并将 key 的版本号覆盖为该选项中设置的值。 MIN ：设置 TairString value 的最小值。 MAX ：设置 TairString value 的最大值。 KEEPTTL ：延用该 key 原本设置的过期时间，该参数不能与 EX 、 PX 、 EXAT 、 PXAT 参数同时设置。 说明 若未设置 KEEPTTL 参数，也未设置 EX 、 PX 等设置过期时间的参数，则该 key 的过期时间将被删除，即表示该 key 不会过期。 |
| 返回值 | 执行成功：操作后 value 的值。 若设置了 MAX 或 MIN，而操作后的 value 超过了该范围：(error) ERR increment or decrement would overflow。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXSET foo 1 命令。 命令示例： EXINCRBYFLOAT foo 10.123 返回示例： (integer) 11.123 |


## EXCAS

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXCAS key newvalue version |
| 时间复杂度 | O(1) |
| 命令描述 | 当目标 key 的 version 值与指定的 version 相等时，则更新 key 的 value 值；version 不相等，则返回旧的 value 和 version。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 newvalue ：若 key 的 version 值与指定的 version 相等，将 value 修改为 newvalue。 version ：用于跟 key 的现有 version 值比较的值。 |
| 返回值 | 执行成功：["OK", "",最新的 version]。中间的""为无意义的空字符串。 执行失败：["ERR update version is stale", value, version]。value 和 version 为 key 当前的 value 和版本。 若 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXSET foo bar 命令。 命令示例： EXCAS foo bzz 1 返回示例： 1) OK 2) 3) (integer) 2 |


## EXCAD

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXCAD key version |
| 时间复杂度 | O(1) |
| 命令描述 | 当目标 key 的 version 值与指定的 version 相等时，则删除 Key。 |
| 选项 | Key ：TairString 的 key，用于指定作为命令调用对象的 TairString。 version ：用于跟 key 的现有 version 值比较的值。 |
| 返回值 | 执行成功：1。 执行失败：0。 若 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXSET foo bar 命令。 命令示例： EXCAD foo 1 返回示例： (integer) 1 |


[上一篇：Redis String命令增强](products/redis/documents/developer-reference/cas-cad-command.md)[下一篇：exHash](products/redis/documents/developer-reference/the-tairhash-command.md)

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
