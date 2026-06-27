ice.yaml
预期输出：
deployment "coffee" created service "coffee-svc" created deployment "tea" created service "tea-svc" created
查看创建的应用和服务的状态。
执行以下命令，查看应用的状态。
kubectl get deploy
预期输出：
NAME READY UP-TO-DATE AVAILABLE AGE coffee 1/2 2 1 2m26s tea 1/1 1 1 2m26s
执行以下命令，查看服务的状态。
kubectl get svc
预期输出：
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE coffee-svc NodePort 172.16.XX.XX <none> 80:32056/TCP 9m38s tea-svc NodePort 172.16.XX.XX <none> 80:31696/TCP 9m38s
