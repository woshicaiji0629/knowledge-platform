和其操作结果按时间的有序集合。文本日志（LogFile）、事件（Event）、数据库日志（BinLog）、时序数据（Metric）等数据都是日志的不同载体。日志服务采用半结构化的数据模式定义一条日志，包含日志主题、日志时间、日志内容、日志来源和日志标签五个数据域。日志服务对各个数据域的格式要求不同，详细说明如下表所示。

| 数据域 | 说明 | 格式 |
| --- | --- | --- |
| 日志主题（Topic） | 日志服务保留字段（ __topic__ ）用于标识日志主题，可区分不同服务、用户或实例产生的日志。例如，系统 A 包含前端 HTTP 请求处理、缓存、逻辑处理、存储等模块时，可分别为其日志设置 Topic（如 http_module、cache_module、logic_module、store_module）。日志采集至同一 LogStore 后，可通过 Topic 快速区分来源。日志主题（Topic）需在 [采集配置](manage-logtail-configurations-for-log-collection.md) 的 全局配置 中设置。 LogStore、Topic、 [Shard](manage-shards.md) 之间的关系如下： | 包括空字符串在内的任意字符串，大小为 0~128 字节。 若不需要区分 LogStore 中的日志，则在采集日志时设置为空字符串即可。空字符串是一个有效的 Topic，即 Topic 的值为空字符串。 |
| 日志时间 | 日志服务保留字段（ __time__ ）用于标识日志时间。更多信息，请参见 [保留字段](reserved-fields.md) 。 | Unix 时间戳。 |
| 日志内容 | 日志的具体内容，由一个或多个内容项组成，内容项为 Key:Value 格式。 您通过 Logtail 极简模式（单行或多行）采集日志时，Logtail 不会对日志内容进行解析。整条原始日志将被上传到 content 字段中。 | Key:Value 的详细说明如下： Key 为字段名称，需为 UTF-8 编码字符串（字母、下划线和数字但不以数字开头）。字符串大小为 1~128 字节。不可使用如下字段。 __time__ __source__ __topic__ __partition_time__ _extract_others_ __extract_others__ Value 为字段值，可以为任意字符串，大小不超过 1 MB。 |
| 日志来源 | 日志服务保留字段（ __source__ ）用于标识日志来源，例如产生日志的服务器 IP 地址。 | 任意字符串，大小为 0~128 字节。 |
| 日志标签 | 日志标签。包括： 自定义标签：通过 [PutLogs](putlogs.md) 接口，在写入日志时添加标签。 系统标签：日志服务为日志添加的标签，包括 __client_ip__ 和 __receive_time__ 。 | 字典格式，Key 和 Value 均为字符串类型。在日志中以 __tag__: 为前缀进行展示。 |
