# 使用安全监控查看并处理容器安全告警与风险-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/use-security-monitoring-capabilities

# 使用安全监控
安全监控提供监控和告警能力，包括恶意镜像启动、病毒和恶意程序的查杀、容器内部入侵行为、容器逃逸和高风险操作预警等主要的容器侧攻击行为。本文介绍如何使用安全监控功能。
## 前提条件
已创建Kubernetes集群，具体操作，请参见[创建](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
已开启云安全中心服务，具体操作，请参见[购买云安全中心](https://help.aliyun.com/zh/security-center/user-guide/purchase-security-center#task-lxj-3bc-zdb)。
如果您使用的是子账号（即RAM用户），请确保子账号有云安全中心的RAM只读访问权限AliyunYundunSASReadOnlyAccess。
## 背景信息
当容器应用通过API Server的认证鉴权和准入控制校验成功部署后，在云原生应用零信任的安全原则下，还需要在容器应用的运行时刻提供相应的安全监控和告警能力。为此，容器服务和云安全中心深度集成告警处理和漏洞检测能力，集群管理员可以在应用运行时提供监控和告警能力，包括恶意镜像启动，病毒和恶意程序的查杀，容器内部入侵行为，容器逃逸和高风险操作预警等主要的容器侧攻击行为。您可以在集群详情页实时接收到相应告警，并根据页面提示查看和处理告警详情。
## 操作步骤
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>安全监控。
在安全监控页面查看集群的安全概况。
安全告警数
显示检测到的安全风险告警事件，包括在容器中或在主机层面发生的病毒和恶意程序攻击、容器内部的入侵行为、容器逃逸和高风险操作预警等主要的容器侧攻击行为。关于安全告警的详细说明，请参见[安全告警概述](https://help.aliyun.com/zh/security-center/user-guide/overview-6#concept-l5g-fzc-zdb)。您可以单击安全告警数区域进入安全告警数页面进行如下操作。
在页面下方，单击目标安全告警操作列的处理，您可以在弹出的对话框中将该安全告警加入白名单或者忽略该安全告警。
在页面下方，单击目标安全告警操作列的详情，在告警事件的详情页面显示安全告警事件详细信息，包括事件的发生时间、受影响资产信息、进程ID等相关信息。然后在详情页面，单击溯源页签，在溯源页面可以对攻击事件进行自动化溯源并提供原始数据预览。
漏洞风险数
查看和处理资产中存在的漏洞，包括Linux漏洞、应用漏洞等。关于漏洞风险的详细说明，请参见[漏洞管理](https://help.aliyun.com/zh/security-center/user-guide/vulnerability-management/)。您可以单击漏洞风险数区域进入漏洞风险数页面进行如下操作。
在页面下方，单击目标漏洞的名称或操作列的处理，您可以查看漏洞详情和待处理漏洞。漏洞详情列表提供漏洞的处理建议，待处理漏洞列表提供漏洞的修复、验证以及详情查看功能。
在页面下方，单击目标漏洞右侧的漏洞编号，将跳转至阿里云漏洞库，提供更详细的漏洞信息。
基线风险数
针对服务器操作系统、数据库、软件和容器的配置进行安全检测，可以帮您加固系统安全，降低入侵风险并满足安全合规要求。关于基线风险的详细说明，请参见[基线检查](https://help.aliyun.com/zh/security-center/user-guide/baseline-check/)。您可以单击基线风险数区域进入基线风险数页面，单击目标基线风险项右侧操作列的详情，查看基线风险描述以及受影响资产列表。
容器防火墙告警数
为容器环境提供的防火墙服务。当黑客利用漏洞或恶意镜像入侵容器集群时，容器防火墙会对容器的异常行为进行告警或拦截。关于容器防火墙的详细说明，请参见[容器防火墙](https://help.aliyun.com/zh/security-center/user-guide/overview)。您可以单击容器防火墙告警数区域进入容器防火墙告警数页面。
在页面的告警列表中，包括告警等级、名称、源、目的网络对象，涉及的端口、集群以及防御模式。
在页面的告警列表中，您可以单击操作列的编辑规则对告警规则进行编辑。
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
