### 增量清单文件
清单任务配置完成后，OSS会按清单规则指定的导出周期生成清单文件。清单文件的目录结构如下：
<dest-bucket-name>/ └── <dest-prefix>/ └── <source-bucket-name>/ └── <inventory-id>/ └── incremental_inventory/ └── YYYY-MM-DDTHH-MMSSZ/ ├── manifest.json └── data/ ├── uuid1_0.csv └── ......

| 目录结构 | 说明 |
| --- | --- |
| dest-prefix | 该目录根据设置的清单报告名前缀生成，如果清单报告名前缀设置为空，将省略该目录。 |
| source-bucket-name | 该目录根据配置清单报告的源 Bucket 名生成。 |
| inventory_id | 该目录根据清单任务的规则名称生成。 |
| incremental_inventory | 增量清单的固定前缀（区分全量导出结果）。 |
| YYYY-MM-DDTHH-MMSSZ | 该目录是标准的格林威治时间戳，表示开始扫描 Bucket 的时间，例如 2020-05-17T16-0000Z。 |
| data | 该目录下存放的是在指定时间周期内，源 Bucket 中发生修改的对象及其元数据的清单文件，清单文件格式为 CSV 文件。 |
