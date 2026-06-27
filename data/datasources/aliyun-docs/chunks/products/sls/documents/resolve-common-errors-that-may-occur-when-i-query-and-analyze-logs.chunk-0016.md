## time # is out of specified time range[​](https://sls.aliyun.com/doc/sqlerror/time_out_of_range.html#time-is-out-of-specified-time-range)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
时间戳超出了指定的时间范围。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
在SQL语句中使用了超出指定时间范围的时间戳，可能是由于数据录入错误或者数据类型不匹配导致的。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
检查时间戳是否正确，如果是由于数据类型不匹配导致的，可以尝试使用相关的数据类型转换函数将时间戳转换为正确的数据类型。
