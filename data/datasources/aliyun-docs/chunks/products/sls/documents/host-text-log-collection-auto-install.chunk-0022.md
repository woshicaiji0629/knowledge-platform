兼容正则表达式。 |
| JSON | 完全支持标准 JSON（ [RFC7159](https://tools.ietf.org/html/rfc7159) 、 [ECMA-404](https://ecma-international.org/publications-and-standards/standards/ecma-404/) ）。不支持非标准 JSON，例如 {"name": "\xE5\xAD\xA6"} 。 |
| 文件打开行为 | Logtail 会保持被采集的文件和轮转队列中待采集的文件处于打开状态，以保证采集数据完整性。出现以下情况，会关闭文件。 文件超过 5 分钟未被修改。 发生轮转且采集完毕。 Logtail 采集配置发生变更。 如果无论文件是否采集完成或仍有日志写入文件，您都希望文件在删除后的可控时间内释放文件句柄，则您可通过启动参数 force_release_deleted_file_fd_timeout 设置超时时间。具体操作，请参见 [Logtail](select-a-network-type.md) [网络类型，启动参数与配置文件](select-a-network-type.md) 。 |
| 首次日志采集行为 | Logtail 只采集增量的日志文件。首次发现文件被修改后，如果文件大小超过 1 MB（容器标准输出为 512 KB），则从最后 1 MB 处开始采集，否则从开始位置采集。 您可通过 Logtail 采集配置中的 tail_size_kb 参数调整新文件首次采集的大小。具体操作，请参见 [Logtail](developer-reference/logtail-configurations.md) [配置（旧版）](developer-reference/logtail-configurations.md) 。 如果下发 Logtail 采集配置后，日志文件一直无修改，则 Logtail 不会采集该文件。如果需要采集历史文件，请参见 [导入历史日志文件](import-historical-logs.md) 。 |
| 文件发生覆盖的行为 | Logtail 采用 inode+文件中前 1024 字节的 Hash 识别文件。文件被覆盖后，如果 inode 或文件前 1024 字节 Hash 发生变化，则文件会作为新文件从头开始采集，否则不会被采集。 |
| 文件发生移动的行为 | 文件发生移动后，如果匹配 Logtail 采集配置，且该 Logtail 采集配置之前从未匹配过该文件，则移动后的文档将被当成新文件从头开始采集，否则不会被采集。 |
| 文件采集历史 | Logtail 会在内存中保留文件采集历史进度，保证文件发生变化后仅采集增量部分，超过保留范围的日志如果发生写入，会导致重复采集。 默认
