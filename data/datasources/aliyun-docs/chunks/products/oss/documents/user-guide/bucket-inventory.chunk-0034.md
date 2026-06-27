-name/inventory-id/data/a1574226-b5e5-40ee-91df-356845777c04.csv.gz", "size": 2046}], "sourceBucket": "source-bucket-name", "version": "2019-09-01" }
各字段详细说明如下：

| 字段名称 | 说明 |
| --- | --- |
| creationTimestamp | 时间戳，显示开始扫描源 Bucket 的时间。 |
| destinationBucket | 存放清单文件的目标 Bucket。 |
| fileFormat | 清单文件的格式。 |
| fileSchema | 清单文件包含的字段，分为固定字段和可选字段。其中，固定字段的顺序是固定的，可选字段的排列顺序取决于配置清单规则时清单内容字段的排列顺序（控制台配置时以字段的勾选先后顺序为准）。 因此，建议以 fileSchema 中的字段顺序去解析 csv.gz 中的数据列，避免出现列和属性对应错误的情况。 配置清单规则时如果对象版本选择了当前版本，则 fileSchema 中，先排列固定字段 Bucket, Key ，后续为可选字段。 配置清单规则时如果对象版本选择了所有版本，则 fileSchema 中，先排列固定字段 Bucket, Key, VersionId, IsLatest, IsDeleteMarker ，后续为可选字段。 |
| files | 包含清单文件的 MD5 值、文件名完整路径及文件大小。 |
| sourceBucket | 配置清单规则的源 Bucket。 |
| version | 清单版本号。 |

manifest.checksum：manifest.checksum文件包含了manifest.json文件的 MD5 哈希值，可用于校验manifest.json文件的完整性，例如F77449179760C3B13F1E76110F07****。
全量清单报告
清单报告存储在data/目录中，包含清单功能导出的文件信息。清单报告示例如下：
