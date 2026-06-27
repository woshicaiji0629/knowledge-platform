## 分析能力
分析能力是基于指标、日志、链路追踪三大基础数据进行的信息聚合，是云数据库 Tair（兼容 Redis）重要的服务能力。
热Key与大Key分析
当某个Key接收的访问次数显著高于其它Key时，可以将其称为热Key（Hotkeys），若未能及时处理热Key可能会导致访问倾斜甚至缓存击穿等问题；当某个Key含有较多数据成员或者占用较大内存时，可以将其称为大Key（Big keys），若未能及时处理大Key会导致执行命令的耗时增加，严重时甚至引发内存溢出（Out Of Memory）。
您可以通过云数据库 Tair（兼容 Redis）的实时Top Key统计功能，帮助定位热Key与大Key，实时Top Key统计功能支持实时展示实例中的热Key和大Key信息，同时支持查看4天内大Key和热Key的历史信息。实时Top Key统计功能准确性高，且对性能几乎无影响，帮助您掌握Key在内存中的占用、Key的访问频次等信息，溯源分析问题，为您的优化操作提供数据支持。
在控制台目标实例详情页的CloudDBA>实时Top Key统计页签中，进行热Key与大Key分析，更多信息请参见[实时](../user-guide/use-the-real-time-key-statistics-feature.md)[Top Key](../user-guide/use-the-real-time-key-statistics-feature.md)[统计](../user-guide/use-the-real-time-key-statistics-feature.md)。
离线全量Key分析
离线全量Key分析功能支持全数据结构、全实例架构及Redis各个版本的离线RDB备份文件解析，对线上服务无影响。相比开源工具redis-rdb-tool的解析速度，离线全量Key分析在大小Key混合（占比1：9）的场景下实现4倍速度提升，在中大Key场景下实现20倍速度提升，同时保证进程内存占用固定维持在1 GB以内，避免大Key解析可能带来内存溢出的问题。离线全量Key分析还提供了最长子元素查询，方便进一步业务排查。
在控制台目标实例详情页的CloudDBA>离线全量Key分析页签中进行分析，更多信息请参见[离线全量](../user-guide/offline-key-analysis.md)[Key](../user-guide/offline-key-analysis.md)[分析](../user-guide/offline-key-analysis.md)。
实例诊断
云数据库 Tair（兼容 Redis）综合了性能指标、慢日志、key分析等能力，提供了一站式全链路的实例诊断功能，从性能水位、访问倾斜情况、慢日志等多方面评估实例的健康状况，并给出改善建议，极大程度地
