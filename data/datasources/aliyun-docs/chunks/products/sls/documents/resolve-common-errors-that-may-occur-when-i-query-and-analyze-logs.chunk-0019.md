## reading data with pagination only allow reading max[​](https://sls.aliyun.com/doc/sqlerror/pagination_max_1000000_rows.html#reading-data-with-pagination-only-allow-reading-max)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
分页最大行数不能超过1,000,000。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
SLS SQL限制最大输出行数为1,000,000，您正在进行的分页读取请求超过了最大行数限制。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
通过LIMIT子句，限制分页读取最大行数不超过1,000,000。
通过缩小查询范围，限制分页读取最大行数不超过1,000,000。
利用Scheduled SQL服务，分窗口定期进行SQL汇聚分析，然后再对汇聚结果进行二次聚合。
