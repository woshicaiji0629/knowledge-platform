## target of repeat operator is not specified[​](https://sls.aliyun.com/doc/sqlerror/target_of_repeat_operator_is_not_specified.html#target-of-repeat-operator-is-not-specified)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/target_of_repeat_operator_is_not_specified.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
重复操作符的目标未指定。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/target_of_repeat_operator_is_not_specified.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
这可能是正则表达式中的错误，提示重复操作符的目标未指定。重复操作符“()”用于匹配前面的字符或组的零个或多个出现，但它需要一个目标来应用重复。例如，"(a) *"表示零个或多个出现的字母"a"。如果没有指定目标，例如在"() *"中，正则表达式引擎将不知道要如何应用重复操作符，从而会抛出该错误。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/target_of_repeat_operator_is_not_specified.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
您需要检查正则表达式中的重复操作符“()”是否有正确的目标，并进行相应修正。
