态为OK的节点数量少于集群中的Worker节点数量。
判断是否已使用YAML文件手动部署DaemonSet。
执行如下命令。如果存在返回结果，则表示之前已使用YAML文件手动部署DaemonSet。
kubectl get po -n kube-system -l k8s-app=logtail
[下载最新版本](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)[DaemonSet](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)[模板。](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)
根据实际值，配置${your_region_name}、${your_aliyun_user_id}、${your_machine_group_name}等参数。
更新资源。
kubectl apply -f ./logtail-daemonset.yaml
4.检查采集配置过滤条件
在日志服务控制台，检查Logtail采集配置。重点关注Logtail配置中的IncludeLabel、ExcludeLabel、IncludeEnv、ExcludeEnv等配置是否符合采集需求。
此处的Label为容器Label，即Docker inspect中的Label，不是Kubernetes中的Label。
可将IncludeLabel、ExcludeLabel、IncludeEnv和ExcludeEnv配置临时去除，查看是否可以正常采集到日志。如果可以，则说明是上述参数的配置存在问题。
