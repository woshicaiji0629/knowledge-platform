## Windows系统
打击运行窗口，输入regedit，然后单击确定。
在注册表编辑器窗口中，搜索计算机\HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\LogtailDaemon，然后单击LogtailDaemon。
单击右键，选择新建>多字符串值，然后命名该新值为Environment。
双击Environment，在数值数据文本框中，输入代理相关的环境变量，然后单击确定。
例如以ALL_PROXY为例，代理服务器地址为192.168.1.0，监听端口为9000，内网服务器与代理服务器之间通过HTTP协议进行通信。关于环境变量的更多信息，请参见[附录：网络代理相关的环境变量](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。例如输入ALL_PROXY=http://192.168.1.0:9000。
打击运行窗口，输入services.msc，然后单击确定。
在服务窗口中，选择Logtail对应的服务。
如果是Logtail 0.x.x.x版本，选择LogtailWorker服务。
如果是Logtail 1.0.0.0及以上版本，选择LogtailDaemon服务。
单击右键，选择重新启动。
