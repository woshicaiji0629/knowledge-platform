### 修改Logtail配置
如果开启传输加速前已安装Logtail，则需要修改Logtail配置。
停止Logtail。
Linux系统
执行sudo /etc/init.d/ilogtaild stop命令。
Windows系统
选择开始>控制面板>管理工具>服务。
在服务对话框中，找到LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本），右键单击停止。
修改Logtail启动配置文件ilogtail_config.json。
将data_server_list参数中的endpoint一行替换为log-global.aliyuncs.com。文件路径，请参见[启动参数配置文件（ilogtail_config.json）](select-a-network-type.md)。
启动Logtail。
Linux系统
执行sudo /etc/init.d/ilogtaild start命令。
Windows系统
选择开始>控制面板>管理工具>服务。
在服务对话框中，找到LogtailDaemon服务（Logtail 1.0.0.0及以上版本）或LogtailWorker服务（Logtail 0.x.x.x版本），右键单击启动。
更多相关操作可参考[管理传输加速](transmission-acceleration.md)。
