## 步骤一：配置数据存储路径
Zabbix会将监控数据保存在其所在的机器上，您可以根据如下步骤设置监控数据的存储路径。
登录Zabbix所在服务器。
打开zabbix_server.conf文件。
vim /etc/zabbix/zabbix_server.conf
在zabbix_server.conf文件中，设置数据存储路径。
使用Zabbix的实时导出（Real-time Export）功能，将Zabbix 的监控数据（事件、历史值、趋势）以JSON格式导出。该功能要求Zabbix版本号不能低于4.0。具体操作，请参见[Real-time export](https://www.zabbix.com/documentation/5.4/en/manual/appendix/install/real_time_export)。
不建议使用ExportDir=/tmp/，/tmp通常为 tmpfs（内存文件系统），写入速度极快但占用内存资源。若导出数据量大（如高频率监控项），可能导致内存耗尽或系统 OOM（Out Of Memory）。
ExportDir=/data/zabbix_export
重启Zabbix服务，使配置生效。
systemctl restart zabbix-server
配置生效后，Zabbix会在/data/zabbix_export目录下生产文件（文件名后缀为.ndjson），用于保存监控数据。
