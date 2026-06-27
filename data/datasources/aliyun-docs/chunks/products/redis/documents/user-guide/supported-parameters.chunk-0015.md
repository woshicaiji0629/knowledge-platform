英文逗号（,）分隔。 说明 为避免影响性能， #no_loose_statistics-cmds 和 #no_loose_statistics-keys 参数中设置的值不宜设置过多，并确保仅在故障排查或运维需要时开启。 从您可以通过日志服务控制台下载审计日志（下载方法参见 [下载审计日志](download-audit-logs.md) ），然后通过关键字过滤所需信息： type 值为 7：表示 IP 地址的 QPS 统计信息。 type 值为 8：表示 IP 地址建连统计信息。 type 值为 9：表示 Key 统计信息。 type 值为 10：表示命令统计信息。 |
| ptod_enabled | 是否将客户端的 IP 地址透传到数据节点，取值： 0 ：不透传，访问数据节点的 IP 地址均为代理节点的 IP 地址。 1 （默认）：透传。 |
| readonly_lua_route_ronode_enable | 开启或关闭只读副本的 Lua 执行模式，取值： 0 （默认）：关闭 Lua 执行模式，只读副本不支持 Lua，Lua 命令会由主节点处理。 1 ：开启 Lua 执行模式，仅包含读操作的 Lua 会被转发到只读副本处理。 |
| read_request_only_ronode_whenrwsplit_enable | 开启或关闭只读账号请求定向转发，取值： 0 （默认）：关闭定向转发，只读账号的请求将按照权重分配到各节点，包括主节点。 1 ：开启定向转发，只读账号的请求将定向转发到只读副本，不会转发到主节点。 |
| rt_threshold_ms | Proxy 节点的慢日志阈值，单位为毫秒（ms），取值范围为[30-2000]，默认为 500。 如果从 Proxy 节点向数据节点发出请求后，到 Proxy 节点收到响应结束的时间超过该阈值，则会生成一条慢日志。 |
| script_check_enable | 开启或关闭代理节点对 Lua 脚本的检测，具体检查项请参见 [Proxy](../support/usage-of-lua-scripts.md) [对](../support/usage-of-lua-scripts.md) [Lua](../support/usage-of-lua-scripts.md) [的检测项](../support/usage-of-lua-scripts.md) ，取值： 0 ：不检查。若执行 Lua 的实例账号权限为只读时， 仍会开启检查。 1 （默认）：检查。 |
| sentinel_compat_enable | 在集群架构代理模式或读写分离架构，开启或关闭哨兵（Sentinel）兼容模式，可选值： 1 ：开启。 0 （默认）：关闭。 |
| transfer_subscrible_to_p
