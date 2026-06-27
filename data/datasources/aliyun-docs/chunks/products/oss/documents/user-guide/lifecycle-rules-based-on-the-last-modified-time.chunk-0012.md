### 相同前缀和标签
当不同生命周期规则作用于相同前缀和标签的Object时，删除操作优先于存储类型转换操作。rule1用于指定所有前缀为abc，标签为a=1的Object 20天后删除，rule2规则不生效。

| rule | prefix | tag | action |
| --- | --- | --- | --- |
| rule1 | abc | a=1 | 20 天后删除 |
| rule2 | abc | a=1 | 20 天后转为 Archive |
