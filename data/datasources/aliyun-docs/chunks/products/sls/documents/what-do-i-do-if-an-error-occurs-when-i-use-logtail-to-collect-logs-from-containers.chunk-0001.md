t-logs-through-sidecar-console.md)[方式采集](collect-container-text-logs-through-sidecar-console.md)[Kubernetes](collect-container-text-logs-through-sidecar-console.md)[容器文本日志](collect-container-text-logs-through-sidecar-console.md)，检查{regionId}、{aliuid}、{access-key-id}和{access-key-secret}是否已正确填写。
如果填写错误，请执行helm del --purge alibaba-log-controller命令，删除安装包，然后重新安装。
机器组心跳状态为OK的节点数量少于集群中的Worker节点数量。
判断是否已使用YAML文件手动部署DaemonSet。
执行如下命令。如果存在返回结果，则表示您之前已使用YAML文件手动部署DaemonSet。
kubectl get po -n kube-system -l k8s-app=logtail
[下载最新版本](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)[DaemonSet](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)[模板。](https://logtail-release.oss-cn-hangzhou.aliyuncs.com/docker/k8s/logtail-daemonset.yaml)
根据实际值，配置${your_region_name}、${your_aliyun_user_id}、${your_machine_group_name}等参数。
执行如下命令，更新文件。
kubectl apply -f ./logtail-daemonset.yaml
