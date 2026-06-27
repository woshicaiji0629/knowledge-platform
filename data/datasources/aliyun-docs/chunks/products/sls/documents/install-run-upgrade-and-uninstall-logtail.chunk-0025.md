## Windows
以管理员身份运行Windows PowerShell或cmd进入logtail_installer目录（安装包的解压目录），执行如下命令。
.\logtail_installer.exe uninstall
卸载成功后，您的Logtail的安装目录会被删除，但仍有部分配置被保留在C:\LogtailData目录中，您可以根据实际情况进行手动删除。遗留信息包括：
checkpoint：存放所有Logtail插件的Checkpoint信息。只有您使用了Logtail插件后，才会出现此文件。
user_config.d：存放本地采集配置的目录。
其中以.json结尾的文件会被视为采集配置，格式类似于/usr/local/ilogtail/user_log_config.json。
logtail_check_point：存放Logtail主体部分的Checkpoint信息。
users：存放您所配置的用户标识文件。
