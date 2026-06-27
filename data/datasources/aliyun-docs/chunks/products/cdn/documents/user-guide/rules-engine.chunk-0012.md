### 匹配运算符（matchOperator）

| 名称 | 域名配置功能函数 [condition](../developer-reference/parameters-for-configuring-features-for-domain-names.md) 中对应的配置参数 | 含义 |
| --- | --- | --- |
| 等于 | matchOperator 为 equals。 | 变量完全等于匹配值或者完全不等于匹配值的时候，条件才成立。 |
| 不等于 | matchOperator 为 equals，并且参数 negate 的值为 true。 |  |
| 存在 | matchOperator 为 exists。 | 变量存在或者不存在时，条件即成立。 |
| 不存在 | matchOperator 为 exists，并且参数 negate 的值为 true。 |  |
| 包含其中任意一个 | matchOperator 为 contains。 | 变量包含（不包含） 任意一个 匹配值的时候，条件即成立。最多支持 32 个匹配值。 包含匹配的情况有两种： 精确匹配：直接输入匹配对象，包含：a，必须=a 才能匹配上。 通配符匹配：可以加入 * 作为通配符，可以支持配置 a* 、 *a 、 *a* ，可以对应 abc、bca、bcabc。 |
| 不包含其中任意一个 | matchOperator 为 contains，并且参数 negate 的值为 true。 |  |
| 大于 | matchOperator 为 gt。 | 即 > |
| 小于 | matchOperator 为 lt。 | 即 < |
| 大于等于 | matchOperator 为 ge。 | 即 >= |
| 小于等于 | matchOperator 为 le | 即 <= |
| 正则匹配 | matchOperator 为 regex。 | 匹配值可以填写正则表达式，实现对变量的正则匹配。 说明 通过控制台或者 OpenAPI 来配置的情况下，无法使用正则相关的匹配运算符（包括正则匹配和正则不匹配），但是可以查看已经存在的配置，如果要使用正则相关的匹配运算符，请 [提交工单](https://selfservice.console.aliyun.com/ticket/createIndex) 申请，或者使用 [边缘安全加速产品](https://www.aliyun.com/product/esa?spm=5176.28536895.J_kUfM_yzYYqU72woCZLHoY.3.11cf586c1lhOVC) 。 |
| 正则不匹配 | matchOperator 为 regex，并且参数 negate 的值为 true。 |  |
