## JSON.NUMINCRBY

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.NUMINCRBY key path value |
| 时间复杂度 | O(N) |
| 命令描述 | 对目标 key 中 path 对应的值增加 value，path 对应的值和待增加的 value 必须是 int 或 double 类型。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 value ：待增加的数值。 |
| 返回值 | 执行成功：返回操作完成后 path 对应的值。 若 key 或 path 不存在：error。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.NUMINCRBY doc .baz 10 返回示例： "52" |
