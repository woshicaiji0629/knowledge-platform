### 容器文本文件日志采集
K8s容器间文件系统隔离，采集器无法直接访问其他容器的文件。但是，容器内的文件系统都是由宿主机的文件系统挂载形成，通过将宿主机根目录所在的文件系统挂载到Loongcollector容器，就可以访问宿主机上的任意文件，从而间接采集业务容器文件系统的文件。
LoongCollector默认将宿主机根目录所在的文件系统挂载到自身的/logtail_host目录下，一般来说无须再手动挂载，例如日志文件在当前容器内的路径是/log/app.log，假设在宿主机上映射路径是/var/lib/docker/containers/<container-id>/log/app.log。则LoongCollector实际采集的文件路径为/logtail_host/var/lib/docker/containers/<container-id>/log/app.log。
