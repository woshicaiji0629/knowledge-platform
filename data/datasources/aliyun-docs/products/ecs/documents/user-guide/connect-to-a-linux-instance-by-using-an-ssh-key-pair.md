# 使用OpenSSH/Xshell远程连接Linux实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair

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

# 使用OpenSSH/Xshell远程连接Linux实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当本地设备为macOS或Windows 10/11，可直接使用系统内置的OpenSSH命令行工具连接Linux实例。此外，本地Windows设备也可以通过Xshell工具连接实例，两种方式均支持密码或密钥对认证。

重要

推荐通过[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)连接阿里云上的实例，该工具可直接通过浏览器使用、支持免密登录，相比使用OpenSSH、Xshell更便捷。

## 适用范围

- 

实例操作系统为Linux。

- 

实例已绑定[固定公网](products/ecs/documents/user-guide/public-ip-address.md)[IP](products/ecs/documents/user-guide/public-ip-address.md)或[弹性公网](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md)[IP](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md)。

## 方式一：使用OpenSSH客户端（命令行）

OpenSSH是macOS和新版Windows系统内置的标准SSH客户端，通过命令行即可快速连接。

### 准备工作

- 

实例公网IP地址：在[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，找到目标实例进入详情，在配置信息区域找到公网IP。

- 

实例登录凭证：为实例[设置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)或[绑定密钥对](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

- 

配置安全组：为实例关联的安全组[配置入方向规则](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，允许本地IP通过SSH（22端口）访问实例。

### 操作步骤

## Windows 10/11

## 密码登录

- 

打开PowerShell

按Win+R输入powershell后按Enter键进入PowerShell命令行界面。

- 

发起远程连接

ssh <实例登录名>@<实例公网IP地址>示例：ssh root@47.98.xxx.xxx

- 

（首次连接时）验证主机指纹

当首次连接一台新的ECS时，会显示类似下方的信息，提示验证主机密钥指纹。

这是SSH的一项安全机制，为确保安全，请[获取实例的主机密钥指纹后比对差异](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)。若不一致，则说明正在遭受中间人攻击，请切换到安全的网络环境下重新连接实例。

确认主机指纹无误后，输入yes并按回车。

The authenticity of host '47.98.xxx.xxx (47.98.xxx.xxx)' can't be established. ED25519 key fingerprint is SHA256:AbCdEf123456... This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?

- 

输入密码，进入实例

输入密码时屏幕不会显示字符，这是正常现象，输入完成后按回车即可。

密码验证通过后，将看到类似下方的欢迎信息，并且命令提示符会变为[<实例登录名>@<hostname> ~]$的形式。表示已成功登录到ECS实例。

Welcome to Alibaba Cloud Elastic Compute Service ! [root@Connect-Instance-Example ~]#

## 密钥对登录

- 

打开PowerShell

按Win+R输入powershell后按Enter键进入PowerShell命令行界面。

- 

发起远程连接

ssh -i /path/to/private_key.pem <实例登录名>@<实例公网IP地址>示例：ssh -i /path/to/private_key.pem root@47.98.xxx.xxx。其中/path/to/private_key.pem为私钥文件路径，例如C:\Users\Administrator\Downloads\private_key.pem。

- 

（首次连接时）验证主机指纹

当首次连接一台新的ECS时，会显示类似下方的信息，提示验证主机密钥指纹。

这是SSH的一项安全机制，为确保安全，请[获取实例的主机密钥指纹后比对差异](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)。若不一致，则说明正在遭受中间人攻击，请切换到安全的网络环境下重新连接实例。

确认主机指纹无误后，输入yes并按回车。

The authenticity of host '47.98.xxx.xxx (47.98.xxx.xxx)' can't be established. ED25519 key fingerprint is SHA256:AbCdEf123456... This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?

- 

验证密钥，进入实例

当密钥验证通过后，将看到类似下方的欢迎信息，并且命令提示符会变为[<实例登录名>@<hostname> ~]$的形式。表示已成功登录到ECS实例。

Welcome to Alibaba Cloud Elastic Compute Service ! [root@Connect-Instance-Example ~]#

## macOS

## 密码登录

- 

打开终端（Terminal）。

- 

发起远程连接。

ssh <实例登录名>@<实例公网IP地址>示例：ssh root@47.98.xxx.xxx

- 

（首次连接时）验证主机指纹

当首次连接一台新的ECS时，会显示类似下方的信息，提示验证主机密钥指纹。

这是SSH的一项安全机制，为确保安全，请[获取实例的主机密钥指纹后比对差异](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)。若不一致，则说明正在遭受中间人攻击，请切换到安全的网络环境下重新连接实例。

确认主机指纹无误后，输入yes并按回车。

The authenticity of host '47.98.xxx.xxx (47.98.xxx.xxx)' can't be established. ED25519 key fingerprint is SHA256:AbCdEf123456... This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?

- 

输入密码，进入实例

输入密码时屏幕不会显示字符，这是正常现象，输入完成后按回车即可。

密码验证通过后，将看到系统的登录欢迎信息（具体内容因操作系统镜像而异），并且命令提示符会变为[<实例登录名>@<hostname> ~]$的形式。表示已成功登录到ECS实例。

Welcome to Alibaba Cloud Elastic Compute Service ! [root@Connect-Instance-Example ~]#

## 密钥对登录

- 

打开终端（Terminal）。

- 

发起远程连接

# chmod 400: 为私钥文件设置仅所有者可读的权限，这是SSH客户端的安全要求 chmod 400 /path/to/private_key.pem ssh -i /path/to/private_key.pem <实例登录名>@<实例公网IP地址>示例：ssh -i /path/to/private_key.pem root@47.98.xxx.xxx。其中/path/to/private_key.pem为私钥文件路径。

- 

（首次连接时）验证主机指纹

当首次连接一台新的ECS时，会显示类似下方的信息，提示验证主机密钥指纹。

这是SSH的一项安全机制，为确保安全，请[获取实例的主机密钥指纹后比对差异](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)。若不一致，则说明正在遭受中间人攻击，请切换到安全的网络环境下重新连接实例。

确认主机指纹无误后，输入yes并按回车。

The authenticity of host '47.98.xxx.xxx (47.98.xxx.xxx)' can't be established. ED25519 key fingerprint is SHA256:AbCdEf123456... This key is not known by any other names. Are you sure you want to continue connecting (yes/no/[fingerprint])?

- 

验证密钥，进入实例

当密钥验证通过后，将看到类似下方的欢迎信息，并且命令提示符会变为[<username>@<hostname> ~]$的形式。表示已成功登录到ECS实例。

Welcome to Alibaba Cloud Elastic Compute Service ! [root@Connect-Instance-Example ~]#

## 方式二：使用Xshell客户端（仅适用于Windows）

Xshell是一款SSH客户端工具，用于在Windows系统远程登录和管理Linux服务器。

### 准备工作

- 

下载并安装Xshell：访问[Xshell 官方网站](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.xshell.com%2Fzh%2Fxshell%2F)下载并安装最新客户端。

- 

实例公网IP地址：在[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，找到目标实例进入详情，在配置信息区域找到公网IP。

- 

实例登录凭证：为实例[设置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)或[绑定密钥对](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

- 

配置安全组：为实例关联的安全组[配置入方向规则](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，允许本地IP通过SSH（22端口）访问实例。

### 操作步骤

- 

启动 Xshell 并新建会话

- 

打开 Xshell 应用程序。

- 

在弹出的会话窗口中，单击新建（或通过菜单栏文件>新建）。

- 

配置连接基本信息

单击左侧导航栏下的连接，完成配置：

- 

名称：为会话取一个易于识别的名称（例如：My-Web-Server）。

- 

协议：保持默认的SSH。

- 

主机：输入实例的公网 IP。

- 

端口号：保持默认的22。

- 

配置用户身份验证

在左侧导航栏中，单击用户身份验证。

## 密码登录

- 

方法：选择Password。

- 

用户名：输入服务器的登录名（如root）。

- 

密码：输入对应的登录密码。

## 密钥对登录

- 

用户名：输入服务器的登录名（如root）。

- 

方法：选择Public Key，并按以下步骤配置用户密钥：

- 

单击设置...。

- 

在弹出的窗口中，选择密钥文件选项，单击用户密钥配置项后的...，单击导入...，选择本地存储的.pem后缀私钥文件。

- 

导入成功后，选中该密钥，单击确定。

- 

（可选）如密钥文件设置了密码，则需要提供密码。

- 

连接到服务器

完成上述配置后，单击连接。

- 

（首次连接时）验证主机密钥

当首次连接一台新的ECS时，Xshell会弹出SSH安全警告窗口，显示主机密钥指纹。

这是SSH的一项安全机制，为确保安全，请[获取实例的主机密钥指纹后比对差异](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)。若不一致，则说明正在遭受中间人攻击，请切换到安全的网络环境下重新连接实例。

确认无误后，单击接受并保存，这样以后连接就不会再弹出此提示。

- 

连接到服务器

当看到命令提示符出现以下内容时，表示已经通过验证，成功连接。

Welcome to Alibaba Cloud Elastic Compute Service ! [root@Connect-Instance-Example ~]#

## 应用于生产环境

在实际生产环境中，建议通过以下操作提升远程连接安全。

- 主动验证主机指纹，防范中间人攻击

在第一次连接到实例时，应先[验证实例的主机密钥指纹](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，确认连接的是目标实例而非攻击者的服务器。

- 禁用密码登录，强制使用密钥对

密钥对认证远比密码认证安全，可降低暴力破解风险。操作如下：

- 

为实例[绑定密钥对](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

- 

禁用密码登录：登录实例，编辑/etc/ssh/sshd_config配置文件，找到PasswordAuthentication，修改为PasswordAuthentication no，重启SSH服务生效配置。

- 修改默认SSH端口

将默认22端口改为其他数值较大的非标准端口（如2222），可有效减少被恶意扫描。

- 

放行新端口：在实例所属的安全组中[添加入方向规则](products/ecs/documents/user-guide/start-using-security-groups.md)，放行新的端口（如2222）

- 

修改SSH服务端口：登录实例，编辑/etc/ssh/sshd_config配置文件，将#Port 22修改为Port 2222。重启SSH服务生效配置。

- 

使用新端口连接：此后使用ssh命令时，需通过-p指定ssh的服务端口，例如：ssh -p 2222 username@instance_ip。

- 仅授权可信的IP访问实例

[修改安全组规则](products/ecs/documents/user-guide/start-using-security-groups.md)安全组规则，仅允许本机IP或其他受信任的IP访问实例SSH服务，拦截未知主机访问实例。

## 常见问题

- 如何配置安全组规则以放行22端口？

在实例所在安全组[添加](products/ecs/documents/user-guide/start-using-security-groups.md)如下安全组规则：

| 授权策略 | 协议 | 访问来源 | 访问目的(本实例) |
| --- | --- | --- | --- |
| 允许 | 自定义 TCP | 输入本地客户端的公网 IP 地址。 重要 若使用 0.0.0.0/0 ，表示允许任意 IP 访问远程服务端口，存在安全风险，请谨慎使用。 | SSH(22) 如果修改了实例的 SSH 服务的端口，需调整为实际端口。 |


- 如何验证实例的主机密钥指纹？

首次连接实例时，会提示验证主机密钥指纹，确认方法如下：

## 控制台

- 

进入[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在左上角选择地域与资源组。

- 

找到对应实例后，单击>获取实例系统日志，然后找到BEGIN SSH HOST KEY FINGERPRINTS，会显示所有主机指纹。

请仔细核对本地客户端提示的指纹（如上例中的 SHA256:******）是否与日志中显示的指纹完全一致。若不一致，则可能正在遭受中间人攻击，需切换至安全网络环境后重试连接。

若找不到BEGIN SSH HOST KEY FINGERPRINTS，需进入实例内查看主机指纹。

## 实例内

[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)后执行以下命令，查看主机密钥指纹：

for f in /etc/ssh/ssh_host_*_key.pub; do ssh-keygen -l -f "$f"; done

输出示例：

1024 SHA256:9C******co root@Connect-Instance-Example (DSA) 256 SHA256:u6******SU root@Connect-Instance-Example (ECDSA) 256 SHA256:iQ******jg root@Connect-Instance-Example (ED25519) 3072 SHA256:8R******64 root@Connect-Instance-Example (RSA)

请仔细核对本地客户端提示的指纹（如上例中的 SHA256:******）是否与日志中显示的指纹完全一致。若不一致，则可能正在遭受中间人攻击，需切换至安全网络环境后重试连接。

- 如何通过SSH的config配置文件简化连接命令？

每次连接都输入完整的ssh -i /path/to/key.pem username@instance_ip命令较为繁琐。通过在本地创建和配置SSHconfig文件，可以为服务器设置别名，简化连接命令。

- 

找到或创建config文件

## Windows 10/11

config配置文件默认路径为C:\Users\YourUsername\.ssh\config。若不存在，需手动创建。

使用时，请替换YourUsername为当前Windows的用户名。

## macOS

config配置文件默认路径为~/.ssh/config。若不存在，需手动创建。

- 

编辑config文件并添加实例信息

使用文本编辑器打开config文件，添加类似如下的配置。每一段Host配置对应一个服务器实例。

# 为Web服务器配置一个别名 "web-server" Host web-server HostName 47.98.xxx.xxx User root Port 22 （可选）如果使用密钥对登录，请指定私钥路径，使用密码登录请忽略 IdentityFile /path/to/your/private_key.pem # 可以为其他服务器添加更多配置 Host other-server HostName 8.123.xxx.xxx User ecs-user Port 2222 IdentityFile ~/.ssh/another_key.pem

参数说明：

- 

Host：服务器的别名，可自定义。

- 

HostName：实例的公网IP地址。

- 

User：登录用户名。

- 

Port：SSH端口号（默认为22）。

- 

IdentityFile：私钥文件的绝对路径。

- 

使用别名快速连接

保存config文件后，可以直接使用别名来连接实例。

# 直接使用别名连接，SSH会自动读取config中的IP、用户名和密钥信息 ssh web-server

- 连接时出现Connection timed out或提示连接超时？

表示客户端无法连接到服务器。排查顺序：

- 

检查公网IP是否正确。

- 

检查安全组是否放行端口。

- 

检查实例是否处于运行状态。

- 

使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。

- 密码输入正确，但提示Permission denied, please try again

表示服务器拒绝了密码。排查顺序：

- 

在控制台[重置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)后重试。

- 

使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。

- 使用密钥对登录时提示Permission denied (publickey)？

表示服务器拒绝了密钥。排查顺序：

- 

在控制台重新[绑定](products/ecs/documents/user-guide/instance-logon-credential-management.md)密钥对后重试。

- 

检查私钥文件路径及是否与实例匹配。

- 

（macOS系统下）检查私钥文件权限是否为400或600。

- 

使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。

- 通过SSH命令登录实例时，提示WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!

这是SSH的安全机制：在第一次连接实例后，会记住主机密钥指纹，后续连接时若指纹不一致，会提示该错误。可能是由于执行过更换系统盘、更换操作系统、删除了实例系统中的主机密钥文件等操作。

解决办法：[验证实例的主机密钥指纹](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，若无误，执行以下命令，删除本地保存的主机密钥指纹。

ssh-keygen -R <实例公网IP地址>

[上一篇：使用第三方客户端工具连接实例](products/ecs/documents/user-guide/connect-to-an-instance-by-using-third-party-client-tools.md)[下一篇：使用远程桌面/Windows App远程连接Windows实例](products/ecs/documents/user-guide/connect-to-a-windows-instance-by-using-a-username-and-password.md)

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
