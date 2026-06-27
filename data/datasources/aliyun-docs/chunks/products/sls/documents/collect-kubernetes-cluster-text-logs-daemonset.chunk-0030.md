## 容器日志采集无数据排查思路
检查是否有增量日志：配置LoongCollector（Logtail）采集后，如果待采集的日志文件没有新增日志，则LoongCollector（Logtail）不会采集该文件。
2.查看LoongCollector（Logtail）运行日志
查看LoongCollector（Logtail）其自身的运行日志以获取详细错误信息。
登录Logtail容器：
查询Logtail的Pod。
kubectl get po -n kube-system | grep logtail
系统将返回如下类似结果。
logtail-ds-****d 1/1 Running 0 8d logtail-ds-****8 1/1 Running 0 8d
登录Pod。
kubectl exec -it -n kube-system logtail-ds-****d -- bash
其中，logtail-ds-****d为Pod ID，请根据实际值替换。
查看Logtail运行日志：
Logtail日志存储在Logtail容器中的/usr/local/ilogtail/目录中，文件名为ilogtail.LOG和logtail_plugin.LOG。登录Logtail容器，执行以下命令查看日志文件：
打开/usr/local/ilogtail/目录。 cd /usr/local/ilogtail 查看ilogtail.LOG和logtail_plugin.LOG文件。 cat ilogtail.LOG cat logtail_plugin.LOG
目的：查看错误日志的告警类型，并根据[日志服务采集数据常见的错误类型](log-collection-error-type.md)查询对应的解决办法。
3.检查机器组心跳
检查机器组心跳状态：前往资源组>机器组页面，单击目标机器组名称，在机器组配置>机器组状态区域，查看心跳状态并记录心跳状态为ok的节点数。
检查容器集群中Worker节点数。
[获取集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[KubeConfig](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)[并通过](../../ack/documents/ac
