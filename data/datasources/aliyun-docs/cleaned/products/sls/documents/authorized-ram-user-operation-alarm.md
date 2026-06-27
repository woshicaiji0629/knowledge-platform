# 使用权限策略为RAM用户授予告警操作权限-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/authorized-ram-user-operation-alarm

# 授权RAM用户操作告警
本文介绍如何为RAM用户授予操作告警权限，并介绍在配置跨Project、地域和阿里云账号监控日志时，如何配置授权。
## 前提条件
已创建RAM用户。具体操作，请参见[创建](../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../ram/documents/user-guide/create-a-ram-user.md)。
## 操作视频
## 授权RAM用户只读访问告警
### 方式一：授予系统权限策略
为RAM用户授予告警只读管理权限（AliyunLogReadOnlyAccess）。具体操作，请参见[为](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
### 方式二：创建自定义权限策略进行授权
使用阿里云账号（主账号）或RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
重要
Project名称表示用于只读告警数据的Project，请根据实际情况替换。
sls-alert-*表示当前阿里云账号下所有的全局告警中心Project。全局告警中心Project中包含该账号下所有告警规则的评估数据、发送的日志和告警相关的全局报表等。如果您不需要查看全局报表信息，可以在资源列表中删除acs:log:*:*:project/sls-alert-*/*。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "log:GetLogStore" ], "Resource": [ "acs:log:*:*:project/Project名称/logstore/internal-alert-history", "acs:log:*:*:project/sls-alert-*/logstore/internal-alert-center-log" ] }, { "Effect": "Allow", "Action": [ "log:GetJob", "log:ListJobs" ], "Resource": "acs:log:*:*:project/Project名称/job/*" }, { "Effect": "Allow", "Action": [ "log:GetProject" ], "Resource": [ "acs:log:*:*:project/sls-alert-*" ] }, { "Effect": "Allow", "Action": [ "log:GetLogStoreLogs", "log:ListLogStores", "log:GetIndex", "log:GetDashboard", "log:ListDashboard" ], "Resource": [ "acs:log:*:*:project/Project名称/*", "acs:log:*:*:project/sls-alert-*/*" ] }, { "Effect": "Allow", "Action": [ "log:GetResource", "log:ListResources", "log:GetResourceRecord", "log:ListResourceRecords" ], "Resource": [ "acs:log:*:*:resource/*" ] } ] }
为RAM用户添加创建的自定义权限策略。具体操作，请参见[为](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
## 授权RAM用户管理告警
### 方式一：授予系统权限策略
为RAM用户授予日志服务管理权限（AliyunLogFullAccess）。具体操作，请参见[为](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
### 方式二：创建自定义权限策略进行授权
使用阿里云账号（主账号）或RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
创建一个自定义权限策略，其中在脚本编辑页签，请使用以下脚本替换配置框中的原有内容。具体操作，请参见[通过脚本编辑模式创建自定义权限策略](../../ram/documents/create-a-custom-policy.md)。
重要
Project名称表示用于管理告警数据的Project，请根据实际情况替换。
sls-alert-*表示当前阿里云账号下所有的全局告警中心Project。全局告警中心Project中包含该账号下所有告警规则的评估数据、发送的日志和告警相关的全局报表等。如果您只想授权RAM用户操作单个全局告警中心Project的权限，您可以将sls-alert-*配置为单个Project的名称，格式为sls-alert-${uid}-${region}，例如sls-alert-148****6461-cn-hangzhou。
创建LogStore、创建索引及更新索引的权限策略，用于RAM用户操作告警相关的系统日志库（告警历史日志库、全局告警中心日志库），从而进行告警历史等报表的查看。
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "log:GetLogStore", "log:UpdateLogStore", "log:CreateLogStore", "log:CreateIndex", "log:UpdateIndex" ], "Resource": [ "acs:log:*:*:project/Project名称/logstore/internal-alert-history", "acs:log:*:*:project/sls-alert-*/logstore/internal-alert-center-log" ] }, { "Effect": "Allow", "Action": [ "log:*" ], "Resource": "acs:log:*:*:project/Project名称/job/*" }, { "Effect": "Allow", "Action": [ "log:GetProject", "log:CreateProject" ], "Resource": [ "acs:log:*:*:project/sls-alert-*" ] }, { "Effect": "Allow", "Action": [ "log:GetLogStoreLogs", "log:ListLogStores", "log:GetIndex", "log:GetDashboard", "log:CreateDashboard", "log:UpdateDashboard", "log:ListDashboard" ], "Resource": [ "acs:log:*:*:project/Project名称/*", "acs:log:*:*:project/sls-alert-*/*" ] }, { "Effect": "Allow", "Action": [ "log:*" ], "Resource": [ "acs:log:*:*:resource/*" ] } ] }
为RAM用户添加创建的自定义权限策略。具体操作，请参见[为](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户授权](../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
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
