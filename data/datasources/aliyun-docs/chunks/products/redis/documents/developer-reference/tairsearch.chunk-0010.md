表 2.自动补齐命令

| 命令 | 语法 | 说明 |
| --- | --- | --- |
| [TFT.ADDSUG](tairsearch.md) | TFT.ADDSUG index text weight [text weight] ... | 在指定索引中，添加自动补全的文本及对应权重，支持添加多个文本。 |
| [TFT.DELSUG](tairsearch.md) | TFT.DELSUG index text [text] ... | 在指定索引中，删除自动补全的文本，支持删除多个文本。 |
| [TFT.SUGNUM](tairsearch.md) | TFT.SUGNUM index | 获取指定索引中自动补全文本的数量。 |
| [TFT.GETSUG](tairsearch.md) | TFT.GETSUG index prefix [MAX_COUNT count] [FUZZY] | 根据指定前缀，查询匹配的自动补全文本，将优先返回权重比较高的 text。 |
| [TFT.GETALLSUGS](tairsearch.md) | TFT.GETALLSUGS index | 获取指定索引的全量自动补全文本。 |

说明
本文的命令语法定义如下：
大写关键字：命令关键字。
斜体：变量。
[options]：可选参数，不在括号中的参数为必选。
A|B：该组参数互斥，请进行二选一或多选一。
...：前面的内容可重复。
