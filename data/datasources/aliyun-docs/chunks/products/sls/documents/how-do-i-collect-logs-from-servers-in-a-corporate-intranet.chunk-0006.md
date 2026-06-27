## 方案二
重要
如果您需要对内网服务器上的所有网络请求进行代理，或者您仅需要对Logtail的网络请求进行代理，但您完全了解服务器上其他进程的网络请求发送地址，您可以考虑此方案。否则，请使用方案一。
登录某台企业内网服务器。
使用export命令在启动文件~/.bash_profile或/etc/profile中添加网络代理相关的环境变量。
关于环境变量的更多信息，请参见[附录：网络代理相关的环境变量](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)。
执行如下命令使环境变量生效。
此处，以~/.bash_profile启动文件为例。
source ~/.bash_profile
执行如下命令，重启Logtail。
/etc/init.d/ilogtaild restart
重复执行步骤[1](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)~[4](how-do-i-collect-logs-from-servers-in-a-corporate-intranet.md)，为其他内网服务器配置代理相关的环境变量。
