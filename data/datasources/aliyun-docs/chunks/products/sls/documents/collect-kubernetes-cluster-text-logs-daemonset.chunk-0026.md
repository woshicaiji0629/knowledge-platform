### 查看上报日志
确认日志文件有新增内容：LoongCollector只采集增量日志。执行tail -f /path/to/your/log/file，并触发业务操作，确保有新的日志正在写入。
查询日志：进入目标 LogStore 的查询分析页面，单击查询 / 分析（默认时间范围为最近15分钟），观察是否有新日志流入。采集的每条容器文本日志中默认包含以下字段信息：

| 字段名称 | 说明 |
| --- | --- |
| __tag__:__hostname__ | 容器宿主机的名称。 |
| __tag__:__path__ | 容器内日志文件的路径。 |
| __tag__:_container_ip_ | 容器的 IP 地址。 |
| __tag__:_image_name_ | 容器使用的镜像名称。 |
| __tag__:_pod_name_ | Pod 的名称。 |
| __tag__:_namespace_ | Pod 所属的命名空间。 |
| __tag__:_pod_uid_ | Pod 的唯一标识符（UID）。 |
