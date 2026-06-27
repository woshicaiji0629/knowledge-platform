## TFT.GETINDEX

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.GETINDEX index |
| 命令描述 | 获取索引的映射内容。 |
| 选项 | index ：待操作的索引名称。 |
| 返回值 | 执行成功：返回索引的映射内容，格式为 JSON。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.GETINDEX idx:product 返回示例： {"idx:product0310":{"mappings":{"_source":{"enabled":true,"excludes":[],"includes":["product_id"]},"dynamic":"false","properties":{"price":{"boost":1.0,"enabled":true,"ignore_above":-1,"index":true,"similarity":"classic","type":"double"},"product_id":{"boost":1.0,"enabled":true,"ignore_above":128,"index":true,"similarity":"classic","type":"keyword"},"product_name":{"boost":1.0,"enabled":true,"ignore_above":-1,"index":true,"similarity":"classic","type":"text"},"product_title":{"analyzer":"chinese","boost":1.0,"enabled":true,"ignore_above":-1,"index":true,"similarity":"classic","type":"text"}}}}} |
