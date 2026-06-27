| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 数据湖 | OSS Select | 您可以使用 SelectObject 对目标文件执行 SQL 语句，返回执行结果。 | [OSS Select](query-objects.md) |
| OSS 加速器 | 随着 AI、数据仓库、大数据分析等业务发展，越来越多运行在 OSS 上的业务对于数据的访问延迟和吞吐量有了更高的要求。OSS 推出加速器功能，可以将 OSS 中的热点 Object 缓存在 NVMe SSD 高性能存储介质上，提供毫秒级低延迟和高吞吐量的数据访问服务。 | - |  |
| OSS-HDFS 服务 | OSS-HDFS 服务（JindoFS 服务）是一个云原生数据湖存储功能。基于统一的元数据管理能力，完全兼容 HDFS 文件系统接口，满足大数据和 AI 等领域的数据湖计算场景。 | [OSS-HDFS](oss-hdfs.md) [服务](oss-hdfs.md) |  |
| 数据处理 | 图片处理 | 针对 OSS 内存储的图片文件，您可以在 GetObject 请求中携带图片处理参数对图片文件进行处理。例如添加图片水印、转换格式等。 | - |
| ZIP 包解压 | 当您需要批量上传文件、按特定目录结构上传文件、上传完整的文件或对文件快速进行资源分发时，可以配置解压规则，上传 ZIP 文件到 OSS 指定路径，触发函数计算自动解压，并将解压后内容保存回 OSS。 | [ZIP](zip-package-decompression.md) [包解压](zip-package-decompression.md) |  |
| 智能媒体 | OSS 与智能媒体管理（IMM）深度结合，支持媒体处理、文档处理等丰富的数据分析处理操作。 | [智能媒体](intelligent-media-management-imm.md) |  |
| 事件通知 | 当您需要对 OSS 中的文件变动进行实时处理、同步、监听、业务触发、日志记录等操作时，您可以通过设置 OSS 的事件通知规则，自定义关注的文件，并及时收到相关通知。 | [事件通知](event-notifications.md) |  |
| OSS 对象 FC（Object FC） | 基于 OSS 对象 FC（Object FC），用户可以在发送 OSS GetObject 等请求时自动触发函数计算服务，并将处理后的数据结果进行返回。OSS 对象 FC（Object FC）帮助用户在保持对象存储语义的情况下，无缝集成自定义的数据处理能力。 | [对象](create-object-fc-access-point.md) [FC](create-object-fc-acc
