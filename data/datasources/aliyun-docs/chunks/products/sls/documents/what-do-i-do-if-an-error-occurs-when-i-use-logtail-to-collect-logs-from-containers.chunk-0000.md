## 排查机器组心跳是否异常
您可以通过检查机器组心跳的状态来判断容器中的Logtail是否已正确安装。
查看机器组心跳状态。
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在左侧导航栏中，选择资源>机器组。
在机器组列表中，单击目标机器组。
在机器组配置页面，查看机器组状态并记录心跳状态为OK的节点数。
检查容器集群中Worker节点数。
[连接集群](../../ack/documents/ack-managed-and-ack-dedicated/user-guide/obtain-the-kubeconfig-file-of-a-cluster-and-use-kubectl-to-connect-to-the-cluster.md)。
执行如下命令，查看集群中Worker节点数。
kubectl get node | grep -v master
系统会返回如下类似结果。
NAME STATUS ROLES AGE VERSION cn-hangzhou.i-bp17enxc2us3624wexh2 Ready <none> 238d v1.10.4 cn-hangzhou.i-bp1ad2b02jtqd1shi2ut Ready <none> 220d v1.10.4
对比心跳状态为OK的节点数是否和容器集群中Worker节点数一致。根据对比结果选择排查方式。
机器组中所有节点的心跳状态均为Failed。
如果您要采集标准Docker容器日志，请参见[采集](collect-docker-container-text-logs.md)[Docker](collect-docker-container-text-logs.md)[容器日志（标准输出/文件）](collect-docker-container-text-logs.md)，检查${your_region_name}、${your_aliyun_user_id}、${your_machine_group_user_defined_id}是否填写正确。
如果您使用的是自建Kubernetes集群，请参见[通过](collect-container-text-logs-through-sidecar-console.md)[Sidecar](collect-container-text-logs-through-sidecar-console.md)[方式采集](collect-container-text-logs-through-sidecar-console.md)[Kubernetes](collect-container-text-logs-through-sidecar-console
