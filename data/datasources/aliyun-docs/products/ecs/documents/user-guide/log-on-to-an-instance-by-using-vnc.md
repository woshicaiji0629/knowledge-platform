# 通过VNC连接实例-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/log-on-to-an-instance-by-using-vnc

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

# 通过VNC连接实例

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

VNC可直接查看实例中操作系统的实时界面。支持查看实例启动阶段或停止中的系统界面。由于不受安全组设置或实例中运行软件的限制，可以作为排查其他连接方式异常的手段。

重要

自2023年7月10日起，远程连接工具VNC无需单独设置VNC登录密码，仅需通过实例的登录名和密码，即可安全访问ECS实例。

阿里云在2023年7月10日对远程连接工具VNC完成安全升级，将自动托管通过VNC访问实例时的用户鉴权，以及通过VNC访问实例的端到端加密数据。

## 适用范围

- 

支持的实例状态：运行中或停止中。

- 

不支持的实例规格：裸金属服务器ecs.ebmhfc7.48xlarge。

## 操作步骤

- 

访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

单击目标实例ID，进入实例详情页。

- 

通过VNC连接。

重要

VNC 连接会因闲置时间超过 300 秒而自动断开，届时需重新连接实例。

- 

单击远程连接>展开其他登录方式，选择通过VNC远程连接中的立即登录。

|  |  |
| --- | --- |


- 

登录操作系统

- 

Linux实例

- 

输入登录用户（如root、ecs-user）后按Enter。

- 

输入实例登录密码后按Enter，进入Linux操作系统。

如果未设置或忘记密码，可在实例详情页的全部操作中重置实例登录密码。

- 

Windows实例

- 

在页面左上角，单击发送远程命令>CTRL+ALT+DELETE，解除系统锁屏。

- 

选择用户账户（默认为Administrator），输入实例登录密码后，按Enter，进入Windows操作系统。

如果未设置或忘记密码，可在实例详情页的全部操作中重置实例登录密码。

## 常见问题

- 如何粘贴命令？

- 

在实例中选中需要粘贴内容的地方。

- 

在界面左上角，单击复制命令输入。

最大支持2000个字符，暂不支持中文等非标准键盘值特殊字符。

- 

在文本内容对话框中，输入拷贝的内容，然后单击确定。

- 如何发送远程命令？

可通过发送远程命令功能模拟特定快捷键操作，例如Windows解除锁屏（CTRL+ALT+DELETE）或Linux切换虚拟终端（CTRL+ALT+F1到CTRL+ALT+F10切换到该实例的不同虚拟终端。）。

- 

使用VNC方式成功登录ECS实例。

- 

在界面左上角，单击发送远程命令，在下拉菜单中单击对应命令即可模拟特定快捷键。

- 忘记密码或未设置实例密码怎么办？

连接时，忘记或未设置实例密码时，可进入实例详情页，在全部操作中选择重置实例密码，根据界面提示完成重置密码操作。

- 连接时，出现“该资源目前的状态不支持此操作”是什么原因？

TDX机密计算环境的实例暂不支持VNC连接。

- ECS默认用户名、初始用户名、默认登录名、初始登录名是什么？

- 

Linux系统实例：默认为root，若创建实例时设置了使用ecs-user则为ecs-user。

- 

Windows系统实例：默认为Administrator。

- ECS默认密码、初始密码、默认远程密码、初始登录密码是什么？

没有。

出于安全考虑，阿里云不会为ECS实例设置默认或初始密码。如在创建实例时未设置密码。

- 连接时提示“当前操作未被授权，请联系主账号进行RAM授权后再执行操作”怎么办？

需要[授予](products/ram/documents/user-guide/grant-permissions-to-the-ram-user.md)RAM用户ecs:DescribeInstances和ecs:DescribeInstanceVncUrl权限。权限策略文件如下：

{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "ecs:DescribeInstances", "ecs:DescribeInstanceVncUrl" ], "Resource": "*" } ] }

- 登录实例时出现Login Incorrect或密码不正确，请再试一次，怎么办？

请保证密码输入无误，若忘记密码，请进入实例详情页，在全部操作中选择重置实例密码，根据界面提示完成重置密码操作后再连接。

- 为什么Linux实例连接后是黑屏？

Linux实例进入休眠状态时会显示黑屏，可单击键盘上任意键唤醒。

- 在轻量应用服务器中如何通过VNC连接？

VNC远程连接在轻量应用服务器中功能名为[救援登录](https://help.aliyun.com/zh/simple-application-server/user-guide/connect-to-a-server-by-using-the-rescue-feature)。

## 相关文档

- 

调用[DescribeInstanceVncUrl](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describeinstancevncurl.md)接口可获取远程连接ECS实例的VNC登录地址。

- 

关于VNC连接实例的问题，请参见[通过](products/ecs/documents/through-vnc-instance-remote-connection-problems.md)[VNC](products/ecs/documents/through-vnc-instance-remote-connection-problems.md)[远程连接实例的问题](products/ecs/documents/through-vnc-instance-remote-connection-problems.md)。

[上一篇：阿里云客户端应用配置项说明](products/ecs/documents/user-guide/use-alibaba-cloud-client.md)[下一篇：使用第三方客户端工具连接实例](products/ecs/documents/user-guide/connect-to-an-instance-by-using-third-party-client-tools.md)

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
