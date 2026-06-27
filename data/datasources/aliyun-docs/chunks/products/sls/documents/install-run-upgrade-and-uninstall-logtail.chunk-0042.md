alibaba-log-controller启动失败，该怎么处理？
请确认您是否按照以下方式进行安装。
在Kubernetes集群的Master节点中执行安装命令。
安装命令参数中输入的是您的集群ID。
如果由于以上问题安装失败，请使用kubectl delete -f deploy命令删除已生成的安装模板并重新执行安装命令。
如何查看Kubernetes集群中Logtail-ds DaemonSet状态？
执行kubectl get ds -n kube-system命令查看Logtail-ds DaemonSet状态。
说明
Logtail容器所在的命名空间，默认为kube-system。
如何查看Logtail的运行日志？
Logtail运行日志保存在/usr/local/ilogtail/目录下，文件名为ilogtail.LOG，轮转文件会压缩存储为ilogtail.LOG.x.gz。例如执行如下命令查看日志。
kubectl exec logtail-ds-gb92k -n kube-system tail /usr/local/ilogtail/ilogtail.LOG
返回结果如下：
[2018-02-05 06:09:02.168693] [INFO] [9] [build/release64/sls/ilogtail/LogtailPlugin.cpp:104] logtail plugin Resume:start [2018-02-05 06:09:02.168807] [INFO] [9] [build/release64/sls/ilogtail/LogtailPlugin.cpp:106] logtail plugin Resume:success [2018-02-05 06:09:02.168822] [INFO] [9] [build/release64/sls/ilogtail/EventDispatcher.cpp:369] start add existed check point events, size:0 [2018-02-05 06:09:02.168827] [INFO] [9] [build/release64/sls/ilogtail/EventDispatcher.cpp:511] add existed check point events, size:0 cache size:0 event size:0 success count:0
如何重启某个Pod中的Logtail？
停止Logtail。
其中logtail-ds-gb92k表示容器名，kube-system表示命名空间，请根据实际情况替换。
kubectl exec logtail-ds-gb92k -n kube-system /etc
