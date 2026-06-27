## JSON.ARRPOP

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRPOP key path [ index ] |
| 时间复杂度 | O(M*N)，M 是 key 包含的子元素，N 是数组元素数量。 |
| 命令描述 | 移除并返回 path 对应数组（array）中指定位置（index）的元素。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 index ：数组的索引，起始下标为 0，负数表示反向取值，若不传该参数默认为最后一个元素。 |
| 返回值 | 执行成功：移除并返回该元素。 数组为空数组：‘ERR array index outflow’。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRPOP doc .id 0 返回示例： "1" |
