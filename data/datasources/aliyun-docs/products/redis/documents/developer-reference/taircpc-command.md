# Cpc数据结构命令参考-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/taircpc-command

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

# Cpc

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

TairCpc是基于CPC（Compressed Probability Counting）压缩算法开发的数据结构，支持仅占用很小的内存空间对采样数据进行高性能计算。

## 背景信息

在大数据实时决策场景中，通常会将业务日志流入实时计算系统完成计算，然后将计算结果存储至在线存储系统，最终由实时规则或决策系统进行决策，例如：

- 

防控信用卡欺诈交易：快速判断刷卡环境是否可信，若发现异常则需第一时间拦截交易。

- 

防控黄牛团伙恶意牟利：实时识别并阻止通过虚拟设备、虚假地址等方式损害平台利益的行为。

您可以利用TairCpc将实时数据，按不同的去重维度，结构化地存储到Tair数据库中，即可在高速的访问场景中直接获得结果，实现存储、计算一体化。同时TairCpc提供多重聚合运算，可以在纳秒级聚合数据结果，具备实时风控的能力。

## TairCpc简介

[CPC](https://arxiv.org/abs/1708.06839)是一种高性能数据去重算法，可以将不同的值作为数据流进行计数，支持将多个数据块合并、去重，获得去重后的总计数。相比HLL（Hyperloglog）算法，在相同精度下，CPC大约可节省40％内存空间。

同时，TairCpc在开源CPC算法的基础上，将误差率优化至0.008%（开源CPC为0.67%；HLL误差率为1.95%）。

主要特征

- 

内存占用低，支持增量读写，实现IO最小化。

- 

高性能去重，同时拥有超高去重精度。

- 

误差率稳定收敛。

典型场景

- 

银行安全系统

- 

秒杀限购

- 

防控用户（或黄牛团伙）恶意牟利

## 前提条件

实例为Tair：

- 

[内存型](products/redis/documents/product-overview/dram-based-instances.md)。若实例为内存型（兼容Redis 5.0），则需要小版本为1.7.20及以上。

- 

[持久内存型](products/redis/documents/product-overview/persistent-memory-optimized-instances-1.md)（小版本为1.2.3.3及以上）

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群实例或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

操作对象为Tair实例中的TairCpc数据。

## 命令列表

表 1.TairCpc命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [CPC.UPDATE](products/redis/documents/developer-reference/taircpc-command.md) | CPC.UPDATE key item [EX|EXAT|PX|PXAT time ] | 在指定 TairCpc 中添加 item。若 TairCpc 不存在则自动新建，若待添加的 item 已存在于目标 TairCpc 中，则不会进行操作。 |
| [CPC.ESTIMATE](products/redis/documents/developer-reference/taircpc-command.md) | CPC.ESTIMATE ke y | 获取指定 TairCpc 去重后的基数估算值，返回值的数据类型为 double 类型，您可以仅取整数部分（忽略小数点后的数据）。 |
| [CPC.UPDATE2EST](products/redis/documents/developer-reference/taircpc-command.md) | CPC.UPDATE2EST key item [EX|EXAT|PX|PXAT time ] | 在指定 TairCpc 中添加 item，返回更新后的基数估算值。若 TairCpc 不存在则自动新建。 |
| [CPC.UPDATE2JUD](products/redis/documents/developer-reference/taircpc-command.md) | CPC.UPDATE2JUD key item [EX|EXAT|PX|PXAT time ] | 在指定 TairCpc 中添加 item，并返回更新后的基数估算值和其与更新前的差值。若返回的差值为 1 则表示写入成功且不存在重复；若为 0 则表示已存在当前 item。若 TairCpc 不存在则自动新建。 |
| [CPC.ARRAY.UPDATE](products/redis/documents/developer-reference/taircpc-command.md) | CPC.ARRAY.UPDATE key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item。若 TairCpc 不存在则自动新建， SIZE 为时间窗口个数， WIN 为时间窗口的长度（单位为毫秒）。随着流式数据的写入，TairCpc 会持续向前更新并保存 SIZE * WIN 时间范围内的数据，超过该时间范围的数据会被覆盖、删除。 SIZE 和 WIN 属性仅在新建 TairCpc 的时生效。 说明 例如目标 key 为计算近 10 分钟内每分钟的数据：可以设置 SIZE 为 10（10 个时间窗口）、 WIN 为 60000（每个时间窗口为 1 分钟）。当目标 key 中写入第 11 分钟的数据时，第 1 分钟的数据会逐渐被覆盖、删除。 |
| [CPC.ARRAY.ESTIMATE](products/redis/documents/developer-reference/taircpc-command.md) | CPC.ARRAY.ESTIMATE key timestamp | 获取指定 TairCpc 中目标 timestamp 所在时间窗口的基数估算值。 |
| [CPC.ARRAY.ESTIMATE.RANGE](products/redis/documents/developer-reference/taircpc-command.md) | CPC.ARRAY.ESTIMATE.RANGE key start_time end_time | 获取指定 TairCpc 的指定时间段内（包含指定时间点）各个时间窗口的基数估算值。 |
| [CPC.ARRAY.ESTIMATE.RANGE.MERGE](products/redis/documents/developer-reference/taircpc-command.md) | CPC.ARRAY.ESTIMATE.RANGE.MERGE key timestamp range | 获取指定 TairCpc 在指定时间点至往前 range（含当前窗口）个时间窗口内，时间窗口合并、去重后的基数估算值。 |
| [CPC.ARRAY.UPDATE2EST](products/redis/documents/developer-reference/taircpc-command.md) | CPC.ARRAY.UPDATE2EST key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item，并返回该时间窗口更新后的基数估算值。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](products/redis/documents/developer-reference/taircpc-command.md) 一致。 |
| [CPC.ARRAY.UPDATE2JUD](products/redis/documents/developer-reference/taircpc-command.md) | CPC.ARRAY.UPDATE2JUD key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item，并返回该时间窗口更新后的基数估算值和其与更新前的差值。若返回的差值为 1，则表示写入成功且不存在重复；若为 0 则表示已存在当前 item。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](products/redis/documents/developer-reference/taircpc-command.md) 一致。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairCpc 数据。 |


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

## CPC.UPDATE

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
| 语法 | CPC.UPDATE key item [EX|EXAT|PX|PXAT time ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中添加 item。若 TairCpc 不存在则自动新建，若待添加的 item 已存在于目标 TairCpc 中，则不会进行操作。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.UPDATE foo f1 EX 3600 返回示例： OK |


## CPC.ESTIMATE

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ESTIMATE ke y |
| 时间复杂度 | O(1) |
| 命令描述 | 获取指定 TairCpc 去重后的基数估算值，返回值的数据类型为 double 类型，您可以仅取整数部分（忽略小数点后的数据）。 |
| 选项 | key ：Key 名称（TairCpc 数据结构）。 |
| 返回值 | 执行成功：返回估算值，数据类型为 double 类型。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ESTIMATE foo 返回示例： "19.000027716212127" |


## CPC.UPDATE2EST

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
| 语法 | CPC.UPDATE2EST key item [EX|EXAT|PX|PXAT time ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中添加 item，返回更新后的基数估算值。若 TairCpc 不存在则自动新建。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 |
| 返回值 | 执行成功：返回更新后的估算值，数据类型为 double 类型。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.UPDATE2EST foo f3 返回示例： "3.0000004768373003" |


## CPC.UPDATE2JUD

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
| 语法 | CPC.UPDATE2JUD key item [EX|EXAT|PX|PXAT time ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中添加 item，并返回更新后的基数估算值和其与更新前的差值。若返回的差值为 1 则表示写入成功且不存在重复；若为 0 则表示已存在当前 item。若 TairCpc 不存在则自动新建。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 |
| 返回值 | 执行成功：返回更新后的估算值和该值与更新前的差值，数据类型均为 double 类型。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.UPDATE2JUD foo f20 返回示例： 1) "20.000027716212127" // 更新后，TairCpc 的估算值为 20。 2) "1.0000014901183398" // 20 - 19 = 1 |


## CPC.ARRAY.UPDATE

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
| 语法 | CPC.ARRAY.UPDATE key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item。若 TairCpc 不存在则自动新建， SIZE 为时间窗口个数， WIN 为时间窗口的长度（单位为毫秒）。随着流式数据的写入，TairCpc 会持续向前更新并保存 SIZE * WIN 时间范围内的数据，超过该时间范围的数据会被覆盖、删除。 SIZE 和 WIN 属性仅在新建 TairCpc 的时生效。 说明 例如目标 key 为计算近 10 分钟内每分钟的数据：可以设置 SIZE 为 10（10 个时间窗口）、 WIN 为 60000（每个时间窗口为 1 分钟）。当目标 key 中写入第 11 分钟的数据时，第 1 分钟的数据会逐渐被覆盖、删除。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：指定的 Unix 时间戳，单位为毫秒。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 SIZE ：时间窗口个数，默认为 10，范围为[1,1000]，建议设置在 120 以内。 WIN ：时间窗口的长度（单位为毫秒），默认为 60000 毫秒（1 分钟）。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.UPDATE foo 1645584510000 f1 SIZE 120 WIN 10000 返回示例： OK |


## CPC.ARRAY.ESTIMATE

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.ESTIMATE key timestamp |
| 时间复杂度 | O(1) |
| 命令描述 | 获取指定 TairCpc 中目标 timestamp 所在时间窗口的基数估算值。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：指定的 Unix 时间戳，单位为毫秒。 |
| 返回值 | 执行成功：返回对应时间窗口的基数估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.ESTIMATE foo 1645584532000 返回示例： "2" |


## CPC.ARRAY.ESTIMATE.RANGE

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.ESTIMATE.RANGE key start_time end_time |
| 时间复杂度 | O(1) |
| 命令描述 | 获取指定 TairCpc 的指定时间段内（包含指定时间点）各个时间窗口的基数估算值。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 start_time ：查询的开始时间（Unix 时间戳），单位为毫秒。 end_time ：查询的结束时间（Unix 时间戳），单位为毫秒。 |
| 返回值 | 执行成功：返回目标时间窗口的基数估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.ESTIMATE.RANGE foo 1645584510000 1645584550000 返回示例： 1) "2" 2) "0" 3) "1" 4) "0" 5) "0" |


## CPC.ARRAY.ESTIMATE.RANGE.MERGE

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | CPC.ARRAY.ESTIMATE.RANGE.MERGE key timestamp range |
| 时间复杂度 | O(1) |
| 命令描述 | 获取指定 TairCpc 在指定时间点至往前 range（含当前窗口）个时间窗口内，时间窗口合并、去重后的基数估算值。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：查询的开始时间（Unix 时间戳），单位为毫秒。 range ：查询的时间窗口个数。 |
| 返回值 | 执行成功：返回目标 key 在指定时间段内去重后的基数估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.ESTIMATE.RANGE.MERGE foo 1645584510000 3 返回示例： "6" |


## CPC.ARRAY.UPDATE2EST

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
| 语法 | CPC.ARRAY.UPDATE2EST key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item，并返回该时间窗口更新后的基数估算值。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](products/redis/documents/developer-reference/taircpc-command.md) 一致。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：指定的 Unix 时间戳，单位为毫秒。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 SIZE ：时间窗口个数，默认为 10，范围为[1,1000]，建议设置在 120 以内。 WIN ：时间窗口的长度（单位为毫秒），默认为 60000 毫秒（1 分钟）。 |
| 返回值 | 执行成功：返回目标时间窗口更新后的估算值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.UPDATE2EST foo 1645584530000 f3 返回示例： "3" |


## CPC.ARRAY.UPDATE2JUD

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
| 语法 | CPC.ARRAY.UPDATE2JUD key timestamp item [EX|EXAT|PX|PXAT time ] [SIZE size ] [WIN window_length ] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定 TairCpc 中，向目标 timestamp 对应的时间窗口添加 item，并返回该时间窗口更新后的基数估算值和其与更新前的差值。若返回的差值为 1，则表示写入成功且不存在重复；若为 0 则表示已存在当前 item。若 TairCpc 不存在则自动新建，新建参数用法与 [CPC.ARRAY.UPDATE](products/redis/documents/developer-reference/taircpc-command.md) 一致。 |
| 选项 | key ：Key 名称（TairCpc 数据结构），用于指定命令调用的 TairCpc 对象。 timestamp ：指定的 Unix 时间戳，单位为毫秒。 item ：待添加的数据。 EX ：指定 key 的相对过期时间，单位为秒，不传此参数表示不过期。 EXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为秒，不传此参数表示不过期。 PX ：指定 key 的相对过期时间，单位为毫秒，不传此参数表示不过期。 PXAT ：指定 key 的绝对过期时间（Unix 时间戳），单位为毫秒 ，不传此参数表示不过期。 SIZE ：时间窗口个数，默认为 10，范围为[1,1000]，建议设置在 120 以内。 WIN ：时间窗口的长度（单位为毫秒），默认为 60000 毫秒（1 分钟）。 |
| 返回值 | 执行成功：返回目标时间窗口更新后的估算值和该值与更新前的差值。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： CPC.ARRAY.UPDATE2JUD foo 1645584530000 f7 返回示例： 1) "8" // 更新后，TairCpc 的估算值为 8。 2) "1" // 8 - 7 = 1 |


[上一篇：TS](products/redis/documents/developer-reference/the-tickets-command.md)[下一篇：Roaring](products/redis/documents/developer-reference/tairroaring-command.md)

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
