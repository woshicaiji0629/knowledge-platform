## JSON.ARRINSERT

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRINSERT key path [ index ] json [ json ...] |
| 时间复杂度 | O(M*N)，M 是要插入的元素（json）数量，N 是数组元素数量。 |
| 命令描述 | 将 JSON 插入到 path 对应的数组（array）中，原有元素会往后移动。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 index ：数组的索引，起始下标为 0，负数表示反向取值，若不传该参数默认为最后一个元素。 json ：需要插入的数据。 |
| 返回值 | 执行成功：返回操作完成后数组（array）中的元素数量。 数组为空数组：‘ERR array index outflow’。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3]}' 命令。 命令示例： JSON.ARRINSERT doc .id 0 10 15 返回示例： (integer) 5 |
