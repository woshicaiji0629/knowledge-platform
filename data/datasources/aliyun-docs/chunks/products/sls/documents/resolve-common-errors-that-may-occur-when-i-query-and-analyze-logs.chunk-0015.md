## ts_compare must gropu by timestamp,your grouping by type is :bigint[​](https://sls.aliyun.com/doc/sqlerror/ts_compare_must_group_by_timestamp.html#ts-compare-must-gropu-by-timestamp-your-grouping-by-type-is-bigint)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
ts_compare函数必须按timestamp类型分组。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
您在SQL中使用ts_compare函数时，group by的列，可能是非timestamp类型的数值型或其他类型。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
请确保ts_compare函数对应的group by列类型使用正确的timestamp类型，您可以使用[from_unixtime](date-and-time-functions-1.md)[函数](date-and-time-functions-1.md)等函数将整型时间戳转换成timestamp类型。
