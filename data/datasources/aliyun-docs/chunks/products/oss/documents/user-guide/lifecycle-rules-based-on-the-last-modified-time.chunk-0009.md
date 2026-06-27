### 匹配元素
按前缀匹配：按指定前缀匹配Object和碎片。可创建多条规则匹配不同的前缀，前缀不能重复。前缀的命名规范与Object命名规范相同，详情请参见[对象（Object）](../terms-2.md)。
按[标签](object-tagging-8.md)匹配：按指定标签的Key和Value匹配Object。单条规则可配置多个标签，仅当Object包含所有标签时执行生命周期规则。

| 生命周期规则设置的标签 | Object 携带的标签 | 生命周期规则是否作用于该 Object |
| --- | --- | --- |
| a:1,b:2 | a:1 | 否 |
| a:1,b:3 | 否 |  |
| a:1,b:2 | 是 |  |
| a;1,b:2,c:3 | 是 |  |

说明
标签匹配规则不作用于碎片。
按前缀+标签匹配：按指定前缀和标签的筛选条件匹配对象。
配置到整个Bucket：匹配整个Bucket内的所有Object和碎片。
NOT元素：如果您希望按照生命周期规则对与前缀和标签匹配的Object进行相应处理的同时，跳过不需要处理的Object，您可以通过NOT元素对不需要处理的Object指定前缀和标签。关于NOT元素的配置示例，请参见[NOT](lifecycle-rules-based-on-the-last-modified-time.md)[示例](lifecycle-rules-based-on-the-last-modified-time.md)。
重要
生命周期规则现支持多 NOT 元素配置，但该功能处于邀测状态，尚未对所有用户开放使用，可联系[技术支持](https://selfservice.console.aliyun.com/ticket/createIndex)申请使用。
单个 Bucket 的 NOT 元素总数上限为 1000；单条规则的 NOT 元素上限为 100，所有规则中的Prefix元素总数上限为2000。
使用多 NOT 元素后，后续的生命周期规则操作请使用控制台管理。
如果多 NOT 元素配置功能尚未开通，请勿通过配置多条规则分别 NOT 不同子目录的方式来替代。不同规则的 NOT 元素互不影响——若 rule1 仅排除了 dir/p1/，dir/p2/ 仍会被 rule1 匹配删除；若 rule2 仅排除了 dir/p2/，dir/p1/ 仍会被 rule2 匹配删除，最终导致 dir/ 下所有文件被删除。
