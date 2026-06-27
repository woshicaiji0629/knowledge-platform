### 监听日志
在服务器上安装Logtail及在日志服务控制台上创建Logtail采集配置后，日志服务会实时下发Logtail采集配置到Logtail，Logtail根据Logtail采集配置开始监听文件。Logtail根据Logtail采集配置中的日志路径和最大监控目录深度，逐层扫描符合规则的日志目录和文件。
将Logtail采集配置应用到机器组后，对应服务器上没有发生修改事件的日志文件会被判定为历史日志文件，Logtail监听到历史日志文件，并不会采集。当日志文件产生了修改事件，才会触发采集流程，Logtail开始读取文件。如果您要采集历史日志文件，请参见[导入历史日志文件](import-historical-logs.md)。
为保证采集日志的时效性以及稳定性，Logtail会对待采集的目录注册事件监听（Linux下使用[Inotify](http://man7.org/linux/man-pages/man7/inotify.7.html)）以及定期轮询。
