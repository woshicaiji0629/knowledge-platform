# 通过会话管理连接实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/connect-to-an-instance-by-using-session-manager-2

# 通过会话管理连接实例
会话管理是阿里云为您提供的免费的连接实例的工具，该工具基于云助手和WebSocket等技术实现，支持一键免密码、免跳板机连接到无公网实例。本文为您介绍会话管理的使用场景以及注意事项。
## 什么是会话管理？
重要
会话管理本身不收费，但如果需要保存会话管理操作记录，需开启会话操作记录投递功能，这将产生数据存储费用，开启该功能的具体操作，请参见[会话操作记录投递](use-the-session-record-delivery-feature.md)。
会话管理是阿里云为您提供的免费的连接实例的工具，该工具主要特点如下：
免密连接实例：在连接实例时无需输入实例密码。
支持连接无公网实例：使用该工具，无需您准备跳板机即可连接到无公网的实例。
在使用会话管理连接实例时，命令会经由阿里云的会话管理服务端转发到ECS实例。
多种客户端形态：
阿里云官网控制台：[直接在浏览器上使用会话管理客户端连接实例（免安装）](connect-to-an-instance-by-using-session-manager-1.md)
本机命令行（安装ali-instance-cli）：[在您的个人计算机上通过会话管理客户端连接实例（需安装](connect-to-an-instance-by-using-ali-instance-cli.md)[ali-instance-cli）](connect-to-an-instance-by-using-ali-instance-cli.md)
### 登录用户说明
通过会话管理连接实例时，Linux实例默认以ecs-assist-user用户登录，Windows实例默认以system用户登录，具体说明如下。
ecs-assist-user：Linux系统的一个普通用户，没有系统级的权限，只能执行被授权的操作，但可以通过使用sudo命令临时获得root权限执行操作。
system：Windows系统的一个本地系统账户，拥有系统最高权限。
### 使用限制&前提条件
仅支持连接到运行中状态的实例。
实例需安装云助手Agent：会话管理基于云助手的功能实现，需要在实例中安装云助手Agent。
2017年12月01日之后使用官方公共镜像创建的ECS实例，默认预装了云助手Agent。如果您的实例是2017年12月01日之前购买的或使用自行上传的自定义镜像创建的实例，若需要使用云助手相关功能，需自行安装云助手Agent，具体操作，请参见[安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
使用前请确保网络连通：由于云助手Agent会通过WebSocket协议与云助手服务端通讯，需要确保实例与云助手服务端的网络连通性，具体说明，请参见[相关安全组设置](connect-to-an-instance-by-using-session-manager-2.md)。
会话限制：在同一地域下，已创建并可用的会话不能超过 1000 个，单台实例处于连接状态的会话不能超过 20 个，单个会话连接的带宽限制为200kb/s。
### 更多功能&适用场景
通过端口转发访问无公网服务
使用会话管理客户端的端口转发功能，将实例的某个服务端口映射到您的本机，然后您可以直接通过访问本机的对应端口访问在ECS上的服务。比如访问内网部署的Web后端服务、通过SSH连接内网实例。会话管理是基于WebSocket建立连接，工作在TCP上，因此只支持TCP端口转发，不支持UDP。具体操作，请参见[通过会话管理](perform-port-forwarding-by-using-ali-instance-cli.md)[CLI](perform-port-forwarding-by-using-ali-instance-cli.md)[的端口转发访问无公网实例](perform-port-forwarding-by-using-ali-instance-cli.md)。
向实例添加临时SSH公钥
在您使用SSH连接实例时，您可以使用会话管理向实例内添加有效时间60s的临时公钥，然后通过密钥对的验证方式连接到实例。具体操作，请参见[通过会话管理](register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)[CLI](register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)[注册临时公钥免密登录实例](register-a-public-key-and-connect-to-an-instance-with-the-key-by-using-ali-instance-cli.md)。
会话操作记录投递
如果您是多人使用场景，可以通过会话操作记录投递功能，查看某个人的操作记录，便于您在后续进行操作审计。开启会话操作记录投递功能，请参见[会话操作记录投递](use-the-session-record-delivery-feature.md)。
### 会话管理工作原理
如图所示，在通过会话管理连接实例时，会话管理客户端和ECS实例将分别与云助手服务端建立WebSocket连接。一旦连接建立，您每次输入的命令都会经过云助手服务端转发至实例，由实例中的云助手Agent代为执行。
| 图中涉及的模块 云助手客户端 ：指您实际操作的客户端工具，如控制台上的会话管理、您本机的 ali-instance-cli 、阿里云客户端等。 云助手服务端 ：会话管理基于云助手实现，负责权限管理、会话状态管理。 ECS 实例中的云助手 Agent ：负责命令的执行。 细节说明 会话管理客户端 与 云助手服务端 建立 WebSocket 连接时（对应 步骤 2~4 ），服务端会进行鉴权，判断操作者是否有通过会话管理连接到该实例的权限。相关权限说明，请参见 [相关权限管理](connect-to-an-instance-by-using-session-manager-2.md) 。 ECS 中的 云助手 Agent 与 云助手服务端 建立 WebSocket 连接时（对应 步骤 5~6 ），是由云助手服务端通知 Agent 建立连接后，云助手 Agent 主动和云助手服务端建立连接。 因此，无需关注 ECS 实例安全组入方向的规则，仅需关注 出方向 上可以访问云助手服务端的对应 WebSocket 连接端口。相关安全组配置说明，请参见 [相关安全组设置](connect-to-an-instance-by-using-session-manager-2.md) 。 安全性 加密 ：会话管理客户端与云助手服务端、云助手服务端与 云助手 Agent 之间通信时，会通过 WSS（Web Socket Secure）协议建立 WebSocket 长连接，WSS 使用 SSL（Secure Socket Layer）加密 WebSocket 长连接，能够保障数据的安全。 鉴权 ：仅使用会话管理功能远程连接实例时无需管理密码，无密码泄露的风险。不同于 SSH、VNC 等需要通过用户名密码进行鉴权，会话管理采用 RAM 进行鉴权。相关权限说明，请参见 [相关权限管理](connect-to-an-instance-by-using-session-manager-2.md) 。 网络 ：由于 云助手 Agent 与云助手服务端之间通过 WebSocket 连接，不需要通过 SSH、VNC 等方式登录 ECS 实例，所以不需要打开 ECS 实例的入方向端口，进一步提高了 ECS 实例的安全性。 |  |
| --- | --- |
## 基本使用流程
在阿里云控制台通过会话管理连接实例。（浏览器中使用）
您可以直接在浏览器登录阿里云官网控制台，通过会话管理连接实例。具体连接操作，请参见[直接在浏览器上使用会话管理客户端连接实例（免安装）](connect-to-an-instance-by-using-session-manager-1.md)。操作流程如图所示：
在您的个人计算机上通过会话管理客户端连接实例。（本机命令行中使用）
您可以在个人计算机上安装ali-instance-cli，直接使用本机命令行，通过会话管理连接实例。
具体操作，请参见[在您的个人计算机上通过会话管理客户端连接实例（需安装](connect-to-an-instance-by-using-ali-instance-cli.md)[ali-instance-cli）](connect-to-an-instance-by-using-ali-instance-cli.md)。操作流程如图所示：
## 相关权限管理
如果RAM用户需要通过会话管理连接实例，相关操作的权限及说明如下：
操作（Action）列对应RAM权限策略中的操作（Action）。
| 操作（Action） | 说明 |
| --- | --- |
| ecs:StartTerminalSession | 通过会话管理功能连接到 ECS 实例。 （必须） |
| ecs:DescribeCloudAssistantStatus | 查询 ECS 实例是否安装云助手 Agent，该权限用于控制台在连接前进行校验。 |
| ecs:DescribeUserBusinessBehavior | 查询会话管理是否开启，该权限用于控制台在连接前进行校验。 |
| ecs:ModifyCloudAssistantSettings | 开启或关闭会话管理，如果当前阿里云账号已经开启会话管理功能，无需分配该权限。 |
### 权限策略示例
示例一：在控制台使用会话管理
如果RAM用户需要在控制台使用会话管理连接实例，根据最小授权原则，需要具有以下权限。
ecs:StartTerminalSession：通过会话管理连接实例的权限，此外，可以通过Resource字段，限制RAM用户可连接（会话管理）的ECS实例。
ecs:DescribeCloudAssistantStatus：查询ECS实例是否需要安装云助手，该权限用于控制台在连接前进行校验。
ecs:DescribeUserBusinessBehavior：查询会话管理功能是否已经开启，该权限用于控制台在连接前进行校验。
ecs:ModifyCloudAssistantSettings（可选）：打开或关闭会话管理的权限，如果当前阿里云账号已经开通会话管理，无需分配该权限。
自定义权限策略示例如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" }, { "Effect": "Allow", "Action": [ "ecs:DescribeUserBusinessBehavior", "ecs:DescribeCloudAssistantStatus", "ecs:ModifyCloudAssistantSettings" ], "Resource": "*" } ] }
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
示例二：通过ali-instance-cli使用会话管理
在使用ali-instance-cli工具时，配置阶段要求设置RAM用户的AccessKey、STS Token。当通过会话管理操作连接实例时，系统会验证此凭证对应的RAM用户是否拥有ecs:StartTerminalSession权限，这是允许通过会话管理建立与ECS实例连接的必要权限。
此外，在自定义权限策略时，可以通过指定Resource字段来限定RAM用户能够通过会话管理连接的具体ECS实例。权限策略示例如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": "ecs:StartTerminalSession", "Resource": "*" } ] }
关于CredentialsURI、STS Token的更多说明，请参见[创建](../../../ram/documents/create-an-accesskey-pair-1.md)[AccessKey](../../../ram/documents/create-an-accesskey-pair-1.md)、[什么是](../../../ram/documents/user-guide/what-is-sts.md)[STS](../../../ram/documents/user-guide/what-is-sts.md)。
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
示例三：通过RAM策略限制可以使用会话管理功能的用户
通过赋予子账号如下的权限策略，可以限制RAM用户只能以testUser1、testUser2创建Session Manager。
{ "Statement": [ { "Effect": "Allow", "Action": [ "ecs:StartTerminalSession" ], "Resource": [ "acs:ecs:*:*:instance/*" ], "Condition": { "StringEquals": { "ecs:SessionStartAs": [ "testUser1", "testUser2" ] } } } ], "Version": "1" }
通过赋予子账号如下的权限策略，可以禁止RAM用户以testUser1、testUser2创建Session Manager。
{ "Statement": [ { "Effect": "Allow", "Action": [ "ecs:StartTerminalSession" ], "Resource": [ "acs:ecs:*:*:instance/*" ], "Condition": { "StringNotEqualsIgnoreCase": { "ecs:SessionStartAs": [ "testUser1", "testUser2" ] } } } ], "Version": "1" }
为RAM用户授权，请参见[为](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
## 相关安全组设置
通过会话管理连接ECS实例时，需要确保ECS中运行的云助手Agent与云助手服务端的网络连通性，即在安全组出方向设置以下规则：
与SSH、RDP等连接方式不同，由于会话管理是由云助手Agent主动与会话管理服务端建立WebSocket连接，因此仅需放行出方向的云助手服务端的WebSocket端口。关于会话管理的原理，请参见[会话管理工作原理](connect-to-an-instance-by-using-session-manager-2.md)。
重要
如果使用普通安全组（包括默认安全组），默认情况下会放行所有的出方向流量，无需配置。
如果使用企业安全组，默认情况下会禁用所有出方向的流量，需要配置以下规则。更多关于企业安全组的说明，请参见[普通安全组与企业级安全组](basic-security-groups-and-advanced-security-groups.md)。
添加安全组规则的具体操作，请参见[添加安全组规则](add-a-security-group-rule.md)。
| 授权策略 | 优先级 | 协议类型 | 端口范围 | 授权对象 | 描述 |
| --- | --- | --- | --- | --- | --- |
| 允许 | 1 | 自定义 TCP | 443 | 100.100.0.0/16 | 用于访问云助手服务端。 |
| 允许 | 1 | 自定义 TCP | 443 | 100.0.0.0/8 | 访问 云助手 Agent 安装包所在服务器，用于安装或更新您的 云助手 Agent 。 |
| 允许 | 1 | 自定义 UDP | 53 | 0.0.0.0/0 | 用于解析域名。 |
此外，如果您计划仅通过会话管理连接实例，为了增加ECS实例的安全性，您可以取消放行安全组入方向上的SSH端口（默认22）或者RDP端口（默认3389）的规则。
## 在自己的应用中集成会话管理远程登录功能
通过会话管理远程连接到云服务器或托管实例的完整代码，请参考开源项目[cloud-assistant-starter](https://github.com/aliyun/cloud-assistant-starter)。本项目中[AxtSession.tsx](https://github.com/aliyun/cloud-assistant-starter/blob/master/src/main/resources/static/components/session/AxtSession.tsx)文件包含了调用API接口[StartTerminalSession - 开始终端会话](../developer-reference/api-ecs-2014-05-26-startterminalsession.md)获取WebSocketURL并建立连接的示例代码，将这段代码移植到您自己的企业应用中，即可使用会话管理连接实例。
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
