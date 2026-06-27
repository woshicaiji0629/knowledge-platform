Object 是否通过分片上传生成。如果是，则该字段值为 true ，否则为 false 。 |
| EncryptionStatus | Object 是否已加密。若 Object 已加密，则该字段值为 true ，否则为 false 。 |
| ObjectAcl | Object 的读写权限。更多信息，请参见 [Object ACL](object-acl.md) 。 |
| TaggingCount | Object 的标签个数。 |
| ObjectType | Object 类型。更多信息，请参见 [Object](object-overview.md) [类型](object-overview.md) 。 |
| Crc64 | Object 的 CRC64。 |
| LastAccessDate | Object 的最后访问时间，格式是格林威治时间，与北京时间相差 8 小时。 说明 仅在 Bucket 开启 [访问跟踪](lifecycle-rules-based-on-the-last-access-time.md) 的情况下才支持导出。如果关闭访问跟踪后，该字段的值不再有含义，通常显示为 null。 |
| LastAccessTimestamp | Object 的最后访问时间戳（Unix 时间戳）。 说明 仅在 Bucket 开启 [访问跟踪](lifecycle-rules-based-on-the-last-access-time.md) 的情况下才支持导出。如果关闭访问跟踪后，该字段的值不再有含义，通常显示为 null。 |
