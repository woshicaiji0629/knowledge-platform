## JSON.MERGE

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.MERGE key path value |
| 时间复杂度 | O(N) |
| 命令描述 | 将 value 的 JSON 合并到指定 Key 的 path 路径中。可对目标路径下的值实现新增、更新、删除等操作。 |
| 选项 | key ：TairDoc 的 Key，用于指定作为命令调用对象的 TairDoc。 path ：目标 Key 的 path，支持部分 JSONPath 语法，例如 $.a.b.c 、 $.a['b'] ，但不支持 $.. 、 $* 等复杂表达式。 value ：待合并的 Json，格式兼容 [Json Merge Patch RFC7386](https://datatracker.ietf.org/doc/html/rfc7386) 。 |
| 返回值 | 执行成功：OK。 若 value 有误：parse merge patch error。 其它情况返回相应的异常信息。 |
| 示例 | 提前执行 JSON.SET doc $ '{"f1": {"a":1}, "f2":{"a":2}}' 命令。 命令示例： JSON.MERGE doc $ '{"f1": null, "f2":{"a":3, "b":4}, "f3":[2,4,6]}' 返回示例： OK 此时，执行 JSON.GET doc . 的结果如下： "{\"f2\":{\"a\":3,\"b\":4},\"f3\":[2,4,6]}" |
