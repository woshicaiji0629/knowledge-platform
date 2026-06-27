## TairString简介
Redis的String仅由key和value组成，而TairString不仅包含key和value，还携带了版本（version），可用于乐观锁等场景。除此之外，TairString在Redis String加减功能的基础上支持了边界设置，可以将INCRBY、INCRBYFLOAT的结果限制在一定的范围内，超出范围则提示错误。
主要特性
value携带版本号。
使用INCRBY、INCRBYFLOAT递增数据时可设置变更范围。
该Module已开源，更多信息请参见[TairString](https://github.com/alibaba/TairString)。
