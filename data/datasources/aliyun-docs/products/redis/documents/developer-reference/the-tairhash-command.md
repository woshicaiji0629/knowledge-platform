# TairHash数据结构命令详解-云数据库Tair-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/the-tairhash-command

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

# exHash

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

TairHash（exHash）是一种可为field设置过期时间和版本的Hash类型数据结构，提高了Hash数据结构的灵活性，简化了很多场景下的业务开发工作。

## TairHash简介

TairHash不但和Redis Hash一样支持丰富的数据接口和高处理性能，还改变了hash只能为key设置过期时间的限制，可以为field设置过期时间和版本，极大地提高了hash数据结构的灵活性，简化了很多场景下的业务开发工作。TairHash使用高效的Active Expire算法，可以在不对响应时间造成明显影响的前提下，更高效的完成对field的过期判断和删除。

主要特征

- 

field支持单独设置expire和version。

- 

field支持高效灵活的主动、被动过期淘汰（expire）策略。

- 

语法和原生Redis Hash数据类型类似。

该Module已开源，更多信息请参见[TairHash](https://github.com/alibaba/TairHash)。

## 前提条件

实例为Tair：

- 

[内存型](products/redis/documents/product-overview/dram-based-instances.md)

- 

[持久内存型](products/redis/documents/product-overview/persistent-memory-optimized-instances-1.md)（小版本为1.2.6及以上）

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群架构或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

操作对象为Tair实例中的TairHash数据。

## 命令列表

表 1.TairHash命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [EXHSET](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHSET key field value [EX time] [EXAT time] [PX time] [PXAT time] [NX | XX] [VER | ABS version] [KEEPTTL] | 向 Key 指定的 TairHash 中插入一个 field。如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 |
| [EXHGET](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHGET key field | 获取 key 指定的 TairHash 中一个 field 的值，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| [EXHMSET](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHMSET key field value [field value ...] | 同时向 key 指定的 TairHash 中插入多个 field，如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 |
| [EXHPEXPIREAT](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHPEXPIREAT key field milliseconds-timestamp [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置绝对过期时间，精确到毫秒。 |
| [EXHPEXPIRE](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHPEXPIRE key field milliseconds [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为毫秒。 |
| [EXHEXPIREAT](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHEXPIREAT key field timestamp [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置绝对过期时间，精确到秒。 |
| [EXHEXPIRE](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHEXPIRE key field seconds [VER | ABS version] | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为秒。 |
| [EXHPTTL](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHPTTL key field | 查看 key 指定的 TairHash 中一个 field 的剩余过期时间，结果精确到毫秒。 |
| [EXHTTL](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHTTL key field | 查看 key 指定的 TairHash 中一个 field 的过期时间，结果精确到秒。 |
| [EXHVER](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHVER key field | 查看 key 指定的 TairHash 中一个 field 的当前版本号。 |
| [EXHSETVER](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHSETVER key field version | 设置 key 指定的 TairHash 中一个 field 的版本号。 |
| [EXHINCRBY](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHINCRBY key field num [EX time] [EXAT time] [PX time] [PXAT time] [VER | ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个整数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 |
| [EXHINCRBYFLOAT](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHINCRBYFLOAT key field num [EX time] [EXAT time] [PX time] [PXAT time] [VER | ABS version] [MIN minval] [MAX maxval] [KEEPTTL] | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个浮点数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 |
| [EXHGETWITHVER](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHGETWITHVER key field | 同时获取 key 指定的 TairHash 一个 field 的值和版本，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| [EXHMGET](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHMGET key field [field ...] | 同时获取 key 指定的 TairHash 多个 field 的值，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| [EXHMGETWITHVER](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHMGETWITHVER key field [field ...] | 同时获取 key 指定的 TairHash 多个 field 的值和版本。 |
| [EXHLEN](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHLEN key [NOEXP] | 获取 key 指定的 TairHash 中 field 个数，该命令不会触发对过期 field 的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的 field。如果只想返回当前没有过期的 field 个数，可以在命令中设置 NOEXP 选项。 |
| [EXHEXISTS](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHEXISTS key field | 查询 key 指定的 TairHash 中是否存在对应的 field。 |
| [EXHSTRLEN](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHSTRLEN key field | 获取 key 指定的 TairHash 中一个 field 对应的 value 的长度。 |
| [EXHKEYS](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHKEYS key | 获取 key 指定的 TairHash 中所有的 field。 |
| [EXHVALS](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHVALS key | 获取 key 指定的 TairHash 中所有 field 的值。 |
| [EXHGETALL](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHGETALL key | 获取 key 指定的 TairHash 中所有 field 及其 value。 |
| [EXHSCAN](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHSCAN key op subkey [MATCH pattern] [COUNT count] | 扫描 Key 指定的 TairHash。 说明 仅内存型实例支持该命令。 |
| [EXHDEL](products/redis/documents/developer-reference/the-tairhash-command.md) | EXHDEL key field [field ...] | 删除 key 指定的 TairHash 中的一个 field，如果 TairHash 不存在或者 field 不存在则返回 0 ，成功删除返回 1。 |
| [DEL](https://valkey.io/commands/del/) | DEL <key> [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairHash 数据。 |


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

## EXHSET

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

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHSET key field value [EX time] [EXAT time] [PX time] [PXAT time] [NX | XX] [VER | ABS version] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 向 Key 指定的 TairHash 中插入一个 field。如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 您也可以通过 EXPIRE 或 EXPIREAT 命令设置 Key 的过期时间。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 value ：field 对应的值，一个 field 只能有一个 value。 EX ：指定 field 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 field 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 field 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 field 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 NX ：只在 field 不存在时插入。 XX ：只在 field 存在时插入。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 KEEPTTL ：在不指定 EX、EXAT、PX 或 PXAT 选项时，使用 KEEPTTL 选项会保留 field 当前的过期设置。 说明 若不使用 KEEPTTL 选项，EXHSET 命令会默认删除 field 上原先设置的过期时间。 |
| 返回值 | 新建 field 并成功为它设置值：1。 field 已经存在，成功覆盖旧值：0。 指定了 XX 且 field 不存在：-1。 指定了 NX 且 field 已经存在：-1。 指定了 VER 且版本和当前版本不匹配："ERR update version is stale"。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHSET myhash field1 val EX 10 返回示例： (integer) 1 |


## EXHGET

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHGET key field |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 key 指定的 TairHash 中一个 field 的值，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | field 存在且操作成功：field 对应的值。 key 不存在或者 field 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHSET myhash field1 val 命令。 命令示例： EXHGET myhash field1 返回示例： "val" |


## EXHMSET

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHMSET key field value [field value ...] |
| 时间复杂度 | O(N) |
| 命令描述 | 同时向 key 指定的 TairHash 中插入多个 field，如果 TairHash 不存在则自动创建一个，如果 field 已经存在则覆盖其值。 说明 创建 Key 后，您可以通过 EXHPEXPIREAT 、 EXHPEXPIRE 、 EXHEXPIREAT 或 EXHEXPIRE 命令设置 field 的过期时间，您也可以通过 EXPIRE 或 EXPIREAT 命令设置 Key 的过期时间。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 value ：field 对应的值，一个 field 只能有一个 value。 |
| 返回值 | 成功：OK。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHMSET myhash field1 val1 field2 val2 返回示例： OK |


## EXHPEXPIREAT

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
| 语法 | EXHPEXPIREAT key field milliseconds-timestamp [VER | ABS version] |
| 时间复杂度 | O(1) |
| 命令描述 | 在 key 指定的 TairHash 中为一个 field 设置绝对过期时间，精确到毫秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 milliseconds-timestamp ：精确到毫秒的 UNIX 时间戳 （Unix timestamp）。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 |
| 返回值 | field 存在且设置成功：1。 field 不存在：0。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHPEXPIREAT myhash field1 1293840000 返回示例： (integer) 1 |


## EXHPEXPIRE

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
| 语法 | EXHPEXPIRE key field milliseconds [VER | ABS version] |
| 时间复杂度 | O(1) |
| 命令描述 | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为毫秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 milliseconds ：相对过期时间，单位为毫秒。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 |
| 返回值 | field 存在且设置成功：1。 field 不存在：0。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHPEXPIRE myhash field1 1000 返回示例： (integer) 1 |


## EXHEXPIREAT

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
| 语法 | EXHEXPIREAT key field timestamp [VER | ABS version] |
| 时间复杂度 | O(1) |
| 命令描述 | 在 key 指定的 TairHash 中为一个 field 设置绝对过期时间，精确到秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 timestamp ：精确到秒的 UNIX 时间戳 （Unix timestamp）。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 |
| 返回值 | field 存在且设置成功：1。 field 不存在：0。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHEXPIREAT myhash field1 1293840000 返回示例： (integer) 1 |


## EXHEXPIRE

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
| 语法 | EXHEXPIRE key field seconds [VER | ABS version] |
| 时间复杂度 | O(1) |
| 命令描述 | 在 key 指定的 TairHash 中为一个 field 设置相对过期时间，单位为秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 seconds ：相对过期时间，单位为秒。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 |
| 返回值 | field 存在且设置成功：1。 field 不存在：0。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHEXPIRE myhash field1 100 返回示例： (integer) 1 |


## EXHPTTL

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHPTTL key field |
| 时间复杂度 | O(1) |
| 命令描述 | 查看 key 指定的 TairHash 中一个 field 的剩余过期时间，结果精确到毫秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | field 存在但是没有设置过期时间：-1。 key 不存在：-2。 field 不存在：-3。 field 存在且设置了过期时间：过期时间，单位为毫秒。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHSET myhash field1 val1 EX 100 命令。 命令示例： EXHPTTL myhash field1 返回示例： (integer) 97213 |


## EXHTTL

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHTTL key field |
| 时间复杂度 | O(1) |
| 命令描述 | 查看 key 指定的 TairHash 中一个 field 的过期时间，结果精确到秒。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在：-2。 field 不存在：-3。 field 存在但是没有设置过期时间：-1。 field 存在且设置了过期时间：过期时间，单位为秒。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHSET myhash field1 val1 EX 100 命令。 命令示例： EXHTTL myhash field1 返回示例： (integer) 85 |


## EXHVER

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHVER key field |
| 时间复杂度 | O(1) |
| 命令描述 | 查看 key 指定的 TairHash 中一个 field 的当前版本号。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在：-1。 field 不存在：-2。 查询成功：field 的版本号。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHVER myhash field1 返回示例： (integer) 1 |


## EXHSETVER

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHSETVER key field version |
| 时间复杂度 | O(1) |
| 命令描述 | 设置 key 指定的 TairHash 中一个 field 的版本号。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | TairHash 或者 field 不存在：0。 设置成功：1。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHSETVER myhash field1 3 返回示例： (integer) 1 |


## EXHINCRBY

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
| 语法 | EXHINCRBY key field num [EX time] [EXAT time] [PX time] [PXAT time] [VER | ABS version] [MIN minval] [MAX maxval] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个整数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 num ：需要为 field 的 value 增加的整数值。 EX ：指定 field 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 field 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 field 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 field 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 MIN ：value 的最小值，小于该值则提示异常。 MAX ：value 的最大值，大于该值则提示异常。 KEEPTTL ：在不指定 EX、EXAT、PX 或 PXAT 选项时，使用 KEEPTTL 选项会保留 field 当前的过期设置。 |
| 返回值 | 成功：与 num 相加后 value 的值。 其它情况返回异常。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 命令。 命令示例： EXHINCRBY myhash field1 100 返回示例： (integer) 110 |


## EXHINCRBYFLOAT

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
| 语法 | EXHINCRBYFLOAT key field num [EX time] [EXAT time] [PX time] [PXAT time] [VER | ABS version] [MIN minval] [MAX maxval] [KEEPTTL] |
| 时间复杂度 | O(1) |
| 命令描述 | 将 key 指定的 TairHash 中一个 field 的 value 增加 num，num 为一个浮点数。如果 TairHash 不存在则自动新创建一个，如果指定的 field 不存在，则在加之前插入该 field 并将其值设置为 0。 说明 为 Key 的 field 设置了超时时间后，再次执行该命令时如果没有设置超时时间，该 field 将被设置为永不过期。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 num ：需要为 field 的 value 增加的值，类型为浮点。 EX ：指定 field 的相对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 EXAT ：指定 field 的绝对过期时间，单位为秒， 为 0 表示马上过期，不传此参数表示不过期 。 PX ：指定 field 的相对过期时间，单位为毫秒， 为 0 表示马上过期，不传此参数表示不过期 。 PXAT ：指定 field 的绝对过期时间，单位为毫秒 ， 为 0 表示马上过期，不传此参数表示不过期 。 VER ：版本号。 如果 field 存在，和当前版本号做比较： 如果相等，继续操作，且版本号加 1。 如果不相等，返回异常。 如果 field 不存在或者 field 当前版本为 0，忽略传入的版本号并继续操作，成功后版本号变为 1。 ABS ：绝对版本号，不论 field 是否存在，可以在插入 field 时设置为本参数所指定的版本号。 MIN ：value 的最小值，小于该值则提示异常。 MAX ：value 的最大值，大于该值则提示异常。 KEEPTTL ：在不指定 EX、EXAT、PX 或 PXAT 选项时，使用 KEEPTTL 选项会保留 field 当前的过期设置。 |
| 返回值 | 成功：与 num 相加后 value 的值。 其它情况返回异常。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 命令。 命令示例： EXHINCRBYFLOAT myhash field1 9.235 返回示例： "19.235" |


## EXHGETWITHVER

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHGETWITHVER key field |
| 时间复杂度 | O(1) |
| 命令描述 | 同时获取 key 指定的 TairHash 一个 field 的值和版本，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | field 存在且操作成功：field 对应的值和版本。 key 不存在或者 field 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHGETWITHVER myhash field1 返回示例： 1) "19.235" 2) (integer) 5 |


## EXHMGET

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHMGET key field [field ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 同时获取 key 指定的 TairHash 多个 field 的值，如果 TairHash 不存在或者 field 不存在，则返回 nil。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在：nil。 key 存在且查询的所有 field 都存在：返回一个数组，数组的每一个元素对应一个 field 的 value。 key 存在且查询的 field 中有不存在的：返回一个数组，数组的每一个元素对应一个 field 的 value，不存在的 field 对应的元素显示为 nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 field2 var1 命令。 命令示例： EXHMGET myhash field1 field2 返回示例： 1) "10" 2) "var1" |


## EXHMGETWITHVER

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHMGETWITHVER key field [field ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 同时获取 key 指定的 TairHash 多个 field 的值和版本。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在：nil。 key 存在且查询的所有 field 都存在：返回一个数组，数组的每一个元素对应一个 field 的 value 和 version。 key 存在且查询的 field 中有不存在的：返回一个数组，数组的每一个元素对应一个 field 的 value 和 version，不存在的 field 对应的元素显示为 nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 field2 var1 命令。 命令示例： EXHMGETWITHVER myhash field1 field2 返回示例： 1) 1) "10" 2) (integer) 1 2) 1) "var1" 2) (integer) 1 |


## EXHLEN

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHLEN key [NOEXP] |
| 时间复杂度 | 未设置 NOEXP 选项时是 O(1)，设置 NOEXP 选项时是 O(N)。 |
| 命令描述 | 获取 key 指定的 TairHash 中 field 个数，该命令不会触发对过期 field 的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的 field。如果只想返回当前没有过期的 field 个数，可以在命令中设置 NOEXP 选项。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 NOEXP ：该命令默认不会触发对过期 field 的被动淘汰，也不会将其过滤掉，所以结果中可能包含已经过期但还未被删除的 field。如果只想返回当前没有过期的 field 个数，可以在命令中设置 NOEXP 选项。在设置 NOEXP 时： 因为要遍历整条 TairHash 数据， EXHLEN 命令的响应时间将受到 Tairhash 大小的影响。 EXHLEN 命令的返回结果中会过滤掉过期的 field，但过期 field 不会被淘汰。 |
| 返回值 | key 不存在或者 field 不存在：0。 成功：field 个数。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHLEN myhash 返回示例： (integer) 2 |


## EXHEXISTS

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHEXISTS key field |
| 时间复杂度 | O(1) |
| 命令描述 | 查询 key 指定的 TairHash 中是否存在对应的 field。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在或者 field 不存在：0。 field 存在：1。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHEXISTS myhash field1 返回示例： (integer) 1 |


## EXHSTRLEN

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHSTRLEN key field |
| 时间复杂度 | O(1) |
| 命令描述 | 获取 key 指定的 TairHash 中一个 field 对应的 value 的长度。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在或者 field 不存在：0。 查询成功：value 的长度。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHSTRLEN myhash field1 返回示例： (integer) 2 |


## EXHKEYS

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHKEYS key |
| 时间复杂度 | O(N) |
| 命令描述 | 获取 key 指定的 TairHash 中所有的 field。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 |
| 返回值 | key 不存在：返回一个空数组。 key 存在：返回一个数组，数组的每一位对应 TairHash 中的每一个 field。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 field2 var1 命令。 命令示例： EXHKEYS myhash 返回示例： 1) "field1" 2) "field2" |


## EXHVALS

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHVALS key |
| 时间复杂度 | O(N) |
| 命令描述 | 获取 key 指定的 TairHash 中所有 field 的值。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 |
| 返回值 | key 不存在：返回一个空数组。 key 存在：返回一个数组，数组的每个元素对应 TairHash 中的一个 field 的 value。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 field2 var1 命令。 命令示例： EXHVALS myhash 返回示例： 1) "10" 2) "var1" |


## EXHGETALL

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHGETALL key |
| 时间复杂度 | O(N) |
| 命令描述 | 获取 key 指定的 TairHash 中所有 field 及其 value。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 |
| 返回值 | key 不存在：返回一个空数组。 key 存在：返回一个数组，数组的每个元素对应 TairHash 中的一对 field 和 value。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhash field1 10 field2 var1 命令。 命令示例： EXHGETALL myhash 返回示例： 1) "field1" 2) "10" 3) "field2" 4) "var1" |


## EXHSCAN

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
| 语法 | EXHSCAN key op subkey [MATCH pattern] [COUNT count] |
| 时间复杂度 | 每次调用时是 O(1)，遍历整个 TairHash 时是 O(N)。 |
| 命令描述 | 扫描 Key 指定的 TairHash。 说明 仅内存型实例支持该命令。 |
| 选项 | key ：TairHash 的 Key，用于指定作为命令调用对象的 TairHash。 op ：用于定位扫描的起点，可选值如下。 > ：表示从第一个大于 subkey 的 field 开始。 >= ：表示从第一个大于等于 subkey 的 field 开始。 < ：表示从第一个小于 subkey 的 field 开始。 <= ：表示从第一个小于等于 subkey 的 field 开始。 == ：表示从第一个等于 subkey 的 field 开始。 ^ ：表示从第一个 field 开始。 $ ：表示从最后一个 field 开始。 subkey ：用于与 op 选项搭配，设置扫描起始位置，当 op 为^或$时该值将被忽略。 MATCH ：用于过滤扫描结果，根据 MATCH 指定的 pattern 对 subkey 进行正则过滤。 COUNT ：用于规定单次扫描 field 的个数（默认为 10）。 说明 COUNT 仅表示每次扫描 TairHash 的 field 的个数，不代表最终一定会返回 COUNT 个 field 结果集，结果集的大小还要根据 TairHash 中当前 field 个数和是否指定 MATCH 进行过滤而定。 |
| 返回值 | Key 不存在：返回一个空数组。 Key 存在：返回一个具有两个元素的数组： 第一个元素：下一次扫描的起始 field，如果该 Key 已扫描完成，则该元素为空。 第二个元素：本次扫描结果，包含 field 和 value。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 EXHMSET myhashkey field1 val1 field2 val2 field3 val3 field4 val4 field5 val5 命令。 命令示例： EXHSCAN myhashkey ^ xx COUNT 3 返回示例： 1) "field4" 2) 1) "field1" 2) "val1" 3) "field2" 4) "val2" 5) "field3" 6) "val3" |


## EXHDEL

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | EXHDEL key field [field ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 删除 key 指定的 TairHash 中的一个 field，如果 TairHash 不存在或者 field 不存在则返回 0 ，成功删除返回 1。 |
| 选项 | Key ：TairHash 的 key，用于指定作为命令调用对象的 TairHash。 field ：TairHash 中的一个元素，一个 TairHash key 可以有多个 field。 |
| 返回值 | key 不存在或者 field 不存在：0。 删除成功：1。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXHDEL myhash field1 返回示例： (integer) 1 |


## 常见问题

- 

Q：为何写入相同的数据时，exHash的内存占用会高于Redis开源版的普通Hash？

A：这是因为exHash支持对field设置过期时间和版本，因此在其内部数据结构中需要存储更多的元数据信息，从而导致内存占用高于Redis开源版的Hash。

[上一篇：exString](products/redis/documents/developer-reference/tairsting-command.md)[下一篇：exZset](products/redis/documents/developer-reference/tairzset-command.md)

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
