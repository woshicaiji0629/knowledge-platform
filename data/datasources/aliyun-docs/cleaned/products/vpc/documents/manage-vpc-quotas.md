# 提升VPC配额-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/manage-vpc-quotas

# 管理VPC配额
您可以通过配额中心或专有网络控制台等方式查看配额、申请提升配额，以及创建配额告警预设配额使用量或剩余可用量的阈值。
如果您正在使用多个阿里云服务，希望在一个界面统一管理所有云服务的配额，推荐使用[配额中心](https://quotas.console.aliyun.com/products)，统一管理。
如果您不需要集中管理多个云服务的配额，您可以直接在[专有网络控制台](https://vpc.console.aliyun.com/quota)管理服务资源。
## 使用权限
默认情况下只有阿里云账号（主账号）可以在配额中心执行操作。如果您需要使用RAM用户（子账号）执行管理操作，请先[为该](https://help.aliyun.com/zh/quota-center/user-guide/authorize-a-ram-user#task-1962367)[RAM](https://help.aliyun.com/zh/quota-center/user-guide/authorize-a-ram-user#task-1962367)[用户授予管理配额的权限](https://help.aliyun.com/zh/quota-center/user-guide/authorize-a-ram-user#task-1962367)，即AliyunQuotasFullAccess。
## 查看配额
您可以选择以下方式中的任意一种查看VPC的配额：
打开产品文档的[限制与配额](understanding-vpc-quotas-in-alibaba-cloud.md)页面，查看所有配额及配额默认值。
[通过配额中心查看配额](https://help.aliyun.com/zh/quota-center/user-guide/query-the-details-of-quotas-supported-by-a-cloud-service)。
通过专有网络控制台查看配额。
通过专有网络控制台查看配额
前往[专有网络控制台 - 配额管理页面](https://vpc.console.aliyun.com/quota)。
选择产品区域的专有网络VPC页签。
查看通用配额：在配额类型区域，选择通用配额页签，可以通过关键词筛选条件进行过滤，查看目标通用配额的配额名称、描述、使用量等信息。
查看API速率配额：在配额类型区域单击API速率配额页签，可以通过关键词、地域等筛选条件进行过滤，查看目标API速率配额项的版本、配额等信息。
查看权益配额：在配额类型区域单击权益配额页签，可以通过配额ID筛选条件进行过滤，查看权益配额的配额名称、描述、默认值等信息。
## 提升配额
如果您的业务对VPC某项配额的实际需求大于该项配额的默认值，同时该配额项支持调整，您可以通过以下方式申请提升配额。
登录阿里云[配额中心控制台](https://quotas.console.aliyun.com/products)，[创建配额提升申请](https://help.aliyun.com/zh/quota-center/user-guide/submit-an-application-to-increase-a-quota)。
通过专有网络控制台进行申请。
配额中心控制台和专有网络控制台使用的配额项和执行后的结果是一致的。
通过专有网络控制台提升配额
前往[专有网络控制台 - 配额管理页面](https://vpc.console.aliyun.com/quota)。
选择产品区域的专有网络VPC页签，选择需要提升的配额类型并进行操作。
提升通用配额
在配额类型区域选择通用配额页签，在目标通用配额的操作列单击申请。
在配额申请对话框，设置申请配额和申请理由，单击确认调整。
配额提升申请由各云产品的技术支持进行审批。如果您想增加通过几率，请在配额申请时填写合理的申请数值和详尽的申请理由。
配额申请结果将通过短信和邮箱通知到您。阿里云会根据您提供的信息对您的申请进行评估，然后会判定通过或拒绝您的申请。
申请完成后，您可以在操作列单击申请历史或选择申请历史，查看配额申请的审核状态。
如果配额提升申请的状态为审批通过，表示配额提升成功。
申请权益配额
在配额类型区域单击权益配额页签，在目标权益配额的操作列单击申请。
在申请权益配额对话框中，设置配额申请值、时间、申请理由和是否通知调整结果，单击确认调整。
如果您未选择生效时间，则生效时间默认为配额提升申请的提交时间。配额申请结果将通过短信和邮箱通知到您。
申请完成后，您可以在操作列单击申请历史或选择申请历史，查看权益配额的申请状态，当申请状态为审批通过时，表示权益配额申请成功。
## 创建配额告警
VPC的部分配额项支持创建告警，即预设配额使用量或剩余可用量的阈值。当配额使用量或剩余可用量达到告警中的预设阈值时，系统向告警回调地址发送告警消息。您可以根据告警消息及时提前申请提升配额，避免业务受到影响。
您可以通过以下方式创建配额告警。
登录阿里云[配额中心控制台](https://quotas.console.aliyun.com/products)，[创建配额告警](https://help.aliyun.com/zh/quota-center/user-guide/create-an-alert-rule-for-a-quota-item)。
登录专有网络控制台进行申请。
专有网络VPC支持创建告警的配额项如下：
配额名称：vpc_quota_secondary_cidr_num，配额描述：单个VPC支持创建的附加IPv4网段的数量。
配额名称：vpc_privilege_allow_buy_havip_instance，配额描述：拥有购买高可用虚拟IP实例的特权。
通过专有网络控制台创建配额告警
前往[专有网络控制台 - 配额管理页面](https://vpc.console.aliyun.com/quota)。
在配额类型区域选择通用配额页签，在目标通用配额的操作列单击创建告警。
在配额告警面板，设置配额告警相关参数，单击确认。
基本信息：自定义规则名称。
告警对象：对应配额项的相关信息。
告警条件：
告警指标：选择配额、配额用量、使用率、可用率，剩余可用率指标，进行告警。
设置阈值及报警级别，根据紧急、警告、普通设置阈值，不同状态将采用不同的通知方式。
通知方式：
选择通道沉默周期：报警发生后未恢复正常，间隔多久重复发送一次报警通知。
设置生效时间和告警联系人组。
告警回调：报警规则被触发时，云监控会将报警消息发送到您指定的URL地址。
## 加入配额模板
当配额模板的状态为已启用，且您已加入配额模板时，如果资源目录的管理账号新增成员，则系统自动将配额模板应用于新增成员，已有成员无变化。通过配额模板，您一次可以申请提升多个配额项，提升整个组织的配额管理效率和自动化水平。
在加入配额模板前，请确保：
您使用企业管理账号登录。
您已[开通资源目录](https://help.aliyun.com/zh/resource-management/resource-directory/user-guide/enable-a-resource-directory#task-2152699)并[启用配额模板](https://help.aliyun.com/zh/quota-center/user-guide/enable-the-quota-template-feature)。
您可以通过以下方式加入配额模板。
登录阿里云[配额中心控制台](https://quotas.console.aliyun.com/products)，[加入配额模板](https://help.aliyun.com/zh/quota-center/user-guide/add-a-quota-to-a-quota-template)。
登录专有网络控制台加入配额模板。
通过专有网络控制台加入配额模板
前往[专有网络控制台 - 配额管理页面](https://vpc.console.aliyun.com/quota)。
选择产品区域的专有网络VPC页签，您可以根据以下信息，选择需要加入配额模板的配额类型并进行操作。
通用配额项加入配额模板
在配额类型区域的通用配额页签，找到目标通用配额，在操作列单击加入配额模板。
设置目标配额的申请配额和是否通知调整结果。
权益配额项加入配额模板
在配额类型区域单击权益配额页签，找到目标权益配额，在操作列单击加入配额模板。
设置目标权益配额项的配额申请值、时间和是否通知调整结果。
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
