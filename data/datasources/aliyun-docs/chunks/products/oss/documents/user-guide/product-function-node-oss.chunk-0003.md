Windows 的快捷方式，通过软链接文件快速打开 Object。 | [软链接](configure-symbolic-links.md) |  |
| 管理文件元信息 | OSS 存储的文件（Object）信息包含 Key、Data 和 Object Meta。Object Meta 是对文件的属性描述，包括 HTTP 标准属性（HTTP Header）和用户自定义元数据（User Meta）两种。您可以通过设置 HTTP 标准属性来自定义 HTTP 请求的策略，例如文件（Object）缓存策略、强制下载策略等。您还可以通过设置用户自定义元数据来标识 Object 的用途或属性等。 | [管理文件元信息](manage-object-metadata-10.md) |  |
| 管理目录 | 与传统文件系统中的层级结构不同，OSS 内部使用扁平结构存储数据。即所有数据均以 Object 的形式保存在 Bucket 中。为方便您对 Object 进行分组并简化权限管理，您可以创建目录，然后将目标 Object 存放至指定目录。当您不需要保留该目录时，还可以通过多种方式删除目录。 | [管理目录](manage-directories.md) |  |
| 数据索引 | 如果您希望从 Bucket 存储的海量 Object 中快速查找与指定的 Object 名称、ETag、存储类型、大小、最后修改时间等条件匹配的 Object，您可以使用数据索引功能。通过数据索引功能，您可以在查找目标 Object 时指定过滤条件，对查询结果按需选择排序和聚合的方式，提升查找目标 Object 的效率。 | [数据索引](scalar-retrieval.md) |  |
| 通过云存储网关挂载 OSS | 通过云存储网关挂载 OSS，您可以将 OSS 映射为一个共享的文件存储系统，实现多个用户在不同地点和设备上共享访问 OSS 数据。挂载完成后，您可以像使用本地文件夹和磁盘一样操作 OSS 资源。 | [通过云存储网关挂载](use-csg-to-attach-oss-buckets-to-ecs-instances.md) [OSS](use-csg-to-attach-oss-buckets-to-ecs-instances.md) |  |
