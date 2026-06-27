## 命令列表
表 1.TairBloom命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [BF.RESERVE](tairbloom-command.md) | BF.RESERVE key error_rate capacity | 创建一个大小为 capacity，错误率为 error_rate 的空的 TairBloom。 |
| [BF.ADD](tairbloom-command.md) | BF.ADD key item | 在 Key 指定的 TairBloom 中添加一个元素。 |
| [BF.MADD](tairbloom-command.md) | BF.MADD key item [ item ...] | 在 Key 指定的 TairBloom 中添加多个元素。 |
| [BF.EXISTS](tairbloom-command.md) | BF.EXISTS key item | 检查一个元素是否存在于 Key 指定的 TairBloom 中。 |
| [BF.MEXISTS](tairbloom-command.md) | BF.MEXISTS key item [ item ...] | 同时检查多个元素是否存在于 Key 指定的 TairBloom 中。 |
| [BF.INSERT](tairbloom-command.md) | BF.INSERT key [CAPACITY cap ] [ERROR error ] [NOCREATE] ITEMS item [ item ...] | 在 Key 指定的 TairBloom 中一次性添加多个元素，添加时可以指定大小和错误率，且可以控制在 TairBloom 不存在的时候是否自动创建。 |
| [BF.INFO](tairbloom-command.md) | BF.INFO key | 查看 Key 指定的 TairBloom 内部信息，如当前层数和每一层的元素个数、错误率等。 |
| [DEL](https://valkey.io/commands/del/) | DEL key [key ...] | 使用原生 Redis 的 DEL 命令可以删除一条或多条 TairBloom 数据。 说明 已加入 TairBloom 数据中的元素无法单独删除，您可以使用 DEL 命令删除整条 TairBloom 数据。 |

说明
本文的命令语法定义如下：
大写关键字：命令关键字。
斜体：变量。
[options]：可选参数，不在括号中的参数为必选。
A|B：该组参数互斥，请进行二选一或多选一。
...：前面的内容可重复。
