# 选择ECS远程连接方式-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/connect-to-instance

# 选择ECS远程连接方式
阿里云提供多种连接方案，可根据操作系统、安全性、便捷性与网络环境，按需选择。
## 选择合适的工具连接实例
| 连接工具 | 适用操作系统 | 是否需本地安装软件 | 是否必须 [开通公网](best-practices-for-configuring-public-bandwidth.md) | 是否支持免密登录 | 是否需要登录阿里云 |
| --- | --- | --- | --- | --- | --- |
| Workbench （浏览器） | Windows、Linux | 否 | 否 | 是 | 是 |
| 会话管理 （浏览器） | Windows、Linux | 否 | 否 | 是 | 是 |
| VNC （浏览器） | Windows、Linux | 否 | 否 | 否 | 是 |
| 阿里云客户端 | Windows、Linux | 是 | 否 | 是 | 是 |
| SSH 客户端工具 （三方） | Linux | 是 | 是 | 否 | 否 |
| RDP 客户端工具 （三方） | Windows | 是 | 是 | 否 | 否 |
## 连接工具介绍&指引
###
###
###
###
###
###
| Workbench [Workbench](workbench-overview.md) 是阿里云提供的免安装远程连接工具，同时支持文件传输、多屏终端等功能。 相关文档 [使用](connect-to-a-linux-instance-by-using-a-password-or-key.md) [Workbench](connect-to-a-linux-instance-by-using-a-password-or-key.md) [登录](connect-to-a-linux-instance-by-using-a-password-or-key.md) [Linux](connect-to-a-linux-instance-by-using-a-password-or-key.md) [实例](connect-to-a-linux-instance-by-using-a-password-or-key.md) [使用](connect-to-a-windows-instance-through-workbench.md) [Workbench](connect-to-a-windows-instance-through-workbench.md) [登录](connect-to-a-windows-instance-through-workbench.md) [Windows](connect-to-a-windows-instance-through-workbench.md) [实例](connect-to-a-windows-instance-through-workbench.md) | 阿里云客户端 [阿里云客户端](overview-of-alibaba-cloud-client.md) 是阿里云官方提供的管理资源的软件，安装后，可通过该软件连接 ECS 实例。 相关文档 [使用阿里云客户端远程连接（SSH）Linux](use-alibaba-cloud-client-to-manage-ecs-instances.md) [实例](use-alibaba-cloud-client-to-manage-ecs-instances.md) [使用阿里云客户端远程连接（RDP）Windows](use-alibaba-cloud-client-to-manage-ecs-instances.md) [实例](use-alibaba-cloud-client-to-manage-ecs-instances.md) |
| --- | --- |
| 会话管理 [会话管理](connect-to-an-instance-by-using-session-manager-2.md) 是云助手提供的高安全级连接功能，通过免除公网 IP 隔绝外部攻击，同时通过审计功能保证操作有据可查。 相关文档 [在控制台通过会话管理连接实例](connect-to-an-instance-by-using-session-manager-1.md) [通过会话管理](connect-to-an-instance-by-using-ali-instance-cli.md) [CLI（ali-instance-cli）连接实例](connect-to-an-instance-by-using-ali-instance-cli.md) | SSH 客户端工具（非阿里云官方） 使用其他第三方 SSH 客户端工具连接 Linux 实例，实例需要分配公网 IP 或 EIP。 常见的 SSH 工具有 OpenSSH 客户端、 PuTTY 、 XShell 等。 相关文档 [使用](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md) [OpenSSH/Xshell](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md) [远程连接](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md) [Linux](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md) [实例](connect-to-a-linux-instance-by-using-an-ssh-key-pair.md) |
| VNC VNC 可直接查看实例中操作系统的实时界面。支持查看实例 启动阶段 或 停止中 的系统界面。由于不受安全组设置或实例中运行软件的限制，可以作为排查其他连接方式异常的手段。 相关文档 [通过](log-on-to-an-instance-by-using-vnc.md) [VNC](log-on-to-an-instance-by-using-vnc.md) [连接实例](log-on-to-an-instance-by-using-vnc.md) | RDP 客户端工具（非阿里云官方） 使用其他第三方 RDP 客户端工具连接 Windows 实例，实例需要分配公网 IP 或 EIP。 常见的 RDP 客户端有 Microsoft Remote Desktop 、 Windows 远程桌面 、 Windows App 等。 相关文档 [使用远程桌面/Windows App](connect-to-a-windows-instance-by-using-a-username-and-password.md) [远程连接](connect-to-a-windows-instance-by-using-a-username-and-password.md) [Windows](connect-to-a-windows-instance-by-using-a-username-and-password.md) [实例](connect-to-a-windows-instance-by-using-a-username-and-password.md) |
## 常见问题
- 如何查看实例是否分配公网IP？
可在实例列表页查看实例是否分配公网IP，若未分配请[开通公网](best-practices-for-configuring-public-bandwidth.md)。
在实例列表的IP地址列中，带有(公)标记的即为实例的公网IP地址；若该列仅显示私有IP，则表示未分配公网IP。
- 如何查看ECS实例的操作系统？
可在实例列表页查看实例的操作系统信息，Windows系统以外的操作系统大多是Linux系统。
如果发现安装了错误的操作系统，需要重装，请参见[更换操作系统（更换系统盘）](replace-the-operating-system-of-an-instance.md)。
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
