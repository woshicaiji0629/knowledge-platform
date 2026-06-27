il（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\app_info.json |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\app_info.json |

Logtail将获取的IP地址记录在app_info.json文件的ip字段中。
{ "UUID" : "", "hostname" : "iZ8vbdlzf******azuhZ", "instance_id" : "E9633380-***********-00163E1AA597_172.16.2.200_166****11", "ip" : "172.**.**.200", "logtail_version" : "1.3.1", "os" : "Linux; 4.19.91-26.1.al7.x86_64; #1 SMP Tue Jul 26 17:52:28 CST 2022; x86_64", "update_time" : "2022-12-27 05:38:33" }
确认机器组中使用的是Logtail获取的IP地址。
日志服务机器组包括IP地址机器组和用户自定义标识机器组。更多信息，请参见[机器组](machine-group-overview.md)。
IP地址机器组：请查看IP地址是否包含[上一步](troubleshoot-the-errors-related-to-logtail-machine-groups.md)获取的IP地址。
若不包含，请确认主机IP的正确值，当IP地址文本框内填写了目标Logtail的其它IP地址（例如公网地址）时，修改IP地址机器组内IP地址，若[上一步](troubleshoot-the-errors-related-to-logtail-machine-groups.md)获取的IP地址有误，则在[设置](select-a-network-type.md)[Logtail](select-a-network-type.md)[启动参数](select-a-network-type.md)中修改参数working_ip的值并重启Logtail。然后观察机器心跳是否正常。如果正常，则可以结束本次排查。
用户自定义标识机器组：请查看机器组状态是否包含[上一步](troubleshoot-the-errors-related-to-logtail-machine-groups.md)获取的IP地址。如果心跳显示OK，则可以结束本次排查流程。
