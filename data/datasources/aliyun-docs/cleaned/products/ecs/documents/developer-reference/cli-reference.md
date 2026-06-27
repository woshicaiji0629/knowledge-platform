# 通过CLI创建并使用ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/developer-reference/cli-reference

# 通过CLI创建并使用ECS实例
阿里云CLI（Command Line Interface）是一种命令行工具，允许用户在终端或命令行界面调用阿里云API，来创建、配置、管理阿里云云资源。本文主要介绍如何使用阿里云CLI调用ECS API来创建和管理ECS实例的方法及其常用示例。
说明
关于阿里云CLI的详细信息，请参见[什么是阿里云 CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。
## 准备工作
由于阿里云账号（主账号）拥有资源的所有权限，其AccessKey一旦泄露风险巨大，所以建议您使用满足最小化权限需求的RAM用户的AccessKey。获取方法请参见[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
给RAM用户授予操作云服务器ECS和专有网络VPC相关资源的权限。本文提供的示例代码需要创建实例、VPC、交换机等资源，建议授予以下权限：
| 云产品 | 授予权限 |
| --- | --- |
| 专有网络 VPC | 本示例选择系统策略：AliyunVPCFullAccess |
| 云服务器 ECS | 本示例选择系统策略：AliyunECSFullAccess |
安装和配置CLI。调试使用阿里云CLI前，您需要先安装阿里云CLI。阿里云CLI提供了Windows、Linux和macOS三种操作系统下的安装服务，请根据您使用设备的操作系统选择：
安装CLI。
[安装](https://help.aliyun.com/zh/cli/install-cli-on-windows#task-525890)[CLI（Windows）](https://help.aliyun.com/zh/cli/install-cli-on-windows#task-525890)
[安装/更新 CLI](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli#task-592837)
[安装](https://help.aliyun.com/zh/cli/install-cli-on-macos#task-592875)[CLI（macOS）](https://help.aliyun.com/zh/cli/install-cli-on-macos#task-592875)
配置CLI。
配置调用阿里云资源所需的身份凭证信息、服务请求地域等。具体配置，请参见[配置身份凭证](https://help.aliyun.com/zh/cli/configure-credentials/#41e7063556zzq)。
如果您只是用于临时调试，不需要安装阿里云CLI，您可使用阿里云提供的云命令行[Cloud Shell](https://shell.aliyun.com/)。更多信息，请参见[什么是云命令行？](https://help.aliyun.com/zh/cloud-shell/what-is-the-cloud-command-line)。登录阿里云控制台，单击顶部导航栏中工单右侧的 Cloud Shell 图标（终端样式图标）即可启动 Cloud Shell。
## 创建ECS实例
创建ECS实例时，有很多必填参数，包括交换机ID、安全组、镜像等。您可以传入已经准备好的资源ID，或者调用以下OpenAPI创建对应资源。
创建VPC。
VPC是一种专有的云上私有网络，允许用户在公共云上配置和管理一个逻辑隔离的网络区域。
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateVpc](../../../vpc/documents/api-createvpc.md) | RegionId | 地域： cn-hangzhou |
| CidrBlock | VPC 网段： 192.168.0.0/16 |  |
创建交换机。
交换机是一种在虚拟化环境中使用的网络交换设备，它模拟了物理交换机的功能，使虚拟机（VMs）之间以及虚拟机与物理网络之间可以进行通信。
| API | 参数 | 示例取值 |
| --- | --- | --- |
|  | RegionId | 地域： cn-hangzhou |
| [CreateVSwitch](../../../vpc/documents/api-createvswitch.md) | ZoneId | 可用区： cn-hangzhou-i |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3**** |  |
| CidrBlock | 交换机网段： 192.168.0.0/24 |  |
创建安全组。
安全组是一种虚拟防火墙，能够控制ECS实例的出入方向流量。
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateSecurityGroup](../api-createsecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |
给安全组添加入防护规则。
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [AuthorizeSecurityGroup](../api-authorizesecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| IpProtocol | 协议： tcp |  |
| SourceCidrIp | 源 CIDR： 0.0.0.0/0 |  |
| PortRange | 端口范围： Linux 实例： 22/22 Windows 实例： 3389/3389 |  |
创建ECS实例。
使用ECS，您可以快速部署和运行应用程序，灵活调整资源以应对业务变化，同时享受高性能、高安全性和低成本的计算能力，适用于网站托管、应用开发、数据处理等多种场景。
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [RunInstances](../api-runinstances.md) | RegionId | 地域： cn-hangzhou |
| ImageId | 镜像：使用 Alibaba Cloud Linux 镜像 aliyun_3_x64_20G_alibase_20240819.vhd |  |
| InstanceType | 实例规格： ecs.e-c1m1.large |  |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| VSwitchId | 交换机 ID： vsw-bp1nzprm8h7mmnl8t **** |  |
| InstanceName | 实例名称： ecs_cli_demo |  |
| InstanceChargeType | 付费方式：实例按照按量付费的方式 PostPaid 说明 您需要确保账号余额能够完成支付。 |  |
| PASSWORD | 登录密码： ****** |  |
| InternetMaxBandwidthOut | 公网出带宽最大值。若大于 0，则自动为实例分配公网 IP。 |  |
| SystemDisk.Category | 系统盘的云盘种类： cloud_essd |  |
| SystemDisk.Size | 系统盘的大小：40 GiB |  |
完整的示例代码如下：
重要
示例代码主要展示了CLI的使用方式。反复执行该脚本会导致VPC、交换机和安全组等资源的重复创建，从而可能引发资源浪费。因此，请务必仔细审阅并结合业务逻辑优化代码。
#!/bin/bash # 配置阿里云CLI使用的AccessKey和SecretKey # 注意：实际使用时，请确保已通过环境变量或配置文件安全地设置了AccessKey和SecretKey # 1. 设置变量 INSTANCE_NAME="ecs_cli_demo" #2. 安装jq工具 echo "正在安装依赖工具jq..." yum install jq sleep 3 # 3. 创建VPC、VSwitch、SecurityGtoup echo "正在创建VPC..." VpcId=$(aliyun vpc CreateVpc --RegionId cn-hangzhou --CidrBlock 192.168.0.0/16 | jq -r .VpcId) aliyun vpc DescribeVpcAttribute --RegionId cn-hangzhou --VpcId ${VpcId} --waiter expr='Status' to=Available > /dev/null 2>&1 echo "正在创建VSwitch..." VSwitchId=$(aliyun vpc CreateVSwitch --CidrBlock 192.168.0.0/24 --VpcId ${VpcId} --ZoneId=cn-hangzhou-i | jq -r .VSwitchId) echo "正在创建SecurityGtoup..." SecurityGroupId=$(aliyun ecs CreateSecurityGroup --RegionId cn-hangzhou --VpcId ${VpcId} | jq -r .SecurityGroupId) aliyun ecs AuthorizeSecurityGroup --RegionId cn-hangzhou --SecurityGroupId ${SecurityGroupId} --IpProtocol tcp --SourceCidrIp 0.0.0.0/0 --PortRange 22/22 > /dev/null 2>&1 read -s -p "Input Your Password:" PASSWORD echo echo "PASSWORD OK." # 4. 执行创建ECS实例的命令 echo "正在创建ECS实例..." INSTANCE_ID_RAW=$(aliyun ecs RunInstances \ --RegionId cn-hangzhou \ --ImageId aliyun_3_x64_20G_alibase_20240819.vhd \ --InstanceType ecs.e-c1m1.large \ --SecurityGroupId ${SecurityGroupId} \ --VSwitchId ${VSwitchId} \ --InstanceName $INSTANCE_NAME \ --InstanceChargeType PostPaid \ --InternetMaxBandwidthOut 1 \ --Password $PASSWORD \ --SystemDisk.Category cloud_essd \ --SystemDisk.Size 40) # 5. 提取InstanceId，用于后续打印状态 INSTANCE_ID=$(echo "$INSTANCE_ID_RAW" | jq -r '.InstanceIdSets.InstanceIdSet[]') # 6. 休息20秒，等待ECS创建中... echo "等待ECS创建中..." sleep 20 # 7. 查询ECS状态 echo "查询ECS状态..." INSTANCE_ID_QUOTED=$(printf '"%s"' "$INSTANCE_ID") aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --InstanceIds "[${INSTANCE_ID_QUOTED}]" \ --output cols=InstanceId,InstanceName,InstanceType,ImageId,Status rows=Instances.Instance[]
创建Shell脚本，并运行，预期结果如下：
[root@i-xxxxx Z ~]# bash ecs-cli.sh 正在安装依赖工具jq... Last metadata expiration check: 0:24:56 ago on Tue 22 Oct 2024 09:24:50 AM CST. Package jq-1.6-15.al8.x86_64 is already installed. Dependencies resolved. Nothing to do. Complete! 正在创建VPC... 正在创建VSwitch... 正在创建SecurityGtoup... Input Your Password: PASSWORD OK. 正在创建ECS实例... 等待ECS创建中... 查询ECS状态... InstanceId | InstanceName | InstanceType | ImageId | Status ---------- | ------------ | ------------ | ------- | ------- i-bpxxxxxxxxxxxz4 | ecs_cli_demo | ecs.e-c1m1.large | aliyun_3_x64_20G_alibase_20240819.vhd | Running
## 连接实例
通过SSH方式登录ECS实例，就可以进行部署业务、搭建应用等操作。
获取实例的公网IP信息。
调用[DescribeInstances](api-ecs-2014-05-26-describeinstances.md)，通过<实例ID>获取实例的公网IP信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --InstanceIds '["<实例ID>"]'
返回示例
参数PublicIpAddresses为实例的公网IP信息。
"PublicIpAddress": { "IpAddress": [ "115.29.xxx.xxx" ] }
连接ECS实例。
ssh <用户名>@<公网IP>[root@i-xxx bfZ ~ ]# ssh root@1xxx The authenticity of host 'xxx (xxx)' can't be established. ECDSA key fingerprint is SHA256:PVyhCaxxx4mecykrU. Are you sure you want to continue connecting (yes/no/[fingerprint])? yes Warning: Permanently added 'xxx' (ECDSA) to the list of known hosts. root@1xxx's password: Welcome to Alibaba Cloud Elastic Compute Service ! Last login: Thu Oct 10 13:31:58 2024 from xxx.67 [root@iZ xxx ugZ ~]#
## 释放资源
当您不再需要所创建的资源时，可以调用以下OpenAPI接口以释放该资源。
说明
根据您的实际需求，选择相应的OpenAPI释放资源 。本示例释放上述步骤创建的所有资源。
释放ECS实例
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteInstances](../api-deleteinstances.md) | RegionId | 地域： cn-hangzhou |
| InstanceId | 实例 ID： i-bp17f3kzgtzzj91r**** |  |
删除安全组
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteSecurityGroup](api-ecs-2014-05-26-deletesecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
删除交换机
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteVSwitch](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevswitch.md) | RegionId | 地域： cn-hangzhou |
| VSwitchId | 交换机 ID： vsw-bp1nzprm8h7mmnl8t **** |  |
删除VPC
| API | 参数 | 示例取值 |
| --- | --- | --- |
| [DeleteVpc](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-deletevpc.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |
示例代码如下：
#!/bin/bash # 定义要释放的资源信息 INSTANCE_ID='ecs_cli_demo' # ECS实例ID SECURITY_GROUP_ID='sg-bp1esyhwfbqeyudt****' # 安全组ID VSWITCH_ID='vsw-bp1nzprm8h7mmnl8t****' # VSwitchID VPC_ID='vpc-bp1aag0sb9s4i92i3****' # VPC ID REGION='cn-hangzhou' # 区域 echo "正在释放资源..." # 删除实例 aliyun ecs DeleteInstance \ --region ${REGION} \ --InstanceId ${INSTANCE_ID} # 删除安全组 aliyun ecs DeleteSecurityGroup \ --region ${REGION} \ --RegionId ${REGION} \ --SecurityGroupId ${SECURITY_GROUP_ID} # 删除 VSwitch aliyun vpc DeleteVSwitch \ --region ${REGION} \ --RegionId ${REGION} \ --VSwitchId ${VSWITCH_ID} # 删除 VPC aliyun vpc DeleteVpc \ --region ${REGION} \ --RegionId ${REGION} \ --VpcId ${VPC_ID} echo "释放完成"
## 相关文档
您可以在命令行执行以下命令，查询支持的CLI命令列表。
aliyun ecs --help
您可以在命令行按照以下命令结构，调用ECS API。详细输入参数，可以参考各API文档。
aliyun ecs <API Name> --<参数1 取值1> --<参数2 取值2> ...
生成CLI命令
为了能够让开发者快速高效地学习和使用云产品OpenAPI，阿里云为用户提供OpenAPI网站。它是一款集OpenAPI智能搜索、文档、在线调试、SDK获取、CodeSample、调用出错诊断、调用统计为一体的产品。您可以通过OpenAPI自动生成API对应的CLI代码。更多信息，请参见[什么是](https://help.aliyun.com/zh/openapi/what-is-openapi)[OpenAPI](https://help.aliyun.com/zh/openapi/what-is-openapi)。
登录[云服务器](https://api.aliyun.com/api/Ecs/2014-05-26/RunInstances?RegionId=cn-hangzhou&params={%22RegionId%22:%22cn-hangzhou%22})[ECS API](https://api.aliyun.com/api/Ecs/2014-05-26/RunInstances?RegionId=cn-hangzhou&params={%22RegionId%22:%22cn-hangzhou%22})[调试列表](https://api.aliyun.com/api/Ecs/2014-05-26/RunInstances?RegionId=cn-hangzhou&params={%22RegionId%22:%22cn-hangzhou%22})。
选择您需要使用的API，并填写参数。
单击右侧的CLI示例页签即可生成携带参数的命令。
例如，选择StartInstanceAPI 并填写InstanceId等参数后，CLI示例页签会自动生成对应命令，如aliyun ecs StartInstance --region cn-hangzhou --InstanceId 'i-bp1i79spj7zmoqg****'。
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
