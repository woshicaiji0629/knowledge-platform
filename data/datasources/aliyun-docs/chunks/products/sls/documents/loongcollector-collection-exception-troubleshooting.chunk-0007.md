### 日志正常采集中突发异常
日志可以正常采集说明配置项大概率正确，若没有修改内容或新增相关采集配置时，可优先关注是否需要调整采集性能与提升配额。
尝试调整采集性能：[修改](loongcollector-management-linux.md)[CPU、内存使用上限。](loongcollector-management-linux.md)
借助[CloudLens for SLS](cloudlens-for-sls.md)监控：在数据洞察中查看配额使用情况，如project写入流量是否超过限额。在采集监控-文件采集监控-采集文件分布中查看是否有延迟的文件。可能当前读取速率跟不上日志的产生速率，CPU usage 满了, 读不完日志导致日志文件一直保持打开状态目录空间没法释放。
