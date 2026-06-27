### 采集丢失
是否pod生命周期过短（<20s），建议日志打到hostPath进行采集。
查看配置env 和 label 是否和容器一致。
检查是否是采集延时导致的数据不全。
如果是标准输出日志非常长（>16K）发生截断并且是ACK、ASK、SAE场景，需要通过文件采集。
采集器重启也会导致采集数据不全。查看/usr/local/ilogtail/app_info.json的update_time确认是否重启。
主动重启：因资源达到配置上限而cuicide，特征是采集器守护进程和工作进程的启动时间有差异，请[修改](loongcollector-management-linux.md)[CPU](loongcollector-management-linux.md)[使用上限或网络发送并发限制](loongcollector-management-linux.md)。
被动重启：因资源达到container配置上限而被k8s杀死或者达到cgroup上限而被kernel杀死，特点是pod的重启次数超过一次。请查看是否OOM被杀，并调整[修改](loongcollector-management-linux.md)[CPU](loongcollector-management-linux.md)[使用上限或网络发送并发限制](loongcollector-management-linux.md)。
注意：当需要调整资源参数时，往往意味着日志量很大，需要注意[Shard](manage-shards.md)[数量](manage-shards.md)与[资源配额](manage-a-project.md)是否充足。
如果采集数据不一致发生在实例之间，需要注意是否是采集器版本不同导致。可参考[配置管理](loongcollector-management-linux.md)查看版本与升级。
不定时的丢数据，重启后过一段时间会复现：
根据[CloudLens for SLS](cloudlens-for-sls.md)检查当前LogStore配置是否超限。
查看/usr/local/ilogtail/目录下ilogtail.LOG和logtail_plugin.LOG，寻找报错进行具体排查。
若不符合上述场景，则在[控制台通过诊断信息排查采集错误](loongcollector-collection-exception-troubleshooting.md)。
