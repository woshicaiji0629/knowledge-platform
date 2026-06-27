## JSON.ARRAPPEND

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRAPPEND key path json [ json ...] |
| 时间复杂度 | O(M*N)，M 是需要插入的元素（json）数量，N 是数组元素数量。 |
| 命令描述 | 在指定 path 对应数组（array）的末尾添加 JSON 数据，支持添加多个 JSON。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 json ：需要插入的数据。 |
| 返回值 | 执行成功：返回操作完成后数组（array）中的元素数量。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRAPPEND doc .id null false true 返回示例： (integer) 6 |
