il 容器重启导致采集重复或丢失。 | "user_config_file_path" : user_log_config.json |
| docker_file_cache_path | String | 该文件记录了容器文件到宿主机文件的路径映射，默认为 /usr/local/ilogtail/docker_path_config.json 。 建议 Docker/Kubernetes 用户参见 [iLogtail](https://developer.aliyun.com/article/901257) [容器重启数据可靠性探讨](https://developer.aliyun.com/article/901257) 进行配置，避免 Logtail 容器重启导致采集重复或丢失。 仅 Linux Logtail 0.16.54 及以上版本或 Windows Logtail 0.16.54.0 及以上版本支持该参数。 | "docker_file_cache_path": /usr/local/ilogtail/docker_path_config.json |
| discard_old_data | Boolean | 是否丢弃历史日志。默认值：true，表示丢弃距离当前时间超过 12 小时的日志。 | "discard_old_data" : true |
| ilogtail_discard_interval | int | 丢弃历史日志距离当前时间的阈值。默认值：43200（12 小时），单位：秒。 | "ilogtail_discard_interval": 43200 |
| working_ip | String | 默认值为空，表示自动从本服务器获取 IP 地址。修改后 Logtail 将以该值作为服务器的 IP 地址上报。 | "working_ip" : "" |
| working_hostname | String | Logtail 上报的本服务器的主机名。默认值为空，表示自动从本服务器获取主机名。 | "working_hostname" : "" |
| max_read_buffer_size | long | 每条日志读取的最大值。默认值：524288（512 KB），最大值：8388608（8 MB）。单位：Byte。 如果您的单条日志超过 524288 Byte，可修改此参数。 | "max_read_buffer_size" : 524288 |
| oas_connect_timeout | long | Logtail 发起获取 Logtail 配置、访问密钥等请求时，连接阶段的超时时间。默认值：5，单位：秒。 网络条件较差，建立连接时间过长时可修改此参数。 | "oas_connect_timeout"
