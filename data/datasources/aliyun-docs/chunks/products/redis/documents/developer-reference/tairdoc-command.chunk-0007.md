## JSON.DEL

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.DEL key path |
| 时间复杂度 | O(N) |
| 命令描述 | 删除目标 key 中 path 对应的 JSON 数据，若未指定 path，则删除 key。若指定的 key 不存在或 path 不存在，则忽略。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 |
| 返回值 | 执行成功：1。 执行失败：0。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.DEL doc .foo 返回示例： (integer) 1 |
