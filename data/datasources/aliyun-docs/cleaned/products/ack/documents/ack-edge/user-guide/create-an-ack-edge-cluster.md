# 调用CreateCluster接口创建ACK Edge集群-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/create-an-ack-edge-cluster

# 通过OpenAPI创建ACK Edge集群
调用CreateCluster创建一个新的ACK Edge集群。
## 调试
[您可以在](https://api.aliyun.com/#product=CS&api=CreateCluster&type=ROA&version=2015-12-15)[OpenAPI Explorer](https://api.aliyun.com/#product=CS&api=CreateCluster&type=ROA&version=2015-12-15)[中直接运行该接口，免去您计算签名的困扰。运行成功后，OpenAPI Explorer](https://api.aliyun.com/#product=CS&api=CreateCluster&type=ROA&version=2015-12-15)[可以自动生成](https://api.aliyun.com/#product=CS&api=CreateCluster&type=ROA&version=2015-12-15)[SDK](https://api.aliyun.com/#product=CS&api=CreateCluster&type=ROA&version=2015-12-15)[代码示例。](https://api.aliyun.com/#product=CS&api=CreateCluster&type=ROA&version=2015-12-15)
## 请求语法
POST /clusters HTTP/1.1 Content-Type:application/json { "name" : "String", "cluster_type" : "String", "disable_rollback" : Boolean, "timeout_mins" : Long, "kubernetes_version" : "String", "runtime" : { "name" : "String", "version" : "String" }, "region_id" : "String", "key_pair" : "String", "login_password" : "String", "num_of_nodes" : Long, "profile" : "String", "logging_type" : "String", "snat_entry" : Boolean, "vswitch_ids" : [ "String" ], "worker_system_disk_category" : "String", "worker_system_disk_size" : Long, "container_cidr" : "String", "cloud_monitor_flags" : Boolean, "endpoint_public_access" : Boolean, "service_cidr" : "String", "addons" : [ { "name" : "String", "config" : "String", "disabled" : Boolean } ], "tags" : [ { "key" : "String", "value" : "String" } ], "vpcid" : "String", "worker_data_disks" : [ { "category" : "String", "size" : Long, "encrypted" : "String", "auto_snapshot_policy_id" : "String" } ], "deletion_protection" : Boolean, "node_cidr_mask" : "String", "worker_instance_types" : [ "String" ], "worker_instance_charge_type" : "String", "security_group_id" : "String", "is_enterprise_security_group" : Boolean, "rds_instances" : [ "String" ] }
## 请求参数
表 1.请求Body参数
| 名称 | 类型 | 是否必选 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | demo-edge-cluster | 集群名称。 命名规则：由数字、汉字、英文字符或短划线（-）组成，长度范围 1~63 个字符，且不能以短划线（-）开头。 |
| cluster_type | String | 是 | ManagedKubernetes | 集群类型。取值 ManagedKubernetes 创建边缘托管版集群。 |
| disable_rollback | Boolean | 否 | true | 【该字段已废弃】 集群创建失败是否回滚。取值： true ：当集群创建失败时，进行回滚操作。 false ：当集群创建失败时，不进行回滚操作。 默认值： false 。 |
| timeout_mins | Long | 否 | 60 | 【该字段已废弃】 集群资源栈创建超时时间，以分钟为单位，默认值 60 分钟。 |
| kubernetes_version | String | 否 | 1.30.1-aliyun.1 | 集群版本，与 Kubernetes 社区基线版本保持一致。建议选择最新版本，若不指定，默认使用最新版本。 目前您可以在 ACK 控制台创建三种最新版本的集群。您可以通过 API 创建其他 Kubernetes 版本集群。关于 ACK 支持的 Kubernetes 版本，请参见 [ACK](../../ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md) [版本发布说明](../../ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions.md) 。 |
| runtime | Array of [runtime](../developer-reference/api-cs-2015-12-15-struct-runtime-edge.md) | 否 | {"name": " containerd ", "version": "1.6.20"} | 容器运行时，支持 containerd 和 docker 两种运行时。 包括以下信息： name ：容器运行时名称。 version ：容器运行时版本。 |
| region_id | String | 是 | cn-beijing | 集群所在地域 ID。 |
| key_pair | String | 是 | demo-key | 【该字段已废弃】 密钥对名称，和 login_password 二选一。 |
| login_password | String | 是 | HelloWorld123 | 【该字段已废弃】 SSH 登录密码，和 key_pair 二选一。密码规则为 8~30 个字符，且至少同时包含三项（大小写字母、数字和特殊符号）。 |
| num_of_nodes | Long | 是 | 1 | 【该字段已废弃】 Worker 节点数。范围是[0,100]。 |
| profile | String | 是 | Edge | ACK Edge 集群 标识，默认取值：Edge。 |
| logging_type | String | 否 | SLS | 集群开启日志服务，只针对 ACK Serverless 集群 生效，且取值必须是 SLS 。 |
| snat_entry | Boolean | 否 | true | 是否为网络配置 SNAT： 当已有 VPC 能访问公网环境时，设置为 false 。 当已有 VPC 无法访问公网环境时： 设置为 true ，表示配置 SNAT，此时可以访问公网环境。 设置为 false ，表示不配置 SNAT，此时无法访问公网环境。 如果您的应用需要访问公网，建议配置为 true 。 默认值： false 。 |
| vswitch_ids | Array of String | 是 | vsw-2ze48rkq464rsdts1**** | 交换机 ID。List 长度范围为[1,3]。 |
| worker_system_disk_category | String | 是 | cloud_efficiency | 【该字段已废弃】 Worker 节点系统盘类型，取值： cloud_efficiency ：高效云盘。 cloud_ssd ：SSD 云盘。 默认值： cloud_ssd 。 |
| worker_system_disk_size | Long | 是 | 100 | 【该字段已废弃】 Worker 节点系统盘大小，单位为 GiB。 取值范围：[40,500]。 该参数的取值必须大于或者等于 max{40, ImageSize}。 默认值： 120 。 |
| container_cidr | String | 否 | 172.20.0.0 | Pod 网络地址段，不能和 VPC 网段冲突。当选择系统自动创建 VPC 时，默认使用 172.16.0.0/16 网段。 重要 当创建 Flannel 网络类型的集群时，该字段为必填。 当创建 Terway 网络类型的集群时，该字段不需要填写。 |
| cloud_monitor_flags | Boolean | 否 | true | 【该字段已废弃】 集群是否安装云监控插件。取值： true ：安装云监控插件。 false ：不安装云监控插件。 默认值： false 。 |
| endpoint_public_access | Boolean | 否 | true | 是否开启公网 API Server。取值： true ：表示开放公网 API Server。 false ：表示不会创建公网的 API Server，仅创建私网的 API Server。 默认值： true 。 重要 在 ACK Edge 集群 场景，边缘节点通过公网和云端管控交互；因此， ACK Edge 集群 需要开启公网访问。 |
| service_cidr | String | 是 | 172.21.0.0 | Service 网络地址段，不能和 VPC 网段及 Pod 网络网段冲突。当选择系统自动创建 VPC 时，默认使用 172.19.0.0/20 网段。 |
| addons | Array of [addon](../developer-reference/api-cs-2015-12-15-struct-addon-edge.md) | 否 | [{"name":"flannel","config":""},{"name":"logtail-ds-docker","config":""},{"name":"alibaba-log-controller","config":"{"IngressDashboardEnabled":"false"}"}] | Kubernetes 集群安装的组件列表。组件的结构包括： name ：必填，组件名称。 config ：可选，取值为空时表示无需配置。 disabled ：可选，是否禁止默认安装。 网络组件 ：必选，包含 Flannel 和 Terway 两种网络类型，创建集群时二选一： Flannel 网络：[{"name":"flannel","config":""}]。 Terway 网络：[{"name": "terway-eniip","config": ""}] 。 存储组件 ：可选，支持 csi 类型： csi ：[{"name":"csi-plugin","config": ""},{"name": "csi-provisioner","config": ""}]。 日志组件 ：可选。 说明 如果不开启日志服务，则无法使用集群审计功能。 使用已有 SLS Project：[{"name": "logtail-ds","config": "{\"IngressDashboardEnabled\":\"true\",\"sls_project_name\":\"your_sls_project_name\"}"}] 。 创建新的 SLS Project：[{"name": "logtail-ds","config": "{\"IngressDashboardEnabled\":\"true\"}"}] 。 Ingress 组件 ：可选，ACK 专有版集群默认安装 Ingress 组件 nginx-ingress-controller。 安装 Ingress 并且开启公网：[{"name":"nginx-ingress-controller","config":"{\"IngressSlbNetworkType\":\"internet\"}"}] 。 不安装 Ingress：[{"name": "nginx-ingress-controller","config": "","disabled": true}] 。 事件中心 ：可选，默认开启。事件中心提供对 Kubernetes 事件的存储、查询、告警等能力。Kubernetes 事件中心关联的 Logstore 在 90 天内免费。关于免费策略的更多信息，请参见 [创建并使用](../../../../sls/documents/create-and-use-an-event-center.md) [K8s](../../../../sls/documents/create-and-use-an-event-center.md) [事件中心](../../../../sls/documents/create-and-use-an-event-center.md) 。 开启事件中心：[{"name":"ack-node-problem-detector","config":"{\"sls_project_name\":\" your_sls_project_name\"}"}]。 |
| tags | Array of [tag](../developer-reference/api-cs-2015-12-15-struct-tag-edge.md) | 否 | [{"key": "env", "value": "prod"}] | 给集群打 tag 标签： key：标签名称。 value：标签值。 |
| vpcid | String | 是 | vpc-2zeik9h3ahvv2zz95**** | 集群使用的专有网络，创建集群时必须为集群提供。 说明 vpc_id 和 vswitch_ids 只能同时为空或者同时都设置对应的值。 |
| worker_data_disks | Array of [data_disk](../developer-reference/api-cs-2015-12-15-struct-data-disk-edge.md) | 否 |  | 【该字段已废弃】 Worker 节点数据盘类型、大小等配置的组合。 |
| deletion_protection | Boolean | 否 | true | 集群删除保护，防止通过控制台或 API 误删除集群。取值： true ：启用集群删除保护，将不能通过控制台或 API 删除集群。 false ：不启用集群删除保护，则能通过控制台或 API 删除集群。 默认值： false 。 |
| node_cidr_mask | String | 否 | 25 | 节点 IP 数量，通过指定网络的 CIDR 来确定 IP 的数量，只对于 Flannel 网络类型集群生效。 默认值： 25 。 |
| worker_instance_types | Array of String | 是 | ecs.n4.large | 【该字段已废弃】 Worker 节点实例规格，至少要指定一个实例规格。更多信息，请参见 [实例规格族](../../../../ecs/documents/user-guide/overview-of-instance-families.md) 。 说明 实例规格优先级随着在数据中的位置增大而依次降低。当无法根据优先级较高的实例规格创建出实例时，会自动选择下一优先级的实例规格来创建实例。 |
| worker_instance_charge_type | String | 是 | PrePaid | 【该字段已废弃】 Worker 节点付费类型，取值： PrePaid ：包年包月。 PostPaid ：按量付费。 默认值：按量付费。 |
| security_group_id | String | 否 | sg-bp1bdue0qc1g7k**** | 使用已有安全组创建集群时需要指定安全组 ID，和 is_enterprise_security_group 二选一，集群节点会自动加入到此安全组。 |
| is_enterprise_security_group | Boolean | 否 | true | 自动创建企业级安全组，当 security_group_id 为空的时生效。 说明 使用普通安全组时，集群内节点与 Terway Pod 数量之和不能超过 2000。因此，创建 Terway 网络类型集群时，建议使用企业安全组。 true ：创建并使用企业级安全组。 false ：不使用企业级安全组。 默认值： true 。 |
| rds_instances | rds_instances | 否 | rm-2zev748xi27xc**** | 【该字段已废弃】 RDS 实例名称。 |
| cluster_spec | String | 否 | ack.pro.small | 托管版集群类型，面向托管集群。取值： ack.pro.small ：专业托管集群，即： ACK Edge 集群 Pro 版 。 ack.standard ：标准托管集群，即 ACK Edge 集群基础版 。 默认值： ack.standard 。取值可以为空，为空时则创建边缘基础版集群。 更多信息，请参见 ACK Edge 集群 Pro 版 [介绍](../../introduction-to-professional-edge-kubernetes-clusters.md) 。 |
| resource_group_id | String | 否 | rg-acfm3mkrure**** | 集群所属资源组 ID，实现不同资源的隔离。 |
## 响应体语法
HTTP/1.1 200 Content-Type:application/json { "cluster_id" : "String", "request_id" : "String", "task_id" : "String" }
## 响应参数
表 2.响应Body参数
| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| cluster_id | String | cb95aa626a47740afbf6aa099b650**** | 集群 ID。 |
| request_id | String | 687C5BAA-D103-4993-884B-C35E4314A1E1 | 请求 ID。 |
| task_id | String | T-5a54309c80282e39ea00002f | 任务 ID。 |
## 创建ACK边缘托管版集群示例
请求示例
POST /clusters <公共请求头> { "name":"ACK边缘托管版", "cluster_type":"ManagedKubernetes", "disable_rollback":true, "timeout_mins":60, "kubernetes_version":"1.14.8-aliyunedge.1", "region_id":"cn-zhangjiakou", "snat_entry":true, "cloud_monitor_flags":true, "endpoint_public_access":true, "deletion_protection":true, "node_cidr_mask":"25", "tags":[ { "key":"tag-k", "value":"tag-v" } ], "addons":[ { "name":"logtail-ds-docker" }, { "name":"alibaba-log-controller", "config":"{\"IngressDashboardEnabled\":\"false\"}" }, { "name":"flannel" }, { "name":"alicloud-monitor-controller" } ], "profile":"Edge", // 边缘集群标识。 "logging_type" : "SLS", "worker_instance_types":[ "ecs.hfc6.large" ], "runtime":{ // 容器运行时。 "name":"containerd", // 运行时名称。 "version":"1.6.20" // 运行时版本。 }, "num_of_nodes":1, "worker_system_disk_category":"cloud_ssd", "worker_system_disk_size":40, "worker_data_disks":[ { "category":"cloud_efficiency", "size":"40", "encrypted":"false", "auto_snapshot_policy_id":"", } ], "worker_instance_charge_type":"PostPaid", "vpcid":"vpc-8vb435kr467tnfj42****", "container_cidr":"172.20.0.0/16", "service_cidr":"172.21.0.0/20", "vswitch_ids":[ "vsw-8vbhdhn461i65p32g****" ], "login_password":"Hello1234", "key_pair": "sin-name", "security_group_id":"sg-8vb7grbyvlb10j0i****", "is_enterprise_security_group":true, "rds_instances": ["rm-xx","rm-xx"] }
正常返回示例
XML格式
<cluster_id>cb95aa626a47740afbf6aa099b650****</cluster_id> <task_id>T-5a54309c80282e39ea00002f</task_id> <request_id>687C5BAA-D103-4993-884B-C35E4314A1E1</request_id>
JSON格式
{ "cluster_id": "cb95aa626a47740afbf6aa099b650****", "task_id": "T-5a54309c80282e39ea00002f", "request_id": "687C5BAA-D103-4993-884B-C35E4314A1E1" }
## 错误码
访问[错误中心](https://error-center.aliyun.com/status/product/CS)查看更多错误码。
## 开发者资源
[SDK](https://next.api.aliyun.com/api-tools/sdk/CS?version=2015-12-15&)
阿里云为您提供多种语言的SDK，帮助您快速通过API集成阿里云的产品和服务，推荐您使用SDK调用API，以免除您手动签名验证，详情请参见SDK参考文档链接。
[OpenAPI Explorer](https://next.api.aliyun.com/api/CS/2015-12-15/CreateCluster)
快速检索，可视化调试API，在线命令行工具，同步动态生成可执行的SDK代码示例。
[阿里云](https://github.com/aliyun/aliyun-cli)[CLI](https://github.com/aliyun/aliyun-cli)
阿里云资产管理和配置工具，可通过命令方式同时管理多个阿里云产品和服务，简单快捷，是您上云好帮手。
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
