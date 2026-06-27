### 如何将ECS服务器的日志传输到同账号不同地域的Project？
如果您尚未安装LoongCollector，请参考[安装采集器](loongcollector-installation-linux.md)选择合适的跨地域场景进行安装；
如果已安装LoongCollector，则需要修改LoongCollector配置。
执行sudo /etc/init.d/ilogtaild stop命令，停止LoongCollector。
修改LoongCollector启动配置文件ilogtail_config.json，根据您的网络需求从以下两种方式中选择一种进行修改：
配置文件路径：/usr/local/ilogtail/ilogtail_config.json
方式一：使用公网传输
参考[RegionID](loongcollector-installation-linux.md)，将配置文件中的地域替换为日志服务所在的地域，需要修改的字段包括：
primary_region
config_servers中的地域部分
data_servers中的region和endpoint_list地域部分
方式二：使用传输加速
将data_server_list参数中的endpoint一行替换为log-global.aliyuncs.com。文件路径，请参见[Logtail](select-a-network-type.md)[网络类型，启动参数与配置文件](select-a-network-type.md)。
配置文件示例
$cat { "primary_region" : "cn-shanghai", "config_servers" : [ "http://logtail.cn-shanghai.log.aliyuncs.com" ], "data_servers" : [ { "region" : "cn-shanghai", "endpoint_list": [ "cn-shanghai.log.aliyuncs.com" ] } ], "cpu_usage_limit" : 0.4, "mem_usage_limit" : 384, "max_bytes_per_sec" : 20971520, "bytes_per_sec" : 1048576, "buffer_file_num" : 25, "buffer_file_size" : 20971520, "buffer_map_num" : 5 }
执行sudo /etc/init.d/ilogtaild start命令，启动LoongCollector。
