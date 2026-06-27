## TairHash简介
TairHash不但和Redis Hash一样支持丰富的数据接口和高处理性能，还改变了hash只能为key设置过期时间的限制，可以为field设置过期时间和版本，极大地提高了hash数据结构的灵活性，简化了很多场景下的业务开发工作。TairHash使用高效的Active Expire算法，可以在不对响应时间造成明显影响的前提下，更高效的完成对field的过期判断和删除。
主要特征
field支持单独设置expire和version。
field支持高效灵活的主动、被动过期淘汰（expire）策略。
语法和原生Redis Hash数据类型类似。
该Module已开源，更多信息请参见[TairHash](https://github.com/alibaba/TairHash)。
