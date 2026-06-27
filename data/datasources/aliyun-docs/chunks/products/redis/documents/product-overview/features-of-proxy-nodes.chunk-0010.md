## 常见问题
Q：是否支持将只进行读操作的Lua脚本转发至只读节点吗？
A：支持，但需要满足以下条件。
使用只读账号，更多信息请参见[创建与管理账号](../user-guide/create-and-manage-database-accounts.md)。
将实例的readonly_lua_route_ronode_enable参数的值设置为1，即仅包含读操作的Lua脚本会被转发到只读副本处理。具体操作，请参见[设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md)。
Q：代理（Proxy）模式和直连模式有什么区别，推荐使用什么模式？
A：推荐使用代理模式，介绍与区别如下：
代理模式：客户端的请求由代理节点转发至数据分片，可享受代理节点带来的负载均衡、读写分离、故障转移、[代理查询缓存](../user-guide/use-read-write-splitting-to-mitigate-issues-caused-by-hotkeys.md)、长连接等特性能力。
直连模式：可通过直连地址绕过代理，直接访问后端的数据分片（类似连接原生Redis集群）。相比代理模式，直连模式节约了通过代理处理请求的时间，可以在一定程度上提高Redis服务的响应速度。
Q：为什么控制台上只有一个数据分片的Pub/Sub监控组有数值显示，而其他分片没有？
A：Proxy会根据channel name进行Hash计算，并路由至对应数据分片，所以在channel数量较少或仅有1个的情况下，仅会路由到一个数据分片上。
如果Pub/Sub的路由仅集中在一个数据分片上，当channel的数据量和流量较大时，会造成该数据分片的CPU使用率和出入流量明显高于其他分片，从而造成资源使用不均衡。
建议多发布几个不同名称的channel，以便Proxy根据Hash计算将channel平均地分布于各个数据分片中。
Q：如果后端的某个数据分片出现异常，对数据读写有什么影响？
A：如果您的实例为[集群版-单副本](https://help.aliyun.com/zh/document_detail/59201.html#concept-ydy-g24-tdb)，由于仅具有主节点，无法保障数据可用性和服务连续性。推荐选择[集群架构](cluster-master-replica-instances.md)，数据分片均采用主备高可用架构，当主节点发生故障后，系统会自动进行主备切换保证服务高可用。在某些极端场景下某个数据分片出现异常后，对数据的影响及优化方案如下。
