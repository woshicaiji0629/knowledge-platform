### Cannot assign requested address
可能原因：客户端通过短连接访问Tair实例时，产生该报错。
解决方法：使用pconnect替换connect的连接方式，或修改客户端所在ECS实例的tcp_max_tw_buckets内核参数，更多信息请参见[Cannot assign requested address](what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)[报错](what-do-i-do-if-the-cannot-assign-requested-address-error-is-returned-when-i-access-apsaradb-for-redis-over-short-lived-connections.md)。
