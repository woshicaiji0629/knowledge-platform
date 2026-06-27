# 使用远程桌面(MSTSC)/Windows App远程连接Windows实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/connect-to-a-windows-instance-by-using-a-username-and-password

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

# 使用远程桌面(MSTSC)/Windows App远程连接Windows实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当本地系统为Windows 10/11时，可直接使用系统内置的远程桌面（MSTSC）连接Windows实例。当本地系统为macOS时，可通过Windows App工具连接Windows实例。

重要

推荐通过[Workbench](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)连接阿里云上的实例，该工具可直接通过浏览器使用、支持免密登录，相比使用远程桌面、Windows App更便捷。

## 适用范围

- 

实例操作系统为Windows。

- 

实例已绑定[固定公网](products/ecs/documents/user-guide/public-ip-address.md)[IP](products/ecs/documents/user-guide/public-ip-address.md)或[弹性公网](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md)[IP](products/ecs/documents/user-guide/associate-or-disassociate-an-eip.md)。

## 方式一：使用远程桌面（适用于Windows）

### 准备工作

- 

实例公网IP地址：在[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，找到目标实例进入详情，在配置信息区域找到公网IP。

- 

准备实例登录凭证：为实例[设置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

- 

配置安全组：为实例关联的安全组[配置入方向规则](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，允许本地IP通过RDP（3389端口）访问实例。

### 操作步骤

- 

启动远程桌面

按Win+R输入mstsc，按Enter键，进入远程桌面工具。

- 

配置连接信息

在计算机文本框中，输入实例的公网IP地址。

- 

发起连接并输入密码

单击连接，在弹出的窗口中，输入用户名（默认为 Administrator）和密码，然后单击确定。

系统会弹出证书安全警告，提示无法验证此远程计算机的身份，单击是信任证书。

- 

成功登录

等待连接完成，系统将显示Windows实例的桌面。

## 方式二：使用Windows App（适用于macOS）

### 准备工作

- 

在App Store搜索并安装Windows App。

- 

实例公网IP地址：在[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，找到目标实例进入详情，在配置信息区域找到公网IP。

- 

准备实例登录凭证：为实例[设置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

- 

配置安全组：为实例关联的安全组[配置入方向规则](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)，允许本地IP通过RDP（3389端口）访问实例。

### 操作步骤

- 

启动Windows App

单击左侧导航栏的设备后，单击右上角的>添加电脑，弹出添加电脑对话框。

- 

配置连接信息

在电脑名称文本框中，输入实例的公网IP地址，单击添加。

- 

发起连接

单击左侧导航栏的设备，双击新创建的电脑连接卡片。

- 

输入凭证

在弹出的输入你的凭证对话框中，输入用户名（默认为 Administrator）和密码，然后单击继续。

系统会弹出证书安全警告，单击继续信任证书。

- 

成功登录

等待连接完成，系统将自动跳转到Windows实例的桌面。

## 应用于生产环境

- 修改默认RDP远程连接端口

建议将默认的3389端口改为其他数值较大的非标准端口（如33890），以降低遭受自动化扫描和暴力破解的风险。

- 

放行新端口：在实例所属的安全组中[添加入方向规则](products/ecs/documents/user-guide/start-using-security-groups.md)，放行新的端口（如33890）。

- 

修改服务端口：登录实例，通过修改注册表来更改端口。

- 

按Win+R输入regedit并按Enter键，打开注册表编辑器。

- 

导航到路径HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp。

- 

找到名为PortNumber的值，右键并单击修改，将其基数修改为十进制，然后输入新端口号（如33890）。

- 

按Win+R输入services.msc并按Enter键打开服务窗口，找到Remote Desktop Services，右键单击并选择重新启动，使配置生效。

- 

使用新端口连接：修改远程桌面端口后，在使用客户端连接实例时，应在实例公网 IP 地址后指定新端口，格式如下：<公网IP>:<端口号>。

- 仅授权可信的IP访问实例

[修改安全组规则](products/ecs/documents/user-guide/start-using-security-groups.md)，仅允许本机IP或其他受信任的IP访问实例RDP服务端口（默认为3389），拦截未知主机访问实例。

## 常见问题

- 如何配置安全组规则以放行3389端口？

在实例所在安全组[添加](products/ecs/documents/user-guide/start-using-security-groups.md)如下安全组规则：

| 授权策略 | 协议 | 访问来源 | 访问目的(本实例) |
| --- | --- | --- | --- |
| 允许 | 自定义 TCP | 填写本地客户端的公网 IP 地址。 重要 若使用 0.0.0.0/0 ，表示允许任意 IP 访问远程服务端口，存在安全风险，请谨慎使用。 | RDP(3389) 如果修改了实例的 RDP 服务的端口，需调整为实际端口。 |


- 发起连接后，等待一段时间后，提示无法连接？

表示客户端无法连接到服务器。排查顺序：

- 

检查公网IP是否正确。

- 

检查安全组是否放行端口。

- 

检查实例是否处于运行状态。

- 

使用[ECS](https://ecs.console.aliyun.com/troubleshooting)[控制台-自助问题排查](https://ecs.console.aliyun.com/troubleshooting)排查异常。

- 使用远程桌面（MSTSC）或Windows App如何传输文件？

- 

[在本地](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[Windows](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[中使用远程桌面连接（MSTSC）传输文件](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)

- 

[在本地](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[macOS](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[中使用](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[Windows APP](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)[向实例传输文件](products/ecs/documents/user-guide/use-mstsc-exe-to-upload-a-file-to-a-windows-instance.md)

[上一篇：使用OpenSSH/Xshell远程连接Linux实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-an-ssh-key-pair.md)[下一篇：在移动设备上连接Linux实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-from-a-mobile-device.md)

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
