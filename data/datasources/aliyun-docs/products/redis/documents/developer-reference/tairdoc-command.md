# Tair文档数据结构命令使用详解-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/developer-reference/tairdoc-command

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

# Doc

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

TairDoc是类似RedisJSON的文档数据结构，支持JSON数据的增删改查。

## TairDoc简介

主要特性

- 

完整地支持JSON标准。

- 

部分兼容[JSONPath](https://datatracker.ietf.org/doc/draft-ietf-jsonpath-base/)RFC draft-4标准。

说明

仅JSON.GET命令支持。

- 

完整地支持[JSONPointer](https://datatracker.ietf.org/doc/html/rfc6901)语法。

- 

文档作为二进制树存储，可以快速访问JSON数据的子元素。

- 

支持JSON到XML或YAML格式的转换。

发布记录

- 

随Tair内存型同时发布TairDoc，支持完整的JSONPointer语法与部分JSONPath语法（仅JSON.GET命令支持JSONPath语法）。

- 

2022年5月17号发布1.8.4版，JSON.GET命令全面支持JSONPath语法，请将小版本升级至1.8.4及以上。

该版本新增支持Dot Wild Card Selector（节点通配符选择器）、Index Selector（索引选择器）与Filter Selector（条件过滤选择器）等。

## 前提条件

实例为Tair[内存型](products/redis/documents/product-overview/dram-based-instances.md)。

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群架构或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

操作对象为Tair实例中的TairDoc数据。

## 命令列表

表 1.TairDoc命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [JSON.SET](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.SET key path json [NX | XX] | 创建 key 并将 JSON 的值存储在对应的 path 中，若 key 及目标 path 已经存在，则更新对应的 JSON 值。 |
| [JSON.GET](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.GET key path [FORMAT XML | YAML] [ROOTNAME root ] [ARRNAME arr ] | 获取目标 key、path 中存储的 JSON 数据。 |
| [JSON.DEL](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.DEL key path | 删除目标 key 中 path 对应的 JSON 数据，若未指定 path，则删除 key。若指定的 key 不存在或 path 不存在，则忽略。 |
| [JSON.TYPE](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.TYPE key path | 获取目标 key 中 path 对应值的类型，结果可能包括 boolean 、 string 、 number 、 array 、 object 、 raw 、 reference 、 const 、 null 等。 |
| [JSON.MERGE](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.MERGE key path value | 将 value 的 JSON 合并到指定 Key 的 path 路径中。可对目标路径下的值实现新增、更新、删除等操作。 |
| [JSON.NUMINCRBY](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.NUMINCRBY key path value | 对目标 key 中 path 对应的值增加 value，path 对应的值和待增加的 value 必须是 int 或 double 类型。 |
| [JSON.STRAPPEND](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.STRAPPEND key path json-string | 在指定 path 对应值中添加 json-string 字符串，path 对应值的类型也需要为字符串。 |
| [JSON.STRLEN](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.STRLEN key path | 获取目标 key 中 path 对应值的字符串长度，path 对应值的类型需要为字符串。 |
| [JSON.ARRAPPEND](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.ARRAPPEND key path json [ json ...] | 在指定 path 对应数组（array）的末尾添加 JSON 数据，支持添加多个 JSON。 |
| [JSON.ARRPOP](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.ARRPOP key path [ index ] | 移除并返回 path 对应数组（array）中指定位置（index）的元素。 |
| [JSON.ARRINSERT](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.ARRINSERT key path [ index ] json [ json ...] | 将 JSON 插入到 path 对应的数组（array）中，原有元素会往后移动。 |
| [JSON.ARRLEN](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.ARRLEN key path | 获取 path 对应数组（array）的长度。 |
| [JSON.ARRTRIM](products/redis/documents/developer-reference/tairdoc-command.md) | JSON.ARRTRIM key path start stop | 修剪目标 key 的 path 对应的数组（array），保留 start 至 stop 范围内的数据。 |
| [DEL](https://valkey.io/commands/del/) | DEL <key> [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairDoc 数据。 |


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

## JSON.SET

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
| 语法 | JSON.SET key path json [NX | XX] |
| 时间复杂度 | O(N) |
| 命令描述 | 创建 key 并将 JSON 的值存储在对应的 path 中，若 key 及目标 path 已经存在，则更新对应的 JSON 值。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path，根元素支持 . 或 $ 。 json ：待新增或更新的 JSON 数据。 NX ：当 path 不存在时写入。 XX ：当 path 存在时写入。 |
| 返回值 | 执行成功：OK。 指定了 XX 且 path 不存在：nil。 指定了 NX 且 path 已存在：nil。 若返回 ERR could not find object to add, please check path ：表示您输入的 path 有误。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： JSON.SET doc $ '{ "store": { "book": [ { "category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95 }, { "category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99 }, { "category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99 }, { "category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99 } ], "bicycle": { "color": "red", "price": 19.95 } } }' 返回示例： OK |


## JSON.GET

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.GET key path [FORMAT XML | YAML] [ROOTNAME root ] [ARRNAME arr ] |
| 时间复杂度 | O(N) |
| 命令描述 | 获取目标 key、path 中存储的 JSON 数据。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path，支持 JSONPath 与 JSON 语法，按需灵活地查询，更多信息请参见 [JSONPath](products/redis/documents/developer-reference/tairdoc-command.md) [介绍](products/redis/documents/developer-reference/tairdoc-command.md) 和 [JSONPointer](products/redis/documents/developer-reference/tairdoc-command.md) [介绍](products/redis/documents/developer-reference/tairdoc-command.md) 。 FORMAT ：指定返回的 JSON 格式，支持 XML、YAML 格式。 ROOTNAME ：指定 XML 语法 ROOT 元素的标签。 ARRNAME ：指定 XML 语法 ARRAY 元素的标签。 说明 ROOTNAME 与 ARRNAME 参数需在指定 FORMAT 参数为 XML 时配合使用。 |
| 返回值 | 执行成功：对应的 JSON 数据。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.GET doc . FORMAT XML ROOTNAME ROOT ARRNAME ARR 返回示例： "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ROOT><foo>bar</foo><baz>42</baz></ROOT>" |


## JSON.DEL

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.DEL key path |
| 时间复杂度 | O(N) |
| 命令描述 | 删除目标 key 中 path 对应的 JSON 数据，若未指定 path，则删除 key。若指定的 key 不存在或 path 不存在，则忽略。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 |
| 返回值 | 执行成功：1。 执行失败：0。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.DEL doc .foo 返回示例： (integer) 1 |


## JSON.TYPE

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.TYPE key path |
| 时间复杂度 | O(N) |
| 命令描述 | 获取目标 key 中 path 对应值的类型，结果可能包括 boolean 、 string 、 number 、 array 、 object 、 raw 、 reference 、 const 、 null 等。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 |
| 返回值 | 执行成功：返回查询到的类型。 执行失败：0。 若 key 或 path 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.TYPE doc .foo 返回示例： string |


## JSON.MERGE

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.MERGE key path value |
| 时间复杂度 | O(N) |
| 命令描述 | 将 value 的 JSON 合并到指定 Key 的 path 路径中。可对目标路径下的值实现新增、更新、删除等操作。 |
| 选项 | key ：TairDoc 的 Key，用于指定作为命令调用对象的 TairDoc。 path ：目标 Key 的 path，支持部分 JSONPath 语法，例如 $.a.b.c 、 $.a['b'] ，但不支持 $.. 、 $* 等复杂表达式。 value ：待合并的 Json，格式兼容 [Json Merge Patch RFC7386](https://datatracker.ietf.org/doc/html/rfc7386) 。 |
| 返回值 | 执行成功：OK。 若 value 有误：parse merge patch error。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc $ '{"f1": {"a":1}, "f2":{"a":2}}' 命令。 命令示例： JSON.MERGE doc $ '{"f1": null, "f2":{"a":3, "b":4}, "f3":[2,4,6]}' 返回示例： OK 此时，执行 JSON.GET doc . 的结果如下： "{\"f2\":{\"a\":3,\"b\":4},\"f3\":[2,4,6]}" |


## JSON.NUMINCRBY

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.NUMINCRBY key path value |
| 时间复杂度 | O(N) |
| 命令描述 | 对目标 key 中 path 对应的值增加 value，path 对应的值和待增加的 value 必须是 int 或 double 类型。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 value ：待增加的数值。 |
| 返回值 | 执行成功：返回操作完成后 path 对应的值。 若 key 或 path 不存在：error。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.NUMINCRBY doc .baz 10 返回示例： "52" |


## JSON.STRAPPEND

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.STRAPPEND key path json-string |
| 时间复杂度 | O(N) |
| 命令描述 | 在指定 path 对应值中添加 json-string 字符串，path 对应值的类型也需要为字符串。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 json-string ：待添加到 path 对应值的字符串。 |
| 返回值 | 执行成功：返回操作完成后 path 对应值的字符串长度。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.STRAPPEND doc .foo rrrrr 返回示例： (integer) 8 |


## JSON.STRLEN

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.STRLEN key path |
| 时间复杂度 | O(N) |
| 命令描述 | 获取目标 key 中 path 对应值的字符串长度，path 对应值的类型需要为字符串。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 |
| 返回值 | 执行成功：返回 path 对应值的字符串长度。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.STRLEN doc .foo 返回示例： (integer) 3 |


## JSON.ARRAPPEND

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRAPPEND key path json [ json ...] |
| 时间复杂度 | O(M*N)，M 是需要插入的元素（json）数量，N 是数组元素数量。 |
| 命令描述 | 在指定 path 对应数组（array）的末尾添加 JSON 数据，支持添加多个 JSON。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 json ：需要插入的数据。 |
| 返回值 | 执行成功：返回操作完成后数组（array）中的元素数量。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRAPPEND doc .id null false true 返回示例： (integer) 6 |


## JSON.ARRPOP

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRPOP key path [ index ] |
| 时间复杂度 | O(M*N)，M 是 key 包含的子元素，N 是数组元素数量。 |
| 命令描述 | 移除并返回 path 对应数组（array）中指定位置（index）的元素。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 index ：数组的索引，起始下标为 0，负数表示反向取值，若不传该参数默认为最后一个元素。 |
| 返回值 | 执行成功：移除并返回该元素。 数组为空数组：‘ERR array index outflow’。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRPOP doc .id 0 返回示例： "1" |


## JSON.ARRINSERT

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRINSERT key path [ index ] json [ json ...] |
| 时间复杂度 | O(M*N)，M 是要插入的元素（json）数量，N 是数组元素数量。 |
| 命令描述 | 将 JSON 插入到 path 对应的数组（array）中，原有元素会往后移动。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 index ：数组的索引，起始下标为 0，负数表示反向取值，若不传该参数默认为最后一个元素。 json ：需要插入的数据。 |
| 返回值 | 执行成功：返回操作完成后数组（array）中的元素数量。 数组为空数组：‘ERR array index outflow’。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRINSERT doc .id 0 10 15 返回示例： (integer) 5 |


## JSON.ARRLEN

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRLEN key path |
| 时间复杂度 | O(N) |
| 命令描述 | 获取 path 对应数组（array）的长度。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 |
| 返回值 | 执行成功：数组（array）的长度。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRLEN doc .id 返回示例： (integer) 3 |


## JSON.ARRTRIM

- 

- 

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRTRIM key path start stop |
| 时间复杂度 | O(N) |
| 命令描述 | 修剪目标 key 的 path 对应的数组（array），保留 start 至 stop 范围内的数据。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 start ：修剪的开始位置，取值为从 0 开始的一个索引值，修剪后的数组包含该位置的元素。 stop ：修剪的结束位置，取值为从 0 开始的一个索引值，修剪后的数组包含该位置的元素。 |
| 返回值 | 执行成功：返回操作完成后数组的长度。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3,4,5,6]}' 命令。 命令示例： JSON.ARRTRIM doc .id 3 4 返回示例： (integer) 2 |


## JSONPath介绍

TairDoc支持[JSONPath](https://datatracker.ietf.org/doc/draft-ietf-jsonpath-base/)的兼容语法如下表所示：

| JSONPath | 说明 |
| --- | --- |
| $ | 根元素。 |
| @ | 当前元素。 |
| .name | 子元素。 |
| .. | 任意位置符合要求的元素。 |
| * | 通配符，表示所有子元素或数组元素。 |
| [ ] | 数组索引，索引从 0 开始，例如[0]；支持选择列表，例如[0,1]，表示 0 和 1；也支持添加元素名，例如['name']。 |
| [start:end:step] | 数组切片选择器（Array Slice Selector），表示从 start 开始，到 end 结束，按照 step 为步长来获取元素，例如[0:3:1]，表示从第 0 位到第 3 位。若步长为负数，则从后向前获取。 |
| ?... | 条件过滤选择器。 |
| () | 支持表达式，优先级为： ( ) > && > || ，更多信息，请参见 [JSONPath](https://datatracker.ietf.org/doc/draft-ietf-jsonpath-base/) 。 |


查询示例

- 

创建JSON文档。

命令实例：

JSON.SET dockey $ '{ "store": { "book": [{ "category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95 }, { "category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99 }, { "category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99 }, { "category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99 } ], "bicycle": { "color": "red", "price": 19.95 } }, "expensive": 10 }'

预计返回：

OK

- 

查询文档。

查询示例如下：

## Root Selector

# 查询整个JSON对象。 JSON.GET dockey $ # 预期输出： "[{"store":{"book":[{"category":"reference","author":"Nigel Rees","title":"Sayings of the Century","price":8.95},{"category":"fiction","author":"Evelyn Waugh","title":"Sword of Honour","price":12.99},{"category":"fiction","author":"Herman Melville","title":"Moby Dick","isbn":"0-553-21311-3","price":8.99},{"category":"fiction","author":"J. R. R. Tolkien","title":"The Lord of the Rings","isbn":"0-395-19395-8","price":22.99}],"bicycle":{"color":"red","price":19.95}}}]"

## Dot Selector

# 查询store中bicycle的所有信息。 JSON.GET dockey $.store.bicycle.* # 预期输出： "["red",19.95]" # 查询store中bicycle的price信息。 JSON.GET dockey $.store.bicycle.price # 预期输出： "[19.95]"

## Index Selector

# 查询store中第一本book的所有信息。 JSON.GET dockey $.store.book[0] # 预期输出： "[{"category":"reference","author":"Nigel Rees","title":"Sayings of the Century","price":8.95}]" # 查询store中所有book的title信息。 JSON.GET dockey "$.store.book[*]['title']" # 预期输出： "["Sayings of the Century","Sword of Honour","Moby Dick","The Lord of the Rings"]"

## Array Slice Selector

# 使用数组分片的方式查询book中第1至第3本书的所有信息，步长为1。 JSON.GET dockey $.store.book[0:2:1] # 预期输出： "[{"category":"reference","author":"Nigel Rees","title":"Sayings of the Century","price":8.95},{"category":"fiction","author":"Herman Melville","title":"Moby Dick","isbn":"0-553-21311-3","price":8.99},{"category":"fiction","author":"Evelyn Waugh","title":"Sword of Honour","price":12.99}]"

## Descendant Selector

# 查询store中所有price信息，包含book和bicycle的price信息。 JSON.GET dockey $..price # 预期输出： "[8.95,12.99,8.99,22.99,19.95]"

## List Selector

# # 查询store中第一本和第三本book的所有信息。 JSON.GET dockey $.store.book[0,2] # 预期输出： "[{"category":"reference","author":"Nigel Rees","title":"Sayings of the Century","price":8.95},{"category":"fiction","author":"Herman Melville","title":"Moby Dick","isbn":"0-553-21311-3","price":8.99}]"

## Filter Selector

# @表达式 # 查询store中book中包含isbn元素的信息。 JSON.GET dockey $.store.book[?(@.isbn)] # 预期输出： "[{"category":"fiction","author":"Herman Melville","title":"Moby Dick","isbn":"0-553-21311-3","price":8.99},{"category":"fiction","author":"J. R. R. Tolkien","title":"The Lord of the Rings","isbn":"0-395-19395-8","price":22.99}]" # COMP表达式 # 查询store中price小于10的book信息。 JSON.GET dockey '$.store.book[?(@.price < 10)]' # 预期输出： "[{"category":"reference","author":"Nigel Rees","title":"Sayings of the Century","price":8.95},{"category":"fiction","author":"Herman Melville","title":"Moby Dick","isbn":"0-553-21311-3","price":8.99}]" # 组合表达式 # 查询目标book信息，条件为price为12.99或者price比bicycle的price贵或者category为reference。 JSON.GET dockey "$..book[?((@.price == 12.99 || @.price > $.store.bicycle.price) || @.category == 'reference')]" # 预期输出： "[{"category":"reference","author":"Nigel Rees","title":"Sayings of the Century","price":8.95},{"category":"fiction","author":"J. R. R. Tolkien","title":"The Lord of the Rings","isbn":"0-395-19395-8","price":22.99},{"category":"fiction","author":"Evelyn Waugh","title":"Sword of Honour","price":12.99}]"

## JSONPointer介绍

TairDoc支持完整的JSONPointer语法，更多信息，请参见[JavaScript Object Notation (JSON) Pointer](https://datatracker.ietf.org/doc/html/rfc6901)。

示例如下。

提前执行JSON.SET doc . '{"foo": "bar", "baz" : [1,2,3]}'命令。

命令示例：

# 获取doc中.baz的第一个值。 JSON.GET doc /baz/0

返回示例：

"1"

[上一篇：Bloom](products/redis/documents/developer-reference/tairbloom-command.md)[下一篇：TS](products/redis/documents/developer-reference/the-tickets-command.md)

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
