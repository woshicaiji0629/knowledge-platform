### 查看上报日志
确认日志文件有新增内容：LoongCollector只采集增量日志。执行tail -f /path/to/your/log/file，并触发业务操作，确保有新的日志正在写入。
查询日志：进入目标 LogStore 的查询分析页面，单击查询 / 分析（默认时间范围为最近15分钟），观察是否有新日志流入。采集的每条Docker容器文本日志中默认包含以下字段信息：

| 字段名 | 说明 |
| --- | --- |
| __source__ | LoongCollector（Logtail）容器的 IP 地址。 |
| _container_ip_ | 业务容器的 IP 地址。 |
| __tag__:__hostname__ | LoongCollector（Logtail）所在 Docker 主机的名称。 |
| __tag__:__path__ | 日志采集路径。 |
| __tag__:__receive_time__ | 日志到达服务端的时间。 |
| __tag__:__user_defined_id__ | 机器组的自定义标识。 |
