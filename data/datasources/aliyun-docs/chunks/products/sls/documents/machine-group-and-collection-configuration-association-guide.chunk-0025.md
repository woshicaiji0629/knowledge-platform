### 同服务器日志上传至多LogStore
需求：例如单台服务器上存在多目录下多类型日志，需要保存到不同LogStore中。
解决方案：
在不同LogStore中分别创建不同的采集配置。
需要注意：若多个配置采集同一个文件，需要在输入配置中，打开允许文件多次采集开关。详情参考[日志多次采集](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md)。
将这些采集配置应用到同一个机器组中。
日志服务会根据不同的采集配置将该机器组中不同日志上传到不同LogStore中。
