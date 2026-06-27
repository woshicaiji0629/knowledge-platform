## 使用桑基图分析请求调度
客户端流量会先被SLB处理，分发到其中一台RealServer中进行实际的业务逻辑处理。SLB可自动检测到不健康的机器并重新分配流量到其它正常服务的RealServer上，等异常机器恢复后再重新分配流量。
为SLB实例添加一个监听，例如服务器（192.168.0.0）同时兼有跳板机职能，其性能是其它三台服务器的4倍，为该服务器设置监听权重为100，其余服务器监听权重为20。执行如下查询分析语句分析请求流量分布情况。
* | select COALESCE(client_ip, vip_addr, upstream_addr) as source, COALESCE(upstream_addr, vip_addr, client_ip) as dest, sum(request_length) as inflow group by grouping sets( (client_ip, vip_addr), (vip_addr, upstream_addr))
[桑基图](display-query-results-in-a-sankey-diagram.md)展示每台RealServer的负载情况，多个客户端向SLB发起请求，请求报文流量基本遵循20:20:20:100比例转发到后端RealServer中。
该文章对您有帮助吗？
反馈
