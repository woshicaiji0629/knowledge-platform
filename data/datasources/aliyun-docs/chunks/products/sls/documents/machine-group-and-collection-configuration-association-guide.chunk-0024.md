### 采集怎么匹配多个目录
需求：例如需要同时采集/var/log/messages和/opt/app/logs/*.log到同一LogStore中。
解决方案：
在目标LogStore中创建两个采集配置，路径分别为/var/log/messages与/opt/app/logs/*.log。
将这两个采集配置应用到同一个机器组中。
日志服务会将该机器组中所有服务器上路径为/var/log/messages与/opt/app/logs/*.log的数据采集到目标LogStore中。
