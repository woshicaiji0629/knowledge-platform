## ROW comparison not supported for fields with null elements
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
ROW比较不支持带有NULL值的字段。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
在SQL语句中使用了包含NULL值元素的ROW类型比较操作，例如使用=或!=运算符进行比较。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
在行比较之前，需要先对包含NULL元素的ROW进行处理。可以使用类似IS NULL或者IS NOT NULL的操作符将NULL值筛选出来，或者使用COALESCE函数对NULL值进行处理。另外，也可以在日志数据写入和处理过程时，中早对包含NULL元素的行进行处理，避免出现以上错误。
