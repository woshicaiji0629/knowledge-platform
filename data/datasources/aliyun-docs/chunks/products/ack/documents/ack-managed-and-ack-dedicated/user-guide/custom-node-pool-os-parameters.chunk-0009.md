软限制，即缓存中的条目数量达到此值时，系统会开始考虑执行垃圾收集，但不会立即强制执行，而会等待 5 秒延迟。 | 1024 |  |
| net.ipv4.neigh.default.gc_thresh3 | ARP 缓存中要保留的最大条目数，为硬限制，即缓存中的条目数量达到此值时，系统会立即执行垃圾收集。如果缓存中的条目数量一直超过此值，系统会不断进行清理。 | 8192 |  |
| user.max_user_namespaces | 单个用户支持创建的 User Namespace 数量上限。 | 0 |  |
| kernel.softlockup_panic | 发生软锁定时，内核会触发 Panic 并重启系统，以快速恢复系统状态。 | 1 |  |
| kernel.softlockup_all_cpu_backtrace | 检测到软锁定时，捕获所有 CPU 的调试信息，便于问题诊断。 | 1 |  |
| vm.max_map_count | 限制单个进程可拥有的最大内存映射区域数量，防止内存过度使用。 | 262144 |  |
| net.core.somaxconn | 设置 Socket 监听队列的最大连接数，控制并发连接处理能力。 | 32768 |  |
| net.ipv4.tcp_wmem | 配置 TCP 连接发送缓冲区的最小值（minimum）、默认值（default）和最大值（maximum）。单位：字节。 此设置直接影响 TCP 连接的网络吞吐量和内存占用。 | 4096 12582912 16777216 |  |
| net.ipv4.tcp_rmem | 配置 TCP 接收缓冲区的最小值（minimum）、默认值（default）和最大值（maximum）。单位：字节。 此设置直接影响 TCP 连接的网络吞吐量和内存占用。 | 4096 12582912 16777216 |  |
| net.ipv4.tcp_max_syn_backlog | 限制 SYN 队列中未完成三次握手的连接请求数量。 | 8096 |  |
| net.ipv4.tcp_slow_start_after_idle | 控制 TCP 连接在长时间空闲后是否重新使用慢启动算法。 | 0 |  |
| net.ipv4.ip_forward | 启用 IPv4 数据包转发功能，允许系统作为路由器转发数据包。 | 1 |  |
| net.bridge.bridge-nf-call-iptables | 使桥接设备在二层转发时应用 iptables 三层规则，以确保网络安全策略生效。 | 1 |  |
| fs.inotify.max_user_instances | 限制单个用户可创建的 inotify 监视器数量，防止资源耗尽。 |
