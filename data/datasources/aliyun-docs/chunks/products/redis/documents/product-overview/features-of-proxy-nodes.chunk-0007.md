您可以通过Tair自研的QUERYCACHE KEYS、QUERYCACHE INFO、QUERYCACHE LISTALL命令，查看代理查询缓存的使用情况。
查看使用情况
QUERYCACHE KEYS
命令格式：QUERYCACHE KEYS
命令描述：查询代理节点中已缓存的所有热点Key，将返回每个热点Key的数据库名和Key名称信息。
命令示例：
QUERYCACHE KEYS
返回示例：
1) 1) (integer) 0 2) "key:000000000003" 2) 1) (integer) 0 2) "key:000000000001" 3) 1) (integer) 0 2) "key:000000000002" 4) 1) (integer) 0 2) "key:000000000000"
QUERYCACHE INFO
命令格式：QUERYCACHE INFO
命令描述：获取代理查询缓存的运行情况。
命令示例：
QUERYCACHE INFO
返回示例：
1) "put_qps:4.00" 2) "get_qps:16570.00" 3) "hit_rate:99.98" 4) "memory_size:180" 5) "query_count:4" 6) "bandwidth_limit_query_cnt:0" 7) "qps_limit_query_cnt:0"
返回示例说明：
put_qps：数据节点每秒往Querycache写入的次数。
get_qps：客户端每秒从Querycache中读取的次数。
hit_rate：缓存的命中率。
memory_size：缓存数据占用的内存容量，单位为字节。
query_count：已缓存的请求的数量。
bandwidth_limit_query_cnt：因带宽限制访问Querycache被限流的次数，默认未开启限制。
qps_limit_query_cnt：因QPS限制访问Querycache被限流的次数，默认未开启限制。
QUERYCACHE LISTALL
命令格式：QUERYCACHE LISTALL
命令描述：获取已缓存的所有请求命令。
命令示例：
QUERYCACHE LISTALL
返回示例：
1) 1) (integer) 0 2) "*2\r\n$3\r\nGET\r\n$16\r\nkey:000000000000\r\n" 3) (integer) 668 2) 1) (integer) 0 2) "*2\r\n$3\r\nGET\r\n$16\r\nkey:000000000001\r\n" 3) (integer) 668 3) 1) (integer) 0 2) "*2\r\n$3\r\nGET\r\n$16\r\nkey:000000000003\r\n" 3
