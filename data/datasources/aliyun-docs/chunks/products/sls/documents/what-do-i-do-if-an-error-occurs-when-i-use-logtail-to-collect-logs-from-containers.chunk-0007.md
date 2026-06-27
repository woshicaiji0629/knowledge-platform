### 查看Logtail的版本号、IP地址、启动时间
在宿主机执行如下命令，查看Logtail的版本号、IP地址、启动时间。
相关信息存储在Logtail容器的/usr/local/ilogtail/app_info.json文件中。
kubectl exec logtail-ds-****k -n kube-system cat /usr/local/ilogtail/app_info.json
系统将返回如下类似结果。
{ "UUID" : "", "hostname" : "logtail-****k", "instance_id" : "0EB****_172.20.4.2_1517810940", "ip" : "172.20.4.2", "logtail_version" : "0.16.2", "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64", "update_time" : "2018-02-05 06:09:01" }
