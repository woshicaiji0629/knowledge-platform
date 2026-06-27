# TairRoaring扩展数据结构命令参考-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/tairroaring-command

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

# Roaring

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

TairRoaring是基于Tair引擎的Roaring Bitmap实现，本文介绍TairRoaring及其支持的命令。

## TairRoaring简介

Bitmap（又名Bitset）是一种常用的数据结构，使用少量的存储空间来实现海量数据的查询优化。尽管Bitmap相比常规基于Hash结构的实现节省了大量内存空间，但是常规Bitmap对于稀疏场景下的数据存储仍不够友好，因此有了各种压缩Bitmap的实现（Compressed bitmap），Roaring Bitmap就是业界公认的一种更高效和均衡的Bitmap压缩存储的实现。

TairRoaring在此基础上完成大量优化：

- 

通过2层索引和多种动态容器（Container），平衡了多种场景下性能和空间效率。

- 

使用了包括SIMD instructions、Vectorization、PopCnt算法等多种工程优化，提升了计算效率，实现了高效的时空效率。

- 

基于Tair提供的强大计算性能和极高的稳定性，为用户场景保驾护航。

典型场景

适用于直播、音乐、电商等行业，通过用户多维度标签，进行个性化推荐、精准营销等场景。

发布记录

重要

V2版本Breaking Change公告：

- 

TR.RANGEINTARRAY：V1版本的TR.RANGEINTARRAY命令名称修改为V2版本的TR.RANGE，其内容无变化。

- 

TR.SETRANGE：V1版本的TR.SETRANGE命令的返回值为OK，V2版本返回值为成功设置bit值为1的数量，其他内容无变化。

- 

2021年9月13日发布TairRoaring V1版本，请将小版本升级至1.7.20及以上。

- 

2022年3月11日发布TairRoaring V2版本，请将小版本升级至1.7.27及以上。

该版本优化了部分命令的实现，提升了性能。新增TR.SETBITS、TR.CLEARBITS等9个命令，向前兼容扩展2个命令，更新1个命令，更名1个命令。

- 

2022年4月20日发布TairRoaring V2.2版本，请将小版本升级至1.8.1及以上。

该版本新增TR.JACCARD、TR.CONTAINS、TR.RANK命令，更新部分命令在key不存在时的返回错误（移除了ERR key not found）。

## 最佳实践

[基于](products/redis/documents/use-cases/introduction-of-user-filtering-scheme-based-on-tairroaring.md)[TairRoaring](products/redis/documents/use-cases/introduction-of-user-filtering-scheme-based-on-tairroaring.md)[实现人群圈选方案](products/redis/documents/use-cases/introduction-of-user-filtering-scheme-based-on-tairroaring.md)

## 前提条件

实例为Tair[内存型](products/redis/documents/product-overview/dram-based-instances.md)。若实例为内存型（兼容Redis 5.0），则需要小版本为1.7.7及以上。

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群实例或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

操作对象为Tair实例中的TairRoaring数据。

## 命令列表

| 类型 | 命令 | 语法 | 说明 | 版本变更 |
| --- | --- | --- | --- | --- |
| 写操作 | [TR.SETBIT](products/redis/documents/developer-reference/tairroaring-command.md) | TR.SETBIT key offset value | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值（1 或者 0），并返回该 bit 位之前的值，Roaring Bitmap 的偏移量（offset）从 0 开始。 | -（表示未更新） |
| [TR.SETBITS](products/redis/documents/developer-reference/tairroaring-command.md) | TR.SETBITS key offset [offset1 offset2 ... offsetN] | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 1，支持传入多个值。 | V2 新增 |  |
| [TR.CLEARBITS](products/redis/documents/developer-reference/tairroaring-command.md) | TR.CLEARBITS key offset [offset1 offset2 ... offsetN] | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 0，若原值为 0 则不操作，支持传入多个值。 | V2 新增 |  |
| [TR.SETRANGE](products/redis/documents/developer-reference/tairroaring-command.md) | TR.SETRANGE key start end | 设置 Roaring Bitmap 中指定区间（偏移量）的 bit 值为 1。 | V2 更新，更新返回值为成功设置 bit 值为 1 的数量。 |  |
| [TR.APPENDBITARRAY](products/redis/documents/developer-reference/tairroaring-command.md) | TR.APPENDBITARRAY key offset bitarray | 将由连续的 0 或 1 组成的 bit 数组（bitarray）插入到 Roaring Bitmap 中指定偏移量（offset）之后的位置，并覆盖原有数据。 | V2 新增 |  |
| [TR.FLIPRANGE](products/redis/documents/developer-reference/tairroaring-command.md) | TR.FLIPRANGE key start end | 对 Roaring Bitmap 中指定区间（偏移量）的 bit 值执行位反转（1 反转为 0；0 反转为 1）。若指定 key 不存在，则自动创建目标 key，并以空 Roaring Bitmap 对指定区间的 bit 值执行位反转。 | V2 新增 |  |
| [TR.APPENDINTARRAY](products/redis/documents/developer-reference/tairroaring-command.md) | TR.APPENDINTARRAY key value [value1 value2 ... valueN] | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 1，支持传入多个值。 说明 在 TairRoaring V2 版本中，建议使用 [TR.SETBITS](products/redis/documents/developer-reference/tairroaring-command.md) 代替该命令。 | - |  |
| [TR.SETINTARRAY](products/redis/documents/developer-reference/tairroaring-command.md) | TR.SETINTARRAY key value [value1 value2 ... valueN] | 根据传入的整型数组，创建对应的 Roaring Bitmap，该命令会重置（覆盖）已存在的 Roaring Bitmap 对象。 说明 在 TairRoaring V2 版本中，建议使用 [TR.SETBITS](products/redis/documents/developer-reference/tairroaring-command.md) 代替该命令。 | - |  |
| [TR.SETBITARRAY](products/redis/documents/developer-reference/tairroaring-command.md) | TR.SETBITARRAY key value | 根据传入的 bit（由 0 和 1 组成的字符串），创建对应的 Roaring Bitmap。若目标 Key 已存在则会重置（覆盖）原有数据。 说明 在 TairRoaring V2 版本中，建议使用 [TR.APPENDBITARRAY](products/redis/documents/developer-reference/tairroaring-command.md) 代替该命令。 | - |  |
| [TR.BITOP](products/redis/documents/developer-reference/tairroaring-command.md) | TR.BITOP destkey operation key [key1 key2 ... keyN] | 对 Roaring Bitmap 执行集合运算操作，计算结果存储在 destkey 中，支持 AND 、 OR 、 XOR 、 NOT 和 DIFF 集合运算类型。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | - |  |
| [TR.BITOPCARD](products/redis/documents/developer-reference/tairroaring-command.md) | TR.BITOPCARD operation key [key1 key2 ... keyN] | 对 Roaring Bitmap 执行集合运算操作，支持 AND 、 OR 、 XOR 、 NOT 和 DIFF 集合运算类型。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | V2 新增 |  |
| [TR.OPTIMIZE](products/redis/documents/developer-reference/tairroaring-command.md) | TR.OPTIMIZE key | 优化 Roaring Bitmap 的存储空间。如果目标对象相对较大，且创建后以只读操作为主，可以主动执行此命令。 | - |  |
| 读操作 | [TR.GETBIT](products/redis/documents/developer-reference/tairroaring-command.md) | TR.GETBIT key offset | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值。 | - |
| [TR.GETBITS](products/redis/documents/developer-reference/tairroaring-command.md) | TR.GETBITS key offset [offset1 offset2 ... offsetN] | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值，支持查询多个值。 | V2 新增 |  |
| [TR.BITCOUNT](products/redis/documents/developer-reference/tairroaring-command.md) | TR.BITCOUNT key [start end] | 获取 Roaring Bitmap 中指定区间（偏移量）bit 值为 1 的数量。 | V2 更新，向前兼容。 |  |
| [TR.BITPOS](products/redis/documents/developer-reference/tairroaring-command.md) | TR.BITPOS <key> <value> [count] | 获取第 count 个 bit 值为 1 或者 0 的偏移量，count 为可选参数，默认为 1（表示从前向后计数的第一个）。 | V2 更新，向前兼容。 |  |
| [TR.SCAN](products/redis/documents/developer-reference/tairroaring-command.md) | TR.SCAN key start_offset [COUNT count] | 从 Roaring Bitmap 中指定偏移量（start_offset）开始向后扫描，返回若干（count）个 bit 值为 1 的偏移量，返回的游标（cursor）为 Roaring Bitmap 对应的 offset。 说明 在迭代过程中被添加、被删除的元素的扫描结果存在不确定性，即可能被返回，也可能不会。 | V2 新增 |  |
| [TR.RANGE](products/redis/documents/developer-reference/tairroaring-command.md) | TR.RANGE key start end | 获取 Roaring Bitmap 指定区间中 bit 值为 1 的偏移量。 | V1 的 TR.RANGEINTARRAY 命令，V2 重命名为 TR.RANGE。 |  |
| [TR.RANGEBITARRAY](products/redis/documents/developer-reference/tairroaring-command.md) | TR.RANGEBITARRAY key start end | 获取 Roaring Bitmap 指定区间中所有 bit 值（0、1）组成的字符串。 | V2 新增 |  |
| [TR.MIN](products/redis/documents/developer-reference/tairroaring-command.md) | TR.MIN key | 获取 Roaring Bitmap 中 bit 值为 1 的最小偏移量（首个），不存在时返回-1。 | - |  |
| [TR.MAX](products/redis/documents/developer-reference/tairroaring-command.md) | TR.MAX key | 获取 Roaring Bitmap 中 bit 值为 1 的最大偏移量，不存在时返回-1。 | - |  |
| [TR.STAT](products/redis/documents/developer-reference/tairroaring-command.md) | TR.STAT key [JSON] | 获取 Roaring Bitmap 的统计信息，包括各种容器的数量以及内存使用状况等信息。 | V2 新增 |  |
| [TR.JACCARD](products/redis/documents/developer-reference/tairroaring-command.md) | TR.JACCARD key1 key2 | 获取两个 Roaring Bitmap 之间的 Jaccard 相似系数，Jaccard 系数值越大，Roaring Bitmap 的相似度越高。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | V2.2 新增 |  |
| [TR.CONTAINS](products/redis/documents/developer-reference/tairroaring-command.md) | TR.CONTAINS key1 key2 | 计算 key2 所对应的 Roaring Bitmap 是否包含 key1 所对应的 Roaring Bitmap（即 key1 是否为 key2 的子集），若包含则返回 1，否则返回 0。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 | V2.2 新增 |  |
| [TR.RANK](products/redis/documents/developer-reference/tairroaring-command.md) | TR.RANK key offset | 获取 Roaring Bitmap 中从 offset 为 0 到指定 offset 区间内（包含该值），bit 值为 1 的数量。 | V2.2 新增 |  |
| 通用 | [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairRoaring 数据。 | - |


说明

- 

本文关于命令语法的定义：

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

- 

本文关于时间复杂度的特别约定：

- 

C表示参数的数量（argc）或范围（range）。

- 

M表示该种数据结构内部bit值为1的数量（例如List的node数量，Hash的field数量等）。

## TR.SETBIT

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETBIT key offset value |
| 时间复杂度 | O(1) |
| 命令描述 | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值（1 或者 0），并返回该 bit 位之前的值，Roaring Bitmap 的偏移量（offset）从 0 开始。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：整型数字，表示待设置 bit 的偏移量，取值范围为 0 ~ 2^32。 value ：待设置的 bit 值，可以设置 1 或者 0。 |
| 返回值 | 执行成功：返回 0 或 1，表示 bit 位之前的值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETBIT foo 0 1 返回示例： (integer) 0 |


## TR.SETBITS

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETBITS key offset [offset1 offset2 ... offsetN] |
| 时间复杂度 | O(C) |
| 命令描述 | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 1，支持传入多个值。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：整型数字，表示待设置 bit 的偏移量，取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回更新后 Roaring Bitmap 中 bit 值为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETBITS foo 9 10 返回示例： (integer) 5 |


## TR.CLEARBITS

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.CLEARBITS key offset [offset1 offset2 ... offsetN] |
| 时间复杂度 | O(C) |
| 命令描述 | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 0，若原值为 0 则不操作，支持传入多个值。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：整型数字，表示待设置 bit 的偏移量，取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回本次命令成功将 bit 值设置为 0 的数量。 若 key 不存在：返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.CLEARBITS foo 9 10 返回示例： (integer) 2 |


## TR.SETRANGE

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETRANGE key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 设置 Roaring Bitmap 中指定区间（偏移量）的 bit 值为 1。 例如执行 TR.SETRANGE foo 1 3 ，将创建 foo 为"0111"。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始偏移量（包含该值），取值范围为 0 ~ 2^32。 end ：结束偏移量（包含该值），取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回本次命令成功将 bit 值设置为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETRANGE foo 1 3 返回示例： (integer) 3 |


## TR.APPENDBITARRAY

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.APPENDBITARRAY key offset bitarray |
| 时间复杂度 | O(C) |
| 命令描述 | 将由连续的 0 或 1 组成的 bit 数组（bitarray）插入到 Roaring Bitmap 中指定偏移量（offset）之后的位置，并覆盖原有数据。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：指定的起始偏移量（不包含该值），取值范围为-1 ~ 2^32。 bitarray ：待添加的 bit 数组，将覆盖原有数据，由连续的 0 或 1，取值范围为 0 ~ 2^32。 说明 指定的 offset 与添加的 bitarray 的总长度不能超过 2^32，否则会操作失败。 |
| 返回值 | 执行成功：返回本次命令成功将 bit 值设置为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 。 命令示例： TR.APPENDBITARRAY foo 1 1101 返回示例： (integer) 4 此时，Roaring Bitmap foo 为“101101”。 |


## TR.FLIPRANGE

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.FLIPRANGE key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 对 Roaring Bitmap 中指定区间（偏移量）的 bit 值执行位反转（1 反转为 0；0 反转为 1）。若指定 key 不存在，则自动创建目标 key，并以空 Roaring Bitmap 对指定区间的 bit 值执行位反转。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始偏移量（包含该值），取值范围为 0 ~ 2^32。 end ：结束偏移量（包含该值），取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回本次命令成功将 bit 值设置为 1 的数量。 若 key 不存在：自动创建目标 key，并以空 Roaring Bitmap 对指定区间的 bit 值执行位反转，返回本次命令成功将 bit 值设置为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 2 3 5 。 命令示例： TR.FLIPRANGE foo 0 5 返回示例： (integer) 2 此时，Roaring Bitmap foo 为“01001”。 |


## TR.APPENDINTARRAY

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.APPENDINTARRAY key value [value1 value2 ... valueN] |
| 时间复杂度 | O(C) |
| 命令描述 | 设置 Roaring Bitmap 中指定偏移量（offset）的 bit 值为 1，支持传入多个值。 说明 在 TairRoaring V2 版本中，建议使用 [TR.SETBITS](products/redis/documents/developer-reference/tairroaring-command.md) 代替该命令。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 value ：整型数字，表示待设置的 bit 位，取值范围为 0 ~ 4294967296。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.APPENDINTARRAY foo 9 10 返回示例： OK |


## TR.SETINTARRAY

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETINTARRAY key value [value1 value2 ... valueN] |
| 时间复杂度 | O(C) |
| 命令描述 | 根据传入的整型数组来设置对应的 Roaring Bitmap，若目标 Key 已存在则会重置（覆盖）原有数据。 说明 在 TairRoaring V2 版本中，建议使用 [TR.SETBITS](products/redis/documents/developer-reference/tairroaring-command.md) 代替该命令。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 value ：整型数字，表示待设置的 bit 位。 |
| 返回值 | 执行成功：返回 OK。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SETINTARRAY foo 2 4 5 6 返回示例： OK |


## TR.SETBITARRAY

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SETBITARRAY key value |
| 时间复杂度 | O(C) |
| 命令描述 | 根据传入的 bit（由 0 和 1 组成的字符串），创建对应的 Roaring Bitmap。若目标 Key 已存在则会重置（覆盖）原有数据。 说明 在 TairRoaring V2 版本中，建议使用 [TR.APPENDBITARRAY](products/redis/documents/developer-reference/tairroaring-command.md) 代替该命令。 |
| 选项 | key ：Key 名称（TairRoaring 数据结构）。 value ：由 0 和 1 构成的字符串，即需要设置的 bit 数组。 |
| 返回值 | 执行成功：返回 OK 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： tr.setbitarray foo 10101001 返回示例： OK |


## TR.BITOP

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.BITOP destkey operation key [key1 key2 ... keyN] |
| 时间复杂度 | O(C * M) |
| 命令描述 | 对 Roaring Bitmap 执行集合运算操作，计算结果存储在 destkey 中，支持 AND 、 OR 、 XOR 、 NOT 和 DIFF 集合运算类型。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 |
| 选项 | destkey ：集合运算结果所存储的目标 Key（TairRoaring 数据结构）。 operation ：集合运算类型，取值：AND（表示与）、OR（表示或）、XOR（表示异或）、NOT（表示非）、DIFF（表示差）。 说明 NOT 仅支持操作 1 个对象。 DIFF 仅支持计算 2 个对象的差集，请注意计算差集对象的运算顺序，例如 TR.BITOP result DIFF key1 key2 是计算 key1 关于 key2 的差集（key1 - key2）。 key ：Key 名称（TairRoaring 数据结构），可传入多个 Key。 |
| 返回值 | 执行成功：返回操作运算结果中 bit 值为 1 的数量，格式为 Integer（整数）。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.BITOP result OR foo bar 返回示例： (integer) 6 |


## TR.BITOPCARD

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.BITOPCARD operation key [key1 key2 ... keyN] |
| 时间复杂度 | O(C * M) |
| 命令描述 | 对 Roaring Bitmap 执行集合运算操作，支持 AND 、 OR 、 XOR 、 NOT 和 DIFF 集合运算类型。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 |
| 选项 | operation ：集合运算类型，取值：AND（表示与）、OR（表示或）、XOR（表示异或）、NOT（表示非）、DIFF（表示差）。 说明 NOT 仅支持操作 1 个对象。 DIFF 仅支持计算 2 个对象的差集，请注意计算差集对象的运算顺序，例如 TR.BITOP result DIFF key1 key2 是计算 key1 关于 key2 的差集（key1 - key2）。 key ：Key 名称（TairRoaring 数据结构），可传入多个 Key。 |
| 返回值 | 执行成功：返回操作运算结果中 bit 值为 1 的数量，格式为 Integer（整数）。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.BITOPCARD NOT foo 返回示例： (integer) 2 |


## TR.OPTIMIZE

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.OPTIMIZE key |
| 时间复杂度 | O(M) |
| 命令描述 | 优化 Roaring Bitmap 的存储空间。如果目标对象相对较大，且创建后以只读操作为主，可以主动执行此命令。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功：返回 OK。 若 key 不存在：返回 nil 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.OPTIMIZE foo 返回示例： OK |


## TR.GETBIT

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.GETBIT key offset |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：待查询的偏移量。 |
| 返回值 | 执行成功：返回 0 或 1，表示 bit 位的值。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.GETBIT foo 0 返回示例： (integer) 1 |


## TR.GETBITS

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.GETBITS key offset [offset1 offset2 ... offsetN] |
| 时间复杂度 | O(C) |
| 命令描述 | 获取 Roaring Bitmap 中指定偏移量（offset）的 bit 值，支持查询多个值。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：待查询的偏移量。 |
| 返回值 | 执行成功：返回对应 bit 的值。 若 key 不存在：返回空数组。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.GETBITS foo 3 4 6 8 返回示例： 1) (integer) 1 2) (integer) 1 3) (integer) 1 4) (integer) 0 |


## TR.BITCOUNT

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.BITCOUNT key [start end] |
| 时间复杂度 | O(M) |
| 命令描述 | 获取 Roaring Bitmap 中指定区间（偏移量）bit 值为 1 的数量。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始偏移量（包含该值），取值范围为 0 ~ 2^32。 end ：结束偏移量（包含该值），取值范围为 0 ~ 2^32。 |
| 返回值 | 执行成功：返回 Roaring Bitmap 中值为 1 的 bit 位数量，格式为 Integer（整数）。 若 key 不存在：返回 0。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.BITCOUNT foo 4 9 返回示例： (integer) 3 |


## TR.BITPOS

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.BITPOS <key> <value> [count] |
| 时间复杂度 | O(C) |
| 命令描述 | 获取第 count 个 bit 值为 1 或者 0 的偏移量，count 为可选参数，默认为 1（表示从前向后计数的第一个）。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 value ：待查找 bit 值（1 或者 0）。 count ：查找第几位，负数表示从末尾向前计数。 |
| 返回值 | 执行成功：返回目标 bit 的偏移量（offset）。 若 key 不存在：返回-1。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.BITPOS foo 1 -1 返回示例： (integer) 6 |


## TR.SCAN

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.SCAN key start_offset [COUNT count] |
| 时间复杂度 | O(C) |
| 命令描述 | 从 Roaring Bitmap 中指定偏移量（start_offset）开始向后扫描，返回若干（count）个 bit 值为 1 的偏移量，返回的游标（cursor）为 Roaring Bitmap 对应的 offset。 说明 在迭代过程中被添加、被删除的元素的扫描结果存在不确定性，即可能被返回，也可能不会。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start_offset ：起始偏移量（包含该值）。 COUNT ：查询的数量（默认为 10）。 |
| 返回值 | 执行成功，返回具有两个元素的数组： 第一个元素：下次查询的 start_offset，若该 key 已扫描完成，则返回 0。 第二个元素：本次查询的目标偏移量。 说明 若 key 不存在，返回 0 与空元素组成的数组。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.SCAN foo 0 COUNT 2 返回示例： 1) (integer) 3 2) 1) (integer) 0 2) (integer) 2 |


## TR.RANGE

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.RANGE key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 获取 Roaring Bitmap 指定区间中 bit 值为 1 的偏移量。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始的偏移量（包含该值）。 end ：结束的偏移量（包含该值）。 |
| 返回值 | 执行成功：返回 bit 值为 1 的偏移量。 若 key 不存在：返回空数组。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 2 3 5 。 命令示例： TR.RANGE foo 0 5 返回示例： 1) (integer) 0 2) (integer) 2 3) (integer) 3 4) (integer) 5 |


## TR.RANGEBITARRAY

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.RANGEBITARRAY key start end |
| 时间复杂度 | O(C) |
| 命令描述 | 获取 Roaring Bitmap 指定区间中所有 bit 值（0、1）组成的字符串。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 start ：起始的偏移量（包含该值）。 end ：结束的偏移量（包含该值）。 |
| 返回值 | 执行成功：返回 bit 值为 1 的偏移量。 若 key 不存在：返回 nil 。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS foo 0 2 3 5 。 命令示例： TR.RANGEBITARRAY foo 0 5 返回示例： "101101" |


## TR.MIN

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.MIN key |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 Roaring Bitmap 中 bit 值为 1 的最小偏移量（首个），不存在时返回-1。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功： 返回首个 bit 值为 1 的偏移量，格式为 Integer（整数）。 返回-1，表示 key 不存在或者该 Roaring Bitmap 中不存在值为 1 的 bit。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.MIN foo 返回示例： 4 |


## TR.MAX

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.MAX key |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 Roaring Bitmap 中 bit 值为 1 的最大偏移量，不存在时返回-1。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功： 返回最后一个 bit 值为 1 的偏移量，格式为 Integer（整数）。 返回-1，表示 key 不存在或者该 Roaring Bitmap 中不存在值为 1 的 bit。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.MAX foo 返回示例： 6 |


## TR.STAT

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.STAT key [JSON] |
| 时间复杂度 | O(M) |
| 命令描述 | 获取 Roaring Bitmap 的统计信息，包括各种容器的数量以及内存使用状况等信息。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 JSON ：若指定 JSON，则以 JSON 格式返回统计信息。 |
| 返回值 | 执行成功：返回 Redis 的统计信息（bulk string），说明如下。 "{\"cardinality\":3, # 元素总数量 \"number_of_containers\":1, # TairRoaring 容器总数（Roaring Bitmap 概念） \"max_value\":6, # 最大元素值 \"min_value\":3, # 最小元素值 \"sum_value\":13, \"array_container\":{ # array 容器数量（Roaring Bitmap 概念） \"number_of_containers\":1, \"container_cardinality\":3, \"container_allocated_bytes\":6}, \"bitset_container\":{ # bitset 容器数量（Roaring Bitmap 概念） \"number_of_containers\":0, \"container_cardinality\":0, \"container_allocated_bytes\":0}, \"run_container\":{ # RLE 容器数量（Roaring Bitmap 概念） \"number_of_containers\":0, \"container_cardinality\":0, \"container_allocated_bytes\":0}}" 若 key 不存在：返回 nil 。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.STAT foo JSON 返回示例： "{\"cardinality\":4,\"number_of_containers\":1,\"max_value\":5,\"min_value\":0,\"sum_value\":10,\"array_container\":{\"number_of_containers\":1,\"container_cardinality\":4,\"container_allocated_bytes\":8},\"bitset_container\":{\"number_of_containers\":0,\"container_cardinality\":0,\"container_allocated_bytes\":0},\"run_container\":{\"number_of_containers\":0,\"container_cardinality\":0,\"container_allocated_bytes\":0}}" |


## TR.JACCARD

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.JACCARD key1 key2 |
| 时间复杂度 | O(M) |
| 命令描述 | 获取两个 Roaring Bitmap 之间的 Jaccard 相似系数，Jaccard 系数值越大，Roaring Bitmap 的相似度越高。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功：返回 Jaccard 相似系数（Double 类型）。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TR.JACCARD foo1 foo2 返回示例： "0.20000000000000001" |


## TR.CONTAINS

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.CONTAINS key1 key2 |
| 时间复杂度 | O(M) |
| 命令描述 | 计算 key2 所对应的 Roaring Bitmap 是否包含 key1 所对应的 Roaring Bitmap（即 key1 是否为 key2 的子集），若包含则返回 1，否则返回 0。 说明 该命令在集群架构实例中不支持执行跨 Slot 的 Key。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 |
| 返回值 | 执行成功： 返回 1，表示 key2 包含 key1，即 key1 是 key2 的子集。 返回 0，表示 key2 不包含 key1，即 key1 不是 key2 的子集。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS fooM 1 2 3 10 、 TR.SETBITS foom 1 2 命令。 命令示例： TR.CONTAINS foom fooM 返回示例： (integer) 1 |


## TR.RANK

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | TR.RANK key offset |
| 时间复杂度 | O(M) |
| 命令描述 | 获取 Roaring Bitmap 中从 offset 为 0 到指定 offset 区间内（包含该值），bit 值为 1 的数量。 |
| 选项 | Key ：Key 名称（TairRoaring 数据结构）。 offset ：指定 bit 的 offset 位，取值为 INT（整型数字）。 |
| 返回值 | 执行成功：目标区间 bit 值为 1 的数量。 其他情况返回相应的异常信息。 |
| 示例 | 提前执行 TR.SETBITS fooM 1 2 3 10 。 命令示例： TR.RANK fooM 10 返回示例： (integer) 4 |


## 异常返回值说明

- 

- 

- 

| 错误信息 | 说明 |
| --- | --- |
| WRONGTYPE Operation against a key holding the wrong kind of value | 对象类型错误：Key 不是 TairRoaring 对象。 |
| ERR bad arguments, must be unsigned 32-bit integer | 参数类型错误：无法按照 32-bit 整型进行转换。 |
| ERR invalid arguments, maybe out of range or illegal | 参数非法： 非 32-bit 整型的 offset 不符合规则。 参数的[start,end]不符合规则。 参数超过 Roaring Bitmap 的元素个数。 |
| ERR key already exist | Roaring Bitmap 对象已存在，且不支持覆盖。 说明 V2.2 版之后将不会产生该报错。 |
| ERR key not found | Roaring Bitmap 对象不存在, 不支持操作。 说明 V2.2 版之后将不会产生该报错。 |


[上一篇：Cpc](products/redis/documents/developer-reference/taircpc-command.md)[下一篇：Search](products/redis/documents/developer-reference/tairsearch.md)

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
