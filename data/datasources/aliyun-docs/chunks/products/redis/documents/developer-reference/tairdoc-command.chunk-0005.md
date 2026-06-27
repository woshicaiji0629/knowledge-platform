## JSON.SET

| 类别 | 说明 |
| --- | --- |
| 语法 | JSON.SET key path json [NX | XX] |
| 时间复杂度 | O(N) |
| 命令描述 | 创建 key 并将 JSON 的值存储在对应的 path 中，若 key 及目标 path 已经存在，则更新对应的 JSON 值。 |
| 选项 | key ：TairDoc 的 key，用于指定作为命令调用对象的 TairDoc。 path ：目标 key 的 path，根元素支持 . 或 $ 。 json ：待新增或更新的 JSON 数据。 NX ：当 path 不存在时写入。 XX ：当 path 存在时写入。 |
| 返回值 | 执行成功：OK。 指定了 XX 且 path 不存在：nil。 指定了 NX 且 path 已存在：nil。 若返回 ERR could not find object to add, please check path ：表示您输入的 path 有误。 其它情况返回相应的异常信息。 |
| 示例 | 命令示例： JSON.SET doc $ '{ "store": { "book": [ { "category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95 }, { "category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99 }, { "category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99 }, { "category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99 } ], "bicycle": { "color": "red", "price": 19.95 } } }' 返回示例： OK |
