| 限制项 | 限制说明 |
| --- | --- |
| 单条日志长度 | 默认限制为 512 KB。您可通过启动参数 max_read_buffer_size 进行调整，最大不能超过 8 MB。具体操作，请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 多行日志按行首正则表达式划分后，每条日志大小限制仍为 512 KB。如果日志超过 512 KB，会被强制拆分为多条进行采集。例如：单条日志大小为 1025 KB，则第一次处理 512 KB，第二次处理 512 KB，第三次处理 1 KB，最终采集结果为多条不完整的日志。 |
| 文件编码 | 支持 UTF-8 或 GBK 编码的日志文件，建议使用 UTF-8 编码获得更好的处理性能。 警告 如果日志文件为其它编码格式则会出现乱码、数据丢失等问题。 |
| 日志文件轮转 | 日志轮转队列大小默认为 20。您可通过启动参数 logreader_max_rotate_queue_size 进行调整。具体操作，请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 支持设置采集路径为 xxx.log 或 xxx.log* 形式。 重要 同一个 Logtail 实例中请勿混用两种形式，否则可能导致同一文件匹配多个 Logtail 采集配置，出现重复采集。 如果未处理完成的文件超过 20 个，将导致新生成的日志丢失。此类情况，请优先排查 LogStore Shard 写入 Quota 是否超限，并调整 Logtail 并发水平。具体操作，请 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 更多信息，请参见 [相关技术文章](https://yq.aliyun.com/articles/204554) 。 |
| 日志解析阻塞时采集行为 | 日志解析阻塞时，Logtail 会保持该日志文件描述符为打开状态，避免阻塞期间文件被删除，导致日志丢失。 如果解析阻塞期间出现多次日志文件轮转，Logtail 会将文件放入轮转队列。 |
| 正则表达式 | 支持 Perl 兼容正则表达式。 |
| JSON | 完全支持标准 JSON（ [RFC7159](https://tools.ietf.org/html/rfc7159) 、 [ECMA-404](https://ecma-international.org/publications-and-standards/standards
