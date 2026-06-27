# 通过CLI工具使用容器服务-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/developer-reference/cli-integration-example

# CLI集成示例
本文以调用ACKDescribeClusterDetail接口查询指定集群详情为例，为您介绍使用阿里云CLI调用ACKOpenAPI的操作步骤。
## 前置概念
阿里云CLI（Alibaba Cloud Command Line Interface）是基于OpenAPI构建的通用命令行工具，您可以通过阿里云CLI实现自动化管理和维护ACK。更多信息，请参见[什么是阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。
## 步骤一：安装阿里云CLI
使用阿里云CLI前，您需要先安装阿里云CLI。阿里云CLI为用户提供了Windows、Linux和macOS三种操作系统下的安装服务，请根据您使用设备的操作系统选择对应的安装服务。
Windows：[安装](https://help.aliyun.com/zh/cli/install-cli-on-windows)[CLI（Windows）](https://help.aliyun.com/zh/cli/install-cli-on-windows)。
Linux：[安装](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)[CLI（Linux）](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli)。
macOS：[安装](https://help.aliyun.com/zh/cli/install-cli-on-macos)[CLI（macOS）](https://help.aliyun.com/zh/cli/install-cli-on-macos)。
云命令行（Cloud Shell）预装了阿里云CLI，且在使用时自动为您配置身份凭证，无需手动操作。您可在云命令行中调试阿里云CLI命令。更多信息，请参见[什么是云命令行](https://help.aliyun.com/zh/cloud-shell/what-is-the-cloud-command-line)。
## 步骤二：配置阿里云CLI
重要
阿里云账号（主账号）拥有所有产品OpenAPI的管理和访问权限，风险很高。强烈建议您创建RAM用户（子账号），并依据最小化权限原则授予权限，使用RAM用户身份访问OpenAPI。关于ACK支持的系统权限策略，请参见[AliyunCSFullAccess](../../../../ram/documents/developer-reference/aliyuncsfullaccess.md)及[AliyunCSReadOnlyAccess](../../../../ram/documents/developer-reference/aliyuncsreadonlyaccess.md)。
使用阿里云CLI之前，您需要在阿里云CLI中配置身份凭证、地域ID等信息。阿里云CLI支持多种身份凭证，详情请参见[身份凭证类型](https://help.aliyun.com/zh/cli/configure-credentials/#30ab0f9c3eovm)。阿里云CLI支持使用RAM用户的AccessKey信息配置AK类型身份凭证，具体操作流程如下。
创建一个RAM用户，并创建AccessKey，以便后续配置身份凭证使用。具体操作，请参见[创建](../../../../ram/documents/create-a-ram-user-1.md)[RAM](../../../../ram/documents/create-a-ram-user-1.md)[用户](../../../../ram/documents/create-a-ram-user-1.md)及[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
为RAM用户授权。本文示例需授予RAM用户只读访问ACK的权限AliyunCSReadOnlyAccess。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
获取可用的地域ID，以便后续配置身份凭证使用。阿里云CLI将使用您指定的地域发起OpenAPI调用，推荐您选择集群所在地域对应的地域ID。ACK的可用地域请参见[服务接入点](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-endpoint.md)。
说明
使用阿里云CLI过程中，您可以使用--region选项指定地域发起命令调用，该选项在使用时将忽略默认身份凭证配置及环境变量设置中的地域信息。更多信息，请参见[命令行选项](https://help.aliyun.com/zh/cli/command-line-options)。
使用RAM用户的AccessKey信息配置AK类型凭证，配置文件命名为AkProfile。具体操作，请参见[配置示例](https://help.aliyun.com/zh/cli/configure-credentials/#237984d36ci83)。
## 步骤三：生成CLI命令示例
在OpenAPI门户中，访问[DescribeClusterDetail](https://api.aliyun.com/api/CS/2015-12-15/DescribeClusterDetail?tab=CLI)[调试地址](https://api.aliyun.com/api/CS/2015-12-15/DescribeClusterDetail?tab=CLI)。
单击右侧面板的CLI示例页签，查看生成的CLI调用命令：aliyun cs GET /clusters/{ClusterId} --header "Content-Type=application/json;"。单击页签右侧的复制图标可复制该命令。
在参数配置中输入请求参数，单击CLI示例页签，查看生成的CLI示例。
复制CLI示例或在云命令行中快速执行：
单击运行命令按钮，可唤出云命令行并快速完成命令调试。
单击复制按钮，将CLI示例复制到剪贴板中，可粘贴至本地Shell工具中运行或用于编辑自动化脚本。
说明
复制CLI示例到本地Shell工具中进行调试时请注意参数格式。关于阿里云CLI命令参数使用格式的详细信息，请参见[参数格式](https://help.aliyun.com/zh/cli/understanding-command-line-parameters)。
OpenAPI门户生成示例中会默认添加--region选项，复制命令到本地调用时阿里云CLI将忽略默认身份凭证配置及环境变量设置中的地域信息，优先使用指定的地域调用命令，您可根据需要对该选项进行删除或保留。
## 步骤四：调用ACKOpenAPI
### 示例一：获取支持阿里云CLI调用的ACKOpenAPI列表
以下示例将为您展示如何使用--help选项获取支持阿里云CLI调用的ACKOpenAPI列表。更多信息，请参见[API](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-overview.md)[概览](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-overview.md)。
执行以下命令。
aliyun cs --help
预期输出。
Product: CS (容器服务 Kubernetes版 ) Version: 2015-12-15 Available Api List: AttachInstances : POST /clusters/[ClusterId]/attach AttachInstancesToNodePool : POST /clusters/[ClusterId]/nodepools/[NodepoolId]/attach CancelClusterUpgrade : POST /api/v2/clusters/[ClusterId]/upgrade/cancel CancelComponentUpgrade : POST /clusters/[clusterId]/components/[componentId]/cancel CancelOperationPlan : DELETE /operation/plans/[plan_id] CancelTask : POST /tasks/[task_id]/cancel CancelWorkflow : PUT /gs/workflow/[workflowName] CheckControlPlaneLogEnable : GET /clusters/[ClusterId]/controlplanelog CheckServiceRole : POST /ram/check-service-role CleanClusterUserPermissions : DELETE /cluster/[ClusterId]/user/[Uid]/permissions
### 示例二：查询集群详情
以下示例将为您展示如何使用阿里云CLI调用ACKDescribeClusterDetail接口，根据集群ID查询指定ACK集群的详细信息。更多接口信息，请参见[查询指定集群的信息](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-describeclusterdetail.md)。
执行以下命令。
aliyun cs GET /clusters/cdde1f21ae22e483ebcb068a6eb7f****
预期输出。
{ "cluster_id": "c82e6987e2961451182edacd74faf****", "cluster_type": "Kubernetes", "created": "2019-11-25T15:50:20+08:00", "init_version": "1.16.6-aliyun.1", "current_version": "1.16.6-aliyun.1", "next_version": "1.18.8-aliyun.1", "deletion_protection": true, "docker_version": "19.03.5", "external_loadbalancer_id": "lb-2zehc05z3b8dwiifh****", "meta_data": "\\\"Addons\\\":***", "name": "cluster-demo", "network_mode": "vpc", "region_id": "cn-beijing", "resource_group_id": "rg-acfmyvw3wjm****", "security_group_id": "sg-25yq****", "container_cidr": "172.20.0.0/16", "service_cidr": "172.21.0.0/20", "proxy_mode": "ipvs", "timezone": "Asia/Shanghai", "node_cidr_mask": "26", "ip_stack": "ipv4", "cluster_domain": "cluster.local", "size": 5, "state": "running", "tags": [ { "key": "env", "value": "prod" } ], "updated": "2020-01-13T23:01:03+08:00", "vpc_id": "vpc-2zecuu62b9zw7a7qn****", "vswitch_id": "vsw-2zete8s4qocqg0mf6****,vsw-2zete8s4qocqg0mf6****", "vswitch_ids": [ "vsw-2zete8s4qocqg0mf6****" ], "subnet_cidr": "172.20.0.0/16", "zone_id": "cn-beijing-a", "master_url": "{\\\"intranet_api_server_endpoint\\\":\\\"https://192.168.0.251:6443\\\"***}", "private_zone": false, "profile": "Default", "cluster_spec": "ack.pro.small", "worker_ram_role_name": "KubernetesWorkerRole-ec87d15b-edca-4302-933f-c8a16bf0****", "maintenance_window": { "enable": false, "maintenance_time": "2020-10-15T12:31:00.000+08:00", "duration": "3h", "weekly_period": "Monday,Thursday", "recurrence": "FREQ=WEEKLY;INTERVAL=4;BYDAY=MO,TU" }, "parameters": { "key": "WorkerImageId" }, "operation_policy": { "cluster_auto_upgrade": { "enabled": true, "channel": "patch" } } }
说明
如果调用ACKOpenAPI后返回错误，您需要根据返回的错误码提示检查传入的请求参数及其取值是否正确。
您也可以记录下调用返回的RequestID或SDK报错信息，通过[阿里云](https://next.api.aliyun.com/troubleshoot)[OpenAPI](https://next.api.aliyun.com/troubleshoot)[诊断平台](https://next.api.aliyun.com/troubleshoot)进行自助诊断。
## 相关文档
[查看所有集群实例](../../ack-managed-and-ack-dedicated/developer-reference/view-all-clusters-1.md)
[查看集群实例](../../ack-managed-and-ack-dedicated/developer-reference/view-information-about-a-cluster.md)
[创建集群](../../ack-managed-and-ack-dedicated/developer-reference/create-a-cluster-2.md)
[添加已有](../../ack-managed-and-ack-dedicated/developer-reference/add-an-existing-ecs-instance.md)[ECS](../../ack-managed-and-ack-dedicated/developer-reference/add-an-existing-ecs-instance.md)[实例](../../ack-managed-and-ack-dedicated/developer-reference/add-an-existing-ecs-instance.md)
[删除集群实例](../../ack-managed-and-ack-dedicated/developer-reference/delete-a-cluster-3.md)
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
