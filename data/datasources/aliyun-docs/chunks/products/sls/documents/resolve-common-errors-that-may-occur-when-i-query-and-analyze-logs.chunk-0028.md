## Left side of LIKE expression must evaluate to a varchar (actual: bigint)[​](https://sls.aliyun.com/doc/sqlerror/left_side_of_like_expression_must_evaluate_to_a_varchar.html#left-side-of-like-expression-must-evaluate-to-a-varchar-actual-bigint)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
LIKE表达式左侧必须为varchar类型（实际为bigint）。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
该错误通常发生在您尝试使用LIKE运算符比较bigint数据类型与varchar数据类型时。 LIKE运算符要求表达式的两侧具有相同的数据类型。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
您可能需要使用CAST函数将bigint转换为varchar。
SELECT * FROM table WHERE CAST(bigint_column AS varchar) LIKE 'pattern'
这将会把bigint_column转换为varchar，然后可以使用LIKE运算符将其与指定模式进行匹配。
