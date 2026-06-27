## Multiple columns returned by subquery are not yet supported.[​](https://sls.aliyun.com/doc/sqlerror/multiple_columns_returned_by_subquery_not_supported.html#multiple-columns-returned-by-subquery-are-not-yet-supported)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
标量查询不支持返回多个列。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
在子查询中SELECT了多个列。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
确保子查询只返回一列或一个值，可以修改子查询或主查询。另外，还可以尝试使用JOIN语句代替子查询来检索所需的数据。
