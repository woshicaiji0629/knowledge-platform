## Expression "*" is not of type ROW[​](https://sls.aliyun.com/doc/sqlerror/expression_is_not_of_type_row.html#expression-is-not-of-type-row)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/expression_is_not_of_type_row.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
表达式'fields'不是ROW类型。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/expression_is_not_of_type_row.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
在使用ROW类型时，表达式“fields”不符合ROW类型的要求。可能是因为在使用ROW函数时，参数不符合要求。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/expression_is_not_of_type_row.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
请检查ROW函数的参数是否正确，并且参数中所有的字段是否存在且符合要求。如果参数正确，但结果仍然不是ROW类型，可以尝试使用CAST函数将其转换为ROW类型。
