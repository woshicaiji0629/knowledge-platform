## 注意事项
操作对象为Tair实例中的TairBloom数据。
提前规划好初始容量与错误率，若目标key的预计容量远大于100，请通过BF.RESERVE创建TairBloom，不建议直接执行BF.ADD命令。
直接执行BF.ADD与执行BF.RESERVE的区别如下。
BF.ADD（或BF.MADD）：执行时若目标key不存在，Tair会自动创建TairBloom，默认容量（capacity）为100，错误率（error_rate）为0.01。若您的容量远远大于100，后续仅能通过扩容增加元素。当TairBloom内部的层数会越来越多，此时会导致完成查询任务需要遍历多层Bloom Filter，性能将严重下降。
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
