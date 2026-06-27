| 字段名称 | 说明 |
| --- | --- |
| Bucket | 执行清单任务的源 Bucket 名称。 |
| Key | Bucket 中 Object 的名称。 Object 名称使用 URL 编码，可按需解码。 |
| VersionId | Object 的版本 ID。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段显示为空。 如果配置清单规则的 Bucket 已开启版本控制，则该字段显示为 Object 的 VersionId。 |
| IsLatest | Object 版本是否为最新版本。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段显示为 true 。 如果配置清单规则的 Bucket 已开启版本控制，且 Object 为最新版本时，则该字段显示为 true 。如果 Object 为历史版本，则该字段显示为 false。 |
| IsDeleteMarker | Object 版本是否为删除标记。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段默认显示为 false 。 如果配置清单规则的 Bucket 已开启版本控制，且 Object 为删除标记时，则该字段显示为 true 。如果 Object 不是删除标记，则该字段显示为 false 。 |
| Size | Object 大小。 |
| StorageClass | Object 的存储类型。 |
| LastModifiedDate | Object 的最后修改时间，格式是格林威治时间，与北京时间相差 8 小时。 |
| TransistionTime | Object 通过生命周期规则转储为冷归档或者深度冷归档存储类型的时间。 |
| ETag | Object 的 ETag。 Object 生成时会创建相应的 ETag，用于标识一个 Object 的内容。 通过 [PutObject](../developer-reference/putobject.md) 接口创建的 Object，ETag 值是其内容的 MD5 值。 通过其他方式创建的 Object，ETag 值是基于一定计算规则生成的唯一值，但不是其内容的 MD5 值。 |
| IsMultipartUploaded | Object 是否通过分片上传生成。如果是，则该字段值为 true ，否则为 false 。 |
| EncryptionStatus | Object 是否已加密。若 Object 已加密，则该字段值为 true ，否则为 false 。 |
| ObjectAcl | Object 的读写权限。更多信息，请参见 [
