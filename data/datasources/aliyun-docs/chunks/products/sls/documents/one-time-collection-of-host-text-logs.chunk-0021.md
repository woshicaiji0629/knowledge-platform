### 如何将服务器加入到已有机器组？
当您已有配置好的机器组，希望将新的服务器（如新部署的 ECS 或自建服务器）加入其中并继承其采集配置时，可通过以下步骤完成绑定。
重要
配置创建5分钟后，新加入机器组中的机器不会接收采集配置，具体时间可以参考采集配置页面上方的倒计时提示。
操作前提：
已存在一个配置完成的机器组。
新服务器已[安装](loongcollector-installation-linux.md)[LoongCollector](loongcollector-installation-linux.md)。
操作步骤：
查看目标机器组标识：
在目标Project页面，单击左侧导航栏资源>机器组。
进入机器组页面，单击目标机器组名称。
在机器组配置页面，查看机器组标识。
根据标识类型执行对应操作：
说明
同一机器组中不允许同时存在Linux服务器、Windows服务器，请勿在Linux和Windows服务器上配置相同的用户自定义标识。一个服务器可配置多个用户自定义标识，标识之间以换行符分隔。
类型一：机器组标识为IP地址
在服务器上，执行如下命令打开app_info.json文件，查看ip值。
cat /usr/local/ilogtail/app_info.json
在目标机器组配置页面，单击修改，填写服务器的IP地址，多个IP之间使用换行符分隔。
配置完成后，单击保存，并确认心跳状态。心跳为OK后，服务器将自动应用机器组的采集配置。
若心跳状态为FAIL，请参考常见问题[机器组心跳连接为](one-time-collection-of-host-text-logs.md)[fail](one-time-collection-of-host-text-logs.md)进一步排查。
类型二：机器组标识为用户自定义标识
根据操作系统，向指定文件写入与目标机器组一致的用户自定义标识字符串：
若目录不存在需手动创建。文件路径和名称由日志服务固定，不可自定义。
Linux：向/etc/ilogtail/user_defined_id文件写入自定义字符串 。
Windows：向C:\LogtailData\user_defined_id写入自定义字符串。
