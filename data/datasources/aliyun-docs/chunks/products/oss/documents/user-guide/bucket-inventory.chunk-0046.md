配置清单规则的 Bucket 未开启版本控制，则该字段默认显示为 false 。 如果配置清单规则的 Bucket 已开启版本控制，且 Object 为删除标记时，则该字段显示为 true 。如果 Object 不是删除标记，则该字段显示为 false 。 |  |
| Size | Object 大小。 |  |
| StorageClass | Object 的存储类型。 |  |
| LastModifiedDate | Object 的最后修改时间，格式是格林威治时间，与北京时间相差 8 小时。 |  |
| ETag | Object 的 ETag。Object 生成时会创建相应的 ETag，用于标识一个 Object 的内容。 通过 [PutObject](../developer-reference/putobject.md) 接口创建的 Object，ETag 值是其内容的 MD5 值。 通过其他方式创建的 Object，ETag 值是基于一定计算规则生成的唯一值，但不是其内容的 MD5 值。 |  |
| IsMultipartUploaded | Object 是否通过分片上传生成。如果是，则该字段值为 true ，否则为 false 。 |  |
| EncryptionStatus | Object 是否已加密。若 Object 已加密，则该字段值为 true ，否则为 false 。 |  |
| ObjectAcl | Object 的读写权限。更多信息，请参见 [Object ACL](object-acl.md) 。 |  |
| ObjectType | Object 类型。更多信息，请参见 [Object](object-overview.md) [类型](object-overview.md) 。 |  |
| Crc64 | Object 的 CRC64。 |  |
