# TairBloom介绍,命令列表-云数据库 Tair（兼容 Redis®）(Tair)-阿里云帮助中心

Source: https://help.aliyun.com/zh/redis/developer-reference/tairbloom-command

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

# Bloom

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/tair)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Bloom是一种概率性数据结构（space-efficient probabilistic data structure），在大规模数据中，仅需消耗较低的内存来判断一个元素是否存在。而TairBloom基于Scalable Bloom Filter实现，具有动态扩容的能力，并且可以在扩容时维持误判率的稳定性。

## TairBloom简介

在传统的Redis数据结构中，可以使用Hash、Set、String的Bitset等实现类似功能，但这些实现方式不是内存占用量非常大，就是无法动态伸缩和保持误判率不变。因此，TairBloom非常适合需要高效判断大量数据是否存在且允许一定误判率的业务场景。业务可以直接使用TairBloom提供的Bloom Filter（布隆过滤器）接口，无需二次封装，更无需在本地实现布隆过滤器的功能。

主要特性

- 

内存占用低。

- 

可动态扩容。

- 

可自定义的误判率（False Positive Rate）且在扩容时保持不变。

典型场景

适用于直播、音乐、电商等行业的推荐系统或爬虫系统等，例如：

- 

推荐系统：将用户读过的文章通过TairBloom记录，并在给用户推荐新文章前进行查询，实现给用户推荐感兴趣，且没读过的文章。

- 

爬虫系统：在面对海量的URL时，将已经爬取过的URL进行过滤、去重操作，减少重复爬取的无效工作量。

最佳实践

## 基于TairBloom打造推荐系统

将已推荐给用户的文章ID通过TairBloom记录，并在推荐新文章前进行查询、判断，轻松实现给用户推荐感兴趣，且未推荐过的文章，伪代码如下：

void recommendedSystem(userid) { while (true) { // 从系统中随机（或者根据用户兴趣）获取一篇文章ID。 docid = getDocByRandom() if (bf.exists(userid, docid)) { // 如果发现可能已向用户推荐过该文章，则推荐下一篇文章。 continue; } else { // 确认未向用户推荐过该文章，则向用户发送推荐。 sendRecommendMsg(docid); // 同时将已推荐的文章ID记录至TairBloom。 bf.add(userid, docid); break; } } }

## 基于TairBloom优化爬虫系统

在面对海量的URL时，将已经爬取过的URL进行过滤、去重操作，减少重复爬取的无效工作量，伪代码如下：

bool crawlerSystem( ) { while (true) { // 获取待爬取的URL。 url = getURLFromQueue() if (bf.exists(url_bloom, url)) { // 如果该URL可能已被爬取，则跳过。 continue; } else { // 爬取该URL内容。 doDownload(url) // 并将该URL加入TairBloom。 bf.add(url_bloom, url); } } }

## 更多最佳实践

- 

[使用](products/redis/documents/use-cases/use-bloom-filter-to-avoid-repeated-push-to-players.md)[Bloom Filter](products/redis/documents/use-cases/use-bloom-filter-to-avoid-repeated-push-to-players.md)[高效管理游戏活动推送](products/redis/documents/use-cases/use-bloom-filter-to-avoid-repeated-push-to-players.md)

## 原理介绍

TairBloom作为一种[Scalable Bloom Filter](https://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf)的实现，具有动态扩容的能力，同时误判率（False Positive Rate）维持不变。而Scalable Bloom Filter是在Bloom Filter的基础上进行优化的，下文将简单介绍Bloom Filter与Scalable Bloom Filter的基本原理。

- 

Bloom Filter

布隆过滤器是一个高空间利用率的概率性数据结构，由Burton Bloom于1970年提出，用于测试一个元素是否在集合中。

新创建的布隆过滤器是一串被置为0的Bit数组（假设有m位），同时声明k个不同的Hash函数生成统一的随机分布（k是一个小于m的常数）。向布隆过滤器中添加元素时，通过k个Hash函数将元素映射到Bit中的k个点，并将这些位置的值设置为1，一个Bit位可能被不同数据共享。下图展示了假设布隆过滤器的k为3，向其插入X1、X2的过程。

查询元素时，仍通过k个Hash函数得到对应的k个位，判断目标位置是否为1，若目标位置全为1则认为该元素在布隆过滤器内，否则认为该元素不存在，下图展示了在布隆过滤器中查询Y1和Y2是否存在的过程。

由上图可以发现，虽然从未向布隆过滤器中插入过Y2这个元素，但是布隆过滤器却判断Y2存在，因此，布隆过滤器是可能存在误判的，即存在假阳性（false positive）。至此，可以得出关于布隆过滤器的几个特性：

- 

Bit位可能被不同数据共享。

- 

存在假阳性（false positive），且布隆过滤器中的元素越多，假阳性的可能性越大，但不存在假阴性（false negative），即不会将存在的元素误判为不存在。

- 

元素可以被加入布隆过滤器，但无法被删除，因为Bit位是可以共享的，删除时有可能会影响到其他元素。

- 

Scalable Bloom Filter

随着布隆过滤器中添加的元素越来越多，误判率也越来越高，若希望误判率稳定不变，需同步增加布隆过滤器的大小，但是布隆过滤器由于结构限制无法进行扩容。因此，Scalable Bloom Filter提出创建新的布隆过滤器，将多个布隆过滤器组装成一个布隆过滤器使用。

下图展示了一个Scalable Bloom Filter的基本模型（下文简称SBF）。该SBF一共包含BF0和BF1两层。在一开始，SBF只包含BF0层，假设在插入a、b、c三个元素后，BF0层已经无法保证用户设定的误判率，此时会创建新的一层（BF1层）进行扩容。因此，后面的d、e、f元素会插入到BF1层中。同理，当BF1层也无法满足误判率时，会创建新的一层（BF2层），如此进行下去。更多信息，请参见[Scalable Bloom Filter](https://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf)。

重要

TairBloom动态扩容时，新一层的元素容量为上一层的两倍，所占用的内存空间是上一层的4倍。

每增加一层，在查询的时候就可能会遍历多层Bloom Filter来完成，这是因为Scalable Bloom Filter只会向最后一层插入数据，也从最后一层开始查询，直到查询至BF0层。因此，TairBloom扩容操作容易产生大Key以及导致性能有所下降，下降的程度是随着元素个数的增长而下降的。

在实际使用过程中请避免发生TairBloom扩容操作，建议将该功能视为一种保障措施。请确保为实例预留足够的内存，以防止在TairBloom扩容后，实例无法写入并触发长时间的数据逐出操作导致实例无法处理请求。您可以通过BF.INFO命令查看Key是否即将触发扩容操作，当最新一层的items（元素数量）等于capacity（容量）时，表示即将触发扩容。

当实际容量超过预设时，TairBloom能够通过扩容操作确保业务正常写入，从而规避线上事故。在TairBloom完成扩容后，建议及时重建，以提升性能并降低下次扩容所带来的风险。

## 前提条件

实例为Tair[内存型](products/redis/documents/product-overview/dram-based-instances.md)。

说明

最新小版本将提供更丰富的功能与稳定的服务，建议将实例的小版本升级到最新，具体操作请参见[升级小版本](products/redis/documents/user-guide/update-the-minor-version.md)。如果您的实例为集群架构或读写分离架构，请将代理节点的小版本也升级到最新，否则可能出现命令无法识别的情况。

## 注意事项

- 

操作对象为Tair实例中的TairBloom数据。

- 

提前规划好初始容量与错误率，若目标key的预计容量远大于100，请通过BF.RESERVE创建TairBloom，不建议直接执行BF.ADD命令。

直接执行BF.ADD与执行BF.RESERVE的区别如下。

- 

BF.ADD（或BF.MADD）：执行时若目标key不存在，Tair会自动创建TairBloom，默认容量（capacity）为100，错误率（error_rate）为0.01。若您的容量远远大于100，后续仅能通过扩容增加元素。当TairBloom内部的层数会越来越多，此时会导致完成查询任务需要遍历多层Bloom Filter，性能将严重下降。

- 

BF.RESERVE（或BF.INSERT）：执行时需要设置capacity（初始容量），该命令会在TairBloom的第一层初始化设置的容量，在TairBloom内部的Bloom Filter层数少，查询速度快。

说明

以插入10,000,000个元素、错误率为0.01为例，直接通过BF.ADD创建，TairBloom需占用176 MB；而通过BF.RESERVE创建时仅占用16 MB。

下表为通过BF.RESERVE创建不同初始容量和错误率的key所占用的内存，仅供参考。

| 容量（元素的个数） | false positive:0.01 | false positive:0.001 | false positive:0.0001 |
| --- | --- | --- | --- |
| 100,000 | 0.12 MB | 0.25 MB | 0.25 MB |
| 1,000,000 | 2 MB | 2 MB | 4 MB |
| 10,000,000 | 16 MB | 32 MB | 32 MB |
| 100,000,000 | 128 MB | 256 MB | 256 MB |
| 1,000,000,000 | 2 GB | 2 GB | 4 GB |


创建超大容量的Key时，您需要关注错误率（error_rate）的精度，超大容量和超高精度的Key可能会因为实例内存不足而导致创建失败。

- 

由于TairBloom只能插入新元素且无法删除已有元素，因此TairBloom的内存占用量只会增加不会减少。为防止TairBloom越来越大，甚至导致Redis内存溢出（Out Of Memory），向您提供如下使用建议。

- 

拆分业务数据：拆分、细化业务数据，避免将大量数据存入一个TairBloom中，这样不仅会导致这个key过大，影响查询性能，同时也会由于这个key中插入了过多数据，大部分的查询流量都会请求到这个key所在的Redis实例上，从而造成热点key，甚至发生访问倾斜的情况。

请拆分业务数据，将数据分散到多个TairBloom中，若您的实例为集群实例，您可以将TairBloom分散到集群内的各个实例上，均衡内存容量与流量，充分发挥分布式集群的优势。

- 

定期重建：如果业务允许，您可以定期重建TairBloom，通过DEL删除TairBloom，从后端数据库拉取数据并重建TairBloom，以控制TairBloom的大小。

您也可以在初期创建多个TairBloom，并采用多个TairBloom轮转切换的方式实现控制单个TairBloom的大小。该方案的优点为仅需创建一次TairBloom，无需频繁地重建TairBloom，缺点是需要创建多个TairBloom，会浪费部分内存空间。

## 命令列表

表 1.TairBloom命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [BF.RESERVE](products/redis/documents/developer-reference/tairbloom-command.md) | BF.RESERVE key error_rate capacity | 创建一个大小为 capacity，错误率为 error_rate 的空的 TairBloom。 |
| [BF.ADD](products/redis/documents/developer-reference/tairbloom-command.md) | BF.ADD key item | 在 Key 指定的 TairBloom 中添加一个元素。 |
| [BF.MADD](products/redis/documents/developer-reference/tairbloom-command.md) | BF.MADD key item [ item ...] | 在 Key 指定的 TairBloom 中添加多个元素。 |
| [BF.EXISTS](products/redis/documents/developer-reference/tairbloom-command.md) | BF.EXISTS key item | 检查一个元素是否存在于 Key 指定的 TairBloom 中。 |
| [BF.MEXISTS](products/redis/documents/developer-reference/tairbloom-command.md) | BF.MEXISTS key item [ item ...] | 同时检查多个元素是否存在于 Key 指定的 TairBloom 中。 |
| [BF.INSERT](products/redis/documents/developer-reference/tairbloom-command.md) | BF.INSERT key [CAPACITY cap ] [ERROR error ] [NOCREATE] ITEMS item [ item ...] | 在 Key 指定的 TairBloom 中一次性添加多个元素，添加时可以指定大小和错误率，且可以控制在 TairBloom 不存在的时候是否自动创建。 |
| [BF.INFO](products/redis/documents/developer-reference/tairbloom-command.md) | BF.INFO key | 查看 Key 指定的 TairBloom 内部信息，如当前层数和每一层的元素个数、错误率等。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairBloom 数据。 说明 已加入 TairBloom 数据中的元素无法单独删除，您可以使用 DEL 命令删除整条 TairBloom 数据。 |


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

## BF.RESERVE

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.RESERVE key error_rate capacity |
| 时间复杂度 | O(1) |
| 命令描述 | 创建一个大小为 capacity，错误率为 error_rate 的空的 TairBloom。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 error_rate ：期望的错误率（False Positive Rate），该值必须介于 0 和 1 之间。该值越小，精度越高，TairBloom 的内存占用量越大，CPU 使用率越高。 capacity ：TairBloom 的初始容量，即期望添加到 TairBloom 中的元素的个数。 当实际添加的元素个数超过该值时，TairBloom 将通过增加 Bloom Filter 的层数完成自动扩容，该过程会导致查询性能下降。每增加一层，就可能需要遍历多层 Bloom Filter 来完成查询。因此，如果对性能非常的敏感，需要在使用前充分评估要添加到 TairBloom 的元素个数，避免发生导致层数增加的扩容操作。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.RESERVE BFKEY 0.01 100 返回示例： OK |


## BF.ADD

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.ADD key item |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 在 Key 指定的 TairBloom 中添加一个元素。 说明 若目标 Key 不存在，Tair 会自动创建一个 TairBloom，创建 TairBloom 的默认容量（capacity）为 100，错误率（error_rate）为 0.01。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 item ：需要添加到 TairBloom 的元素。 |
| 返回值 | 1：表示该元素之前一定不存在，并往 TairBloom 中添加该元素。 0：表示该元素可能已存在，所以不会进行添加或更新操作。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.ADD BFKEY item1 返回示例： (integer) 1 |


## BF.MADD

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.MADD key item [ item ...] |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 在 Key 指定的 TairBloom 中添加多个元素。 说明 若目标 Key 不存在，Tair 会自动创建一个 TairBloom，创建 TairBloom 的默认容量（capacity）为 100，错误率（error_rate）为 0.01。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 item ：需要添加到 TairBloom 的元素，可设置多个。 |
| 返回值 | 1：表示该元素之前一定不存在，并往 TairBloom 中添加该元素。 0：表示该元素可能已存在，所以不会进行添加或更新操作。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.MADD BFKEY item1 item2 item3 返回示例： (integer) 1 (integer) 1 (integer) 1 |


## BF.EXISTS

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.EXISTS key item |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 检查一个元素是否存在于 Key 指定的 TairBloom 中。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 item ：需要查询的元素。 |
| 返回值 | 0：表示该元素一定不存在。 1：表示该元素可能存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.EXISTS BFKEY item1 返回示例： (integer) 1 |


## BF.MEXISTS

- 

- 

- 

- 

- 

| 类别 | 说明 |
| --- | --- |
| 语法 | BF.MEXISTS key item [ item ...] |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 同时检查多个元素是否存在于 Key 指定的 TairBloom 中。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 item ：需要查询的元素，可设置多个。 |
| 返回值 | 0：表示该元素一定不存在。 1：表示该元素可能存在。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.MEXISTS BFKEY item1 item5 返回示例： (integer) 1 (integer) 0 |


## BF.INSERT

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
| 语法 | BF.INSERT key [CAPACITY cap ] [ERROR error ] [NOCREATE] ITEMS item [ item ...] |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 在 Key 指定的 TairBloom 中一次性添加多个元素，添加时可以指定大小和错误率，且可以控制在 TairBloom 不存在的时候是否自动创建。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 capacity ：TairBloom 的初始容量，即期望添加到 TairBloom 中元素的个数，当 TairBloom 已经存在时该值将被忽略。 当实际添加的元素个数超过该值时，TairBloom 将进行自动的扩容。 error_rate ：期望的错误率（False Positive Rate），该值必须介于 0 和 1 之间。该值越小，精度越高，TairBloom 的内存占用量越大，CPU 使用率越高。 NOCREATE ：设置该选项后，当指定的 TairBloom 不存在的时候不要自动创建该 TairBloom。该参数不能与 CAPACITY 和 ERROR 同时设置。 item ：需要添加的元素，可设置多个。 |
| 返回值 | 1：表示该元素之前一定不存在，并往 TairBloom 中添加该元素。 0：表示该元素可能已存在，所以不会进行添加或更新操作。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.INSERT bfkey1 CAPACITY 10000 ERROR 0.001 ITEMS item1 item2 item3 返回示例： (integer) 1 (integer) 1 (integer) 1 |


## BF.INFO

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
| 语法 | BF.INFO key |
| 时间复杂度 | O(log N) ，其中 N 是 TairBloom 的层数。 |
| 命令描述 | 查看 Key 指定的 TairBloom 内部信息，如当前层数和每一层的元素个数、错误率等。 |
| 选项 | Key ：Key 名称（TairBloom 数据结构），用于指定作为命令调用对象的 TairBloom。 |
| 返回值 | 执行成功将返回 TairBloom 信息。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： BF.INFO bk1 返回示例： 1) "total_items:6,num_blooms:2" 2) "bytes:4 bits:32 hashes:7 hashwidth:64 capacity:3 items:3 error_ratio:0.01" 3) "bytes:16 bits:128 hashes:9 hashwidth:64 capacity:10 items:3 error_ratio:0.0025" BF.INFO 返回参数说明： total_items 表示总元素数量、num_blooms 表示总 Bloom Filter 层数。 每层 Bloom Filter 的信息： bytes：占用字节数。 bits：占用 bit 位数，bits = bytes * 8。 hashes：Hash 函数数量。 hashwidth：Hash 函数宽度。 capacity：容量。 items：元素数量。 error_ratio：错误率。 |


[上一篇：GIS](products/redis/documents/developer-reference/tairgis-command.md)[下一篇：Doc](products/redis/documents/developer-reference/tairdoc-command.md)

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
