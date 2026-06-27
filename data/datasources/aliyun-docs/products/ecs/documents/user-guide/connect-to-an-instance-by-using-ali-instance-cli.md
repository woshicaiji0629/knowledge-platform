# 通过会话管理CLIali-instance-cli）连接实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/connect-to-an-instance-by-using-ali-instance-cli

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 通过会话管理CLI（ali-instance-cli）连接实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以在本机命令行通过会话管理CLI连接到ECS实例，支持免密连接无公网实例。相比于传统的SSH或RDP直连的方式更加安全方便。本文为您介绍会话管理CLI的基本使用。

## 什么是会话管理CLI？

会话管理CLI，即ali-instance-cli，是阿里云为您提供的命令行工具，在您的个人计算机上安装并配置该工具后，即可通过命令行的方式使用会话管理连接实例。

此外，在使用ali-instance-cli时， 您可以配合使用阿里云CLI工具，实现纯命令行操作，关于阿里云CLI的更多信息，请参见[什么是阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)。

## 准备工作

开启会话管理服务

在使用ali-instance-cli之前，需要先确保当前阿里云账号已开启会话管理服务。开启会话管理服务仅可以在控制台操作，具体操作如下：

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

在实例页面，找到待连接的实例，单击对应操作列的远程连接。

- 

单击展开其他登录方式，找到通过会话管理远程连接，将会话管理已关闭右侧的按钮打开，并根据界面提示完成开通操作。

检查实例运行状态是否为运行中

仅支持通过会话管理连接到运行中状态的实例。

## 控制台

实例运行状态可以在ECS控制台中的实例模块查看，运行中的实例如图所示：

查看实例状态的操作说明，请参见[查看实例信息](products/ecs/documents/user-guide/view-instance-information.md)。

|  |  |
| --- | --- |


## 阿里云CLI

如果您已经配置好了阿里云CLI，您可以通过以下命令查询实例运行状态。关于该API的更多参数说明，请参见[查询实例的状态信息列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstancestatus.md)。

以查询杭州地域下实例ID为i-bp1******实例为例，输入以下命令查询实例运行状态。aliyun ecs DescribeInstanceStatus --region cn-hangzhou --RegionId 'cn-hangzhou' --InstanceId.1 'i-bp1******'

如果查询出对应实例的Status为Running则实例为运行中。

{ "TotalCount": 1, "RequestId": "A413****-****-****-****-****611B", "PageSize": 1, "PageNumber": 1, "InstanceStatuses": { "InstanceStatus": [ { "Status": "Running", "InstanceId": "i-bp1******" } ] } }

除此API外，您还可以通过其他API查询实例运行状态，请参见[查询实例的详细信息列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)。

## API

如果需要通过API查询实例运行状态，请参见[查询实例的状态信息列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstancestatus.md)、[查询实例的详细信息列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)。

检查实例云助手Agent是否已安装

会话管理基于云助手的功能实现，您可以通过以下方式查询实例是否已经安装云助手Agent。

2017年12月01日之后使用官方公共镜像创建的ECS实例，默认预装了云助手Agent。如果您的实例是2017年12月01日之前购买的或使用自行上传的自定义镜像创建的实例，需自行安装云助手Agent，请参见[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

## 控制台

会话管理基于云助手的功能实现，需要在实例中安装云助手Agent。云助手Agent状态可以在ECS控制台的云助手模块查看，已经安装云助手的实例如图所示：

2017年12月01日之后使用官方公共镜像创建的ECS实例，默认预装了云助手Agent。如果您的实例是2017年12月01日之前购买的或使用自行上传的自定义镜像创建的实例，需自行安装云助手Agent，请参见[安装云助手](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)[Agent](products/ecs/documents/user-guide/install-the-cloud-assistant-agent.md)。

|  |  |
| --- | --- |


查看云助手Agent状态以及处理异常状态的具体操作，请参见[查看云助手状态及异常状态处理](products/ecs/documents/user-guide/check-the-status-of-cloud-assistant-and-handle-exceptions.md)。

## 阿里云CLI

如果您已经配置好了阿里云CLI，您可以通过以下命令查询实例是否安装云助手且云助手版本是否支持使用会话管理。具体参数说明，请参见[查询云助手安装状态](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)。

以查询杭州地域下实例ID为i-bp1******实例为例，输入以下命令查询实例运行状态。aliyun ecs DescribeCloudAssistantStatus --region cn-hangzhou --RegionId 'cn-hangzhou' --InstanceId.1 'i-bp1******'

如果查询出CloudAssistantStatus（云助手运行状态）为true且SupportSessionManager（是否支持会话管理）也为true，即该实例支持通过会话管理连接实例。

{ "TotalCount": 1, "PageSize": 1, "RequestId": "DB34****-****-****-****-****A749", "NextToken": "", "PageNumber": 1, "InstanceCloudAssistantStatusSet": { "InstanceCloudAssistantStatus": [ { "CloudAssistantVersion": "2.2.3.857", "SupportSessionManager": true, "InstanceId": "i-bp1******", "InvocationCount": 4, "OSType": "Linux", "CloudAssistantStatus": "true", "LastHeartbeatTime": "2024-12-10T02:38:04Z", "LastInvokedTime": "2024-12-08T16:02:45Z", "ActiveTaskCount": 0 } ] } }

## API

如果需要通过API查询实例云助手Agent状态，请参见[查询云助手安装状态](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)。

准备用于使用会话管理的RAM用户的凭证

在使用ali-instance-cli工具时，配置阶段要求设置RAM用户的AccessKey、STS Token。当通过会话管理操作连接实例时，系统会验证此凭证对应的RAM用户是否拥有ecs:StartTerminalSession权限，这是允许通过会话管理建立与ECS实例连接的必要权限。

此外，在自定义权限策略时，可以通过指定Resource字段来限定RAM用户能够通过会话管理连接的具体ECS实例。权限策略示例如下：

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" } ] }

关于CredentialsURI、STS Token的更多说明，请参见[创建](products/ram/documents/create-an-accesskey-pair-1.md)[AccessKey](products/ram/documents/create-an-accesskey-pair-1.md)、[什么是](products/ram/documents/user-guide/what-is-sts.md)[STS](products/ram/documents/user-guide/what-is-sts.md)。

为RAM用户授权，请参见[为](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。

## 1. 安装&配置会话管理CLI

说明

如果您已经安装并配置完成会话管理CLI，可跳过本步骤。

### 1.1 安装

首先需要在您的个人计算机中安装会话管理CLI（ali-instance-cli），不同操作系统安装方式不同，具体操作如下。

## Windows

[点击下载](https://aliyun-client-assist.oss-accelerate.aliyuncs.com/session-manager/windows/ali-instance-cli.exe)[Windows](https://aliyun-client-assist.oss-accelerate.aliyuncs.com/session-manager/windows/ali-instance-cli.exe)[版](https://aliyun-client-assist.oss-accelerate.aliyuncs.com/session-manager/windows/ali-instance-cli.exe)[ali-instance-cli](https://aliyun-client-assist.oss-accelerate.aliyuncs.com/session-manager/windows/ali-instance-cli.exe)，并保存到本地文件夹中。

本文以将ali-instance-cli.exe保存在C:\Users\test文件夹中为例。

## macOS

在macOS的终端中，输入以下命令下载mac版ali-instance-cli。

curl -O https://aliyun-client-assist.oss-accelerate.aliyuncs.com/session-manager/mac/ali-instance-cli

下载完成后，输入以下命令为ali-instance-cli赋予可执行权限。

chmod a+x ali-instance-cli

## Linux

输入以下命令安装Linux版ali-instance-cli。

## x86架构

curl -O https://aliyun-client-assist.oss-accelerate.aliyuncs.com/session-manager/linux/ali-instance-cli

## arm架构

curl -O https://aliyun-client-assist.oss-cn-beijing.aliyuncs.com/session-manager/linux_arm/ali-instance-cli

下载完成后，输入以下命令为ali-instance-cli赋予可执行权限。

chmod a+x ali-instance-cli

### 1.2 配置

在您的个人计算机使用ali-instance-cli连接阿里云实例时，需要配置相关身份凭证，即AccessKey，具体说明，请参见[准备用于使用会话管理的](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)[RAM](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)[用户的凭证](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)。

## Windows

- 

选择开始>运行，输入cmd，按Enter键，打开命令提示符窗口。

- 

切换到ali-instance-cli.exe所在目录，本文以C:\Users\test为例。

cd C:\Users\test

- 

配置凭证。支持以下三种配置方式：

## AccessKey

执行如下命令，并根据界面提示配置Access Key Id、Access Key Secret、Region Id。

ali-instance-cli.exe configure --mode AK

## STS Token

执行以下命令完成配置操作：

ali-instance-cli.exe configure set --mode StsToken --region "<region>" --access-key-id "<ak>" --access-key-secret "<sk>" --sts-token "<sts_token>"

<region>、<ak>、<sk>、<sts_token>要修改为实际的Region ID、AccessKey ID、AccessKey Secret和STS Token。

## CredentialsURI

执行如下命令，根据界面提示，输入Credentials URI和Region Id。

ali-instance-cli.exe configure --mode=CredentialsURI

配置完成后，显示如下内容证明配置完成。

## macOS/Linux

- 

进入ali-instance-cli所在目录，本文以当前用户根目录~为例。

cd ~

- 

配置凭证。

## AccessKey

执行如下命令，并根据界面提示配置Access Key Id、Access Key Secret、Region Id。

./ali-instance-cli configure --mode AK

## STS Token

执行以下命令完成配置操作：

./ali-instance-cli configure set --mode StsToken --region "<region>" --access-key-id "<ak>" --access-key-secret "<sk>" --sts-token "<sts_token>"

<region>、<ak>、<sk>、<sts_token>要修改为实际的Region ID、AccessKey ID、AccessKey Secret和STS Token。

## CredentialsURI

执行如下命令，根据界面提示，配置Credentials URI和Region Id。

./ali-instance-cli configure --mode=CredentialsURI

配置完成后，显示如下内容证明配置完成。

## 2. 通过会话管理连接实例

### 2.1 获取待连接实例的ID

通过会话管理连接实例时，需要先获取到目标实例的实例ID。

## 控制台

- 

- 

- 

| 访问 [ECS](https://ecs.console.aliyun.com/server/region) [控制台-实例](https://ecs.console.aliyun.com/server/region) 。 在页面左侧顶部，选择目标资源所在的资源组和地域。 在 实例 页面，找到待连接的实例，实例 ID 如图所示。 |  |
| --- | --- |


## 阿里云CLI

如果您已经配置好了阿里云CLI，您可以通过以下命令获取实例ID。具体参数说明，请参见[查询实例的详细信息列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)。

以查询杭州地域下名称为SessionManager-example的实例为例。aliyun ecs DescribeInstances --region cn-hangzhou --RegionId 'cn-hangzhou' --InstanceName 'SessionManager-example'

返回结果中InstanceId即实例ID。

## API

通过API查询实例ID，请参见[查询实例的详细信息列表](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstances.md)。

### 2.2 使用ali-instance-cli的会话管理功能

## 本机为Windows

进入命令提示符，在ali-instance-cli.exe所在目录，输入命令远程连接实例。其中<instance_id>为步骤2.1中获取的实例ID。

ali-instance-cli.exe session --instance <instance_id>

例如连接实例ID为i-bp1******的实例时，可输入以下命令完成连接操作。

ali-instance-cli.exe session --instance i-bp1******

如图所示，连接成功后，会进入对应实例的命令行界面。

## 本机为macOS/Linux

在终端中，进入ali-instance-cli所在目录，输入命令远程连接实例。其中<instance_id>为步骤2.1中获取的实例ID。

./ali-instance-cli session --instance <instance_id>

例如连接实例ID为i-bp1******的实例时，可输入以下命令完成连接操作。

./ali-instance-cli session --instance i-bp1******

如图所示，连接成功后，会进入对应实例的命令行界面。

## 更多功能

除了会话管理功能外，会话管理CLI（ali-instance-cli）还有以下功能：

- 

[访问无公网的实例（端口转发实现）](products/ecs/documents/user-guide/perform-port-forwarding-by-using-ali-instance-cli.md)

您可以通过ali-instance-cli的端口转发功能，将实例的某个端口映射到您个人计算机的某个端口，支持无公网实例。由此功能，您可以实现免代理，免跳板机的访问无公网实例上的服务。

- 

[注册临时](products/ecs/documents/user-guide/register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)[SSH](products/ecs/documents/user-guide/register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)[公钥](products/ecs/documents/user-guide/register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)

如果您使用SSH连接实例，您可以选择通过该功能向目标实例中注册临时公钥，此时，您可以通过与之对应的私钥连接实例。

## 常见问题

执行命令后卡住没反应（实例非运行中状态）

如果执行ali-instance-cli命令后命令行卡住没反应，可能是实例没有处于运行中状态，如何查看实例状态，请参见本文准备工作章节下的[检查实例运行状态是否为运行中](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)。

执行命令后卡住没反应（安全组设置问题）

如果执行ali-instance-cli命令后命令行卡住没反应，可能是没有在安全组出方向放通对应的端口。默认情况下普通安全组会在出方向放通所有端口的访问，如果更改了出方向规则或者使用了企业安全组，则可能会出现该问题。相关安全组说明如下：

通过会话管理连接ECS实例时，需要确保ECS中运行的云助手Agent与云助手服务端的网络连通性，即在安全组出方向设置以下规则：

与SSH、RDP等连接方式不同，由于会话管理是由云助手Agent主动与会话管理服务端建立WebSocket连接，因此仅需放行出方向的云助手服务端的WebSocket端口。关于会话管理的原理，请参见[会话管理工作原理](products/ecs/documents/user-guide/connect-to-an-instance-by-using-session-manager-2.md)。

重要

- 

如果使用普通安全组（包括默认安全组），默认情况下会放行所有的出方向流量，无需配置。

- 

如果使用企业安全组，默认情况下会禁用所有出方向的流量，需要配置以下规则。更多关于企业安全组的说明，请参见[普通安全组与企业级安全组](products/ecs/documents/user-guide/basic-security-groups-and-advanced-security-groups.md)。

添加安全组规则的具体操作，请参见[添加安全组规则](products/ecs/documents/user-guide/add-a-security-group-rule.md)。

| 授权策略 | 优先级 | 协议类型 | 端口范围 | 授权对象 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 允许 | 1 | 自定义 TCP | 443 | 100.100.0.0/16 | 用于访问云助手服务端。 |
| 允许 | 1 | 自定义 TCP | 443 | 100.0.0.0/8 | 访问 云助手 Agent 安装包所在服务器，用于安装或更新您的 云助手 Agent 。 |
| 允许 | 1 | 自定义 UDP | 53 | 0.0.0.0/0 | 用于解析域名。 |


此外，如果您计划仅通过会话管理连接实例，为了增加ECS实例的安全性，您可以取消放行安全组入方向上的SSH端口（默认22）或者RDP端口（默认3389）的规则。

执行命令后出现DeliveryTimeout提示（云助手Agent不在线）

如图所示，如果执行ali-instance-cli的命令时出现DeliveryTimeout提示，可能是云助手Agent不在线，检查云助手状态，请参见[检查实例云助手](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)[Agent](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)[是否已安装](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)。

执行命令报错session manager is disabled, please enable first

如果执行ali-instance-cli的命令出现session manager is disabled, please enable first报错，代表会话管理功能未开启，请通过控制台开启会话管理功能，具体操作，请参见[开启会话管理服务](products/ecs/documents/user-guide/connect-to-an-instance-by-using-ali-instance-cli.md)。

长时间未连接自动断开

使用会话管理连接到目标实例后，如果长时间没有任何操作连接会自动断开。默认的连接空闲时间为3分钟，可以通过--idle-timeout参数自定义最大空闲时间。

例如执行以下命令连接到目标实例后，连接空闲达到10分钟就会自动断开。

./ali-instance-cli session --instance instance-id --idle-timeout 600

说明

此功能需确保ali-instance-cli不低于以下版本：

- 

Linux：1.2.0.48

- 

Windows：1.1.0.48

- 

macOS：1.3.0.48

如何分析ali-instance-cli的日志

当使用会话管理CLI出现问题时，可以通过查看log分析具体问题。

- 

查看会话管理CLI工具的日志：在使用会话管理CLI（ali-instance-cli）时，会在该工具所在目录下生成log目录，如~/log/aliyun_ecs_session_log.2022XXXX，可以进入该目录查看相关日志。

- 

查看云助手Agent日志：

- 

Linux

/usr/local/share/aliyun-assist/云助手版本号/log/

- 

Windows

C:\ProgramData\aliyun\assist\云助手版本号\log

[上一篇：为会话管理开启会话加密](products/ecs/documents/user-guide/turn-on-session-encryption-for-session-management.md)[下一篇：通过会话管理CLI的端口转发访问无公网实例](products/ecs/documents/user-guide/perform-port-forwarding-by-using-ali-instance-cli.md)

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
