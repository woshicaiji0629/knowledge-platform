### 验证清单
确认日志文件有新增内容：LoongCollector只采集增量日志。执行tail -f /path/to/your/log/file，并触发业务操作，确保有新的日志正在写入。
检查LoongCollector状态：sudo /etc/init.d/loongcollectord status。
检查机器组心跳：前往资源组>机器组页面，单击目标机器组名称，在机器组配置>机器组状态区域，查看心跳状态。
如果心跳为OK，则表示机器组与日志服务 Project 连接正常。
如果心跳为FAIL：参考[机器组心跳连接为](host-text-log-collection-auto-install.md)[fail](host-text-log-collection-auto-install.md)进行排查。
查询日志：进入目标 LogStore 的查询分析页面，单击查询 / 分析（默认时间范围为最近15分钟），观察是否有新日志流入。
