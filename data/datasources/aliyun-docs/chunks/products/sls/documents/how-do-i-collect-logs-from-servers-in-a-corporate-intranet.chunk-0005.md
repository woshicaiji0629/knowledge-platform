## 方案一
登录某台企业内网服务器。
打开/etc/init.d/ilogtaild文件，在start()函数中增加如下环境变量，然后保存文件。
关于环境变量的更多信息，请参见[附录：网络代理相关的环境变量](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。
start() { cd $BIN_DIR umask $UMASK # 在$BIN_DIR/ilogtail前新增代理相关环境变量。 # 这里以ALL_PROXY为例，假设代理服务器地址为192.168.1.0，监听端口为9000。 # 内网服务器与代理服务器之间通过HTTP协议进行通信。 ALL_PROXY=http://192.168.1.0:9000 $BIN_DIR/ilogtail RETVAL=$? }
执行如下命令重启Logtail。
/etc/init.d/ilogtaild restart
重复执行步骤[1](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)~[3](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)，为其他内网服务器设置代理相关的环境变量。
