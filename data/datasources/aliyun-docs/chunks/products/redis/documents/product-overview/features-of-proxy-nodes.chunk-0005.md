## 代理查询缓存
代理节点支持缓存：包含热点Key的请求和对应查询结果。当Proxy在缓存有效期内收到同样请求时，将直接返回结果至客户端，无需和后端的数据分片交互。本功能可缓解或预防热点Key读请求引发的访问性能倾斜问题。
此热点Key与[Top Key](../user-guide/use-the-real-time-key-statistics-feature.md)[统计](../user-guide/use-the-real-time-key-statistics-feature.md)功能中的热Key（QPS）一致，由数据库内核根据排序和统计算法进行识别。默认为Key的QPS超过5000，也可以通过bigkey-threshold参数自定义阈值。
若热点Key在缓存有效期内被修改，其修改结果不会同步至缓存中。即后续请求可能会读到缓存中的脏数据，直至缓存失效。对此，您可以根据实际情况缩短缓存有效期。
说明
Proxy节点并不缓存整个热点Key，而是缓存包含热点Key的请求和对应查询结果。
本功能仅支持Tair内存型、持久内存型实例，且实例为集群架构代理模式或读写分离架构。
应用场景
适用于热搜榜单、大V用户信息、游戏公告等场景，应用程序能够容忍稍旧的数据。
功能架构使用方法
本功能默认关闭，您可以设置query_cache_enabled[参数](../user-guide/parameter-support.md)开启该功能。
查看使用方法详细说明
