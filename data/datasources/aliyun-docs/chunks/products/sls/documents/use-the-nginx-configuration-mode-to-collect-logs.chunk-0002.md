## 前提条件
已创建Logtail机器组并添加相应服务器，创建机器组的步骤，请参见[创建用户自定义标识机器组](manage-machine-groups.md)和[创建](manage-machine-groups.md)[IP](manage-machine-groups.md)[地址机器组](manage-machine-groups.md)。
服务器具备访问远端服务器80端口和443端口的能力，确保Logtail能够将日志数据发送给日志服务。
服务器日志的内容持续新增。Logtail只采集增量日志，如果下发Logtail配置后日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[采集流程](use-logtail-to-collect-data.md)。
