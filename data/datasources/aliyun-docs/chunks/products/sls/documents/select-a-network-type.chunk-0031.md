### AppInfo记录文件（app_info.json）
app_info.json文件记录Logtail的启动时间、获取到的IP地址、主机名等信息。
如果已在服务器的/etc/hosts文件中设置了主机名与IP地址绑定，则自动获取绑定的IP地址。如果没有设置主机名绑定，会自动获取本机的第一块网卡的IP地址。
重要
AppInfo记录文件仅用于记录Logtail内部信息。修改该文件不会改变Logtail获取的IP地址。
如果修改了服务器的主机名等网络配置，请重启Logtail，获取新的IP地址。
文件路径
主机环境

| 操作系统 | Logtail | app_info.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/app_info.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\app_info.json 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |

容器环境
app_info.json文件存储在Logtail容器中，文件路径为/usr/local/ilogtail/app_info.json。
文件示例
$cat /usr/local/ilogtail/app_info.json { "UUID" : "", "hostname" : "logtail-ds-slpn8", "instance_id" : "E5F93BC6-B024-11E8-8831-0A58AC14039E_1**.***.***.***_1536053315", "ip" : "1**.***.***.***", "logtail_version" : "0.16.13", "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64", "update_time" : "2018-09-04 09:28:36" }
