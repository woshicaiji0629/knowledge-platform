### 查看Kubernetes集群中日志服务相关组件的状态
执行如下命令，查看日志服务的Deployment的状态和信息。
kubectl get deploy -n kube-system | grep -E 'alibaba-log-controller|loongcollector-operator'
返回结果：
NAME READY UP-TO-DATE AVAILABLE AGE alibaba-log-controller 1/1 1 1 11d
执行以下命令，查看关于DaemonSet资源的状态信息。
kubectl get ds -n kube-system | grep -E 'logtail-ds|loongcollector-ds'
返回结果：
NAME DESIRED CURRENT READY UP-TO-DATE AVAILABLE NODE SELECTOR AGE logtail-ds 2 2 2 2 2 **ux 11d
