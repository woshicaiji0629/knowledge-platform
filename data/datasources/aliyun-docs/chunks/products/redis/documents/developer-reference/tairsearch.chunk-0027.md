## TFT.SCANDOCID

| 类别 | 说明 |
| --- | --- |
| 语法 | TFT.SCANDOCID index cursor [MATCH *value*] [COUNT count] |
| 命令描述 | 获取索引中所有的 doc_id。 |
| 选项 | index ：待查询的索引名称。 cursor ：指定本次扫描的游标。 MATCH *value* ：模式匹配，value 为待匹配的值，例如 MATCH *redis* 。 COUNT count ：指定本次扫描的最大数量，默认为 100。 |
| 返回值 | 执行成功：返回一个数组。 第一个元素：下次查询的 cursor ，若该 key 已扫描完成，则返回 0。 第二个元素：本次查询的 doc_id。 其他情况返回相应的异常信息。 |
| 示例 | 命令示例： TFT.SCANDOCID idx:product 0 COUNT 3 返回示例： 1) "0" 2) 1) "00001" 2) "00011" 3) "00012" |
