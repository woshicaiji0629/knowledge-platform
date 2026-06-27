## JSON.STRAPPEND

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.STRAPPEND key path json-string |
| 时间复杂度 | O(N) |
| 命令描述 | 在指定 path 对应值中添加 json-string 字符串，path 对应值的类型也需要为字符串。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 json-string ：待添加到 path 对应值的字符串。 |
| 返回值 | 执行成功：返回操作完成后 path 对应值的字符串长度。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.STRAPPEND doc .foo rrrrr 返回示例： (integer) 8 |
