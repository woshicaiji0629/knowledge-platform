缩文件按照 uuid.csv.gz 、 uuid-1.csv.gz 、 uuid-2.csv.gz 的顺序依次递增。可以从 manifest.json 文件中获取 CSV 文件列表，然后按照以上顺序依次解压 CSV 文件并读取清单数据。 Object 的单条记录信息仅出现在一个清单文件内，不会分布到不同的清单文件。 |

manifest文件
manifest文件包含manifest.json和manifest.checksum，详细说明如下：
manifest.json：提供了有关清单的元数据和其他基本信息。
{ "creationTimestamp": "1642994594", "destinationBucket": "dest-bucket-name", "fileFormat": "CSV", "fileSchema": "Bucket, Key, VersionId, IsLatest, IsDeleteMarker, Size, StorageClass, LastModifiedDate, ETag, IsMultipartUploaded, EncryptionStatus, ObjectAcl, TaggingCount, ObjectType, CRC64", "files": [{ "MD5checksum": "F77449179760C3B13F1E76110F07****", "key": "dest-prefix/source-bucket-name/inventory-id/data/a1574226-b5e5-40ee-91df-356845777c04.csv.gz", "size": 2046}], "sourceBucket": "source-bucket-name", "version": "2019-09-01" }
各字段详细说明如下：
