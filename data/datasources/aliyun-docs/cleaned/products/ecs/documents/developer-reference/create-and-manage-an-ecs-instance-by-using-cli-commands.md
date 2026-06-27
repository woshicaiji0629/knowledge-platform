# 通过CLI使用和管理ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/developer-reference/create-and-manage-an-ecs-instance-by-using-cli-commands

# CLI参考
阿里云CLI（Command Line Interface）是一种命令行工具，允许用户在终端或命令行界面调用阿里云API，来创建、配置、管理阿里云云资源。本文主要介绍如何使用阿里云CLI调用ECS API来创建和管理ECS实例的方法及其常用示例。
说明
关于阿里云CLI的详细信息，请参见[什么是阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。
## CLI使用方式
### 安装和配置CLI
使用本地终端
安装CLI。
阿里云CLI提供了Windows、Linux和macOS三种操作系统下的安装服务，请根据您使用设备的操作系统选择：
[安装](https://help.aliyun.com/zh/cli/install-cli-on-windows#task-525890)[CLI（Windows）](https://help.aliyun.com/zh/cli/install-cli-on-windows#task-525890)
[安装](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli#task-592837)[CLI（Linux）](https://help.aliyun.com/zh/cli/install-update-alibaba-cloud-cli#task-592837)
[安装](https://help.aliyun.com/zh/cli/install-cli-on-macos#task-592875)[CLI（macOS）](https://help.aliyun.com/zh/cli/install-cli-on-macos#task-592875)
配置CLI。
配置调用阿里云资源所需的凭证信息、地域、语言等。具体配置，请参见[配置凭证](https://help.aliyun.com/zh/cli/configure-credentials/#b265231e1dwy9)。
重要
为保证账号安全，建议您创建专用于API访问的RAM用户并创建对应的AccessKey。更多关于凭据的安全使用建议，请参见[凭据的安全使用方案](https://help.aliyun.com/zh/openapi/accesskey-security-solution)。
通过Cloud Shell（适用于调试）
通过阿里云控制台使用CLI时，无需做任何安装配置操作即可使用。由于其销毁特性会导致数据丢失，建议您使用阿里云控制台做简单、快速的操作，例如调试。
重要
到期销毁：Cloud Shell创建的虚拟机只有1小时使用期限，到期后会立即销毁虚拟机。再次启动时，会创建一台全新的虚拟机。
无操作销毁：无交互式操作30分钟或者关闭所有会话窗口将视为终止操作，在终止操作后15分钟云命令行将销毁此台虚拟机。再次启动云命令行时，会为您创建一台全新的虚拟机。更多使用限制，请参见[使用限制](https://help.aliyun.com/zh/cloud-shell/restrictions-on-use)。
登录[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)，单击右上角的Cloud Shell图标，进入Cloud Shell控制台。
### 通过CLI调用ECS API
重要
不同数据类型字段需要遵循的格式要求，详细说明，请参见[参数格式](https://help.aliyun.com/zh/cli/understanding-command-line-parameters)。
关于命令结构说明，请参见[生成并调用命令](https://help.aliyun.com/zh/cli/sample-commands#1640a5c2c077i)。
调用接口前建议您仔细阅读相关API的使用说明。
安装配置好CLI后，您可以在终端按照以下命令结构，调用ECS API。
aliyun ecs <API Name> --<参数1 取值1> --<参数2 取值2> ...
可以通过OpenAPI自动生成API对应的CLI代码
登录[云服务器](https://api.aliyun.com/api/Ecs/2014-05-26/RunInstances?RegionId=cn-hangzhou&params={%22RegionId%22:%22cn-hangzhou%22})[ECS API](https://api.aliyun.com/api/Ecs/2014-05-26/RunInstances?RegionId=cn-hangzhou&params={%22RegionId%22:%22cn-hangzhou%22})[调试列表](https://api.aliyun.com/api/Ecs/2014-05-26/RunInstances?RegionId=cn-hangzhou&params={%22RegionId%22:%22cn-hangzhou%22})。
选择您需要使用的API，并填写参数。
单击右侧的CLI示例页签即可生成携带参数的命令。
## CLI调用示例
以下示例为您展示如何使用阿里云CLI调用云服务器ECS API。
重要
以下请求仅为示例，具体请求命令请根据实际需求修改。
### 创建ECS实例
以在杭州地域创建一个基于Alibaba Cloud Linux镜像的包年包月的ECS实例为例，指导您如何通过CLI创建ECS实例。
准备工作。
在创建ECS实例前，请确保您已经创建了专有网络VPC、交换机、安全组，并获取其ID。
说明
如果您已有上述资源且符合需求，可跳过该步骤。
调用[CreateVpc](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-createvpc.md)创建VPC。
假设在华东1（杭州）创建专有网络VPC，VPC网段为192.168.0.0/16。
请求示例
aliyun vpc CreateVpc \ --RegionId cn-hangzhou \ --CidrBlock 192.168.0.0/16
返回示例
{ "RequestId": "EC94C73B-8103-4B86-B353-E65C7C9E****", "ResourceGroupId": "rg-acfmzw2jz2z****", "RouteTableId": "vtb-bp1jxpr9ji5wcn4yv****", "VRouterId": "vrt-bp1dyxemup2q4ouga****", "VpcId": "vpc-bp1d9v4763ym2hlzt****" }
调用[CreateVSwitch](../../../vpc/documents/developer-reference/api-vpc-2016-04-28-createvswitch.md)在VPC中创建交换机。
假设交换机网段为192.168.0.0/24，VPC ID为vpc-bp1d9v4763ym2hlzt****。
请求示例
aliyun vpc CreateVSwitch \ --CidrBlock 192.168.0.0/24 \ --VpcId vpc-bp1d9v4763ym2hlzt**** \ --ZoneId=cn-hangzhou-i
返回示例
{ "RequestId": "AF1787C4-0D81-44F0-A324-D5C54EA0****", "VSwitchId": "vsw-bp11hf5r945gewysp****" }
调用[CreateSecurityGroup](api-ecs-2014-05-26-createsecuritygroup.md)创建安全组。
请求示例
aliyun ecs CreateSecurityGroup \ --RegionId cn-hangzhou \ --VpcId vpc-bp1d9v4763ym2hlzt****
返回示例
{ "RequestId": "B1C25C34-9B84-49E3-9E50-FB7D7970****", "SecurityGroupId": "sg-bp18z2q1jg4gq95t****" }
调用[AuthorizeSecurityGroup](api-ecs-2014-05-26-authorizesecuritygroup.md)添加安全组规则。
假设在安全组（ID为sg-bp18z2q1jg4gq95t****）的入方向放行22端口，协议为TCP。
请求示例
aliyun ecs AuthorizeSecurityGroup \ --RegionId cn-hangzhou \ --SecurityGroupId sg-bp18z2q1jg4gq95t**** \ --IpProtocol tcp \ --SourceCidrIp 0.0.0.0/0 \ --PortRange 22/22
返回示例
{ "RequestId": "FA8B1E61-C9C9-4D91-9628-64B8E2F4****" }
创建ECS实例。
调用[RunInstances](api-ecs-2014-05-26-runinstances.md)创建一个包年包月的ECS实例。
场景示例
| 参数 | 示例取值 |
| --- | --- |
| RegionId | 地域： cn-hangzhou |
| ImageId | 镜像：推荐使用 Alibaba Cloud Linux 镜像 aliyun_3_x64_20G_alibase_20240528.vhd 。 |
| InstanceType | 实例规格： 个人应用：推荐选择 2 vCPU 2 GiB 的实例规格 ecs.e-c1m1.large 。 中小企业应用：推荐选择 2 vCPU 4 GiB 的实例规格 ecs.c7.large 。 |
| SecurityGroupId | 安全组 ID：根据 [CreateSecurityGroup](../api-createsecuritygroup.md) 返回结果。 示例： sg-bp18z2q1jg4gq95t**** |
| VSwitchId | 交换机 ID：根据 [CreateVSwitch](../../../vpc/documents/api-createvswitch.md) 返回结果。 示例： vsw-bp11hf5r945gewysp**** |
| InstanceName | 实例名称。 示例： ecs_cli_demo |
| InstanceChargeType | 付费方式：实例按照包年包月的付费方式 PrePaid 。 说明 您需要确保账号余额能够完成支付。 |
| PeriodUnit | 付费周期单位： Month |
| Period | 付费时长： 1 |
| InternetMaxBandwidthOut | 公网 IP 带宽： 1 |
| Password | 实例登录密码： <yourPassword> 说明 您需要自定义复杂密码以保护 ECS 实例的安全。 |
| SystemDisk.Category | 系统盘类型：cloud_essd |
| SystemDisk.Size | 系统盘大小：40 |
请求示例
aliyun ecs RunInstances \ --RegionId cn-hangzhou \ --ImageId aliyun_3_x64_20G_alibase_20240528.vhd \ --InstanceType ecs.c7.large \ --SecurityGroupId sg-bp18z2q1jg4gq95t**** \ --VSwitchId vsw-bp11hf5r945gewysp**** \ --InstanceName ecs_cli_demo \ --InstanceChargeType PrePaid \ --PeriodUnit Month \ --Period 1 \ --InternetMaxBandwidthOut 1 \ --Password <yourPassword> \ --SystemDisk.Category cloud_essd \ --SystemDisk.Size 40
返回示例
{ "InstanceIdSets": { "InstanceIdSet": [ "i-bp1de173dp87k5uv****" ] }, "OrderId": 23577729747****, "RequestId": "B0855F1A-279F-5153-BAA9-C245E073****", "TradePrice": **** }
### 连接实例
获取实例的公网IP信息。
调用[DescribeInstances](api-ecs-2014-05-26-describeinstances.md)，通过实例ID（i-bp1ducce5hs1jm98****）获取实例的公网IP信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --InstanceIds '["i-bp1ducce5hs1jm98****"]'
返回示例
参数PublicIpAddresses为实例的公网IP信息。
连接ECS实例。
ssh <用户名>@<公网IP>
### 启动实例
调用[StartInstance](../api-startinstance.md)接口启动一台ECS实例。
场景示例：实例ID为i-bp1aq39j2yul5y01****，地域为华东1（杭州）（cn-hangzhou），启动实例时不进行故障处理，并且预检查后直接启动ECS实例。
请求示例
aliyun ecs StartInstance \ --RegionId cn-hangzhou \ --InstanceId i-bp1aq39j2yul5y01**** \ --InitLocalDisk false \ --DryRun false
返回示例
{ "RequestId": "2DD09CBD-1F4D-4923-94C7-F3BD67137BBE" }
### 查询实例的详细信息
您可以调用[DescribeInstances](../api-describeinstances.md)接口查询一台或多台ECS实例的详细信息。
示例1：根据实例ID查询ECS实例
假设查询实例ID为i-bp14a7xie8erwsvo****的实例信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --InstanceIds '["i-bp14a7xie8erwsvo****"]' \ --output cols=InstanceId,InstanceName,Description,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | Description | ImageId | Status ---------- | ------------ | ----------- | ------- | ------ i-bp1de173dp87k5uv**** | ecs_cli_demo | | aliyun_3_x64_20G_alibase_20240528.vhd | Running
示例2：根据标签查询ECS实例
假设查询绑定owner:zhangsan标签的ECS实例信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --Tag.1.Key owner \ --Tag.1.Value zhangsan \ --output cols=InstanceId,InstanceName,Description,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | Description | ImageId | Status ---------- | ------------ | ----------- | ------- | ------ i-bp1de173dp87k5uv**** | ecs_cli_demo | | aliyun_3_x64_20G_alibase_20240528.vhd | Running
示例3：根据镜像ID查询ECS实例
查询镜像为m-bp12qhgxbmp5eh02****标签的ECS实例信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --ImageId m-bp12qhgxbmp5eh02**** \ --output cols=InstanceId,InstanceName,Description,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | Description | ImageId | Status ---------- | ------------ | ----------- | ------- | ------ i-bp14a7xie8erwsvo**** | demo01 | desc01 | m-bp12qhgxbmp5eh02**** | Running i-bp1aq39j2yul5y01**** | demo02 | desc02 | m-bp12qhgxbmp5eh02**** | Stopped
示例4：查询指定VPC内的ECS实例
假设VPC ID为vpc-bp1vwnn14rqpyiczj****、交换机ID为vsw-bp1ddbrxdlrcbim46****。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --VpcId vpc-bp1vwnn14rqpyiczj**** \ --VSwitchId vsw-bp1ddbrxdlrcbim46**** \ --output cols=InstanceId,InstanceName,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | ImageId | Status ---------- | ------------ | ------- | ------ i-bp14a7xie8erwsvo**** | namedemo01 | m-bp12qhgxbmp5eh02**** | Running i-bp1c271nqm264lwj**** | namedemo02 | P2VSImageLnx125 | Running i-bp18a6ub0vt1tvn1**** | namedemo03 | aliyun_3_x64_20G_alibase_20240528.vhd | Running i-bp1aq39j2yul5y01**** | namedemo04 | m-bp12qhgxbmp5eh02**** | Stopped
示例5：分页查询ECS实例
调用[DescribeInstances](../api-describeinstances.md)分页查询杭州地域的ECS实例，每页展示5条信息。
请求示例
aliyun ecs DescribeInstances \ --RegionId cn-hangzhou \ --PageNumber 2 \ --PageSize 5 \ --output cols=InstanceId,InstanceName,ImageId,Status rows=Instances.Instance[]
返回示例
InstanceId | InstanceName | ImageId | Status ---------- | ------------ | ------- | ------ i-bp1akazu9o0rm7q0**** | demoname01 | centos_8_0_x64_20G_alibase_20191225.vhd | Running i-bp134jm1g6kqyiqu**** | demoname02 | m-bp1bc3g3b032o0ja**** | Running i-bp17qwke5y0v7hk2**** | demoname03 | centos_7_02_64_20G_alibase_20170818.vhd | Running i-bp18a6ub0vt1tvn1**** | demoname04 | centos_7_02_64_20G_alibase_20170818.vhd | Running i-bp1aq39j2yul5y01**** | demoname05 | m-bp12qhgxbmp5eh02**** | Stopped
### 创建快照
调用[CreateSnapshot](../api-createsnapshot.md)接口创建快照。
场景示例：为ESSD云盘d-bp14bjlwo3t3owin****创建一个快照（快照名称为demoname，描述为demo，保留时间：3天）。
请求示例
aliyun ecs CreateSnapshot \ --DiskId d-bp14bjlwo3t3owin**** \ --SnapshotName demoname \ --Description demo \ --RetentionDays 3
返回示例
{ "RequestId": "DFB0B01F-420D-4932-911E-7328920C2012", "SnapshotId": "s-bp1eyr9nxxoo9icj****" }
### 通过实例创建自定义镜像
调用[CreateImage](../api-createimage.md)接口，基于ECS实例创建一个自定义镜像。
场景示例
| 参数 | 示例取值 |
| --- | --- |
| 实例 ID | i-bp1aq39j2yul5y01**** |
| 操作系统 | Alibaba Cloud Linux（即 Platform 为 Aliyun） |
| 地域 | cn-hangzhou |
请求示例
aliyun ecs CreateImage \ --RegionId cn-hangzhou \ --InstanceId i-bp1aq39j2yul5y01**** \ --ImageName demoimage \ --Description demoimage \ --Platform Aliyun
返回示例
{ "ImageId": "m-bp1503ydxxrppctb****", "RequestId": "011AE447-20CE-4043-81AC-7AF2BBC4****" }
### 停止实例
调用[StopInstance](../api-stopinstance.md)停止一台运行中（Running）的ECS实例，正常关机（ForceStop为 false）且停机模式为普通停机模式（StoppedMode为KeepCharging，即停止后仍旧保留实例并继续收费），预检查后正常停止ECS实例。
场景示例：实例ID为i-bp1aq39j2yul5y01****，地域为华东1（杭州）（cn-hangzhou）。
请求示例
aliyun ecs StopInstance \ --RegionId cn-hangzhou \ --InstanceId i-bp1aq39j2yul5y01**** \ --ForceStop false \ --StoppedMode KeepCharging \ --DryRun false
返回示例
{ "RequestId": "121B5745-4983-57B1-BC97-C3A3536E****" }
## 相关文档
本示例仅使用部分API，更多ECS API信息，请参见[API](api-ecs-2014-05-26-overview.md)[概览](api-ecs-2014-05-26-overview.md)。
在阿里云CLI中，您可根据需要使用命令行选项，用来修改命令的默认行为或为命令提供额外功能，请参见[命令行选项](https://help.aliyun.com/zh/cli/command-line-options)。
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
