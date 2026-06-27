### NOT
对同一个Bucket配置多条生命周期规则，且某条生命周期规则涉及NOT元素时，NOT元素指定的行为只对本条生命周期规则生效。具体示例如下：
示例一
通过生命周期规则1，指定examplebucket中前缀为dir/的Object 100天后删除。
通过生命周期规则2，通过NOT元素指定examplebucket中除前缀为dir/以外的所有Object 50天后删除。
以生命周期规则生效时间为起点，examplebucket中Object的删除行为如下表所示。

| Object | 删除行为 |
| --- | --- |
| 前缀为 dir/的 Object | 100 天后删除 |
| 前缀不为 dir/的 Object | 50 天后删除 |

示例二
通过生命周期规则1，通过NOT元素指定examplebucket内除标签（key1:value1）以外的所有Object 30天后删除。
通过生命周期规则2，指定examplebucket内包含标签（key2:value2）的所有Object 50天后删除。
以生命周期规则生效时间为起点，examplebucket内Object的删除行为如下表所示：

| Object | 删除行为 |
| --- | --- |
| 对于未包含以上标签的所有 Object | 30 天后删除 |
| 对于仅包含 key1:value1 标签的 Object | 不删除 |
| 对于仅包含 key2:value2 标签的 Object | 30 天后删除 |
| 对于同时包含 key1:value1 以及 key2:value2 标签的 Object | 50 天后删除 |
