## JSON.GET

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.GET key path [FORMAT XML | YAML] [ROOTNAME root ] [ARRNAME arr ] |
| 时间复杂度 | O(N) |
| 命令描述 | 获取目标 key、path 中存储的 JSON 数据。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path，支持 JSONPath 与 JSON 语法，按需灵活地查询，更多信息请参见 [JSONPath](tairdoc-command.md) [介绍](tairdoc-command.md) 和 [JSONPointer](tairdoc-command.md) [介绍](tairdoc-command.md) 。 FORMAT ：指定返回的 JSON 格式，支持 XML、YAML 格式。 ROOTNAME ：指定 XML 语法 ROOT 元素的标签。 ARRNAME ：指定 XML 语法 ARRAY 元素的标签。 说明 ROOTNAME 与 ARRNAME 参数需在指定 FORMAT 参数为 XML 时配合使用。 |
| 返回值 | 执行成功：对应的 JSON 数据。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.GET doc . FORMAT XML ROOTNAME ROOT ARRNAME ARR 返回示例： "<?xml version=\"1.0\" encoding=\"UTF-8\"?><ROOT><foo>bar</foo><baz>42</baz></ROOT>" |
