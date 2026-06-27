## max distinct num is:10, please use approx_distinct[​](https://sls.aliyun.com/doc/sqlerror/max_distinct_num_10.html#max-distinct-num-is-10-please-use-approx-distinct)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
单个Query中限制最多使用10个distinct。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
您在SQL中使用了超过10个distinct计算。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
减少SQL中使用的distinct数量到10个以下。
使用approx_distinct替换distinct。
