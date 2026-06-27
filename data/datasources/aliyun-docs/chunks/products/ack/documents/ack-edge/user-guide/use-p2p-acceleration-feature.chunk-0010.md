### 指标说明
指标名
DADIP2P_Alive：服务是否存活。
DADIP2P_Read_Throughtput：P2P服务吞吐，单位：byte/s。
DADIP2P_QPS：QPS。
DADIP2P_MaxLatency：延迟统计，单位：us。
DADIP2P_Count：流量统计，单位：bytes。
DADIP2P_Cache：单机Cache用量，单位：bytes。
Tag
node：P2P Agent/Root的服务IP和端口。
type：指标类型。
pread：处理下游请求。
download：回源。
peer：P2P网络分发。
disk：处理磁盘。
http：处理HTTP请求。
allocated：缓存分配空间。
used：缓存使用空间。
指标示例
DADIP2P_Count{node="11.238.108.XXX:9877",type="http",mode="agent"} 4248808352.000000 1692157615810 Agent服务累计处理HTTP请求流量：4248808352字节。 DADIP2P_Cache{node="11.238.108.XXX:9877",type="used",mode="agent"} 2147487744.000000 1692157615810 当前Agent缓存用量：2147487744字节。
