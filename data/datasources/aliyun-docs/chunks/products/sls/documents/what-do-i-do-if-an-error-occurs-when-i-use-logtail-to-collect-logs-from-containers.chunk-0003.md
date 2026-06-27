### 登录Logtail容器
普通Docker
在宿主机上执行如下命令，查询Logtail容器。
docker ps | grep logtail
系统将返回如下类似结果。
223****6e registry.cn-hangzhou.aliyuncs.com/log-service/logtail "/usr/local/ilogta..." 8 days ago Up 8 days logtail-iba
执行如下命令，在Logtail容器内启动bash shell。
docker exec -it 223****6e bash
其中，223****6e为容器ID，请根据实际值替换。
Kubernetes
执行如下命令，查询Logtail的Pod。
kubectl get po -n kube-system | grep logtail
系统将返回如下类似结果。
logtail-ds-****d 1/1 Running 0 8d logtail-ds-****8 1/1 Running 0 8d
执行如下命令，登录Pod。
kubectl exec -it -n kube-system logtail-ds-****d -- bash
其中，logtail-ds-****d为Pod ID，请根据实际值替换。
