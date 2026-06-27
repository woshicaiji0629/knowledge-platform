### 读取日志
Logtail监听到日志文件，并确认有更新后，开始读取。
首次读取日志文件时，日志服务默认首次读取大小为1024 KB。
如果文件小于1024 KB，则从文件内容起始位置开始读取。
如果文件大于1024 KB，则从距离文件末尾1024 KB的位置开始读取。
说明
日志服务支持自定义首次读取大小。
控制台方式：在Logtail配置中修改首次采集大小参数。具体操作，请参见[高级配置](collect-logs-in-simple-mode.md)。
API方式：在Logtail配置中修改tail_size_kb参数。具体操作，请参见[advanced](developer-reference/logtail-configurations.md)[参数说明](developer-reference/logtail-configurations.md)。
如果Logtail已读取过该日志文件，则从上次读取的Checkpoint处继续读取。
读取日志文件时，每次最多可以读取512 KB，因此每条日志的大小请控制在512 KB以内，否则无法正常读取。
说明
如果您修改了服务器上的时间，请手动重启Logtail，否则会导致日志时间不正确、意外丢弃日志等现象。
