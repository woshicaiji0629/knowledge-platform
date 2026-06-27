### 集群常见问题
多个Kubernetes集群如何共用一个日志服务Project？
如果您希望将多个集群中的容器日志采集到同一个日志服务Project中，安装其他集群日志服务组件时，将安装参数中的设置与您第一次安装集群日志服务组件时保持一致。
如何查看Logtail日志？
Logtail日志存储在Logtail容器中的/usr/local/ilogtail/目录中，文件名为ilogtail.LOG和logtail_plugin.LOG。
Logtail容器中的标准输出并不具备参考意义，请忽略以下标准输出内容。
start umount useless mount points, /shm$|/merged$|/mqueue$ umount: /logtail_host/var/lib/docker/overlay2/3fd0043af174cb0273c3c7869500fbe2bdb95d13b1e110172ef57fe840c82155/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/d5b10aa19399992755de1f85d25009528daa749c1bf8c16edff44beab6e69718/merged: must be superuser to unmount umount: /logtail_host/var/lib/docker/overlay2/5c3125daddacedec29df72ad0c52fac800cd56c6e880dc4e8a640b1e16c22dbe/merged: must be superuser to unmount ...... xargs: umount: exited with status 255; aborting umount done start logtail ilogtail is running logtail status: ilogtail is running
如何查看Kubernetes集群中日志服务相关组件的状态？
执行如下命令进行查看。
kubectl get deploy alibaba-log-controller -n kube-system kubectl get ds logtail-ds -n kube-system
alibaba-log-controller启动失败，该怎么处理？
请确认您是否按照以下方式进行安装。
在Kubernetes集群的Master节点中执行安装命令。
安装命令参数中输入的是您的集群ID。
如果由于以上问题安装失败，请使用kubectl delete -f deploy命令删除已生成的安装模板并重新执行安
