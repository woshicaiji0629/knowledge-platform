## 索引过滤语法
您可以根据Skey的标签（LABELS）过滤目标Skey。过滤条件（filter）的语法如下：
说明
构造filter时，支持如下所有命令及组合使用，但必须存在EQ、CONTAINS、LIST_MATCH逻辑中的任意一个。

| filter 命令 | 说明 | 逻辑 |
| --- | --- | --- |
| L = V | 标签 L 等于 V。 | EQ（equals） |
| L != | 标签 L 不为 NULL, 即目标 Skey 包含标签 L。 | CONTAINS |
| L = (v1,v2,...) | 标签 L 为 v1 或 v2 等。 | LIST_TMATCH |
| L != V | 标签 L 不等于 V。 | NOEQ（equals） |
| L = | 标签 L 为 NULL, 即目标 Skey 不包含标签 L。 | NOCONTAINS |
| L != (v1,v2,...) | 标签 L 不为 v1 和 v2 等。 | LIST_NOTMATCH |
