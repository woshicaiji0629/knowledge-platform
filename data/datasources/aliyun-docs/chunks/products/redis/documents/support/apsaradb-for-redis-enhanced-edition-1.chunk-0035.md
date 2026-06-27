ash 新增 exhgetAll2 接口，用于订正命令的响应格式。 |
| 缺陷修复 | 修正未设置正确白名单时，实例返回的错误提示，由 (error) ERR invalid password 修正为 (error) ERR illegal address 。 修复使用 TairGIS 操作多个 POLYGON 时可能出现的内存泄露问题。 修复 TairDoc 的默认路径问题。 修复 Pub 和 Sub 类命令在多线程引擎中，可能出现的竞争问题。 |  |  |  |
| 1.3.1 | HIGH | 2020-04-03 | 新特性 | 支持数据闪回功能，最长可恢复 7 天内任意时间点的 Tair 数据，避免误操作带来的数据损失，极大降低了运维复杂度，实时保护用户数据。 TairGIS 支持兼容 Redis GEO 相关命令。 TairBloom 支持对 BFRESERVE 接口的容量安全校验。 TairHash 支持更多新特性： EXHSET 、 EXHEXPIRE 、 EXHINCRBY 、 EXHINCRBYFLOAT 等命令增加了 NOACTIVE 选项，在某些场景下可降低内存开销。 EXHINCRBY 增加了 MAX 和 MIN 选项，实现边界保证。 EXHLEN 增加了 noexp 选项，用于返回真实长度。 支持 Hash 结构下的 HINCRBY 和 HINCRBYFLOAT 命令，可使用此命令事务性能力，对同一 Key 下的多个 field 做同增和同减操作。 |
| 功能优化 | 优化数据结构模块的使用。 大幅提升 JedisCluster 客户端在集群架构实例中，执行 MGET 和 MSET 的性能。 |  |  |  |
| 缺陷修复 | 修复 binlog 占用空间溢出的问题。 修复热点 Key 在被执行逐出时可能出现的崩溃问题。 修复 TairHash 可能出现的 double deallocation 引发崩溃的问题。 修复关闭审计日志时因 UAF（Use-After-Free）导致的崩溃问题。 |  |  |  |
| 1.0.10 | LOW | 2020-02-19 | 新特性 | 增加 BITFIELD_RO 命令，大幅优化其在读写分离场景下的性能。 说明 如果 BITFIELD 命令只有 get 选项，Proxy 节点会将此命令转换为 BITFIELD_RO 并转发到后端多个数据分片上。 |
| 1.0.9 | HIGH | 2020-02-19 | 缺陷修复 | 修复执行 Lua 脚本中的某些复杂命令时导致的复制进程崩溃的问题。 |
| 1.0.8 | HIGH | 2020-02-10 | 功能优化 | 优化流控的算法和性能。 |
| 缺陷修复 | 修复由于客户端 output buffer 堆积触发服务端过载保
