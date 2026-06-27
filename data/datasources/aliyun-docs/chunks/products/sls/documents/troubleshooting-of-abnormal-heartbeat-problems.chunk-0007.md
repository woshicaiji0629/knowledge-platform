### 服务器曾经心跳成功但当前为FAIL
曾经心跳成功说明配置项正确，若机器组类型为用户自定义标识型，则配置项中阿里云主账号信息，地域与传输方式，用户自定义标识等是固定值，未修改不会改变心跳状态，可能需要检查网络能否联通访问域名。若机器组类型为IP型，则最有可能是IP地址冲突或IP改变导致心跳为FAIL，请参考如下步骤解决：
在服务器上重启LoongCollector以获取最新IP信息。
若使用的是Logtail采集器，重启命令为：sudo /etc/init.d/ilogtaild restartsudo /etc/init.d/loongcollectord restart
在服务器上查看/usr/local/ilogtail/app_info.json中ip字段的信息。
ip取值规则：若已在服务器的/etc/hosts文件中设置了主机名与IP地址绑定，则自动获取绑定的IP地址。若没有设置主机名绑定，自动获取本机第一块网卡的IP地址。若设置了/usr/local/ilogtail/ilogtail_config.json中的working_ip参数，则以working_ip值作为服务器的IP地址。
登录[日志服务控制台](https://sls.console.aliyun.com/)。在Project列表中，单击目标Project。
单击资源，单击机器组，在机器组中单击目标机器组。
查看机器组配置页面，确认IP地址中信息是否包含/usr/local/ilogtail/app_info.json中ip字段。若不包含则添加ip字段的值到IP地址中。
若一致但心跳仍为FAIL，则不适合使用IP型机器组，请切换机器组类型后尝试。
