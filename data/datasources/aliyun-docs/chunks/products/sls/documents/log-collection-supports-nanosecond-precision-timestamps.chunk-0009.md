## 提取日志时间（Go语言时间格式）
单击添加处理插件，选择拓展处理插件>[提取日志时间（Go](extract-log-time.md)[语言时间格式）](extract-log-time.md)，进行如下配置：
原始时间字段：解析日志前，用于存放时间的原始字段，本示例为asctime。
原始时间格式：根据原始日志的时间字段设置对应的时间格式，需要按照[Golang](log-collection-supports-nanosecond-precision-timestamps.md)[的时间格式规范](log-collection-supports-nanosecond-precision-timestamps.md)来编写。格式化时间模板为Go语言的诞生时间2006-01-02 15:04:05 -0700 MST。本示例对应的时间格式为2006-01-02 15:04:05,999999999。
时间格式字符串必须与原始日志中的时间格式（包括秒和纳秒之间的分隔符，如,或.）完全一致，否则无法正确解析。
结果时间字段：解析日志后，用于存放时间的目标字段，本示例为result_asctime。
结果时间格式：解析日志后的时间格式，按照[Golang](log-collection-supports-nanosecond-precision-timestamps.md)[的时间格式规范](log-collection-supports-nanosecond-precision-timestamps.md)编写。本示例为2006-01-02 15:04:05,999999999Z07:00。
3. 配置索引
完成Logtail配置后，单击下一步。进入查询分析配置页面：
系统默认开启[全文索引](create-indexes.md)，支持对日志原始内容进行关键词搜索。
如需按字段进行精确查询，请在页面加载出预览数据后，单击自动生成索引，日志服务将根据预览数据中的第一条内容生成[字段索引](create-indexes.md)。
配置完成后，单击下一步，完成整个采集流程的设置。
通过CRD配置（Kubernetes 场景）
在 ACK 或自建 Kubernetes 集群中，可以通过 AliyunLog CRD 来配置纳秒精度时间戳的采集。以下是三种不同插件的配置样例。
