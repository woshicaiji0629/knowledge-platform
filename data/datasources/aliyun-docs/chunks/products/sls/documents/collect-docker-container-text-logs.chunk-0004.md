## 步骤一：配置机器组（安装LoongCollector）
在Docker宿主机上以容器方式部署LoongCollector，并将其加入到机器组中。通过机器组实现对多个采集节点的统一管理、配置分发与状态监控。
拉取镜像
在已安装Docker的宿主机上执行如下命令，拉取 LoongCollector 镜像。请将${region_id}替换为宿主机所在地域或就近[地域](collect-docker-container-text-logs.md)[ID](collect-docker-container-text-logs.md)（如cn-hangzhou），以提升下载速度和稳定性。
