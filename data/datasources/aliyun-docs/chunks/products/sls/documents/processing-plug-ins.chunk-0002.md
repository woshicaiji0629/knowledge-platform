### 日志采集限制
扩展插件对文本日志的处理采用行模式，即文件级别的元数据（例如__tag__:__path__、__topic__等）会被存放到每一条日志中。
添加扩展插件后会影响和Tag相关的功能：
上下文查询和LiveTail功能不可用。如果您要使用这些功能，需要额外添加aggregators配置。
__topic__字段会被重命名为__log_topic__。如果您添加了aggregators配置，日志中将同时存在__topic__字段和__log_topic__字段。如果您不需要__log_topic__字段，可使用[processor_drop](drop-fields.md)插件删除该字段。
__tag__:__path__等字段不再具备原生字段索引，需要[创建字段索引](create-indexes.md)。
