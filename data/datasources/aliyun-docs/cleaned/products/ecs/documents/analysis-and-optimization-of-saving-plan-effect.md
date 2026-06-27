# 分析节省计划使用率与覆盖率并优化成本-云服务器 ECS-阿里云-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/analysis-and-optimization-of-saving-plan-effect

# 查询与优化节省计划使用情况
当您购买并使用节省计划后，您可以前往[节省计划总览页面](https://usercenter2.aliyun.com/resource/spn/overview)查看已购买的节省计划及其使用效果，阿里云会根据您的节省计划抵扣情况为您生成两份用于查看节省计划使用情况的报告，您可以结合报告和业务需求对您当前开通的节省计划进行调整优化以达到更好的成本优化效果。
## 查看节省计划使用情况
节省计划使用率报告用于查看节省计划是否存在浪费，覆盖率报告用于查看节省计划是否有效降低资源使用成本。
### 使用率报告
您可以查看一个或者多个节省计划使用率情况。使用率指节省计划在购买后按多少比例参与了抵扣，使用率越大越说明节省计划的使用效果越佳。
节省计划使用率 = 节省计划已抵扣金额 / 节省计划总金额
节省计划已抵扣金额：您购买节省计划之后，节省计划抵扣的按量付费账单。
节省计划总金额：是指在筛选的时间范围内购买节省计划花费的总金额，即节省计划每小时承诺消费乘以筛选时长的金额。
说明
如果您需要详细的操作指引信息，请参见[查询节省计划使用率](https://help.aliyun.com/zh/user-center/how-to-check-saving-plan-usage#1f6d7e9072rdg)。
### 覆盖率报告
覆盖率用来查看资源的使用情况，您可以查看当前账号下所有节省计划的综合覆盖率，覆盖率越大越说明节省计划有效帮助您降低了成本。
节省计划覆盖率 = 节省计划已抵扣金额 / 节省计划适用资源的总支出金额
节省计划已抵扣金额：您购买节省计划之后，节省计划抵扣的按量付费账单。
节省计划适用资源的总支出金额：节省计划总金额 + 超过节省计划部分需要按常规按量单价计费的金额。
费用与成本的覆盖率是包含所有支持节省计划的产品，如果只是查看单产品的覆盖率，需要去筛选相应的产品明细。
说明
如果您需要详细的操作指引信息，请参见[查询节省计划覆盖率](https://help.aliyun.com/zh/user-center/how-to-check-saving-plan-usage#f9939a5072u9r)。
### 使用率及覆盖率报告解读及建议
使用率高，覆盖率高：说明您购买的节省计划额度合适，没有额度浪费，且有效地帮您节省了成本。
使用率高，覆盖率低：说明还有较大抵扣的空间，您可以尝试提升节省计划承诺消费的额度，进一步降低成本。
使用率低，覆盖率低：说明节省计划实际可以帮您节省的成本较大，您购买的节省计划抵扣比例较少，成本损失较大。您需要调整自己的使用习惯，尽可能用节省计划去抵扣按量付费的账单，减少成本损失。
使用率低，覆盖率高：说明当前抵扣空间较小，如果您的企业存在多个账号使用资源，您可以开启节省计划共享，将其他账号的资源纳入当前节省计划抵扣范围，或等待当前节省计划到期后重新评估您购买的权益折扣产品。
## 节省计划使用优化
为了更有效地利用节省计划降低资源使用成本，您应定期查看报告，并根据实际使用情况调整节省计划的配置，以保持良好的使用率和覆盖率。
如果您的业务增长导致云服务器ECS的使用量大幅超出之前的预期，或业务变化使当前节省计划无法充分抵扣资源，那么继续使用原有计划可能无法降低成本。对此，阿里云建议您考虑新购或升级节省计划，以提高覆盖率。
若当前节省计划已基本抵扣大部分资源，但实际消费仍远低于承诺金额，阿里云建议您可以通过多账号共享节省计划来提高使用率。
### 新购节省计划
阿里云支持您持有多份节省计划，您可以结合覆盖率报告新购节省计划提升节省计划覆盖度。多份节省计划存在一定的抵扣顺序，购买前请参见[多份节省计划的抵扣优先级](savings-plan-credit-rules.md)。
您可以前往[节省计划购买方案测算页面](https://usercenter2.aliyun.com/resource/spn/recommend)查看推荐配置。在节省计划购买方案测算页面中，输入节省计划类型、购买时长和付费类型，然后单击测算。系统会自动测算优化建议及每小时承诺消费金额，并给出预期节省幅度供您参考。如果推荐方案符合您的需求，单击立即购买即可。
说明
阿里云建议您在企业内部使用一个账号集中购买和管理节省计划，当您根据优化建议新购节省计划时，需要按照测算时的账号范围，将新购的节省计划共享给其他账号，具体操作请参见[开通节省计划多账号共享](savings-plan-credit-rules.md)。
### 升级当前节省计划
如果您不希望叠加多份节省计划，您可以前往[节省计划购买方案测算页面](https://usercenter2.aliyun.com/resource/spn/recommend)，根据当前资源情况的推荐购买数据，参考下面操作升级当前开通的节省计划，通过提高承诺消费金额来获取更低的折扣。
升级规则
升级规则说明如下：
升级生效周期：升级后在下个计费周期生效。例如15:30发起升级并支付完成，16:00开始计算升级差价，在16:00时系统自动将节省计划的承诺消费金额变更为升级后更高的承诺消费金额。升级后原节省计划的到期时间不变。
升级应付金额：（升级后的小时承诺消费金额*剩余小时数-升级前的小时承诺消费金额*剩余小时数）*预付比例。
手动升级节省计划
登录[费用与成本控制台](https://billing-cost.console.aliyun.com/resource/spn/overview)。
在总览页签下，单击需要升级的节省计划操作列的升级。
在节省计划 | 变配页面，输入承诺消费金额，然后单击立即购买，根据界面提示完成支付。
### 多账号共享一份节省计划
如果您的企业的ECS及ECI按量付费资源购买并持有在多个阿里云账号中，阿里云支持您使用一份节省计划抵扣多个阿里云账号下的按量付费资源。当您仅有一个阿里云账号购买并开通了节省计划，且其他阿里云账号中有符合抵扣规则的按量付费资源时，开启多账号共享一份节省计划可以帮助您提高节省计划使用率。具体操作请参见[开通节省计划多账号共享](savings-plan-credit-rules.md)。
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
