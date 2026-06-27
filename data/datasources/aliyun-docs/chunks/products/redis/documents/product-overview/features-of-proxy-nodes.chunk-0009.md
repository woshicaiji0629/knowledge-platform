## 连接数使用说明
通常情况下，Proxy通过与数据分片建立长连接来处理请求。当请求中包含以下命令时，Proxy会根据命令的处理需求在相应的数据分片上创建额外的连接，此时连接无法聚合，实例的最大连接数会受到数据节点单个分片的限制（单个分片的限制请参见具体的实例规格）。您需要合理使用下述命令，避免连接数超限。
说明
代理模式下，Redis社区版实例每个数据分片的连接数上限为10,000，Tair（企业版）实例每个数据分片的连接数上限为30,000。
阻塞类命令：BRPOP、BRPOPLPUSH、BLPOP、BZPOPMAX、BZPOPMIN、BLMOVE、BLMPOP、BZMPOP。
事务类命令：MULTI、EXEC、WATCH。
MONITOR类命令：MONITOR、IMONITOR、RIMONITOR。
订阅命令：SUBSCRIBE、UNSUBSCRIBE、PSUBSCRIBE、PUNSUBSCRIBE、SSUBSCRIBE、SUNSUBSCRIBE。
