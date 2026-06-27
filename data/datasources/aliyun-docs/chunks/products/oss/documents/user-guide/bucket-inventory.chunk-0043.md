果）。 |
| YYYY-MM-DDTHH-MMSSZ | 该目录是标准的格林威治时间戳，表示开始扫描 Bucket 的时间，例如 2020-05-17T16-0000Z。 |
| data | 该目录下存放的是在指定时间周期内，源 Bucket 中发生修改的对象及其元数据的清单文件，清单文件格式为 CSV 文件。 |

manifest文件{ "startTimestamp": "1759320000", "endTimestamp": "1759320600", "destinationBucket": "destbucket", "fileFormat": "CSV", "fileSchema": "Bucket, Key, VersionId, IsDeleteMarker, SequenceNumber, RecordType, RecordTimestamp, Requester, RequestId, SourceIp, Size, StorageClass, LastModifiedDate, ETag, IsMultipartUploaded, ObjectType, ObjectAcl, CRC64, EncryptionStatus", "files": [{ "MD5checksum": "60463A9A34019CF448A730EB2CB3****", "key": "dest-prefix/source-bucket-name/inventory-id/incremental_inventory/2025-09-28T07-4000Z/data/5b7c6cf0db490db906c60e87b917b148_5550506986a37a62abce56a83db6736d_0.csv", "size": 2046}], "sourceBucket": "srcbucket", "version": "2025-09-30" }
各字段详细说明如下：
