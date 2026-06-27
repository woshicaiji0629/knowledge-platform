# 如何通过CLI创建ACK集群-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/create-a-cluster

# 创建集群
创建一个新的集群实例，并新建指定数量的节点。
关于该命令的详细参数说明，请参见API文档[创建集群](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-createcluster.md)。
## API请求响应
请求格式
aliyun cs POST /clusters --region=${regionId} --header "Content-Type=application/json" --body "$(cat create.json)"
参数说明：
--header：需要指定Content-Type为application/json。
--region：集群所在的地域。
--body：是要发送给服务端的body内容，可以从本地文件读取，需要是有效的JSON格式。create.json的内容如下所示。
请求示例：
Kubernetes集群
{ "cluster_type":"Kubernetes", "name":"webService", "region_id":"cn-beijing", "disable_rollback":true, "timeout_mins":60, "kubernetes_version":"1.14.8-aliyun.1", "snat_entry":true, "endpoint_public_access":true, "ssh_flags":true, "cloud_monitor_flags":true, "deletion_protection":false, "node_cidr_mask":"26", "proxy_mode":"ipvs", "tags":[], "addons":[{"name":"flannel"},{"name":"arms-prometheus"},{"name":"flexvolume"},{"name":"alicloud-disk-controller"},{"name":"logtail-ds","config":"{"IngressDashboardEnabled":"false"}"},{"name":"ack-node-problem-detector","config":"{"sls_project_name":""}"},{"name":"nginx-ingress-controller","config":"{"IngressSlbNetworkType":"internet"}"}], "os_type":"Linux", "platform":"CentOS", "node_port_range":"30000-32767", "key_pair":"sian-sshkey", "cpu_policy":"none", "master_count":3, "master_vswitch_ids":["vsw-2zete8s4qocqg0mf6****","vsw-2zete8s4qocqg0mf6****","vsw-2zete8s4qocqg0mf6****"], "master_instance_types":["ecs.n4.large","ecs.n4.large","ecs.n4.large"], "master_system_disk_category":"cloud_ssd", "master_system_disk_size":120, "runtime":{"name":"docker","version":"18.09.2"}, "worker_instance_types":["ecs.i1.xlarge"], "num_of_nodes":1, "worker_system_disk_category":"cloud_efficiency", "worker_system_disk_size":120, "vpcid":"vpc-2zecuu62b9zw7a7q****", "worker_vswitch_ids":["vsw-2zete8s4qocqg0mf6****"], "container_cidr":"172.20.0.0/16", "service_cidr":"172.21.0.0/20" }
请求示例补充说明
如果是terway网络类型的集群，"pod_vswitch_ids"为必填参数，请求入参示例如下。 { "cluster_type":"Kubernetes", "name":"webService-terway", "region_id":"cn-beijing", "disable_rollback":true, "timeout_mins":60, "kubernetes_version":"1.14.8-aliyun.1", "snat_entry":true, "endpoint_public_access":true, "ssh_flags":true,"cloud_monitor_flags":true, "deletion_protection":false, "proxy_mode":"ipvs", "tags":[], "addons":[{"name":"terway-eni"},{"name":"flexvolume"},{"name":"alicloud-disk-controller"},{"name":"logtail-ds","config":"{\"IngressDashboardEnabled\":\"false\"}"},{"name":"ack-node-problem-detector","config":"{\"sls_project_name\":\"\"}"},{"name":"nginx-ingress-controller","config":"{\"IngressSlbNetworkType\":\"internet\"}"}], "os_type":"Linux", "platform":"CentOS", "node_port_range":"30000-32767", "pod_vswitch_ids":["vsw-2zete8s4qocqg0mf6****"], "key_pair":"sian-sshkey", "cpu_policy":"none", "master_count":3, "master_vswitch_ids":["vsw-2zed90q9inwtuyfzd****","vsw-2zed90q9inwtuyfzd****","vsw-2zed90q9inwtuyfzd****"], "master_instance_types":["ecs.i1.4xlarge","ecs.i1.4xlarge","ecs.i1.4xlarge"], "master_system_disk_category":"cloud_ssd", "master_system_disk_size":120, "runtime":{"name":"docker","version":"18.09.2"}, "worker_instance_types":["ecs.i1.4xlarge"], "num_of_nodes":1, "worker_system_disk_category":"cloud_efficiency", "worker_system_disk_size":120, "vpcid":"vpc-2zecuu62b9zw7a7q****", "worker_vswitch_ids":["vsw-2zed90q9inwtuyfzd****"], "is_enterprise_security_group":true, "service_cidr":"172.21.0.0/20" }
托管Kubernetes集群
{ "name":"amk-cluster", "cluster_type":"ManagedKubernetes", "disable_rollback":true, "timeout_mins":60, "kubernetes_version":"1.16.9-aliyun.1", "region_id":"cn-beijing", "snat_entry":true, "cloud_monitor_flags":true, "endpoint_public_access":true, "deletion_protection":true, "node_cidr_mask":"26", "proxy_mode":"ipvs", "tags":[ { "key":"tier", "value":"backend" } ], "addons":[{"name":"flannel"},{"name":"csi-plugin"},{"name":"csi-provisioner"},{"name":"logtail-ds","config":"{\"IngressDashboardEnabled\":\"true\"}"},{"name":"ack-node-problem-detector","config":"{\"sls_project_name\":\"\"}"},{"name":"nginx-ingress-controller","config":"{\"IngressSlbNetworkType\":\"internet\"}"},{"name":"arms-prometheus"}], "os_type":"Linux", "platform":"CentOS", "runtime":{ "name":"docker", "version":"19.03.5" }, "worker_instance_types":[ "ecs.i2.2xlarge" ], "num_of_nodes":3, "worker_system_disk_category":"cloud_efficiency", "worker_system_disk_size":120, "worker_data_disks":[ { "category":"cloud_efficiency", "size":"40", "encrypted":"true", "auto_snapshot_policy_id":"" } ], "worker_instance_charge_type":"PrePaid", "worker_period_unit":"Month", "worker_period":1, "worker_auto_renew":true, "worker_auto_renew_period":1, "vpcid":"vpc-2zemm8mo5rmdppgqm****", "container_cidr":"172.20.0.0/16", "service_cidr":"172.21.0.0/20", "vswitch_ids":[ "vsw-2zej67xyhh61oqn7i****" ], "login_password":"Hello1234", "logging_type":"SLS", "cpu_policy":"none", "taints":[ { "key":"key1", "value":"value1", "effect":"NoSchedule" } ], "security_group_id":"sg-2zeg3u73kkhtixda****" }
ACK Serverless集群
{ "cluster_type":"Ask", "name":"ask-cluster", "kubernetes_version":"1.16.9-aliyun.1", "region_id":"cn-shenzhen", "endpoint_public_access":true, "private_zone":true, "tags":[ { "key":"tier", "value":"frontend" } ], "deletion_protection":true, "addons":[ { "name":"logtail-ds" } ], "zone_id":"cn-shenzhen-a", "vpc_id":"vpc-wz984yvbd6lck22z3****", "vswitch_ids":[ "vsw-wz9uwxhawmtzg7u9h****" ], "logging_type":"SLS", "security_group_id":"sg-wz9b86l4s7nthi1k****" }
响应结果
{ "cluster_id": "c61cf530524474386a7ab5a1c192****", "request_id": "348D4C9C-9105-4A1B-A86E-B58F0F875575", "task_id": "T-5ad724ab94a2b109e8000004" }
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
