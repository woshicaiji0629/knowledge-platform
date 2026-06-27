## The specified key does not exist.[​](https://sls.aliyun.com/doc/sqlerror/oss_access_key_not_exist.html#the-specified-key-does-not-exist)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
这通常发生在您使用OSS做外表关联查询时，访问OSS bucket失败：指定Key不存在。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
您正在访问的OSS bucket中不存在指定的对象，可能已被删除或者从未存在。这有可能是您指定了错误的OSS bucket端点，也可能是您指定了错误的对象Key。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
检查OSS bucket和待访问对象Key名称，确保无误。
前往OSS确认指定对象Key是否存在于指定的OSS bucket中。
