| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [JSON.SET](tairdoc-command.md) | JSON.SET key path json [NX | XX] | 创建 key 并将 JSON 的值存储在对应的 path 中，若 key 及目标 path 已经存在，则更新对应的 JSON 值。 |
| [JSON.GET](tairdoc-command.md) | JSON.GET key path [FORMAT XML | YAML] [ROOTNAME root ] [ARRNAME arr ] | 获取目标 key、path 中存储的 JSON 数据。 |
| [JSON.DEL](tairdoc-command.md) | JSON.DEL key path | 删除目标 key 中 path 对应的 JSON 数据，若未指定 path，则删除 key。若指定的 key 不存在或 path 不存在，则忽略。 |
| [JSON.TYPE](tairdoc-command.md) | JSON.TYPE key path | 获取目标 key 中 path 对应值的类型，结果可能包括 boolean 、 string 、 number 、 array 、 object 、 raw 、 reference 、 const 、 null 等。 |
| [JSON.MERGE](tairdoc-command.md) | JSON.MERGE key path value | 将 value 的 JSON 合并到指定 Key 的 path 路径中。可对目标路径下的值实现新增、更新、删除等操作。 |
| [JSON.NUMINCRBY](tairdoc-command.md) | JSON.NUMINCRBY key path value | 对目标 key 中 path 对应的值增加 value，path 对应的值和待增加的 value 必须是 int 或 double 类型。 |
| [JSON.STRAPPEND](tairdoc-command.md) | JSON.STRAPPEND key path json-string | 在指定 path 对应值中添加 json-string 字符串，path 对应值的类型也需要为字符串。 |
| [JSON.STRLEN](tairdoc-command.md) | JSON.STRLEN key path | 获取目标 key 中 path 对应值的字符串长度，path 对应值的类型需要为字符串。 |
| [JSON.ARRAPPEND](tairdoc-command.md) | JSON.ARRAPPEND key path json [ json
