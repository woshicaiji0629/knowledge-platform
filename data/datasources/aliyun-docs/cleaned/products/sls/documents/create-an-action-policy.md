# 如何创建行动策略-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/create-an-action-policy

# 行动策略
行动策略用于控制告警通知的渠道。您可以根据业务需求动态分派给特定通知渠道的特定的人、用户组或值班组，也支持告警未及时处理下的通知升级。
## 创建行动策略
登录[日志服务控制台](https://sls.console.aliyun.com)。
进入行动策略管理页面。
在Project列表区域，单击任意一个Project。
在左侧导航栏中，单击告警。
在告警中心页面，选择通知策略>行动策略。
在行动策略页签中，单击创建。
在添加行动策略对话框中，配置标识符和名称。
| 参数 | 描述 |
| --- | --- |
| 标识符 | 行动策略标识符，单个阿里云账号下不可重复。 |
| 名称 | 行动策略的名称。 |
添加第一行动策略项。
在第一行动列表页签中，单击图标。
配置触发告警通知的条件。
| 参数 | 描述 |
| --- | --- |
| 条件 | 所有 ：每个告警集合中所有的告警都满足所有条件时才会执行相应的行动组。 任意 ：每个告警集合中任意一条告警满足所有条件时就会执行相应的行动组。 |
| 条件表达式 | 针对符合条件的告警进行渠道分派。系统根据您配置的条件（对象、操作符、对象值），执行相应的行动组。例如阿里云账号等于 174****2745。 |
| 模式 | 您可以通过标准模式或高级模式添加多个条件。 标准模式 ：多个条件之间为 and 关系。 高级模式 ：多个条件之间可以为 and 或 or 关系，并支持您使用圆括号将多个条件归为一组并支持嵌套。 |
配置行动组。
根据控制台界面，配置通知渠道及配置相关参数。更多信息，请参见[通知渠道说明](notification-methods.md)。
说明
选择渠道为事件总线（EventBridge）或函数计算（FC）时，需先根据页面提示完成授权（本操作只需执行一次）。在授权过程中，阿里云自动为您创建一个服务关联角色AliyunServiceRoleForSLSAlert，用于授予日志服务使用该角色访问事件总线、函数计算等产品。
单击条件、行动组对话框对应的图标，结束第一行动列表配置。
如果您需要继续添加条件和行动组，请单击图标。
单击确认。
## 删除节点
将鼠标悬浮在目标节点上，单击右键，然后单击删除节点。
## 添加节点
说明
如果您已经添加了结束节点，则删除结束节点后，才能继续添加条件节点或行动组节点。
单击图标，添加条件节点。
单击图标，添加行动组节点。
单击图标，添加结束节点。
在条件配置面板中，将匹配方式设置为任意，对象选择规则名，操作符选择等于，值填写具体规则名称（例如删除节点失败），然后在流程线底部的动作配置区域添加所需动作（如通知、联系人等），单击确认完成条件配置。支持单击高级模式切换到高级条件编辑。
## 相关文档
[渠道分派与发送机制](manage-methods-to-send-alert-notifications.md)
[通知发送时段机制](periods-for-sending-alert-notifications.md)
[通知渠道说明](notification-methods.md)
[非定制的通知内容](non-customized-notification-content.md)
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
