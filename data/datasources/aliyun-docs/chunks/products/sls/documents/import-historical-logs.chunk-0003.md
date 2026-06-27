## 操作步骤
获取Logtail配置的唯一标识。
您可以在Logtail安装目录下的user_log_config.json文件中获取Logtail配置的唯一标识。此处以Linux系统为例，查看Logtail配置的唯一标识。
grep "##" /usr/local/ilogtail/user_log_config.json | awk '{print $1}'
添加本地事件。
在Logtail安装目录下，创建local_event.json文件。
在local_event.json文件中添加本地事件，类型为标准JSON，格式如下所示。
重要
为了防止Logtail加载无效的JSON，建议您先将本地事件配置保存在临时文件中，编辑完成后拷贝到local_event.json文件中。
[ { "config" : "${your_config_unique_id}", "dir" : "${your_log_dir}", "name" : "${your_log_file_name}" }, { ... } ... ]

| 参数 | 说明 |
| --- | --- |
| config | 填写步骤 [1](import-historical-logs.md) 中获取的 Logtail 配置唯一标识，例如 ##1.0##log-config-test$ecs-test 。 |
| dir | 历史日志文件所在目录，例如： /data/logs 。 重要 文件夹不能以 / 结尾。 文件夹目录不能是 Logtail 安装目录（ /usr/local/ilogtail ）。 |
| name | 历史日志文件名，支持通配符，例如 access.log.2018-08-08、access.log*。 |

本文以Linux系统为例，介绍配置示例。
$ cat /usr/local/ilogtail/local_event.json [ { "config": "##1.0##log-config-test$ecs-test", "dir": "/data/log", "name": "access.log*" }, { "config": "##1.0##log-config-test$tmp-test", "dir": "/tmp", "name": "access.log.2017-08-09" } ]
