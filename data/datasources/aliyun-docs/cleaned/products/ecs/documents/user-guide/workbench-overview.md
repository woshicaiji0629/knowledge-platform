# 通过Workbench连接实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/workbench-overview

# 通过Workbench连接实例
Workbench是阿里云提供的在浏览器使用的远程连接工具，使用该工具，无需额外安装任何软件即可通过浏览器直接访问ECS实例。
## 什么是Workbench？
### Workbench介绍
Workbench是阿里云提供的一款Web远程连接工具，该工具无需安装，直接在浏览器使用。使用该工具连接ECS实例流程如图所示。
### Workbench的特点
- 支持多种连接方式
通过Workbench可以使用多种方式连接实例，如SSH（Linux常用）、RDP（Windows常用）、运维安全中心等。
相关文档
[使用](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](connect-to-a-linux-instance-by-using-a-password-or-key.md)
[使用](connect-to-a-windows-instance-through-workbench.md)[Workbench](connect-to-a-windows-instance-through-workbench.md)[登录](connect-to-a-windows-instance-through-workbench.md)[Windows](connect-to-a-windows-instance-through-workbench.md)[实例](connect-to-a-windows-instance-through-workbench.md)
- 支持通过公网或私网连接实例
当您在使用Workbench通过SSH或RDP方式连接到实例时，可以选择通过私网或公网IP连接实例。
### Workbench更多功能
除了连接实例外，Workbench还支持以下功能。
文件管理：支持可视化管理Linux实例中的文件，支持文件上传下载。请参见[使用](manage-files.md)[Workbench](manage-files.md)[管理](manage-files.md)[ECS](manage-files.md)[上的文件](manage-files.md)。
AI Agent模式：在AI Agent模式下，可通过自然语言指令规划并执行Linux运维操作，简化软件安装、异常问题诊断等任务。请参见[AI Agent](workbench-ai-agent-mode.md)[模式](workbench-ai-agent-mode.md)。
终端助手：帮助您生成运维中需要的脚本/命令。请参见[终端助手](intelligent-assistant.md)。
智能命令补全：当在命令行中输入命令时，它能够根据上下文实时预测并以列表形式展示后续可能使用的命令、参数或选项。请参见[智能命令补全](intelligent-command-completion.md)。
系统管理：可通过 Workbench 的系统管理功能，统一管理 Linux 实例的用户、登录日志和系统服务，实时监控系统运行状态。同时支持可视化地为 Java 应用添加堆分析、线程栈分析或性能分析等运维任务。请参见[系统管理](workbench-system-management.md)。
脚本库：允许将常用的命令或脚本片段保存在Workbench，并在任何通过Workbench连接的实例会话中一键调用执行。请参见[脚本库](workbench-script-library.md)。
录屏审计：录制终端用户在ECS实例内部的操作视频，以便管理员进行操作审计时查看终端用户的操作行为，为安全审计提供有效依据。请参见[录屏审计](screen-recording-audit.md)。
命令行审计：审查经过Workbench登录会话执行的历史命令是否符合安全标准，帮助您发现异常操作和风险事件，并记录具体的执行命令、执行命令时间等信息，以便进行后续分析和审计。请参见[命令行审计](command-audit.md)。
多屏终端：可以通过Workbench的多屏终端功能同时连接多台ECS实例，然后在多台实例中同时执行相同的命令。请参见[多屏终端](use-the-multi-terminal-feature.md)。
软件安装：可在Workbench中使用AI Agent或OOS预设软件包自动部署Docker、MySQL等软件。请参见[软件安装](workbench-software-installation.md)。
## Workbench基本使用流程
使用Workbench连接实例的流程如图所示。
找到待连接的实例。
打通Workbench与ECS实例之间的网络连接。
这一步需要设置实例所在的安全组与实例内防火墙，需放行来自Workbench的入方向流量。
使用Workbench连接实例。
在控制台选择通过Workbench连接实例，输入用户名、密码、密钥对等信息。
开通服务关联角色。
如果您在使用Workbench连接实例时没有创建服务关联角色，系统会提示您授予Workbench访问ECS实例的权限，即开通服务关联角色。
成功连接到实例，执行运维操作。
## Workbench的服务关联角色
由于Workbench需要操作您的ECS实例，因此，在首次使用Workbench连接实例时，会提示您创建服务关联角色AliyunServiceRoleForECSWorkbench，Workbench服务会以该角色的身份访问您的ECS实例。更多服务关联角色的说明，请参见[服务关联角色](https://help.aliyun.com/zh/ram/user-guide/service-linked-roles#concept-2448621)。
在首次连接实例时会出现对话框，单击确定系统会自动为您创建该服务关联角色。
如果您是RAM用户，您需要联系主账号或管理员为您授予AliyunECSWorkbenchFullAccess系统权限策略，拥有该权限的用户才可以创建Workbench的服务关联角色。
## RAM用户使用Workbench的权限设置
在开通服务关联角色后，RAM用户使用Workbench需设置如下权限策略，该策略代表用户可以使用Workbench连接所有ECS实例。
{ "Version": "1", "Statement": [ { "Action": "ecs-workbench:LoginInstance", "Resource": "*", "Effect": "Allow" } ] }
如果需要限制用户可以通过Workbench连接的实例，可通过修改Resource字段实现，格式如下：
{ "Version": "1", "Statement": [ { "Action": "ecs-workbench:LoginInstance", "Resource": [ "acs:ecs-workbench:{#regionId}:{#accountId}:workbench/{#instanceId}", "acs:ecs-workbench:{#regionId}:{#accountId}:workbench/{#instanceId}" ], "Effect": "Allow" } ] }
参数说明如下：
{#regionId}：实例所在地域ID，可设置为通配符*。
{#accountId}：主账号ID，可设置为通配符*。
{#instanceId}：目标实例ID，可设置为通配符*。
示例
例如，设置RAM用户可使用Workbench连接所有地域和账号下实例ID为i-001和i-002的实例时，可设置以下权限策略。
{ "Version": "1", "Statement": [ { "Action": "ecs-workbench:LoginInstance", "Resource": [ "acs:ecs-workbench:*:*:workbench/i-001", "acs:ecs-workbench:*:*:workbench/i-002" ], "Effect": "Allow" } ] }
## Workbench相关安全组设置
由于使用Workbench通过SSH或RDP方式连接实例时，您需要在实例所在安全组放通来自Workbench服务端的入网流量，您可以根据您网络类型的不同，参考下表添加安全组规则。具体操作，请参见[添加安全组规则](start-using-security-groups.md)。
重要
如果您在实例系统内开启了防火墙，请参照安全组修改防火墙规则。
| 授权策略 | 优先级 | 协议类型 | 端口范围 | 授权对象 |
| --- | --- | --- | --- | --- |
| 允许 | 1 | 自定义 TCP | 配置的端口取决于您实例内运行的远程连接服务的端口。 连接 Linux 实例： 选择 SSH (22) 。 Linux 实例默认远程连接服务为 SSH，默认端口为 22 。 连接 Windows 实例： 选择 RDP (3389) 。 Windows 实例默认远程连接服务为 RDP，默认端口为 3389 。 重要 如果您在实例内修改了相关远程服务的端口，请根据实际情况进行设置。 | 通过公网连接： 添加 47.96.60.0/24, 118.31.243.0/24, 8.139.112.0/24, 8.139.99.192/26 。 通过私网连接： 添加 100.104.0.0/16 。 警告 使用 0.0.0.0/0 ，代表所有 IP 地址均可以连接远程服务端口，该配置存在安全风险，请谨慎使用。 |
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
