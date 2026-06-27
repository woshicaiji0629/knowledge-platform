## Key not present in map[​](https://sls.aliyun.com/doc/sqlerror/key_not_in_map.html#key-not-present-in-map)
错误描述[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E9%94%99%E8%AF%AF%E6%8F%8F%E8%BF%B0)
Map中不存在指定key。
报错原因[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E5%8F%AF%E8%83%BD%E5%8E%9F%E5%9B%A0)
您在SQL中使用了map类型，并指定了一个不存在的key。
解决方法[​](https://sls.aliyun.com/doc/sqlerror/pattern_cannot_access_group.html#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95)
检查map类型数据，确认您指定的key在map中存在。
如果map类型数据中有可能不存在该key，您可以使用try函数将map访问包裹，以忽略该错误，例如：
SELECT try(map['name']) -- map是一个map类型列，如果该列中不存在名为'name'的key，则返回NULL
