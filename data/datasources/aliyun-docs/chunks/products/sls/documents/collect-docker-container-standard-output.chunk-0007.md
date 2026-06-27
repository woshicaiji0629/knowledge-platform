## 步骤三： 查看上传结果
重要
Logtail只采集增量日志，如果下发Logtail配置后标准输出无新日志产生，则Logtail不会采集以前的日志。更多信息，请参见[读取日志](use-logtail-to-collect-data.md)。
Docker标准输出的每条日志默认包含如下字段：

| 字段名 | 说明 |
| --- | --- |
| __source__ | Logtail 容器的 IP 地址。 |
| __tag__:__hostname__ | Logtail 所在 Docker 主机的名称。 |
| __tag__:__receive_time__ | 日志到达服务端的时间。 |
| _time_ | 数据上传时间，例如 2024-02-02T02:18:41.979147844Z 。 |
| _source_ | 输入源类型，stdout 或 stderr。 |
| _image_name_ | 镜像名。 |
| _container_name_ | 容器名。 |
| _container_ip_ | 业务容器 IP 地址。 |
