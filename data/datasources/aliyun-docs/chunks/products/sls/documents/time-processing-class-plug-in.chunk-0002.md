## 原生插件与拓展插件的区别
原生插件：C++实现，性能更强。
拓展插件：Go实现，生态丰富且灵活，当业务日志过于复杂，无法使用原生插件处理时，可以考虑使用拓展插件。
拓展插件性能限制
使用拓展插件进行日志处理时，LoongCollector会消耗更多的资源（以CPU为主），如有需求可以调整LoongCollector参数配置进行[配置管理](loongcollector-management-linux.md)。
当原始数据量的生成速度超过5 MB/s时，不建议使用过于复杂的插件组合来处理日志，可以使用拓展插件进行简单处理，再通过[数据加工概述](data-transformation-overview.md)完成进一步处理。
日志采集限制
拓展插件对文本日志的处理采用行模式，即文件级别的元数据（例如__tag__:__path__、__topic__等）会被存放到每一条日志中。
添加拓展插件后会影响和Tag相关的功能：
上下文查询和LiveTail功能不可用。如果要使用这些功能，需要额外添加aggregators配置。
__topic__字段会被重命名为__log_topic__。如果添加了aggregators配置，日志中将同时存在__topic__字段和__log_topic__字段。如果您不需要__log_topic__字段，可使用[丢弃字段插件](field-processing-class-plug-in.md)删除该字段。
__tag__:__path__等字段不再具备原生字段索引，需要[创建索引](create-indexes.md)。
