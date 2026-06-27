## TFT.GETSUG

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.GETSUG index prefix [MAX_COUNT count] [FUZZY] |
| 命令描述 | 根据指定前缀，查询匹配的自动补全文本，将优先返回权重比较高的 text。 |
| 选项 | index ：待查询的索引名称。 prefix ：指定的查询前缀。 MAX_COUNT count ：配置返回文本的最大数量，count 的取值范围为[0,255]。 FUZZY ：是否启用模糊匹配。 |
| 返回值 | 执行成功：返回自动补全文本的列表。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.GETSUG idx:redis res MAX_COUNT 2 FUZZY 返回示例： 1) "redis cluster" 2) "redis lock" |
