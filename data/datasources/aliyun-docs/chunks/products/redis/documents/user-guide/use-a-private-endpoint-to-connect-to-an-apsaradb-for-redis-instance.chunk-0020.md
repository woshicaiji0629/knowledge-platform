| 参数 | 默认配置 | 说明 | 修改配置 |
| --- | --- | --- | --- |
| enablePeriodicRefresh(Duration refreshPeriod) | 关闭 | 启用后将进行周期性集群拓扑刷新。 | 建议配置为 60s。 开启此配置可以使不活跃的长连接也能及时更新本地拓扑。 |
| dynamicRefreshSources(boolean dynamicRefreshSources) | true | 为 true 时，使用 Cluster Nodes 命令返回的所有节点进行集群拓扑刷新；为 false 时，使用指定节点地址。 | 如无特殊需求，应配置为 false。 启用此选项会向所有节点发送 CLUSTER NODES 命令，增加服务端压力。此外，在变配期间，使用 endpoint 地址更新拓扑通常更为迅速可靠。 |
| enableAllAdaptiveRefreshTriggers() | 关闭 | 启用后，当收到 MOVED 消息时，会自动刷新集群拓扑。 | 必须启用。 启用此配置才能确保拓扑变更后 Lettuce 能及时更新本地拓扑。 |
| adaptiveRefreshTriggersTimeout(Duration timeout) | 30s | 限制集群拓扑刷新频率，在指定时间内仅允许一次刷新。 | 建议配置为 15s。 由于集群中多个节点的拓扑变更并非原子操作，Lettuce 触发的初次拓扑刷新可能会失败，因此需要快速进行后续刷新以确保拓扑正确更新。当应用数量较少时，由于不会有大量客户端同时发送 CLUSTER NODES 命令，可以适当降低该值，以实现更快的拓扑表收敛时间。 |
| validateClusterNodeMembership(boolean validateClusterNodeMembership) | true | 在拓扑变化时，Lettuce 使用 MOVED 将命令重定向到正确的节点。启用此配置后，只允许将命令重定向到 CLUSTER NODES 输出中已知的节点。 | 必须配置为 false。 配置为 false 可以防止在集群拓扑变更后，本地拓扑刷新完成前无法访问新增节点。 |
