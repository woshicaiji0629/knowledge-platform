性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\user_log_config.json |

容器环境
user_log_config.json文件存储在Logtail容器中，文件路径为/usr/local/ilogtail/user_log_config.json。
文件示例
$cat /usr/local/ilogtail/user_log_config.json { "metrics" : { "##1.0##k8s-log-c12ba2028*****939f0b$app-java" : { "aliuid" : "16542189*****50", "category" : "app-java", "create_time" : 1534739165, "defaultEndpoint" : "cn-hangzhou-intranet.log.aliyuncs.com", "delay_alarm_bytes" : 0, "enable" : true, "enable_tag" : true, "filter_keys" : [], "filter_regs" : [], "group_topic" : "", "local_storage" : true, "log_type" : "plugin", "log_tz" : "", "max_send_rate" : -1, "merge_type" : "topic", "plugin" : { "inputs" : [ { "detail" : { "IncludeEnv" : { "aliyun_logs_app-java" : "stdout" }, "IncludeLable" : { "io.kubernetes.container.name" : "java-log-demo-2", "io.kubernetes.pod.namespace" : "default" }, "Stderr" : true, "Stdout" : true }, "type" : "service_docker_stdout" } ] }, "priority" : 0, "project_name" : "k8s-log-c12ba2028c*****ac1286939f0b", "raw_log" : false, "region" : "cn-hangzhou", "send_rate_expire" : 0, "sensitive_keys" : [], "tz_adjust" : false, "version" : 1 } } }
