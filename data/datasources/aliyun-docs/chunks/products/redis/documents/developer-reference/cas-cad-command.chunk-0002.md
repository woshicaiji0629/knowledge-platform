## 命令列表
表 1.String增强命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [CAS](cas-cad-command.md) | CAS key oldvalue newvalue [EX|PX|EXAT|PXAT time] | CAS（Compare And Set），查看指定的 oldvalue 是否与目标 Key 的 Value 相等，若相等则将 Value 修改成新的值（ newvalue ），不相等则不修改。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAS。 |
| [CAD](cas-cad-command.md) | CAD key value | CAD（Compare And Delete），查看指定 Value 值是否与目标 Key 的 Value 相等，若相等则删除该 Key，不相等则不删除。 说明 该命令仅适用于操作 Redis String 类型的数据，如需对 TairString 做相同的操作，请使用 EXCAD。 |

说明
本文的命令语法定义如下：
大写关键字：命令关键字。
斜体：变量。
[options]：可选参数，不在括号中的参数为必选。
A|B：该组参数互斥，请进行二选一或多选一。
...：前面的内容可重复。
