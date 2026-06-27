### 解析清单报告
清单任务以异步方式执行。清单报告的所有文件都存储在一个以扫描启动时间命名的文件夹中。核心文件包括manifest.json和data/目录下的.csv.gz数据文件。要确认任务是否完成，可以检查目标是否已生成manifest.json文件。
读取manifest.json文件：解析manifest.json文件以获取正确的列顺序和数据文件信息，重点关注以下两个字段：
fileSchema：字符串类型，定义了 CSV 文件中各列的名称和确切顺序。
files：数组类型，列出了本次报告生成的所有.csv.gz数据文件的详细信息，包括：
key：文件路径
size：文件大小
MD5checksum：MD5 校验值
根据fileSchema解析 CSV 数据文件
获取并解压数据文件：从manifest.json的files数组中获取每个数据文件的key（即文件路径）。根据该路径下载对应的.csv.gz压缩包。解压文件，得到 CSV 格式的数据。
按序解析数据：
以fileSchema字段中定义的顺序作为 CSV 文件的列标题。逐行读取解压后的 CSV 文件。每一行代表一个对象（文件）的完整记录，每一列则对应fileSchema中指定的一个字段。
CSV 内容示例：如果fileSchema为"Bucket,Key,Size,StorageClass,LastModifiedDate"，解压后的 CSV 内容格式如下：
source-bucket,"dir%2Fbody.xml","102400","Standard","2025-04-14T07-06-00Z" source-bucket,"dest.png","312049","Standard","2025-04-14T07-05-59Z"Key 使用URL编码，可按需解码。
