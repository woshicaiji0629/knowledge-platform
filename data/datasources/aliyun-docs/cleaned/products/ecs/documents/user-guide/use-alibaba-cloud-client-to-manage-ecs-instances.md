# 通过阿里云客户端查看和管理ECS实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/use-alibaba-cloud-client-to-manage-ecs-instances?spm=a2c4g.11186623.help-menu-25365.d_4_1_5_5_3.27257686KzDHaC&scm=20140722.H_438478._.OR_help-T_cn-DAS-zh-V_1

# 通过阿里云客户端管理ECS实例
[配置阿里云客户端身份凭证](add-one-or-more-accounts-to-alibaba-cloud-client.md)后，可免密、免公网连接并管理ECS实例。可通过端口转发实现在本地安全访问实例上部署的服务。
## 连接实例
### Linux实例
无公网IP的实例可通过会话管理连接的安全通道访问，有公网IP且端口开放的实例可使用SSH远程连接直连。
通过会话管理连接
重要
使用会话管理连接ECS实例前，需[确保会话管理已开启](connect-to-an-instance-by-using-session-manager-1.md)。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择启动远程会话...。
通过SSH远程连接
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择远程连接(SSH)...。
在对话框中，配置用户名和端口。并选择认证方式：
临时密码：临时生成一个密钥对，并把公钥通过云助手发送到实例内，再使用私钥登录实例。此方式无需管理密码或密钥文件，更为简便。
密码：需要输入ECS实例的密码。
密钥文件：使用SSH私钥文件进行登录。可通过以下两种方式获取私钥文件。
在目标实例对应的操作列选择实例系统管理>添加SSH密钥，将SSH密钥绑定到ECS实例，后续可实现免密登录。
在ECS控制台[创建密钥对](ssh-key-pairs.md)（.pem文件），并绑定到ECS实例。
[手动绑定密钥对](bind-a-key-pair-to-enable-ssh-passwordless-logon.md)，并绑定到ECS实例。
单击连接，打开SSH终端。
### Windows实例
需要图形桌面时，有公网IP的实例用公网IP连接，无公网IP则用云助手连接；若只需命令行，选择会话管理连接。
通过云助手连接
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择远程桌面(云助手)...。
在弹出的对话框中，配置端口转发规则（本地端口需未被占用），单击开始。客户端将启动操作系统的远程桌面应用。
在远程桌面连接窗口中，输入实例的登录密码完成连接。
通过会话管理连接
重要
使用会话管理连接ECS实例前，需[确保会话管理已开启](connect-to-an-instance-by-using-session-manager-1.md)。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择启动远程会话...。
Windows实例默认以system用户登录，且会话连接不支持图形化界面，仅支持命令行输入。
通过公网IP地址连接
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择远程桌面(RDP)...。
在弹出的对话框，确认连接信息，单击连接。阿里云客户端将启动操作系统的远程桌面应用。
在远程桌面连接窗口中，输入实例的登录密码完成连接。
## 启动和停止实例
重要
停止实例和重启实例都会中断业务，请谨慎执行。
启动实例
在实例列表中找到目标实例，在对应的操作列中选择更改实例状态>启动实例。
在弹窗的对话框中确认实例信息，然后单击启动实例。
停止实例
在实例列表中找到目标实例，在对应的操作列中选择更改实例状态>停止实例。
在弹窗的对话框中配置停机模式，然后单击停止实例。
重启实例
在实例列表中找到目标实例，在对应的操作列中选择更改实例状态>重启实例。
在弹窗的对话框中确认实例信息，然后单击重启实例。
## 重置实例密码
新密码通过加密传输，立即生效，无需重启实例。
在实例列表中找到目标实例，在对应的操作列中选择实例系统管理>重置实例密码。
在重置实例密码对话框中，输入并确认新密码，选择开启或保持原有密码登录方式，然后单击重置实例密码。
## 开启释放保护
若按量付费实例承载了关键业务，可[开启实例释放保护](enable-or-disable-release-protection-for-ecs-instances.md)，防止被意外释放。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择更改实例状态>添加实例保护。
## 管理安全组
在实例列表中找到目标实例，在对应的操作列中选择查看安全组。
可查看安全组ID、安全组名称、安全组类型、安全组的出入规则以及安全组的描述信息。
管理安全组。
添加入方向或者出方向规则。
在安全组列表所在行的操作列中单击添加入方向规则或者添加出方向规则。
填写详细的规则信息。参数信息 ，请参见[安全组规则](security-group-rules.md)。
修改授权策略。
在安全组列表所在行单击出方向规则或者入方向规则列的规则数。
在安全组规则列表所在行的操作列中选择修改授权策略。
选择允许或拒绝，然后单击修改授权策略。
## 上传和下载文件
重要
该功能仅适用于已分配公网IP地址的Linux实例。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择文件管理(SFTP)...。
在对话框中，配置用户名和端口。并选择认证方式：
临时密码：临时生成一个密钥对，并把公钥通过云助手发送到实例内，再使用私钥登录实例。此方式无需管理密码或密钥文件，更为简便。
密码：需要输入ECS实例的密码。
密钥文件：使用SSH私钥文件进行登录。可通过以下两种方式获取私钥文件。
在目标实例对应的操作列选择实例系统管理>添加SSH密钥，将SSH密钥绑定到ECS实例，后续可实现免密登录。
在ECS控制台[创建密钥对](ssh-key-pairs.md)（.pem文件），并绑定到ECS实例。
[手动绑定密钥对](bind-a-key-pair-to-enable-ssh-passwordless-logon.md)，并绑定到ECS实例。
在文件列表中找到目标文件或目录。
通过客户端可在ECS实例与OSS Bucket间[互传文件](use-alibaba-cloud-client-to-manage-ecs-instances.md)。
下载文件：在对应的操作列中选择下载此文件或下载此目录。
上传文件：在文件列表上方选择上传本地目录或上传本地文件。
## 端口转发（云助手）
通过端口转发（云助手）功能，可免用公网IP地址远程连接实例端口，将网络流量从本地端口转发到实例端口，可以便捷、安全地访问实例上的服务。例如，在一个没有公网IP的ECS实例上开发了一个Web应用，可通过端口转发在本地电脑浏览器访问ECS实例80端口上的Web应用。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择端口转发（云助手）...。在弹出的对话框中依次输入服务器端口号（实例内部服务的访问端口）、本地端口号（在本机上启动监听的端口），并根据需要选择是否打印请求/响应内容、是否在启动后打开本地端口对应的网页。单击开始。
在客户端查看端口转发日志。单击开始后，终端输出如下信息表示端口转发启动成功：
# 检查实例的运行状态... # 检查当前用户SessionManager协议开通状态[已开通] > localhost: start server socket : { address: '127.0.0.1', family: 'IPv4', port: 8088 } > localhost: start socket listen : { address: '127.0.0.1', family: 'IPv4', port: 8088 } > 开始监听本地端口 localhost:8088，该监听只接受来自本机的连接请求。
## 发送远程命令
为快速完成实例的日常维护（例如批量在ECS实例上安装或卸载软件、重置用户密码及自动化运维脚本等），可向ECS实例发送远程命令。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择实例系统管理>发送远程命令。在发送远程命令对话框，填写自动化运维脚本，然后单击发送。
## 释放实例
重要
实例一旦释放，数据将无法恢复。释放实例前，请确认数据是否需要保留。如需保留，可[创建快照](create-a-snapshot.md)来备份数据。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择更改实例状态>释放实例。
在弹窗的对话框中确认实例信息，然后单击释放实例。
## 常见问题
在客户端查看实例监控，为什么看不到数据？
在客户端查看监控数据前需要先[为登录的](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授予](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[AliyunCloudMonitorMetricDataReadOnlyAccess](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)权限。
如何设置SSH密钥文件实现免密登录？
为绑定密钥对的ECS实例在客户端添加SSH密钥，可实现免密登录ECS，不需要输入密码、密钥文件等。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择实例系统管理>添加SSH密钥。
在添加SSH密钥对话框中，选择本地SSH密钥文件，选择追加密钥或替换密钥，然后单击添加SSH密钥。
如何在客户端中下载OSS文件到实例？
重要
需要先为[登录的](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授予](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[AliyunOSSFullAccess](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)的权限。
客户端还支持下载OSS文件到实例和上传实例文件到OSS。
在阿里云客户端首页，单击云服务器(ECS)。在实例列表上方选择实例所在地域。
在实例列表中找到目标实例，在对应的操作列中选择文件管理(SFTP)...。
在对话框中，配置用户名和端口。并选择认证方式：
临时密码：临时生成一个密钥对，并把公钥通过云助手发送到实例内，再使用私钥登录实例。此方式无需管理密码或密钥文件，更为简便。
密码：需要输入ECS实例的密码。
密钥文件：使用SSH私钥文件进行登录。可通过以下两种方式获取私钥文件。
在目标实例对应的操作列选择实例系统管理>添加SSH密钥，将SSH密钥绑定到ECS实例，后续可实现免密登录。
在ECS控制台[创建密钥对](ssh-key-pairs.md)（.pem文件），并绑定到ECS实例。
[手动绑定密钥对](bind-a-key-pair-to-enable-ssh-passwordless-logon.md)，并绑定到ECS实例。
在文件列表中找到目标文件或目录。
在对应的操作列中选择上传到OSS。
在文件列表上方选择下载OSS文件。
为何无法使用临时密码登录或通过云助手连接ECS实例？
该功能依赖云助手在实例内部正常运行。自2017年12月1日起，通过公共镜像创建的ECS实例已预装云助手Agent，若实例未安装云助手请[手动安装云助手](install-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
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
