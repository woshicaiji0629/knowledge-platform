## 前提条件
已创建Project和LogStore。更多信息，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)和[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
宿主机已[安装并使用](../../ecs/documents/user-guide/install-and-use-docker.md)[Docker](../../ecs/documents/user-guide/install-and-use-docker.md)[和](../../ecs/documents/user-guide/install-and-use-docker.md)[Docker Compose](../../ecs/documents/user-guide/install-and-use-docker.md)且可以持续产生标准输出日志。
说明
Logtail只采集增量日志。如果下发Logtail配置后，日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[读取日志](log-collection-process-of-logtail.md)。
