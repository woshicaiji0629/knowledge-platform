## EXTS.S.CREATE

| 类别 | 说明 |
| --- | --- |
| 语法 | EXTS.S.CREATE Pkey Skey [DATA_ET time] [CHUNK_SIZE size] [UNCOMPRESSED] [LABELS label1 val1 label2 val2 ...] |
| 时间复杂度 | O(1) |
| 命令描述 | 在指定的 Pkey 中创建一个 Skey，若 Pkey 不存在则会自动创建，若 Skey 已经存在则创建失败。 说明 您可以在创建 Skey 时设置其相关属性，例如过期时间、是否开启压缩等。 |
| 选项 | Pkey ：PKey 名称（TairTS 数据结构），用于指定命令调用的 TairTS 对象。 Skey ：Skey 名称。 DATA_ET time ：Datapoint 数据的相对过期时间，单位为毫秒，默认为不填（表示不会过期）。 CHUNK_SIZE ：单个 Chunk 的大小，用于存储 Datapoint。单位为 16 byte（字节），默认值为 256，意味着系统会直接给该 Chunk 分配 4 KB 内存（16 byte * 256）用于存储 Datapoint 数据，当该 Chunk 写满时系统会再创建一个新的 Chunk，以此类推。 CHUNK_SIZE 取值范围为[1,256]。 说明 以 CHUNK_SIZE 为 256 为例，若 Skey 不开启压缩，单个 Chunk 能存储 256 个 Datapoint 数据；若开启压缩，则能存储超过 256 个，但具体能存多少取决于不同数据的压缩效果。 为节省内存空间以及平衡读写效率，关于设置 CHUNK_SIZE 的建议如下： 若 Skey 的平均数据点大于 5,000 个，设置 CHUNK_SIZE 为 256（默认值）。大 Chunk 可以减少整体的 Chunk 数量，减少元数据的占用。 若 Skey 的平均数据点小于 5,000 个，设置 CHUNK_SIZE 为平均数据点个数 / 20。例如某 Skey 的平均数据点为 1,000，可以设置 CHUNK_SIZE 为 50。在小范围查询时仅需解压缩更少数据，可以获得更好的性能。但如果在此情况下写入大量数据，会因创建大量 Chunk 而导致性能变慢。 UNCOMPRESSED ：设置 Skey 不开启压缩，默认为不填（即开启压缩）。 LABELS ：Skey 的属性，输入一组或多组对应的标签名、标签值，例如 LABELS sensor_id 1 。 |
| 返回值 | OK：表示执行成功。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： EXTS.S.CREATE foo temperature DATA_ET 10000000 LABELS sensor_id 1 返回示例： OK |
