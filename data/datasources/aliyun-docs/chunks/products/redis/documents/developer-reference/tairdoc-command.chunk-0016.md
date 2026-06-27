## JSON.ARRLEN

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRLEN key path |
| 时间复杂度 | O(N) |
| 命令描述 | 获取 path 对应数组（array）的长度。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 |
| 返回值 | 执行成功：数组（array）的长度。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRLEN doc .id 返回示例： (integer) 3 |
