data/5b7c6cf0db490db906c60e87b917b148_5550506986a37a62abce56a83db6736d_0.csv", "size": 2046}], "sourceBucket": "srcbucket", "version": "2025-09-30" }
各字段详细说明如下：

| 字段名称 | 说明 |
| --- | --- |
| startTimestamp | 时间戳，增量清单统计开始时间。 |
| endTimestamp | 时间戳，增量清单统计结束时间。 |
| destinationBucket | 存放清单文件的目标 Bucket。 |
| fileFormat | 清单文件的格式。 |
| fileSchema | 清单文件包含的字段，分为固定字段和可选字段。其中，固定字段的顺序是固定的，可选字段的排列顺序取决于配置清单规则时清单内容字段的排列顺序（控制台配置时以字段的勾选先后顺序为准）。 因此，建议以 fileSchema 中的字段顺序去解析 csv.gz 中的数据列，避免出现列和属性对应错误的情况。 配置清单规则时如果对象版本选择了当前版本，则 fileSchema 中，先排列固定字段 Bucket, Key ，后续为可选字段。 配置清单规则时如果对象版本选择了所有版本，则 fileSchema 中，先排列固定字段 Bucket, Key, VersionId, IsDeleteMarker ，后续为可选字段。 |
| files | 包含清单文件的 MD5 值、文件名完整路径及文件大小。 |
| sourceBucket | 配置清单规则的源 Bucket。 |
| version | 清单版本号。 |

增量清单报告字段
