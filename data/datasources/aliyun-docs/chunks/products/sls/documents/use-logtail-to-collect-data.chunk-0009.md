## 核心概念
机器组：一个机器组包含一台或多台待采集同类日志的服务器。将Logtail采集配置应用到机器组后，日志服务会根据Logtail采集配置采集机器组内所有服务器上的日志。
日志服务通过机器组管理所有需要通过Logtail采集日志的服务器，支持通过IP地址或者用户自定义标识的方式定义机器组。您可以通过日志服务控制台管理机器组（包括创建、删除机器组，添加、移除机器等操作）。 更多信息，请参见[机器组](machine-group-overview.md)。
Logtail：日志服务提供的日志采集Agent，运行在待采集日志的服务器上。
Linux操作系统：Logtail安装在/usr/local/ilogtail目录下，启动两个以ilogtail开头的独立进程，一个为采集进程，另外一个为守护进程，程序运行日志保存在/usr/local/ilogtail/ilogtail.LOG文件中。更多信息，请参见[安装](install-logtail-on-a-linux-server.md)[Logtail（Linux](install-logtail-on-a-linux-server.md)[系统）](install-logtail-on-a-linux-server.md)。
Windows操作系统
Logtail（32位程序）
安装在Windows 32位操作系统中时，对应的安装目录为C:\Program Files\Alibaba\Logtail。
安装在Windows 64位操作系统中时，对应的安装目录为C:\Program Files (x86)\Alibaba\Logtail。
说明
Windows 64位操作系统支持运行32/64位应用程序，但是出于兼容性考虑，在Windows 64位操作系统上，Windows会使用单独的x86目录来存放32位应用程序。
Logtail（64位程序）
只支持安装在Windows 64位操作系统中，对应的安装目录为C:\Program Files\Alibaba\Logtail。
您可以通过控制面板>管理工具>服务，查看LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本），确认Logtail的运行状态。程序运行日志保存在安装目录下的ilogtail.LOG文件中。更多信息，请参见[安装](install-logtail-on-a-windows-server.md)[Logtail（Windows](install-logtail-on-a-windows-server.md)[系统）](install-logtail-on-a-windows-server.md)。
Logtail配置：Logtail采集日志的策略集合
