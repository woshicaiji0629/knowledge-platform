# 使用Workbench登录Linux实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key

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

# 使用Workbench登录Linux实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

Workbench是阿里云提供的可在浏览器中使用的远程连接工具，可直接免密连接Linux实例，支持登录无公网IP的实例。

## 适用范围

- 

实例状态：必须处于运行中，且健康状态为正常。

- 

RAM权限：RAM用户使用Workbench时，需被授予[相关权限](products/ecs/documents/user-guide/workbench-overview.md)。

## 方式一：免密连接（推荐）

免密登录时，默认通过[会话管理](products/ecs/documents/user-guide/connect-to-an-instance-by-using-session-manager-2.md)方式连接，未开启会话管理则通过[临时](products/ecs/documents/user-guide/workbench-password-free-login-principle-temporary-ssh-key-pair.md)[SSH](products/ecs/documents/user-guide/workbench-password-free-login-principle-temporary-ssh-key-pair.md)[密钥对](products/ecs/documents/user-guide/workbench-password-free-login-principle-temporary-ssh-key-pair.md)方式连接。

- 

登录[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面顶部选择资源组和地域。

- 

找到目标实例后，单击远程连接，在对话框中，单击通过Workbench远程连接对应的立即登录。

- 

在Workbench的登录实例页面，选择免密连接后，输入用户名后，单击登录。

实例登录成功界面如图所示：

重要

Workbench的远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接，建议[后台执行](products/ecs/documents/configure-linux-to-keep-the-process-running-after-the-ssh-client-is-disconnected.md)长任务。

## 方式二：终端连接（SSH）

- 

登录[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)，在页面顶部选择资源组和地域。

- 

找到目标实例后，单击远程连接，在对话框中，单击通过Workbench远程连接对应的立即登录。

- 

在Workbench的登录实例页面，完成以下配置后，单击登录。

### 

- 

- 

- 

### 

- 

- 

- 

| 配置项 | 说明 |
| --- | --- |
| 实例 | 自动填充当前实例的信息。 |
| 连接方式 | 选择 终端连接 ，该方式底层使用 SSH 协议连接实例。 |
| 认证方式 | 重要 SSH 密钥认证相比密码有较高的安全性，推荐 [绑定密钥对](products/ecs/documents/user-guide/instance-logon-credential-management.md) 后，通过 SSH 密钥认证方式登录。 SSH 密钥认证 用户名 ：Linux 实例默认用户名为 root。 若创建实例时设置使用 ecs-user 作为登录名，则需输入 ecs-user。 私钥 ：输入私钥文件的内容。如果私钥文件设置了口令，还需输入 密钥口令 。 为避免每次登录需要重复输入用户名和私钥，可以 [记住密钥](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md) ，以便之后使用。 SSH 端口 （可选）：SSH 连接端口默认 22，可在 登录实例 界面的 完整选项 > 端口 中修改。 密码认证 用户名 ：Linux 实例默认用户名为 root。 若创建实例时设置使用 ecs-user 作为登录名，则需输入 ecs-user。 密码 ：若忘记密码或未设置需先 [重置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md) 。 为避免每次登录需要重复输入用户名和密码，可以 [记住密码](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md) ，以便之后使用。 SSH 端口 （可选）：SSH 连接端口默认 22，可在 登录实例 界面的 完整选项 > 端口 中修改。 |


单击登录后，系统因需要放行Workbench的IP地址段，可能会提示添加安全组规则，以允许其访问实例的SSH端口（默认为22），可单击一键添加快速完成安全组的配置，具体配置的安全组规则以控制台界面为准。

登录成功界面如图所示。

重要

Workbench的远程连接会话最久维持6个小时，如果超过6小时没有任何操作，连接会自动断开，需要重新连接，建议[后台执行](products/ecs/documents/configure-linux-to-keep-the-process-running-after-the-ssh-client-is-disconnected.md)长任务。

## 常见问题

如何记住密码/密钥？

为避免每次登录需要重复输入用户名和密码，可以将用户名和密码保存为凭据，以便之后使用。

该凭据不会与其他用户共享，仅供创建凭据者登录实例使用。

- 保存登录凭据

在登录实例时，勾选保存登录凭据，登录成功后，凭据即被保存。

- 使用凭据登录实例

在登录实例，设置用户名时，可通过使用凭据选项，使用已保存的凭证登录。

免密登录原理是什么？

免密登录默认采用[临时](products/ecs/documents/user-guide/workbench-password-free-login-principle-temporary-ssh-key-pair.md)[SSH](products/ecs/documents/user-guide/workbench-password-free-login-principle-temporary-ssh-key-pair.md)[密钥对](products/ecs/documents/user-guide/workbench-password-free-login-principle-temporary-ssh-key-pair.md)免密登录；若启用会话管理功能，则优先通过[会话管理](products/ecs/documents/user-guide/connect-to-an-instance-by-using-session-manager-2.md)链路连接实例。

Workbench通过私网连接实例原理是什么？

在Workbench通过私网IP连接实例时，会自动在实例所属的VPC内创建反向访问规则，以建立安全的双向通信通道。可在>私网链路查看或管理。

Linux实例的默认登录名/初始登录名是什么？

Linux实例默认登录名为root，若创建实例时选择ecs-user，则会使用ecs-user。

实例的默认密码/初始密码是什么？

实例没有默认密码或初始密码。如需设置，可[重置密码](products/ecs/documents/user-guide/instance-logon-credential-management.md)。

无法远程连接故障排查

在无法远程连接实例时，可优先通过以下自助问题诊断工具排查问题，也可通过[无法连接](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[Linux](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)[实例的排查方法](products/ecs/documents/troubleshooting-guidelines-when-you-cannot-remotely-log-on-to-a-linux-instance-through-ssh.md)自助排查。

- 

单击一键诊断进入自助问题排查页面，并切换至目标地域。

- 

单击实例无法连接下的发起诊断，根据界面提示选择问题实例并发起诊断。

- 

诊断完成后，可根据提示完成修复操作。

[上一篇：通过Workbench连接实例](products/ecs/documents/user-guide/workbench-overview.md)[下一篇：使用Workbench登录Windows实例](products/ecs/documents/user-guide/connect-to-a-windows-instance-through-workbench.md)

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
