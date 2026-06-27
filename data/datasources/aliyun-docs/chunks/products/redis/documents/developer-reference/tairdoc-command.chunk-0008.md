## JSON.TYPE

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.TYPE key path |
| 时间复杂度 | O(N) |
| 命令描述 | 获取目标 key 中 path 对应值的类型，结果可能包括 boolean 、 string 、 number 、 array 、 object 、 raw 、 reference 、 const 、 null 等。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path。 |
| 返回值 | 执行成功：返回查询到的类型。 执行失败：0。 若 key 或 path 不存在：nil。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc . '{"foo": "bar", "baz" : 42}' 命令。 命令示例： JSON.TYPE doc .foo 返回示例： string |
