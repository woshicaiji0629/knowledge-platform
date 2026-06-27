## JSON.ARRTRIM

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.ARRTRIM key path start stop |
| 时间复杂度 | O(N) |
| 命令描述 | 修剪目标 key 的 path 对应的数组（array），保留 start 至 stop 范围内的数据。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 start ：修剪的开始位置，取值为从 0 开始的一个索引值，修剪后的数组包含该位置的元素。 stop ：修剪的结束位置，取值为从 0 开始的一个索引值，修剪后的数组包含该位置的元素。 |
| 返回值 | 执行成功：返回操作完成后数组的长度。 key 不存在：-1。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"id": [1,2,3,4,5,6]}' 命令。 命令示例： JSON.ARRTRIM doc .id 3 4 返回示例： (integer) 2 |
