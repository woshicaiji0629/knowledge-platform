## 限制说明
Logtail可运行在容器模式或宿主机上，需具备访问Docker的权限（可以访问到/var/run/docker.sock）。
Logtail采集Kubernetes日志请参见[采集](overview-of-log-collection-from-containers.md)[Kubernetes](overview-of-log-collection-from-containers.md)[日志](overview-of-log-collection-from-containers.md)，采集标准容器日志请参见[采集](collect-docker-container-text-logs.md)[Docker](collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](collect-docker-container-text-logs.md)。
Logtail在重启或停止期间，无法采集容器事件。
