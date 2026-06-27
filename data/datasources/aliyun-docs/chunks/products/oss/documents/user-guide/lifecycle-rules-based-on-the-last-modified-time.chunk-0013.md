### 前缀重叠+标签相同
rule1用于指定所有标签为a=1的Object 10天后转为IA。rule2用于指定前缀为abc且标签为a=1的Object 120天后删除。

| rule | prefix | tag | action |
| --- | --- | --- | --- |
| rule1 | - | a=1 | 10 天后转为 IA |
| rule2 | abc | a=1 | 120 天后被删除 |

rule3用于指定所有标签为a=1的Object 20天后转为Archive。由于Archive类型文件无法转换为IA类型，因此rule4指定的前缀为abc且标签为a=1的Object 30天后转为IA的规则不生效。

| rule | prefix | tag | action |
| --- | --- | --- | --- |
| rule3 | - | a=1 | 20 天后转为 Archive |
| rule4 | abc | a=1 | 30 天后转为 IA |
