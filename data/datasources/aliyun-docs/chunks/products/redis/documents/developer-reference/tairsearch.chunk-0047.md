## TFT.GETALLSUGS

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.GETALLSUGS index |
| 命令描述 | 获取指定索引的全量自动补全文本。 |
| 选项 | index ：待查询的索引名称。 |
| 返回值 | 执行成功：返回自动补全文本的列表。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.GETALLSUGS idx:redis 返回示例： 1) "redis cluster" 2) "redis lock" 3) "redis is a memory database" |
