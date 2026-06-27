ent size:0 success count:0
如何重启某个Pod中的Logtail？
停止Logtail。
其中logtail-ds-gb92k表示容器名，kube-system表示命名空间，请根据实际情况替换。
kubectl exec logtail-ds-gb92k -n kube-system /etc/init.d/ilogtaild stop
返回如下结果表示停止成功。
kill process Name: ilogtail pid: 7 kill process Name: ilogtail pid: 9 stop success
启动Logtail。
其中logtail-ds-gb92k表示容器名，kube-system表示命名空间，请根据实际情况替换。
kubectl exec logtail-ds-gb92k -n kube-system /etc/init.d/ilogtaild start
返回如下结果表示启动成功。
ilogtail is running
该文章对您有帮助吗？
反馈
