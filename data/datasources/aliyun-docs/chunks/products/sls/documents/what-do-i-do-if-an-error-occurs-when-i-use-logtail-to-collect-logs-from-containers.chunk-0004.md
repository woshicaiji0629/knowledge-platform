### 查看Logtail的运行日志
Logtail日志存储在Logtail容器中的/usr/local/ilogtail/目录中，文件名为ilogtail.LOG和logtail_plugin.LOG。
登录Logtail容器。具体操作，[登录](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)[Logtail](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)[容器](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
打开/usr/local/ilogtail/目录。
cd /usr/local/ilogtail
查看ilogtail.LOG和logtail_plugin.LOG文件。
cat ilogtail.LOG cat logtail_plugin.LOG
