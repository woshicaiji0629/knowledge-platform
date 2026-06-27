### 用户自定义标识文件（user_defined_id）
user_defined_id文件用于配置用户自定义标识。更多信息，请参见[创建用户自定义标识机器组](machine-group-overview.md)。
重要
创建自定义标识机器组时需要配置user_defined_id文件。
文件路径
主机环境
Linux：/etc/ilogtail/user_defined_id。
Windows：C:\LogtailData\user_defined_id。
容器环境
用户自定义标识配置在Logtail容器的环境变量ALIYUN_LOGTAIL_USER_DEFINED_ID中，可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_USER_DEFINED_ID命令查看。
文件示例
$cat /etc/ilogtail/user_defined_id aliyun-ecs-rs1e16355
