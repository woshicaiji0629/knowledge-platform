|
| net.bridge.bridge-nf-call-iptables | 使桥接设备在二层转发时应用 iptables 三层规则，以确保网络安全策略生效。 | 1 |  |
| fs.inotify.max_user_instances | 限制单个用户可创建的 inotify 监视器数量，防止资源耗尽。 | 16384 |  |
| fs.inotify.max_queued_events | 设置内核队列中可缓存的文件系统事件数量。 | 16384 |  |
| fs.may_detach_mounts | 允许内核在挂载点仍被进程访问时将其从命名空间中安全分离，避免整个命名空间被锁定。 | 1 |  |
