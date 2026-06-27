| 字段名称 | 说明 | 默认值 | 是否支持控制台或 OpenAPI 配置 |
| --- | --- | --- | --- |
| fs.aio-max-nr | 异步 I/O 操作的最大数量。 | 65536 |  |
| fs.file-max | 系统级别能够打开的最大文件句柄数。 | 2097152 |  |
| fs.inotify.max_user_watches | 单用户能够创建的 inotify 监视的最大数量。 | 524288 |  |
| fs.nr_open | 每个进程能够打开的文件描述符数的最大数量。 此值应小于 fs.file-max 的取值 | 1048576 |  |
| kernel.pid_max | 系统可分配的最大 PID 数量。 | 4194303 |  |
| kernel.threads-max | 系统可创建的最大线程数量。 | 504581 |  |
| net.core.netdev_max_backlog | 接口接收数据包的速度快于内核的处理速度时，可以在 INPUT 端排队的数据包的最大数量。 | 16384 |  |
| net.core.optmem_max | 每个网络套接字允许的最大辅助缓冲区（Ancillary Buffer）大小，以字节为单位。 | 20480 |  |
| net.core.rmem_max | 每个网络套接字接收缓冲区的最大大小，以字节为单位。 | 16777216 |  |
| net.core.wmem_max | 每个网络套接字发送缓冲区的最大大小，以字节为单位。 | 16777216 |  |
| net.core.wmem_default | 每个网络套接字发送缓冲区的默认大小，以字节为单位。 | 212992 |  |
| net.ipv4.tcp_mem | TCP 栈可以使用的内存量，以内存页（大小通常为 4KB）为单位。该参数由三个整数值组成，分别表示低水位、压力水位和最高水位，必须严格按照顺序设置。 | 根据系统总内存动态计算 |  |
| net.ipv4.neigh.default.gc_thresh1 | ARP 缓存中保留的最少条目数。缓存中的条目数量低于此值时，系统不会执行垃圾收集。 | 系统预设置 |  |
| net.ipv4.neigh.default.gc_thresh2 | ARP 缓存中的最大条目数，为软限制，即缓存中的条目数量达到此值时，系统会开始考虑执行垃圾收集，但不会立即强制执行，而会等待 5 秒延迟。 | 1024 |  |
| net.ipv4.neigh.default.gc_thresh3 | ARP 缓存中要保留的最大条目数，为硬限制，即缓存中的条目数量达到此值时，系统会立即执行垃圾收集。如果缓存中的
