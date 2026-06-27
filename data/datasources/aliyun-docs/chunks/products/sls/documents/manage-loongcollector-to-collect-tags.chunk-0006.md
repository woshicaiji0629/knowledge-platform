ffset__字段显示在左侧显示字段列表和日志详情区域中，其值为文件读取偏移量（如1465）。
{ "Tags": { "FileInodeTagKey": "__default__", "FilePathTagKey": "__default__" }, "FileOffsetKey":"__default__" }

| 参数名 | 类型 | 是否必填 | 默认值 | 样例 | 说明 |
| --- | --- | --- | --- | --- | --- |
| Tags | object | 否 | 空 | {"FileInodeTagKey":"__inode__"} | key 为 Tag 参数名，value 为 Tag 在日志中的字段名。当 value 为__default__时，取默认值。当 value 为空字符串时，表示删除 Tag。 可配置 Tag 如下： FileInodeTagKey：文件 inode。 默认不添加，默认值为"__inode__"。 FilePathTagKey：文件路径。默认添加，默认值为"__path__"。 以下参数仅当 EnableContainerDiscovery 参数取值为 true 时有效。 K8sNamespaceTagKey：文件所在容器命名空间。默认添加，默认值为"_namespace_"。 K8sPodNameTagKey：文件所在 Pod 名。默认添加，默认值为"_pod_name_"。 K8sPodUidTagKey：文件所在 Pod UID。默认添加，默认值为"_pod_uid_"。 ContainerNameTagKey：文件所在容器名。默认添加，默认值为"_container_name_"。 ContainerIpTagKey：文件所在容器 IP。默认添加，默认值为"_container_ip_"。 ContainerImageNameTagKey：文件所在容器镜像。默认添加，默认值为"_image_name_"。 |
| FileOffsetKey | string | 否 | 空 | __file_offset__ | 日志在文件中的位置 Tag。默认不添加，默认值为__file_offset__。当 value 为__default__时，取默认值。当 value 为空字符串时，表示删除 Tag。 重要 当 EnableLogPositionMeta 参数与 Tags.FileInodeTagKey 或 FileOffsetKey 参数同时存在时，EnableLogPositionMeta 参数会被忽略。 |
