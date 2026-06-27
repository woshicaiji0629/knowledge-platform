## API请求响应
请求格式
aliyun cs POST /clusters --region=${regionId} --header "Content-Type=application/json" --body "$(cat create.json)"
参数说明：
--header：需要指定Content-Type为application/json。
--region：集群所在的地域。
--body：是要发送给服务端的body内容，可以从本地文件读取，需要是有效的JSON格式。create.json的内容如下所示。
请求示例：
Kubernetes集群
{ "cluster_type":"Kubernetes", "name":"webService", "region_id":"cn-beijing", "disable_rollback":true, "timeout_mins":60, "kubernetes_version":"1.14.8-aliyun.1", "snat_entry":true, "endpoint_public_access":true, "ssh_flags":true, "cloud_monitor_flags":true, "deletion_protection":false, "node_cidr_mask":"26", "proxy_mode":"ipvs", "tags":[], "addons":[{"name":"flannel"},{"name":"arms-prometheus"},{"name":"flexvolume"},{"name":"alicloud-disk-controller"},{"name":"logtail-ds","config":"{"IngressDashboardEnabled":"false"}"},{"name":"ack-node-problem-detector","config":"{"sls_project_name":""}"},{"name":"nginx-ingress-controller","config":"{"IngressSlbNetworkType":"internet"}"}], "os_type":"Linux", "platform":"CentOS", "node_port_range":"30000-32767", "key_pair":"sian-sshkey", "cpu_policy":"none", "master_count":3, "master_vswitch_ids":["vsw-2zete8s4qocqg0mf6****","vsw-2zete8s4qocqg0mf6****","vsw-2zete8s4qocq
