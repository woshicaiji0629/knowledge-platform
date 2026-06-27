## 步骤二：确认机器组中的IP地址是否为Logtail获取的IP地址
说明
Logtail获取Linux服务器IP地址的方式如下：
如果您没有设置主机名绑定，则Logtail会获取服务器中第一块网卡的IP地址。
如果想自定义IP地址，可以在[步骤三](troubleshoot-the-errors-related-to-logtail-machine-groups.md)的ilogtail_config.json文件中设置working_ip。设置此参数后，app_info.json文件中的ip字段将自动与working_ip字段值同步更新。关于working_ip，请参见[设置启动参数](configure-the-startup-parameters-of-logtail.md)。
如果您在/etc/hosts文件中设置了主机名绑定，则Logtail会获取绑定的主机名对应的IP地址。
获取app_info.json文件中的ip字段值。
该文件在不同系统下的默认路径说明如下表所示：

| 操作系统 | Logtail | app_info.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/app_info.json |
| Windows（64 位操作系统） | Logtail （64 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\app_info.json |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |
