### 启动参数配置文件（ilogtail_config.json）
ilogtail_config.json文件用于配置Logtail的启动参数，文件类型为JSON。更多信息，请参见[设置](select-a-network-type.md)[Logtail](select-a-network-type.md)[启动参数](select-a-network-type.md)。
重要
该文件必须为合法JSON，否则无法启动Logtail。
修改该文件后，必须重启Logtail才能生效。具体操作，请参见[启动和停止](install-run-upgrade-and-uninstall-logtail.md)[Logtail](install-run-upgrade-and-uninstall-logtail.md)。
Logtail默认使用HTTP协议和服务端进行管控面和数据面的通信，使用HTTPS协议和服务端进行鉴权。
如果出于安全考虑，需要使用HTTPS协议和服务端进行通信，则可以分别将config_server_address和data_server_list.endpoint显式指定为https。
如果使用HTTPS协议传输数据，会增加传输延时，非关键场景不建议使用。
安装Logtail后，您可以在ilogtail_config.json文件进行如下操作。
修改Logtail的运行参数。
检验安装命令是否正确。
ilogtail_config.json文件中的config_server_address参数和data_server_list参数的值取决于安装时选择的安装命令，如果其中的地域和日志服务所在地域不一致或地址无法联通，说明安装时选择了错误的命令。这时Logtail无法正常采集日志，需重新安装。
文件路径
主机环境
