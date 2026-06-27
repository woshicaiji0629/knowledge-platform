| 元数据类型 | 字段名称 | 说明 |
| --- | --- | --- |
| System Metadata | Bucket | 执行清单任务的源 Bucket 名称。 |
| Event Metadata | SequenceNumber | 序列号，每条记录的 SequenceNumber 唯一，同 Bucket 同 Object 下的记录，可按照 SequenceNumber 排序，通常保证排序后的记录遵循时间逻辑顺序。 |
| RecordType | 事件类型：CREATE、UPDATE_METADATA、DELETE CREATE：所选前缀下发生的所有上传方式，如 Put/Post/Append/MultipartUpload/Copy UPDATE_METADATA：所选前缀下所有元数据的更新都记录在该类型中 DELETE：所选前缀下的文件的所有删除方式，如 DeleteObject/DeleteMultipleObjects、开启多版本后生成 DeleteMarker、生命周期删除。删除有 DeleteMarker 和永久删除，其中，永久删除记录仅保留 Bucket 、 Key 、 SequenceNumber 、 RecordType 、 RecordTimestamp 和 VersionId 核心字段，其余列均为空（null）。 |  |
| RecordTimestamp | 时间戳 ( 示例："2024-08-25 18:08:01.024")，采用格林威治时区，精度到毫秒。 |  |
| Requester | 请求者的阿里云 ID 或者 Principal ID。 |  |
| RequestId | 请求的唯一标识。 |  |
| SourceIp | 请求者源 IP。 |  |
| System Metadata | Key | Bucket 中 Object 的名称，采用 URL 编码。 |
| VersionId | Object 的版本 ID。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段显示为空。 如果配置清单规则的 Bucket 已开启版本控制，则该字段显示为 Object 的 VersionId。 |  |
| IsDeleteMarker | Object 版本是否为删除标记。仅当配置的清单规则为导出所有版本时出现此字段。 如果配置清单规则的 Bucket 未开启版本控制，则该字段默认显示为 false 。 如果配置清单规则的 Bucket 已开启版本控制，且 Object 为删除标记时，则该字段显示为 true 。如果 Object 不是删除标记，则该字段显示为 false 。 |  |
| Size | Object 大小。 |  |
|
