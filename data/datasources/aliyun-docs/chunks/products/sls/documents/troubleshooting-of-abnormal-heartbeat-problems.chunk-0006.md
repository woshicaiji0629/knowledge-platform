## IP地址
将服务器上/usr/local/ilogtail/app_info.json中ip字段的信息添加到IP地址中。
ip取值规则：若已在服务器的/etc/hosts文件中设置了主机名与IP地址绑定，则自动获取绑定的IP地址。若没有设置主机名绑定，自动获取本机第一块网卡的IP地址。若设置了/usr/local/ilogtail/ilogtail_config.json中的working_ip参数，则以working_ip值作为服务器的IP地址。请至少保证一种情况下能获取到ip，否则ip字段值为空，无法建立心跳。
