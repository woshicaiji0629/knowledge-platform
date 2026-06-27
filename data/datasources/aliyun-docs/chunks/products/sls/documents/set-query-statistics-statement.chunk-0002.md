行操作，该操作结果再与第三个集合进行集合操作。例如：
集合A左联集合B左联集合C：集合A和集合B先完成左联操作，该结果再左联集合C。
集合A拼接集合B内联集合C：集合A和集合B完成拼接操作，该结果再内联集合C。
集合A左斥集合B不合并集合C：集合A和集合B完成左斥操作，忽略集合C。
集合操作支持9种配置，具体如下所示：

| 集合操作 | 图示 | 说明 |
| --- | --- | --- |
| [不合并](set-query-statistics-statement.md) |  | 两个集合之间无关联。 集合 A 为查询和分析结果，集合 B 仅在告警信息中作为内容模板的变量被引用。 |
| [笛卡尔积](set-query-statistics-statement.md) | 无 | 集合 A 与集合 B 任意数据互相交叉组合，一般用于过滤评估。 |
| [拼接](set-query-statistics-statement.md) |  | 集合 B 中的数据添加到集合 A 中，根据字段对齐。 |
| [内联](set-query-statistics-statement.md) |  | 集合 A 中仅保留在集合 B 中存在的数据，即集合 B 是集合 A 的白名单。 |
| [左联](set-query-statistics-statement.md) |  | 在集合 A 中补充部分来自集合 B 的信息，即集合 B 是 A 的维表。 |
| [右联](set-query-statistics-statement.md) |  | 在集合 B 中补充部分来自集合 A 的信息，即集合 A 是集合 B 的维表。 |
| [全联](set-query-statistics-statement.md) |  | 集合 A 和集合 B 互相补充信息。 |
| [左斥](set-query-statistics-statement.md) |  | 在集合 A 中删除集合 B 中存在的数据，即集合 B 是集合 A 的黑名单。 |
| [右斥](set-query-statistics-statement.md) |  | 在集合 B 中删除集合 A 中存在的数据，即集合 A 是集合 B 的黑名单。 |
