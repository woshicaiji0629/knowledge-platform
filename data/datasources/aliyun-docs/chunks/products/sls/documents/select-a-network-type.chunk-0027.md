### 用户标识配置文件
用户标识配置文件中包含阿里云主账号的ID信息，用于标识这台服务器有权限被该账号访问、采集日志。更多信息，请参见[配置用户标识](machine-group-overview.md)。
重要
在采集非本账号ECS、自建IDC、其他云厂商服务器日志时需要配置用户标识。
用户标识配置文件中必须配置阿里云账号（主账号）ID，不支持RAM用户。
用户标识配置文件只需配置文件名，无需配置文件后缀。
一台服务器上可配置多个用户标识，Logtail容器中仅支持配置一个用户标识。
文件路径
主机环境
Linux：/etc/ilogtail/users/。
Windows：C:\LogtailData\users\。
容器环境
用户标识保存在Logtail容器的环境变量ALIYUN_LOGTAIL_USER_ID中，您可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_USER_ID命令查看。
文件示例
$ls /etc/ilogtail/users/
