性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |

容器环境
ilogtail_config.json文件存储在Logtail容器中，文件路径配置在Logtail容器的环境变量ALIYUN_LOGTAIL_CONFIG中，您可通过docker inspect ${logtail_container_name} | grep ALIYUN_LOGTAIL_CONFIG命令查看。例如：/etc/ilogtail/conf/cn-hangzhou/ilogtail_config.json。
文件示例
$cat /usr/local/ilogtail/ilogtail_config.json { "config_server_address" : "http://logtail.cn-hangzhou-intranet.log.aliyuncs.com", "data_server_list" : [ { "cluster" : "cn-hangzhou", "endpoint" : "cn-hangzhou-intranet.log.aliyuncs.com" } ], "cpu_usage_limit" : 0.4, "mem_usage_limit" : 100, "max_bytes_per_sec" : 2097152, "process_thread_count" : 1, "send_request_concurrency" : 15, "streamlog_open" : false }
