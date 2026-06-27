### Linux系统
登录已安装Logtail的机器。
执行如下命令。
ps -ef | grep ilogtail
返回结果中出现两条如下类似信息（分别代表Logtail守护进程和Logtail工作进程）时，说明Logtail正常运行。
UID PID PPID C STIME TTY TIME CMD ... root 12 1 0 Nov10 ? 00:00:00 /usr/local/ilogtail/ilogtail root 14 12 0 Nov10 ? 03:07:43 /usr/local/ilogtail/ilogtail ...
重要
如果返回结果中出现3条及以上Logtail运行信息，则说明当前服务器中有多个Logtail实例在运行，存在重复采集的风险，请检查是否为预期行为。
如果返回结果显示Logtail相关进程未运行。
已经安装Logtail，但是未启动。请参见[启动和停止](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
未安装Logtail，请安装Logtail。具体操作，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
重要
安装时，请务必选择支持安装Logtail的操作系统、按照日志服务Project所属地域选择安装参数以及根据网络类型选择安装方式。关于网络类型的更多信息，请参见[Logtail](select-a-network-type.md)[网络类型，启动参数与配置文件](select-a-network-type.md)。
