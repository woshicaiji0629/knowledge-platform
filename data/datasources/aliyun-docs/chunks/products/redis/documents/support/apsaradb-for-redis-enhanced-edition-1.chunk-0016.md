| 小版本号 | 更新级别 | 发布日期 | 类型 | 说明 |
| --- | --- | --- | --- | --- |
| 2.7.3 | HIGH | 2026-05-06 | 缺陷修复 | 提升稳定性。 |
| 2.7.2 | HIGH | 2026-02-05 | 缺陷修复 | 提升稳定性。 |
| 2.7.1 | HIGH | 2026-01-05 | 功能优化 | LUA 支持在 worker 线程中执行（默认关闭，可通过 [设置参数](../user-guide/modify-the-values-of-parameters-for-an-instance.md) script-run-in-worker-threads 值为 yes 开启）。 |
| 缺陷修复 | 提升稳定性。 |  |  |  |
| 2.7.0 | HIGH | 2025-11-24 | 功能优化 | 支持 [离线全量](../user-guide/offline-key-analysis.md) [Key](../user-guide/offline-key-analysis.md) [分析](../user-guide/offline-key-analysis.md) 。 |
| 缺陷修复 | 提升稳定性。 |  |  |  |
| 2.6.1 | HIGH | 2025-11-06 | 功能优化 | 优化 zset 的 zrange/zremrange/zpopmin/zpopmax 接口的性能：在 zset 通过 zremrange(by rank 或者 by score)、zpopmin 或 zpopmax 接口一端删除，而另一端写入， 即 score 递增或递减时，zrange/zremrange/zpopmin/zpopmax 不受已删除但未实际回收的数据的影响。 支持查询慢日志条数查询。 优化 optimise-huge-value 开启后的吞吐稳定性。 |
| 缺陷修复 | 提升稳定性。 |  |  |  |
| 2.6.0 | MEDIUM | 2025-09-23 | 新特性 | 支持实时 TopKey 分析功能，包括热 Key 和大 Key。 |
| 功能优化 | 支持 DTS 全量传输时的断点续传。 新增 optimise-huge-value 参数，开启后可提升约 2 倍大 Value 写入性能。 优化长 Key 的索引大小，提高性能。 |  |  |  |
| 缺陷修复 | 提升 SCAN 命令的稳定性。 |  |  |  |
| 2.5.8.1 | LOW | 2025-09-15 | 功能优化 | 提升在小数据量、低写入流量场景下的 CPU 稳定性。 |
| 2.5.8 | MEDIUM | 2025-08-08 | 功能优化 |
