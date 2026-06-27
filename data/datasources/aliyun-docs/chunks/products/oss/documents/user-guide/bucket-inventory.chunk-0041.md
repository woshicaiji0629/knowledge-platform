### 解析清单报告
清单任务完成后，会在目标 Bucket 的指定路径下生成报告文件，核心包括：
manifest.json文件
data/目录下的.csv数据文件
判断任务是否已完成，可以检查目标 Bucket 中是否生成了manifest.json文件。
解析步骤如下：
读取manifest.json文件：清单报告的列顺序是动态的，取决于配置清单规则时所勾选的字段。需要先解析manifest.json中的fileSchema字段，该字段定义了 CSV 文件中各列的名称及其顺序。
根据fileSchema解析 CSV 数据文件
以fileSchema中定义的顺序作为 CSV 文件的列标题。
按行读取 CSV 文件：每一行代表一个对象（文件）的完整记录，每一列对应fileSchema中声明的一个字段。
