## Array subscript out of bounds[​](https://sls.aliyun.com/doc/sqlerror/array_subscript_out_of_bounds.html#array-subscript-out-of-bounds)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/array_subscript_out_of_bounds.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
数组下标越界。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/array_subscript_out_of_bounds.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
您使用数组时，正在尝试访问了一个超出数组范围的索引位置。例如，访问负数索引、超出数组长度的索引等。这可能是因为SQL中存在错误的逻辑或者数据输入错误。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/array_subscript_out_of_bounds.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
SQL中数组索引位置从1开始计起，请检查SQL中数组的有效长度，然后检查数组索引位置的引用情况，并确保数组的下标没有超出范围。
