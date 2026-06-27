### 查看Logtail状态、版本及IP地址
运行如下命令，查看Logtail状态。
kubectl get po -n kube-system | grep logtail
返回结果如下：
NAME READY STATUS RESTARTS AGE logtail-ds-gb92k 1/1 Running 0 2h logtail-ds-wm7lw 1/1 Running 0 4d
运行如下命令，查看Logtail的版本号、IP地址等信息。
kubectl exec logtail-ds-gb92k -n kube-system cat /usr/local/ilogtail/app_info.json
返回结果如下：
{ "hostname" : "logtail-ds-gb92k", "instance_id" : "0EBB2B0E-0A3B-11E8-B0CE-0A58AC140402_172.20.4.2_1517810940", "ip" : "192.0.2.0", "logtail_version" : "0.16.2", "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64", "update_time" : "2021-02-05 06:09:01" }
