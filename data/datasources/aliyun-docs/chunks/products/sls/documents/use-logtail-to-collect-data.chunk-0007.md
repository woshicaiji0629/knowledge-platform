## 功能优势
基于日志文件，无侵入式采集日志。您无需修改应用程序代码，且采集日志不会影响您的应用程序运行。
除采集文本日志外，还支持采集binlog、http数据、容器日志等。
支持Docker、Kubernetes集群等容器集群的数据采集。
阿里云容器服务Kubernetes：请参见[K8s](overview-of-log-collection-from-containers.md)[容器日志提取](overview-of-log-collection-from-containers.md)。
自建Kubernetes：请参见[K8s](overview-of-log-collection-from-containers.md)[容器日志提取](overview-of-log-collection-from-containers.md)。
自建Docker集群：请参见[采集](collect-docker-container-text-logs.md)[Docker](collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](collect-docker-container-text-logs.md)。
稳定处理日志采集过程中的各种异常。当遇到网络异常、服务端异常等问题时会采取主动重试、本地缓存数据等措施保障数据安全。
基于日志服务的集中管理能力。安装Logtail后，只需要在日志服务上配置机器组、Logtail采集配置等信息即可。
完善的自我保护机制。为保证运行在服务器上的Logtail不会明显影响您服务器上其他服务的性能，Logtail在CPU、内存及网络使用方面都做了严格的限制和保护机制。
