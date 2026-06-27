## IN value and list items must be the same type: varchar
错误描述[​](https://sls.aliyun.com/doc/sqlerror/in_value_and_list_must_be_the_same_type.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
SQL语句中存在语法错误，IN子句中的值和列表项必须是同一数据类型：varchar。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/in_value_and_list_must_be_the_same_type.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
在使用IN操作符进行查询时，提供的值和列表项数据类型不一致，例如值为varchar类型，列表项为整数类型。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/in_value_and_list_must_be_the_same_type.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
确保IN操作符中提供的值和列表项数据类型一致。可以使用CAST或CONVERT函数将数据类型进行转换，或者将值和列表项都转换为相同的数据类型后再进行查询。另外，建议在写入日志时，对应的列字段应该使用相同的数据类型，以避免类似的错误。
