## JSONPath介绍
TairDoc支持[JSONPath](https://datatracker.ietf.org/doc/draft-ietf-jsonpath-base/)的兼容语法如下表所示：

| JSONPath | 说明 |
| --- | --- |
| $ | 根元素。 |
| @ | 当前元素。 |
| .name | 子元素。 |
| .. | 任意位置符合要求的元素。 |
| * | 通配符，表示所有子元素或数组元素。 |
| [ ] | 数组索引，索引从 0 开始，例如[0]；支持选择列表，例如[0,1]，表示 0 和 1；也支持添加元素名，例如['name']。 |
| [start:end:step] | 数组切片选择器（Array Slice Selector），表示从 start 开始，到 end 结束，按照 step 为步长来获取元素，例如[0:3:1]，表示从第 0 位到第 3 位。若步长为负数，则从后向前获取。 |
| ?... | 条件过滤选择器。 |
| () | 支持表达式，优先级为： ( ) > && > || ，更多信息，请参见 [JSONPath](https://datatracker.ietf.org/doc/draft-ietf-jsonpath-base/) 。 |

查询示例
创建JSON文档。
命令实例：
JSON.SET dockey $ '{ "store": { "book": [{ "category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95 }, { "category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99 }, { "category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99 }, { "category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99 } ], "bicycle": { "color": "red", "price": 19.95 } }, "expensive": 10 }'
预计返回：
OK
查询文档。
查询示例如下：
