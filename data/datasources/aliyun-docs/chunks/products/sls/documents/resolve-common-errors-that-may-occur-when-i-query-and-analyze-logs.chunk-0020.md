## Could not choose a best candidate operator. Explicit type casts must be added.[​](https://sls.aliyun.com/doc/sqlerror/could_not_choose_a_best_candidate_operator.html#could-not-choose-a-best-candidate-operator-explicit-type-casts-must-be-added)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
无法选择最佳的候选操作符，必须添加显式类型转换。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
这通常是因为您正在尝试在不同类型变量之间执行算术或比较操作，而系统无法自动识别应该使用哪种类型的操作符。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
您需要添加显式的类型转换来告诉系统应该使用哪种类型的操作符。
例如，如果您正在尝试将一个字符串类型的变量和一个整数类型的变量相加，您可以使用CAST函数来将字符串类型的变量转换为整数类型，然后再执行加法操作。示例代码如下：
SELECT CAST('10' AS INTEGER) + 5;
在这里，我们使用CAST函数将字符串类型的变量'10'转换为整数类型，然后将其与整数类型的变量5相加。这样可以避免出现以上错误。
