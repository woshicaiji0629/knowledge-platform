# ACK基于Alibaba Cloud Linux的等保加固使用说明-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/security-and-compliance/ack-reinforcement-based-on-classified-protection

# ACK等保加固使用说明
ACK基于Alibaba Cloud Linux提供了等保2.0三级版。您可以为节点池启用等保加固并配置基线检查策略，ACK会为集群自动配置等保加固项，执行等保合规基线检查，使其满足操作系统的等级保护要求。
## 等保加固满足的保合规要求
阿里云根据国家信息安全部的等级保护要求，ACK基于Alibaba Cloud Linux实现等保2.0三级版。您可以使用ACK的等保加固配置满足以下等保合规要求：
根据国家信息安全部发布的《GB/T22239-2019信息安全技术网络安全等级保护基本要求》中对操作系统提出的一些等级保护要求，ACK基于[Alibaba Cloud Linux](https://help.aliyun.com/zh/alinux/product-overview/alibaba-cloud-linux-overview)实现了等保2.0三级版。您可以启用等保加固功能，满足以下等保合规要求。
身份鉴别
访问控制
安全审计
入侵防范
恶意代码防范
## Alibaba Cloud Linux等保2.0三级版镜像检查规则说明
Alibaba Cloud Linux等保2.0三级版镜像按照《GB/T22239-2019信息安全技术网络安全等级保护基本要求》进行等级保护加固，满足对应的检查项。详细信息如下表所示。
| 检查项类型 | 检查项名称 | 检查内容 |
| --- | --- | --- |
| 身份鉴别 | 应对登录的用户进行身份标识和鉴别，身份标识具有唯一性，身份鉴别信息具有复杂度要求并定期更换。 | 检查是否存在空密码账户。 身份标识（UID）具有唯一性。 设置密码复杂度要求。 定期更换密码。 设置密码最短修改时间，防止非法用户短期内更改多次。 限制密码重用。 确保 root 是唯一的 UID 为 0 的账户。 |
| 当对服务器进行远程管理时，应采取必要措施，防止鉴别信息在网络传输过程中被窃听。 | 检查 SSHD 是否强制使用 V2 安全协议。 禁止 Telnet 等不安全的远程连接服务。 |  |
| 应具有登录失败处理功能，应配置并启用结束会话、限制非法登录次数和当登录连接超时自动退出等相关措施。 | 检测是否配置登录失败锁定策略，是否设置空闲会话断开时间，以及启用登录时间超期后断开与客户端的连接设置。 |  |
| 访问控制 | 应对登录的用户分配账户和权限。 | 除系统管理用户之外，应该分配普通用户、审计员、安全员账户。 确保用户 umask 为 027 或更严格。 确保每个用户的 home 目录权限设置为 750 或者更严格。 |
| 应重命名或删除默认账户，修改默认账户的默认口令。 | Linux 下 root 账号不应删除，检查是否禁止 SSH 直接登录即可。 root 之外的系统默认账户、数据库账户禁止登录（non-login）。 确保无弱密码存在，对应的弱密码基线检测通过。 |  |
| 访问控制的粒度应达到主体为用户级或进程级，客体为文件、数据库表级。 | 检查重要文件，如访问控制配置文件和用户权限配置文件的权限，是否达到用户级别的粒度。 |  |
| 应及时删除或停用多余的、过期的账户，避免共享账户的存在。 | root 之外的系统默认账户、数据库账户禁止登录（non-login）。 锁定或删除 shutdown、halt 账户。 |  |
| 应授予管理用户所需的最小权限，实现管理用户的权限分离。 | 确保 su 命令的访问受限制。 检查 /etc/sudoers 配置 sudo 权限的用户，根据需要给 root 以外用户配置 sudo 权限，但除管理员外不能给所有用户配置（ALL）权限。 |  |
| 应由授权主体配置访问控制策略，访问控制策略规定主体对客体的访问规则。 | 确保用户 home 目录权限设置为 750 或者更严格。 无主文件或文件夹的所有权，根据需要重置为系统上的某个活动用户。 设置 SSH 主机公钥文件的权限和所有权。 设置 SSH 主机私钥文件的权限和所有权。 |  |
| 安全审计 | 应对审计记录进行保护，定期备份，避免受到未预期的删除、修改或覆盖等情况。 | 检查 auditd 文件大小、日志拆分配置或者备份至日志服务器。若自动修复失败，请先修复启用安全审计功能检查项。 |
| 审计记录应包括事件的日期和时间、用户、事件类型、事件是否成功及其他与审计相关的信息。 | 满足启用安全审计功能检查项，即满足此项。 |  |
| 应启用安全审计功能，审计覆盖到每个用户，对重要的用户行为和重要安全事件进行审计。 | 启用 auditd 服务。 启用 rsyslog 或 syslog-ng 服务。 确保收集用户的文件删除事件。 确保收集对系统管理范围（sudoers）的更改。 确保收集修改用户或用户组信息的事件。如使用了第三方日志收集服务，可自行举证并忽略此项。 |  |
| 应保护审计进程，避免受到未预期的中断。 | auditd 是审计进程 audit 的守护进程，syslogd 是日志进程 syslog 的守护进程，查看系统进程是否启动。 |  |
| 入侵防范 | 应能发现可能存在的已知漏洞，并在经过充分测试评估后，及时修补漏洞。 | 云安全中心的漏洞检测和修复功能可以满足。如果有其他方式，可自行举证并忽略此项。 |
| 应遵循最小安装的原则，仅安装需要的组件和应用程序。 | Alibaba Cloud Linux 3：应卸载 avahi-daemon、Bluetooth、firstboot、Kdump、wdaemon、wpa_supplicant、ypbind 等软件。 Alibaba Cloud Linux 2：应卸载 NetworkManager、avahi-daemon、Bluetooth、firstboot、Kdump、wdaemon、wpa_supplicant、ypbind 等软件。 |  |
| 应关闭不需要的系统服务、默认共享和高危端口。 | 应关闭不需要的系统服务、文件共享服务。 关闭 21 、23、25、111、427、631 等高危端口。 如果有特殊需求必须严格配置访问控制策略，需自行举证并忽略此项。 |  |
| 应能够检测到对重要节点进行入侵的行为，并在发生严重入侵事件时提供报警。 | 云安全中心入侵检测和告警功能可以满足。如果已有其他检测与告警方式，可自行举证并忽略此项。 |  |
| 应通过设定终端接入方式或网络地址范围对通过网络进行管理的管理终端进行限制。 | Alibaba Cloud Linux 3： 根据实际配置登录服务器的终端，编辑 /etc/ssh/sshd_config 文件。 根据实际情况设置参数 AllowUsers <user>@<host> 。 说明 <user> 表示需要登录的服务器用户名， <host> 表示服务器的 IP 地址，请根据实际情况进行替换。 修改完成后按 Esc 键，输入 :wq 后按下回车键，保存并退出。 执行 sudo systemctl restart sshd 命令重启 sshd 服务。 Alibaba Cloud Linux 2： /etc/hosts.allow 文件指定允许连接到主机的 IP 地址，不应配置为 ALL:ALL 。 /etc/hosts.deny 文件指定禁止连接到主机的 IP 地址，应该配置为 ALL:ALL ，默认禁止所有连接。 两者需要配合使用，且必须先配置 /etc/hosts.allow 规则。若是已通过其他方式实现，例如网络安全组、防火墙等，可自行举证并忽略此项。 |  |
| 恶意代码防范 | Alibaba Cloud Linux 3：应采用免受恶意代码攻击的技术措施或主动免疫可信验证机制及时识别入侵和病毒行为，并将其有效阻断。 Alibaba Cloud Linux 2：应安装防恶意代码软件，并及时更新防恶意代码软件版本和恶意代码库。 | 检测是否安装使用云安全中心，如安装了其他防恶意代码软件，可自行举证并忽略此项。 |
## 使用Alibaba Cloud Linux等保2.0三级版
[创建](../user-guide/create-an-ack-managed-cluster-2.md)[ACK](../user-guide/create-an-ack-managed-cluster-2.md)[集群](../user-guide/create-an-ack-managed-cluster-2.md)时，您可以启用等保加固。ACK会为集群自动配置等保加固项，使其满足国家信息安全部发布的《GB/T22239-2019信息安全技术网络安全等级保护基本要求》中对操作系统的等级保护要求。
重要
为满足等保2.0三级版的标准要求，ACK会在等保加固的Alibaba Cloud Linux中默认创建ack_admin、ack_audit、ack_security三个普通用户。
为满足等保2.0三级版的标准要求，等保加固的Alibaba Cloud Linux禁止使用root用户通过SSH登录。您可通过[ECS](https://ecs.console.aliyun.com/)[控制台](https://ecs.console.aliyun.com/)[通过](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)[VNC](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)[连接实例](../../../../ecs/documents/user-guide/log-on-to-an-instance-by-using-vnc.md)，创建可使用SSH的普通用户。
## 配置Alibaba Cloud Linux等保2.0三级版镜像基线检查策略
阿里云已为Alibaba Cloud Linux 2和Alibaba Cloud Linux 3等保2.0三级版镜像提供了等保合规的基线检查标准和扫描程序。本文以Alibaba Cloud Linux 3为例为您介绍如何配置等保合规的基线检查策略，以实现对ECS实例进行等保合规基线检查。
### 前提条件
已购买支持基线检查的云安全中心，请参见[购买云安全中心](https://help.aliyun.com/zh/security-center/user-guide/purchase-security-center#task-lxj-3bc-zdb)。云安全中心的不同版本对基线检查的支持情况不同，请参见[功能特性](https://help.aliyun.com/zh/security-center/product-overview/functions-and-features#section-2ou-l3x-fir)。
### 操作步骤
登录[云安全中心控制台](https://yundun.console.aliyun.com/?p=sas)。
在风险治理>云安全态势管理页面右上角，单击策略管理。
在策略管理面板，单击基线扫描策略页签，按需配置等保合规的基线检查策略。
设置基线扫描覆盖等级。
您可以设置等级范围（高、中和低）的任一个或全部等级。该配置对所有扫描策略生效。
单击添加标准策略，然后在基线检查策略面板，完成配置，并单击确认。下文仅介绍主要配置项。详细信息，请参见[基线风险检查](https://help.aliyun.com/zh/security-center/user-guide/baseline-check/#section-5li-98f-3hs)。
策略名称：输入用于识别该策略的名称，例如Alibaba Cloud Linux 3等保合规检查，同时选择检测周期和检测开始时间。
基线名称：搜索并选中等保三级-Alibaba Cloud Linux 3合规基线。
扫描方式：选择生效服务器的扫描方式。可选项：
分组：以资产分组为单位扫描，仅支持全选一个或多个分组下的服务器。
ECS：以ECS为单位扫描，支持选择不同分组的部分或全部服务器。
生效服务器：选择需要应用该策略的资产分组。新购买的服务器默认归属在未分组中，如需对新购资产应用该策略，请选择未分组。
完成扫描策略配置后，您也可根据业务场景，单击策略操作列的编辑或删除，修改或删除该策略。
说明
策略被删除后不可恢复。对于默认策略，不支持删除，也不支持修改基线检查项，仅支持修改开始检测时间和应用默认策略的生效服务器。
执行基线检查策略。
在风险治理>云安全态势管理页面，单击系统基线风险页签，在基线检查策略页签下单击展开图标，选中已配置的等保合规基线检查策略，然后单击右侧检查项扫描的立即检查。
执行扫描策略后，立即检查按钮置灰，直至扫描执行完成。完成基线检查后，您需要在系统基线风险>风险情况页签，查看未通过的检查项及检查详情，并及时修复风险检查项。具体操作，请参见[查看并处理基线风险项](https://help.aliyun.com/zh/security-center/user-guide/view-and-handle-baseline-risks)。
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
