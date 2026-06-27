# 如何创建告警策略-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/create-an-alert-policy

# 创建告警策略
告警监控规则触发告警后，日志服务会根据告警策略进一步处理告警信息，包括合并和静默告警。 本文介绍创建告警策略的操作步骤。
## 第一步：添加策略
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击任意一个Project。
在左侧导航栏中，单击告警。在告警中心页面，选择通知策略>告警策略。在告警策略页签中，单击创建。
单击行动策略页签。
在添加策略对话框中，配置标识符和名称。
对话框下方提供路由合并策略和静默策略两个页签，可按需选择策略类型后在画布中编排流程。
| 参数 | 描述 |
| --- | --- |
| 标识符 | 告警策略标识符，不可重复。 |
| 名称 | 告警策略的名称。 |
## 第二步：路由合并策略
当系统产生大量重复的告警时，通过合并策略可将这些告警合并为一个告警进行通知。您可以在日志服务提供的图形化界面中配置条件和分组合并规则，制定一条路由合并策略。
### 配置说明
条件节点的匹配模式
您在配置告警策略和行动策略时，可添加条件节点，当告警集合中的告警满足条件时才会执行相应的动作。
操作符：条件配置支持正则匹配和数据范围匹配。
正则匹配：通过正则表达式完成条件匹配。
例如，在条件配置中，将对象设置为规则名，输入正则表达式\d+进行匹配。
数值范围匹配：通过数值比较（例如等于、数值大于等于等）完成条件匹配。
例如，选择对象为时间相关，字段为恢复时间，操作符选择数值范围，并输入条件值[*,100003]。配置完成后单击确认。您也可以单击高级模式切换配置方式。
模式：您可以通过标准模式或高级模式添加多个条件。
标准模式：多个条件之间为AND关系。
例如，在标准模式下添加筛选条件：将对象设置为严重度，操作符设置为数值等于，值设置为严重；将对象设置为所属区域，操作符设置为等于，值设置为cn-huhehaote。单击每行右侧的加号或减号按钮可增删条件，完成后单击确认。
高级模式：多个条件之间可以为AND或OR关系，并支持您使用圆括号将多个条件归为一组。
例如在高级模式下，每行条件可分别设置对象（如严重度、所属区域、规则名）、操作符（如数值等于、等于）和对应的值，行间通过或或且连接符组合逻辑关系，并可通过右侧加减号按钮增删条件行。
合并基准、行动策略、首次等待、变化等待和重复等待，配置说明请参见[告警分组合并](deduplicate-alerts.md)。
### 配置示例
在路由合并策略页签中，单击图标。
配置判断条件。
在条件面板中，将对象设置为阿里云账号ID，操作符设置为等于，并在值输入框中输入目标账号ID，然后单击确认。
配置合并告警的规则。
如果env标签为prd，按照告警源项目合并，执行SLS内置行动策略；如果env标签为test，按照告警规则合并，执行test行动策略。
两个分组合并配置的等待时间均为：首次等待30秒、变化等待10分钟、重复等待4小时。
单击条件和合并告警对话框对应的图标，结束配置。
## 第三步：静默策略
在静默时间内，符合条件的告警，不会触发告警通知。您可以在日志服务提供的图形化界面中配置条件和静默时间，制定一条静默策略。
### 配置说明
条件节点的匹配模式，详细说明请参见第二步配置说明。
若告警策略已配置静默规则，那么所有使用该告警策略的告警规则都会受到该静默规则影响。告警静默机制的基本原理请参见[告警静默机制](silence-policies.md)。
### 配置示例
在静默策略页签中，单击图标。
配置判断条件和静默时间。
符合告警严重度为中，监控规则所属项目的名称包含test-project，标签expired为true等条件的告警，静默1个小时；否则没有owner标签的告警持续静默。示例中第一个条件节点包含三个条件：告警严重度数值大于等于中、监控规则所属项目正则匹配test-project.*、标签.expired等于true。满足条件时，静默时间类型选择特定时间范围（如 2022-06-10 17:18:47 至 2022-06-10 18:18:47）；不满足时进入第二个条件节点：标签.owner不存在。满足该条件时，静默时间类型选择持续；不满足则不做静默处理，流程直接结束。
## 删除节点和添加节点说明
删除节点
将鼠标悬浮在目标节点上，单击右键，然后单击删除节点。
添加节点
此处以路由合并策略为例。
说明
如果您已经添加了结束节点，则删除结束节点后，才能继续添加条件、分组合并等节点。
单击图标，添加条件节点。
单击图标，添加分组合并节点。
单击图标，添加结束节点。
在工作流编辑器中，条件节点的判断条件设置为「阿里云账号ID 等于 指定账号ID」。当条件结果为是时，流程连接至分组合并节点，按照配置的合并规则对告警进行分组合并处理；当条件结果为否时，流程连接至后续操作节点，可继续添加相应的处理动作。所有分支最终连接至结束节点，完成路由合并策略的流程。
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
