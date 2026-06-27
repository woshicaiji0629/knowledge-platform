## All COALESCE operands must be the same type: *[​](https://sls.aliyun.com/doc/sqlerror/coalesce_operands_must_be_the_same_type.html#all-coalesce-operands-must-be-the-same-type)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
COALESCE函数中的所有参数必须类型一致。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
在COALESCE函数中，操作数必须具有相同的数据类型，否则会出现数据类型错误。在此错误中，操作数中至少有一个是布尔类型，而其他操作数则具有不同的数据类型，例如数字、字符串等。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
请检查COALESCE函数中的每个操作数，并确保它们具有相同的数据类型。如果数据类型不同，请进行数据类型转换，以使它们具有相同的数据类型。可以使用CAST函数执行数据类型转换。
