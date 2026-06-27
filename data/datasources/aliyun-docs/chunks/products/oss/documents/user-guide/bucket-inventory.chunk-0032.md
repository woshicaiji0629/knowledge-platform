### 全量清单文件
清单任务配置完成后，OSS会按清单规则指定的导出周期生成清单文件。清单文件的目录结构如下：
<dest-bucket-name>/ └── <dest-prefix>/ └── <source-bucket-name>/ └── <inventory-id>/ ├── YYYY-MM-DDTHH-MMZ/ (扫描开始的UTC时间) │ ├── manifest.json (清单任务的元数据文件) │ └── manifest.checksum (manifest.json 文件的 MD5 校验和) └── data/ └── <uuid>.csv.gz (多份GZIP 压缩的清单数据文件)

| 目录结构 | 说明 |
| --- | --- |
| dest-prefix | 该目录根据设置的清单报告名前缀生成，如果清单报告名前缀设置为空，将省略该目录。 |
| source-bucket-name | 该目录根据配置清单报告的源 Bucket 名生成。 |
| inventory_id | 该目录根据清单任务的规则名称生成。 |
| YYYY-MM-DDTHH-MMZ | 该目录是标准的格林威治时间戳，表示开始扫描 Bucket 的时间，例如 2025-05-17T16-00Z。该目录下包含了 manifest.json 和 manifest.checksum 文件。 |
| data | 该目录下存放了包含源 Bucket 中的对象列表以及每个对象的元数据的清单文件，清单文件格式为使用 GZIP 压缩的 CSV 文件。 重要 当导出的源 Bucket 中 Object 数量较多时，为方便用户下载和处理数据，程序会自动将清单文件切分成多个 CSV 压缩文件。CSV 压缩文件按照 uuid.csv.gz 、 uuid-1.csv.gz 、 uuid-2.csv.gz 的顺序依次递增。可以从 manifest.json 文件中获取 CSV 文件列表，然后按照以上顺序依次解压 CSV 文件并读取清单数据。 Object 的单条记录信息仅出现在一个清单文件内，不会分布到不同的清单文件。 |
