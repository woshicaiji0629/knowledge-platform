## GROUP BY clause cannot contain aggregations or window functions: *[​](https://sls.aliyun.com/doc/sqlerror/group_by_clause_cannot_contain_aggregations_or_window_functions.html#group-by-clause-cannot-contain-aggregations-or-window-functions)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
GROUP BY子句不能包含聚合函数或窗口函数。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
在GROUP BY子句中包含聚合函数或窗口函数。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
请在GROUP BY子句中只包含列名，而不是聚合函数或窗口函数。聚合函数和窗口函数应该在SELECT语句中使用，而不是在GROUP BY子句中使用。如果您需要在GROUP BY子句中使用聚合函数，则可以使用列的别名或数字索引来代替聚合函数。例如，使用以下查询：
SELECT column1, column2, COUNT(column3) as count_column3 FROM table GROUP BY column1, column2, 3
在这个查询中，count_column3 是 COUNT(column3) 的别名，3 是 COUNT(column3) 在SELECT语句中的位置。请注意，使用数字索引可能会使代码难以理解，建议使用列别名。
