# 什么是Tair扩展数据结构TairZset-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/developer-reference/tairzset-command

# exZset
通过TairZset（exZset）可实现256维度的double类型的分值排序，适用于游戏、直播、音乐、电商等行业的排行榜场景，可极大提升数据处理效率，且客户端适配简易，无需任何编解码封装。
## TairZset简介
原生Redis支持的排序结构Sorted Set（也称Zset）只支持1个double类型的分值排序，实现多维度排序时较为困难。例如通过IEEE 754结合拼接的方式实现多维度排序，此类方式存在实现复杂、精度下降、EXZINCRBY命令无法使用等局限性。
借助阿里云自研的TairZset数据结构，可帮助您轻松实现多维度排序能力，相较于传统方案具有如下优势：
最大支持256维的double类型的分值排序（排序优先级为从左往右）。
对于多维score而言，左边的score优先级大于右边的score，以一个三维score为例：score1#score2#score3，TairZset在比较时，会先比较score1，只有score1相等时才会比较score2，否则就以score1的比较结果作为整个score的比较结果。同样，只有当score2相等时才会比较score3。若所有维度分数都相同，则会按照元素顺序（ascii顺序）进行排序。
为了方便理解，可以把#想象成小数点（.），例如0#99、99#90和99#99大小关系可以理解为0.99 < 99.90 < 99.99，即0#99 < 99#90 < 99#99。
支持EXZINCRBY命令，不再需要取回当前数据，在本地增加值后再拼接写回Tair。
支持和原生Zset相似的API。
提供普通排行榜和分布式架构排行榜的能力。
提供开源[TairJedis](https://github.com/aliyun/alibabacloud-tairjedis-sdk)[客户端](https://github.com/aliyun/alibabacloud-tairjedis-sdk)，无需任何编解码封装，您也可以参考开源自行实现封装其他语言版本。
典型场景
适用于游戏、直播、音乐、电商等行业的排行榜场景，例如：
直播排行榜：直播PK中，主播之间先按照当前人气值排序；如果人气值相同，再按照点赞数排序；如果点赞数也相同，再按照礼物金额进行排序等。
奖牌排行榜：从金、银、铜牌的维度对参赛方进行排名，先按照金牌数量排序；如果金牌数量一致，再以银牌数量排序；如果银牌数量也一致，再按照铜牌数量排序。
游戏排行榜：玩家之间按照得分、任务完成时长、段位等多个维度进行排名。
该Module已开源，更多信息请参见[TairZset](https://github.com/alibaba/TairZset)。
## 最佳实践
[基于](../use-cases/tair-multidimensional-and-distributed-ranking-scheme.md)[exZset](../use-cases/tair-multidimensional-and-distributed-ranking-scheme.md)[轻松实现多维排行榜](../use-cases/tair-multidimensional-and-distributed-ranking-scheme.md)
[基于](../use-cases/implementation-of-distributed-architecture-ranking-list-based-on-tairzset.md)[exZset](../use-cases/implementation-of-distributed-architecture-ranking-list-based-on-tairzset.md)[实现分布式架构排行榜](../use-cases/implementation-of-distributed-architecture-ranking-list-based-on-tairzset.md)
## 前提条件
实例为Tair[内存型](../product-overview/dram-based-instances.md)。若实例为内存型（兼容Redis 5.0），则需要小版本为1.7.1及以上。
说明
最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](../user-guide/update-the-minor-version.md)。如果您的实例为集群实例或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。
## 注意事项
操作对象为Tair实例中的TairZset数据。
## 命令列表
| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [EXZADD](tairzset-command.md) | EXZADD key [NX|XX] [CH] [INCR] score member [score member ...] | 将指定的分数与成员信息存储到 TairZset 结构的 Key 中，支持指定多个分数与成员。 说明 如需实现多维度的排序，各维度的分数之间使用井号（#）分隔，例如 111#222#121 ，且要求该 Key 中所有成员的分数格式必须相同。 |
| [EXZINCRBY](tairzset-command.md) | EXZINCRBY key increment member | 为 Key（TairZset 数据结构）中的成员增加分数， increment 为要增加的分数值。 |
| [EXZSCORE](tairzset-command.md) | EXZSCORE key member | 返回存储在 Key（TairZset 数据结构）中成员的分数，如果 Key 或 Key 中的成员不存在，系统会返回 nil。 |
| [EXZRANGE](tairzset-command.md) | EXZRANGE key min max [WITHSCORES] | 返回存储在 Key（TairZset 数据结构）中指定范围的元素。 |
| [EXZREVRANGE](tairzset-command.md) | EXZREVRANGE key min max [WITHSCORES] | 返回存储在 Key（TairZset 数据结构）中指定范围内的元素，元素按分值从高到低的顺序排列，按字典序降序排列分数相同的元素。 说明 除排序方式相反外，本命令和 [EXZRANGE](tairzset-command.md) 用法相似。 |
| [EXZRANGEBYSCORE](tairzset-command.md) | EXZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count] | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素，返回元素按分数从低到高排列，分数相同的元素按照字典顺序返回。 |
| [EXZREVRANGEBYSCORE](tairzset-command.md) | EXZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count] | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素。和 TairZset 中元素默认排序相反，该命令返回元素按照分数从高到低排列，分数相同的元素按照逆字典序排列。 说明 除排序方式相反外，本命令和 [EXZRANGEBYSCORE](tairzset-command.md) 用法相似，注意本命令中 max 在前。 |
| [EXZRANGEBYLEX](tairzset-command.md) | EXZRANGEBYLEX key min max [LIMIT offset count] | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令返回存储在 Key 中介于 min 和 max 值之间的元素。 |
| [EXZREVRANGEBYLEX](tairzset-command.md) | EXZREVRANGEBYLEX key max min [LIMIT offset count] | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令返回存储在 Key 中介于 max 和 min 之间的元素。 说明 除排序方式相反外，本命令和 [EXZRANGEBYLEX](tairzset-command.md) 用法相同，注意本命令中 max 在前。 |
| [EXZREM](tairzset-command.md) | EXZREM key member [member ...] | 移除存储 Key 中的指定成员，如果指定成员不存在，则忽略。 |
| [EXZREMRANGEBYSCORE](tairzset-command.md) | EXZREMRANGEBYSCORE key min max | 移除存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的元素。 |
| [EXZREMRANGEBYRANK](tairzset-command.md) | EXZREMRANGEBYRANK key start stop | 移除存储在 Key（TairZset 数据结构）中，级别介于 start 和 stop 之间的元素。 |
| [EXZREMRANGEBYLEX](tairzset-command.md) | EXZREMRANGEBYLEX key min max | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令移除存储在 Key 中介于 max 和 min 之间的元素。 说明 若使用相同的 min 和 max 参数值执行该命令和 [EXZRANGEBYLEX](tairzset-command.md) 命令，则该命令移除的元素与 EXZRANGEBYLEX 命令返回的元素相同。 |
| [EXZCARD](tairzset-command.md) | EXZCARD key | 返回存储在 Key（TairZset 数据结构）中的基数（即元素的个数）。 |
| [EXZRANK](tairzset-command.md) | EXZRANK key member | 返回存储在 Key（TairZset 数据结构）中的成员的级别，按照分数由低到高排列。 级别（或索引）从 0 开始计数，即分数最低的成员的级别为 0。 |
| [EXZREVRANK](tairzset-command.md) | EXZREVRANK key member | 返回存储在 Key（TairZset 数据结构）中的成员的级别。返回结果按照分数从高到低排列。 级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 除排序规则相反外，本命令和 [EXZRANK](tairzset-command.md) 用法类似。 |
| [EXZCOUNT](tairzset-command.md) | EXZCOUNT key min max | 返回存储在 Key（TairZset 数据结构）中，分数介于 min 和 max 之间的元素的个数。 |
| [EXZLEXCOUNT](tairzset-command.md) | EXZLEXCOUNT key min max | 为确保元素按照字典序排列，若 Key 中所有元素分数相同，则该命令返回存储在 Key，值介于 min 和 max 之间的元素的数量。 |
| [EXZRANKBYSCORE](tairzset-command.md) | EXZRANKBYSCORE key score | 计算指定的分数在 Key（TairZset 数据结构）中按照分数从低到高排序的排名位置。级别（或索引）从 0 开始计数，即分数最低的成员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之前。 |
| [EXZREVRANKBYSCORE](tairzset-command.md) | EXZREVRANKBYSCORE key score | 计算指定的分数在 Key（TairZset 数据结构）中按照分数从高到低排序的排名位置。级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之后。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairZset 数据。 |
说明
本文的命令语法定义如下：
大写关键字：命令关键字。
斜体：变量。
[options]：可选参数，不在括号中的参数为必选。
A|B：该组参数互斥，请进行二选一或多选一。
...：前面的内容可重复。
## EXZADD
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZADD key [NX|XX] [CH] [INCR] score member [score member ...] |
| 时间复杂度 | O(N) |
| 命令描述 | 将指定的分数与成员信息存储到 TairZset 结构的 Key 中，支持指定多个分数与成员，系统会根据 Key 和成员是否存在，执行不同的策略： 如果指定 Key 或 member 不存在，系统将新建并插入分数。 如果指定 Key 或 member 已存在，系统将更新（覆盖）分数。 每个分数值使用双精度浮点数的字符串表示，+inf 和-inf 值都是有效值。 说明 如需实现多维度的排序，各维度的分数之间使用井号（#）分隔，例如 111#222#121 ，且要求该 Key 中所有成员的分数格式必须相同。 |
| 选项 | NX ：只添加新元素，不更新已经存在的元素。 XX ：只更新已经存在的元素，不添加新的元素。 CH ：一般情况下，本命令的返回值为添加的新元素数量，通过该参数可以将返回值改为发生变化的元素总数。 说明 发生变化的元素包含新元素和分数有更新的已有元素。 因此，如果命令行中已存在的一个元素的分数没有发生变化，则该元素不算作发生变化的元素。 INCR ：指定此选项时，EXZADD 的行为与 [EXZINCRBY](tairzset-command.md) 类似，即该模式下仅支持指定一对分数与元素。 |
| 返回值 | 返回值为整数数字，具体为： 未指定任何选项时，返回值为添加到 Key 中的元素数量（不包括仅更新分数的元素）。 指定了 CH 选项时，返回值为发生变化的（新增或更新）元素数量。 指定了 INCR 选项时，则返回值为成员的新分数（字符串形式）。如果使用了多维度分数，则该成员分数的格式为 "分数 1#分数 2#分数 3#..." ，例如 2#0#6 。 说明 如果停止该操作（命令中包含 XX 或 NX 选项），则返回 nil。 |
| 示例 | 命令示例： EXZADD testkey NX 1#0#3 a 1#0#2 b 返回示例： (integer) 2 |
## EXZINCRBY
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZINCRBY key increment member |
| 时间复杂度 | O(log(N)) |
| 命令描述 | 为 Key（TairZset 数据结构）中的成员增加分数， increment 为要增加的分数值，系统会根据 Key 和成员是否存在，执行不同的策略： 如果指定 Key 或 member 不存在，系统将新建并插入分数。 如果指定 Key 或 member 已存在，系统将更新（增加）分数。 每个分数值使用双精度浮点数的字符串表示，+inf 和-inf 值都是有效值。 说明 如需实现多维度的排序，各维度的分数之间使用井号（#）分隔，例如 111#222#121 ，且要求该 Key 中所有成员的分数格式必须相同。 分数值应为数字值的字符串形式，可以为双精度浮点数。 如果需要降低成员的分数，则指定一个负数。 |
| 选项 | 无 |
| 返回值 | 返回成员的新分数（字符串形式），如果使用了多维度分数，则该成员分数的格式为 "分数 1#分数 2#分数 3#..." ，例如 2#0#6 。 |
| 示例 | 命令示例： EXZINCRBY testkey 2#2#1 a 返回示例： "3#2#4" |
## EXZSCORE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZSCORE key member |
| 时间复杂度 | O(1) |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中成员的分数，如果 Key 或 Key 中的成员不存在，系统会返回 nil。 |
| 选项 | 无 |
| 返回值 | 返回成员的分数（字符串形式），如果使用了多维度分数，则该成员分数的格式为 "分数 1#分数 2#分数 3#..." ，例如 2#0#6 。 |
| 示例 | 命令示例： EXZSCORE testkey a 返回示例： "3#2#4" |
## EXZRANGE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZRANGE key min max [WITHSCORES] |
| 时间复杂度 | O(log(N)+M)，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中指定范围的元素。 |
| 选项 | min 、 max ：代表基于 0 的索引值。其中，第一个元素的索引值为 0，第二个元素的索引值为 1，依此类推。 可使用这两个参数指定一个闭区间。 说明 如果索引值为负数，则表示返回的元素末尾往前偏移的量。比如，-1 代表 Key 的最后一个元素，-2 代表倒数第二个元素，依此类推。 如需查询所有的元素信息， min 取值为 0， max 取值为-1。 如果 min 的值比 Key 中最后一个元素的索引值或 max 的值更大，则返回空列表。 WITHSCORES ：返回值中包含元素的分数，即返回列表的数据格式为 值 1，分数 1，...，值 N，分数 N ，例如： 1) "b" 2) "1#0#2" 3) "a" 4) "3#2#4" |
| 返回值 | 返回指定范围内元素的列表，如果使用了 WITHSCORES 选项，则返回结果中包含元素的分数。 |
| 示例 | 命令示例： EXZRANGE testkey 0 -1 WITHSCORES 返回示例： 1) "b" 2) "1#0#2" 3) "a" 4) "3#2#4" |
## EXZREVRANGE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANGE key min max [WITHSCORES] |
| 时间复杂度 | O(log(N)+M)，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中指定范围内的元素，元素按分值从高到低的顺序排列，按字典序降序排列分数相同的元素。 说明 除排序方式相反外，本命令和 [EXZRANGE](tairzset-command.md) 用法相似。 |
| 选项 | min 、 max ：代表基于 0 的索引值。其中，第一个元素的索引值为 0，第二个元素的索引值为 1，依此类推。 可使用这两个参数指定一个闭区间。 说明 如果索引值为负数，则表示返回的元素末尾往前偏移的量。比如，-1 代表 Key 的最后一个元素，-2 代表倒数第二个元素，依此类推。 如需查询所有的元素信息， min 取值为 0， max 取值为-1。 如果 min 的值比 Key 中最后一个元素的索引值或 max 的值更大，则返回空列表。 WITHSCORES ：返回值中包含元素的分数，即返回列表的数据格式为 值 1，分数 1，...，值 N，分数 N ，例如： 1) "b" 2) "1#0#2" 3) "a" 4) "3#2#4" |
| 返回值 | 返回指定范围内的元素列表，如果使用了 WITHSCORES 选项，则返回结果中包含元素的分数。 |
| 示例 | 命令示例： EXZREVRANGE testkey 0 -1 WITHSCORES 返回示例： 1) "a" 2) "3#2#4" 3) "b" 4) "1#0#2" |
## EXZRANGEBYSCORE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count] |
| 时间复杂度 | O(log(N)+M)，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 说明 当 M 为常量时（例如使用 LIMIT 选项指定总是返回前 10 个元素时），可将该公式看作 O(log(N))。 |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素，返回元素按分数从低到高排列，分数相同的元素按照字典顺序返回。 |
| 选项 | min 、 max ：分别表示最小分数和最大分数，如 Key 中的元素采用了多维度的分数，各维度的分数之间使用井号（#）分隔。 说明 在不确定 Key 中元素的最高分和最低分的情况下，如果想要查询 Key 中分数大于等于或小于等于某一特定值的元素，请将 min 和 max 分别设置为负无穷大（ -inf ）和正无穷大（ +inf ）。 默认数据范围为闭区间，如需指定开区间，则在分数范围前添加半角圆括号，例如 (1 5 表示返回分数大于 1 且小于等于 5 的元素。 WITHSCORES ：返回值中包含元素的分数。 LIMIT offset count ：指定返回结果的数量及区间，如果 count 为负数，则返回从 offset 开始的所有元素。 说明 如果 offset 较大，则需要遍历整个 Key 以定位到 offset 元素，然后才能返回元素，即会增加时间复杂度。 |
| 返回值 | 返回指定分数范围内的元素列表，如果使用了 WITHSCORES 选项，则返回结果中包含元素的分数。 |
| 命令示例 | 命令示例： EXZRANGEBYSCORE testkey 0#0#0 6#6#6 WITHSCORES 返回示例： 1) "b" 2) "1#0#2" 3) "a" 4) "3#2#4" |
## EXZREVRANGEBYSCORE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANGEBYSCORE key max min [WITHSCORES] [LIMIT offset count] |
| 时间复杂度 | O(log(N)+M) ，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 说明 当 M 为常量时（比如使用 LIMIT 选项指定总是返回前 10 个元素时），可将该公式看作 O(log(N))。 |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的所有元素。和 TairZset 中元素默认排序相反，该命令返回元素按照分数从高到低排列，分数相同的元素按照逆字典序排列。 说明 除排序方式相反以外，本命令和 [EXZRANGEBYSCORE](tairzset-command.md) 用法相似，注意本命令中 max 在前。 |
| 选项 | min 、 max ：分别表示最小分数和最大分数，如 Key 中的元素采用了多维度的分数，各维度的分数之间使用井号（#）分隔。 说明 在不确定 Key 中元素的最高分和最低分的情况下，如果想要查询 Key 中分数大于等于或小于等于某一特定值的元素，请将 min 和 max 分别设置为负无穷大（ -inf ）和正无穷大（ +inf ）。 默认数据范围为闭区间，如需指定开区间，则在分数范围前添加半角圆括号，例如 (1 5 表示返回分数大于 1 且小于等于 5 的元素。 WITHSCORES ：返回值中包含元素的分数。 LIMIT offset count ：指定返回结果的数量及区间，如果 count 为负数，则返回从 offset 开始的所有元素。 说明 如果 offset 较大，则需要遍历整个 Key 以定位到 offset 元素，然后才能返回元素，即会增加时间复杂度。 |
| 返回值 | 返回指定分数范围内的元素列表，如果使用了 WITHSCORES 选项，则返回结果中包含元素的分数。 |
| 命令示例 | 命令示例： EXZREVRANGEBYSCORE testkey 6#6#6 0#0#0 WITHSCORES 返回示例： 1) "a" 2) "3#2#4" 3) "b" 4) "1#0#2" |
## EXZRANGEBYLEX
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZRANGEBYLEX key min max [LIMIT offset count] |
| 时间复杂度 | O(log(N)+M)，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 说明 当 M 为常量时（例如使用 LIMIT 选项指定返回前 10 个元素时），可将该公式看作 O(log(N))。 |
| 命令描述 | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令返回存储在 Key 中介于 min 和 max 值之间的元素。 说明 如果 Key 中元素分数不同，则返回元素未知。 采用 memcmp() C 函数逐个比对两个元素字符串中的字节。根据比对结果，由低到高排列元素。 若两个字符串包含相同的子字符串，那么字符串越长，其分值越高。 |
| 选项 | min 、 max ：分别表示成员名称的最小值和最大值（字符串形式），需指定字符的区间，例如 开区间：在值的前面增加半角圆括号，例如 (a 。 闭区间：在值的前面增加方括号，例如 [a 说明 正负无穷大分别为 + 和 - 。 LIMIT offset count ：指定返回结果的数量及区间，如果 count 为负数，则返回从 offset 开始的所有元素。 说明 如果 offset 较大，则需要遍历整个 Key 以定位到 offset 元素，然后才能返回元素，即会增加时间复杂度。 |
| 返回值 | 返回元素名称在指定范围内的元素列表。 |
| 命令示例 | 命令示例： EXZRANGEBYLEX zzz [a [b 返回示例： 1) "aba" 2) "abc" |
## EXZREVRANGEBYLEX
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANGEBYLEX key max min [LIMIT offset count] |
| 时间复杂度 | O(log(N)+M)，其中，N 表示 TairZset 中元素的数量，M 表示返回的元素的数量。 说明 当 M 为常量时（例如使用 LIMIT 选项指定总是返回前 10 个元素时），可将该公式看作 O(log(N))。 |
| 命令描述 | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令返回存储在 Key 中介于 max 和 min 之间的元素。 说明 除排序方式相反外，本命令和 [EXZRANGEBYLEX](tairzset-command.md) 用法相同，注意本命令中 max 在前。 |
| 选项 | min 、 max ：分别表示成员名称的最小值和最大值（字符串形式），需指定字符的区间，例如 开区间：在值的前面增加半角圆括号，例如 (a 。 闭区间：在值的前面增加方括号，例如 [a 说明 正负无穷大分别为 + 和 - 。 LIMIT offset count ：指定返回结果的数量及区间，如果 count 为负数，则返回从 offset 开始的所有元素。 说明 如果 offset 较大，则需要遍历整个 Key 以定位到 offset 元素，然后才能返回元素，即会增加时间复杂度。 |
| 返回值 | 返回元素名称在指定范围内的元素列表。 |
| 命令示例 | 命令示例： EXZREVRANGEBYLEX zzz [b [a 返回示例： 1) "abc" 2) "aba" |
## EXZREM
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREM key member [member ...] |
| 时间复杂度 | O(M*log(N))，其中，N 为 TairZset 中元素的数量，M 为待移除的元素的数量。 |
| 命令描述 | 移除存储 Key 中的指定成员，如果指定成员不存在，则忽略。 说明 如果指定的 Key 存在，但其数据结构不是 TairZset，系统将返回错误。 |
| 选项 | 无 |
| 返回值 | 返回 Key 中被移除的成员数量，不包含不存在的成员。 |
| 命令示例 | 命令示例： EXZREM testkey a 返回示例： (integer) 1 |
## EXZREMRANGEBYSCORE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREMRANGEBYSCORE key min max |
| 时间复杂度 | O(log(N)+M)，其中，N 为 TairZset 中元素的数量，M 为待移除的元素的数量。 |
| 命令描述 | 移除存储在 Key（TairZset 数据结构）中，分数大于等于 min 且小于等于 max 值的元素。 |
| 选项 | min 和 max 分别表示最小分数和最大分数，如 Key 中的元素采用了多维度的分数，各维度的分数之间使用井号（#）分隔。 说明 在不确定 Key 中元素的最高分和最低分的情况下，如果想要移除 Key 中分数大于等于或小于等于某一特定值的元素，请将 min 和 max 分别设置为负无穷大（ -inf ）和正无穷大（ +inf ）。 默认数据范围为闭区间，如需指定开区间，则在分数范围前添加半角圆括号，例如 EXZREMRANGEBYSCORE (1 5 表示删除分数大于 1 且小于等于 5 的元素。 |
| 返回值 | 返回被移除的元素的数量。 |
| 命令示例 | 命令示例： EXZREMRANGEBYSCORE testkey 3#2#4 6#6#6 返回示例： (integer) 1 |
## EXZREMRANGEBYRANK
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREMRANGEBYRANK key start stop |
| 时间复杂度 | O(log(N)+M)，其中，N 为 TairZset 中元素的数量，M 为该操作移除的元素的数量。 |
| 命令描述 | 移除存储在 Key（TairZset 数据结构）中，级别介于 start 和 stop 之间的元素。 |
| 选项 | start 和 stop 均为基于零的索引值，其中，0 代表分数最低的元素。 当索引值为负数，代表从最高分数元素开始的偏移量，例如-1 为分数最高的元素，-2 为分数第二高的元素，依此类推。 |
| 返回值 | 被移除的元素的数量。 |
| 命令示例 | 命令示例： EXZREMRANGEBYRANK testkey 0 1EXZREVRANGEBYSCORE 返回示例： (integer) 1 |
## EXZREMRANGEBYLEX
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREMRANGEBYLEX key min max |
| 时间复杂度 | O(log(N)+M)，其中，N 为 TairZset 中元素的数量，M 为该操作移除的元素的数量。 |
| 命令描述 | 为确保元素按照字典序排列，当 Key 中所有元素分数相同时，则该命令移除存储在 Key 中介于 max 和 min 之间的元素。 说明 若使用相同的 min 和 max 参数值执行该命令和 [EXZRANGEBYLEX](tairzset-command.md) 命令，则该命令移除的元素与 EXZRANGEBYLEX 命令返回的元素相同。 |
| 选项 | min 、 max ：分别表示成员名称的最小值和最大值（字符串形式），需指定字符的区间，例如 开区间：在值的前面增加半角圆括号，例如 (a 。 闭区间：在值的前面增加方括号，例如 [a |
| 返回值 | 被移除的元素的数量。 |
| 命令示例 | 命令示例： EXZREMRANGEBYLEX [a [b 返回示例： (integer) 2 |
## EXZCARD
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZCARD key |
| 时间复杂度 | O(1) |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中的基数（即元素的个数）。 |
| 选项 | 无 |
| 返回值 | 返回 Key 中的元素的数量，如果 Key 不存在，则返回 0。 |
| 命令示例 | 命令示例： EXZCARD testkey 返回示例： (integer) 2 |
## EXZRANK
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZRANK key member |
| 时间复杂度 | O(log(N)) |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中的成员的级别，按照分数由低到高排列。 级别（或索引）从 0 开始计数，即分数最低的成员的级别为 0。 |
| 选项 | 无 |
| 返回值 | 当 Key 中存在指定的成员，则返回成员的级别（整数）。 当 Key 或 Key 中的成员不存在，则返回 nil。 |
| 命令示例 | 命令示例： EXZRANK testkey b 返回示例： (integer) 0 |
## EXZREVRANK
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANK key member |
| 时间复杂度 | O(log(N)) |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中的成员的级别。返回结果按照分数从高到低排列。 级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 除排序规则相反外，本命令和 [EXZRANK](tairzset-command.md) 用法类似。 |
| 选项 | 无 |
| 返回值 | 当 Key 中存在指定的成员，则返回成员的级别（整数）。 当 Key 或 Key 中的成员不存在，则返回 nil。 |
| 命令示例 | 命令示例： EXZREVRANK testkey b 返回示例： (integer) 1 |
## EXZCOUNT
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZCOUNT key min max |
| 时间复杂度 | O(log(N))，其中，N 为 TairZset 中元素的数量。 说明 由于采用了元素级别获取查询范围，该操作涉及的工作量和查询范围的大小即不成正比。 |
| 命令描述 | 返回存储在 Key（TairZset 数据结构）中，分数介于 min 和 max 之间的元素的个数。 |
| 选项 | min 、 max ：分别表示最小分数和最大分数，如 Key 中的元素采用了多维度的分数，各维度的分数之间使用井号（#）分隔。 说明 在不确定 Key 中元素的最高分和最低分的情况下，如果想要查询 Key 中分数大于等于或小于等于某一特定值的元素，请将 min 和 max 分别设置为负无穷大和正无穷大。 默认数据范围为闭区间，如需指定开区间，则在分数范围前添加半角圆括号，例如 (1 5 表示返回分数大于 1 且小于等于 5 的元素。 |
| 返回值 | 返回分数在指定范围内的元素的数量（整数）。 |
| 命令示例 | 命令示例： EXZCOUNT testkey (1#0#2 6#6#6 返回示例： (integer) 1 |
## EXZLEXCOUNT
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZLEXCOUNT key min max |
| 时间复杂度 | O(log(N))，其中，N 为 TairZset 中元素的数量。 说明 由于采用了元素级别获取查询范围，该操作涉及的工作量和查询范围的大小即不成正比。 |
| 命令描述 | 为确保元素按照字典序排列，若 Key 中所有元素分数相同，则该命令返回存储在 Key，值介于 min 和 max 之间的元素的数量。 说明 如果 Key 中元素分数不同，则返回元素未知。 采用 memcmp() C 函数逐个比对两个元素字符串中的字节。根据比对结果，由低到高排列元素。 若两个字符串包含相同的子字符串，那么字符串越长，其分值越高。 |
| 选项 | min 、 max ：分别表示成员名称的最小值和最大值（字符串形式），需指定字符的区间，例如 开区间：在值的前面增加半角圆括号，例如 (a 。 闭区间：在值的前面增加方括号，例如 [a |
| 返回值 | 返回分数在指定范围内的元素的个数（整数）。 |
| 命令示例 | 命令示例： EXZLEXCOUNT zzz [a [b 返回示例： (integer) 2 |
## EXZRANKBYSCORE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZRANKBYSCORE key score |
| 时间复杂度 | O(log(N)) |
| 命令描述 | 计算指定的分数在 Key（TairZset 数据结构）中按照分数从低到高排序的排名位置。级别（或索引）从 0 开始计数，即分数最低的成员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之前。 |
| 选项 | 无 |
| 返回值 | 返回指定分数在 Key 中的排名。 |
| 命令示例 | 命令示例： EXZRANKBYSCORE testkey 2#0#2 返回示例： (integer) 1 |
## EXZREVRANKBYSCORE
| 类别 | 说明 |
| --- | --- |
| 语法 | EXZREVRANKBYSCORE key score |
| 时间复杂度 | O(log(N)) |
| 命令描述 | 计算指定的分数在 Key（TairZset 数据结构）中按照分数从高到低排序的排名位置。级别（或索引）从 0 开始计数，即分数最高的成员的级别为 0。 说明 若指定的分数不存在，则返回该分数在 Key（TairZset 数据结构）中的预计排名；若指定的分数已存在，Tair 会默认将指定的分数排在已存在的分数之后。 |
| 选项 | 无 |
| 返回值 | 返回指定分数在 Key 中的排名。 |
| 命令示例 | 命令示例： EXZREVRANKBYSCORE testkey 2#0#2 返回示例： (integer) 1 |
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
